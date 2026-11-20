#!/usr/bin/env python3
"""Regenerate _sources/prov-bundled/schema.json from the modular schemas.

Merges the $defs of prov, prov-entity, prov-activity and prov-agent into a
single self-contained schema: cross-module `bblocks://ogc.ogc-utils.<module>#<Name>`
references become local `#/$defs/<Name>` references, external building block
references become their published schema URLs, and the per-definition
`$anchor` keywords (needed only for cross-module references) are dropped.
"""

import json
import re
import sys
from argparse import ArgumentParser
from pathlib import Path

SOURCES = Path(__file__).resolve().parent / "_sources"
MODULES = ["prov", "prov-entity", "prov-activity", "prov-agent"]


EXTERNAL = {
    "bblocks://ogc.ogc-utils.iri-or-curie": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json",
    "bblocks://ogc.ogc-utils.json-link": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json",
}
# Definitions whose $anchor is referenced as `#objectref` inside the bundle
KEEP_ANCHOR = {"objectref"}

# Output ordering of $defs; any definition not listed is appended in module order
ORDER = [
    "objectref",
    "oneOrMoreObjectref",
    "oneOrMoreActivitiesOrRefIds",
    "oneOrMoreEntitiesOrRefIds",
    "oneOrMoreAgentsOrRefIds",
    "externalLink",
    "influenced",
    "Entity",
    "dateTime",
    "Activity",
    "Agent",
    "Usage",
    "ActivityInfluence",
    "Generation",
    "Invalidation",
    "Communication",
    "StartOrEnd",
    "Start",
    "End",
    "Derivation",
    "PrimarySource",
    "Quotation",
    "Revision",
    "Delegation",
    "Attribution",
    "Association",
    "Influence",
    "Prov",
]

MODULE_REF = re.compile(r"^bblocks://ogc\.ogc-utils\.([\w-]+)#(.+)$")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def convert_ref(ref):
    for prefix, url in EXTERNAL.items():
        if ref == prefix or ref.startswith(prefix + "#"):
            return url + ref[len(prefix) :]
    return ref


def convert(node):
    if isinstance(node, list):
        return [convert(n) for n in node]
    if not isinstance(node, dict):
        return node
    out = {}
    for key, value in node.items():
        if key == "$ref" and isinstance(value, str):
            m = MODULE_REF.match(value)
            if m and m.group(1) in MODULES:
                target = m.group(2)
                # `Name` -> #/$defs/Name ; `/$defs/Name` -> #/$defs/Name
                value = "#" + (target if target.startswith("/") else "/$defs/" + target)
            else:
                value = convert_ref(value)
            out[key] = value
        else:
            out[key] = convert(value)
    return out


def bundle():
    modules = {m: load(SOURCES / m / "schema.json") for m in MODULES}
    defs = {}
    for m in MODULES:
        for name, definition in modules[m]["$defs"].items():
            if name in defs:
                raise SystemExit(f"Duplicate definition {name!r} (in {m})")
            definition = convert(definition)
            if name not in KEEP_ANCHOR:
                definition.pop("$anchor", None)
            defs[name] = definition

    ordered = {n: defs[n] for n in ORDER if n in defs}
    ordered.update((n, d) for n, d in defs.items() if n not in ordered)

    root = modules["prov"]
    out = {}
    out["$schema"] = root["$schema"]
    out["description"] = root["description"]
    out["$defs"] = ordered
    out["anyOf"] = convert(root["anyOf"])
    for key, value in root.items():
        if key not in out:
            out[key] = convert(value)
    return json.dumps(out, indent=2, ensure_ascii=False) + "\n"


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit with status 1 if the bundled schema is " "out of date (no write)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output file to write",
        default=SOURCES / "prov-bundled" / "schema.json",
    )
    args = parser.parse_args()
    result = bundle()
    if args.check:
        current = ""
        if args.output and args.output.exists():
            current = args.output.read_text(encoding="utf-8")
        if current != result:
            print(
                f"{args.output} is out of date; run bundle_schema.py", file=sys.stderr
            )
            return 1
        return 0
    args.output.write_text(result, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
