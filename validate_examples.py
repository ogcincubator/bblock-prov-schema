#!/usr/bin/env python3
"""Validate the examples and tests of every building block in _sources.

For each block directory containing a schema.json:
  * every snippet listed in examples.yaml (`ref`, optionally `schema-ref`) must
    validate against the block's schema (or the `schema-ref` fragment);
  * every JSON file in tests/ must validate, except files whose name contains
    "fail", which must be rejected.

Example files may contain `{"$ref": "<relative path>"}` objects, which are
inlined (relative to the examples.yaml directory) before validation.

Requires: jsonschema, referencing, pyyaml.
Usage: python3 validate_examples.py [block ...]   (default: all blocks)
"""
import json
import sys
import urllib.request
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

SOURCES = Path(__file__).resolve().parent / "_sources"
PREFIX = "bblocks://ogc.ogc-utils."
EXTERNAL = {
    "iri-or-curie": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json",
    "json-link": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json",
}


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def build_registry(blocks):
    resources = []
    for name, url in EXTERNAL.items():
        contents = fetch(url)
        resources.append((PREFIX + name, Resource.from_contents(contents, DRAFT202012)))
        resources.append((url, Resource.from_contents(contents, DRAFT202012)))
    for block in blocks:
        res = Resource.from_contents(read_json(SOURCES / block / "schema.json"), DRAFT202012)
        resources.append((PREFIX + block, res))
    return Registry().with_resources(resources)


def inline_refs(node, base):
    if isinstance(node, dict):
        if set(node) == {"$ref"}:
            return inline_refs(read_json(base / node["$ref"]), base)
        return {k: inline_refs(v, base) for k, v in node.items()}
    if isinstance(node, list):
        return [inline_refs(v, base) for v in node]
    return node


def examples_of(block):
    path = SOURCES / block / "examples.yaml"
    if not path.exists():
        return
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    for example in (data if isinstance(data, list) else data.get("examples", [])):
        for snippet in example.get("snippets", []):
            if snippet.get("language") == "json" and "ref" in snippet:
                yield (SOURCES / block / snippet["ref"], snippet.get("schema-ref"),
                       example.get("title", ""))


def resolve_block(block, schema_ref):
    """Return the block defining `schema_ref` (`#/$defs/Name`), preferring `block`.

    Examples may point at a definition that lives in another block of this
    repository (e.g. prov examples referring to the Activity definition).
    """
    parts = schema_ref.lstrip("#").strip("/").split("/")
    if len(parts) != 2 or parts[0] != "$defs":
        return block
    candidates = [block] + sorted(p.parent.name for p in SOURCES.glob("*/schema.json"))
    for candidate in candidates:
        if parts[1] in read_json(SOURCES / candidate / "schema.json").get("$defs", {}):
            return candidate
    return block


def make_validator(block, schema_ref, registry):
    if schema_ref:
        block = resolve_block(block, schema_ref)
    uri = PREFIX + block
    if schema_ref:
        schema = {"$ref": uri + (schema_ref if schema_ref.startswith("#") else "#" + schema_ref)}
    else:
        schema = {"$ref": uri}
    return Draft202012Validator(schema, registry=registry)


def short(error):
    return error.message if len(error.message) < 200 else error.message[:200] + "..."


def main(selected):
    blocks = sorted(p.parent.name for p in SOURCES.glob("*/schema.json"))
    registry = build_registry(blocks)
    failures = 0
    for block in blocks:
        if selected and block not in selected:
            continue
        print(f"== {block}")
        cases = []  # (file, schema_ref, expect_valid)
        for path, schema_ref, _title in examples_of(block):
            cases.append((path, schema_ref, True))
        listed = {p.resolve() for p, _, _ in cases}
        for path in sorted((SOURCES / block / "examples").glob("*.json")):
            if path.resolve() not in listed:
                print(f"  note {path.relative_to(SOURCES)} is not listed in examples.yaml")
                cases.append((path, None, True))
        for path in sorted((SOURCES / block / "tests").glob("*.json")):
            cases.append((path, None, "fail" not in path.name))
        for path, schema_ref, expect_valid in cases:
            label = path.resolve().relative_to(SOURCES)
            if not path.exists():
                print(f"  FAIL {label}: file not found")
                failures += 1
                continue
            validator = make_validator(block, schema_ref, registry)
            errors = list(validator.iter_errors(inline_refs(read_json(path), path.parent.parent)))
            if bool(errors) != (not expect_valid):
                failures += 1
                reason = short(errors[0]) if errors else "expected a validation error but it passed"
                print(f"  FAIL {label}: {reason}")
            else:
                print(f"  ok   {label}" + ("" if expect_valid else " (rejected as expected)"))
    print(f"\n{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(set(sys.argv[1:])))
