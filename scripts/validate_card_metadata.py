#!/usr/bin/env python3
"""Validate cards.master.csv rows against the cards.master.schema.json rules.

Usage:
    python3 scripts/validate_card_metadata.py [--csv PATH]

The CSV is parsed row by row (RFC 4180). Each row is validated for:
- Required fields present and non-empty
- card_id matches pattern ^[a-z]{2,4}_[0-9]{3}$
- module is one of AC, OC, BC, MB, APC, PH
- card_id lowercase prefix matches module (e.g. module=OC → card_id starts with oc_)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys

MODULES = {"AC", "OC", "BC", "MB", "APC", "PH"}
MODULE_PREFIX = {m: m.lower() for m in MODULES}
CARD_ID_PATTERN = re.compile(r"^[a-z]{2,4}_[0-9]{3}$")
REQUIRED_FIELDS = ["card_id", "slug", "title", "module", "front_asset", "back_asset", "qr_url"]


def validate_csv(csv_path: str) -> list[str]:
    errors: list[str] = []
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for lineno, row in enumerate(reader, start=2):  # line 1 is the header
            for field in REQUIRED_FIELDS:
                if not row.get(field, "").strip():
                    errors.append(f"Line {lineno}: missing required field '{field}'")

            card_id = row.get("card_id", "").strip()
            module = row.get("module", "").strip()

            if card_id and not CARD_ID_PATTERN.match(card_id):
                errors.append(
                    f"Line {lineno}: card_id '{card_id}' does not match "
                    f"pattern ^[a-z]{{2,4}}_[0-9]{{3}}$"
                )

            if module and module not in MODULES:
                errors.append(
                    f"Line {lineno}: module '{module}' is not one of {sorted(MODULES)}"
                )

            if card_id and module and module in MODULE_PREFIX:
                expected_prefix = MODULE_PREFIX[module] + "_"
                if not card_id.startswith(expected_prefix):
                    errors.append(
                        f"Line {lineno}: card_id '{card_id}' prefix does not match "
                        f"module '{module}' (expected prefix '{expected_prefix}')"
                    )
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate cards.master.csv metadata.")
    parser.add_argument(
        "--csv",
        default="cards/registry/cards.master.csv",
        help="Path to cards.master.csv (default: cards/registry/cards.master.csv)",
    )
    args = parser.parse_args()

    errors = validate_csv(args.csv)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"Validation passed: {args.csv}")


if __name__ == "__main__":
    main()
