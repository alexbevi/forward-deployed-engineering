"""Evaluate the table views used by this vault, without executing expressions."""

from __future__ import annotations

import json
import re
from pathlib import PurePosixPath


def property_value(record: dict, field: str):
    path = PurePosixPath(record["path"])
    if field == "file.name":
        return path.stem
    if field == "file.ext":
        return path.suffix.removeprefix(".")
    if field.startswith(("file.", "formula.")):
        raise ValueError(f"Unsupported Base property: {field}")
    return record["meta"].get(field.removeprefix("note."))


def filter_test(expression):
    if isinstance(expression, dict):
        if len(expression) != 1:
            raise ValueError(f"Invalid Base filter: {expression}")
        operator, children = next(iter(expression.items()))
        if operator not in {"and", "or", "not"} or not isinstance(children, list):
            raise ValueError(f"Unsupported Base filter: {expression}")
        tests = [filter_test(child) for child in children]
        if operator == "or":
            return lambda record: any(test(record) for test in tests)
        if operator == "not":
            return lambda record: not any(test(record) for test in tests)
        return lambda record: all(test(record) for test in tests)
    if not isinstance(expression, str):
        raise TypeError(f"Invalid Base expression: {expression}")
    match = re.fullmatch(
        r'([\w.]+)\s*(==|!=)\s*("[^"\\]*"|null|true|false|-?\d+)', expression
    )
    if not match:
        raise ValueError(f"Unsupported Base expression: {expression}")
    field, operator, literal = match.groups()
    length = field.endswith(".length")
    field = field.removesuffix(".length") if length else field
    expected = json.loads(literal)

    def test(record):
        actual = property_value(record, field)
        if length:
            actual = len(actual) if isinstance(actual, (list, str)) else 0
        equal = actual == expected
        return equal if operator == "==" else not equal

    return test


def table_views(spec: dict, records: list[dict]) -> list[dict]:
    if set(spec) - {"filters", "views"} or not spec.get("views"):
        raise ValueError(
            "Unsupported Base configuration; only filtered table views are supported"
        )
    selected = filter_test(spec.get("filters", {"and": []}))
    candidates = [record for record in records if selected(record)]
    views = []
    for view in spec["views"]:
        if (
            set(view) - {"type", "name", "order", "filters", "groupBy"}
            or view.get("type") != "table"
        ):
            raise ValueError(f"Unsupported Base view: {view}")
        columns = view.get("order")
        if not view.get("name") or not isinstance(columns, list) or not columns:
            raise ValueError(f"Incomplete Base view: {view}")
        group = view.get("groupBy", {})
        if group and (
            set(group) != {"property", "direction"}
            or group["direction"] not in {"ASC", "DESC"}
        ):
            raise ValueError(f"Unsupported Base grouping: {group}")
        included = filter_test(view.get("filters", {"and": []}))
        rows = []
        for record in candidates:
            if included(record):
                values = [property_value(record, column) for column in columns]
                group_value = property_value(record, group["property"]) if group else ""
                if isinstance(group_value, (list, dict)):
                    raise ValueError("Base grouping requires a scalar property")
                rows.append(
                    {
                        "path": record["path"],
                        "values": values,
                        "group": str(group_value or ""),
                    }
                )
        rows.sort(key=lambda row: row["path"].casefold())
        views.append(
            {"name": view["name"], "columns": columns, "rows": rows, "group": group}
        )
    return views
