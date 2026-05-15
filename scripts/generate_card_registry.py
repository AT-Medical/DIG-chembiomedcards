from __future__ import annotations
"""Scan card metadata YAML files and build the master registry CSV.

Usage:
    python3 generate_card_registry.py --source-dir cards \
        --output cards/registry/cards.master.csv

Walks all <module>/metadata/*.yaml files under source-dir and collects
the defined fields into a CSV.  The script is currently a scaffold; the
actual YAML\u2192CSV mapping is marked with TODO comments.
"""

import argparse
import csv
import sys
from pathlib import Path


FIELDNAMES = [
    "card_id",
    "title",
    "module",
    "chapter",
    "card_type",
    "level",
    "qr_url",
    "lms_url",
    "print_status",
    "web_status",
    "review_status",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build cards.master.csv from YAML metadata files."
    )
    parser.add_argument(
        "--source-dir",
        default="cards",
        metavar="DIR",
        help="Root directory containing module subdirectories (default: cards).",
    )
    parser.add_argument(
        "--output",
        default="cards/registry/cards.master.csv",
        metavar="FILE",
        help="Output CSV file path (default: cards/registry/cards.master.csv).",
    )
    return parser.parse_args()


def load_yaml_metadata(yaml_path: Path) -> dict:
    """Load a single YAML metadata file and return its contents as a dict.

    TODO: Replace with actual yaml.safe_load() call:
        import yaml
        with yaml_path.open(encoding='utf-8') as fh:
            return yaml.safe_load(fh) or {}
    """
    print(f"[TODO] Load YAML: {yaml_path}")
    return {}


def main() -> int:
    args = parse_args()

    source_dir = Path(args.source_dir)
    if not source_dir.is_dir():
        print(f"ERROR: Source directory not found: {source_dir}", file=sys.stderr)
        return 1

    yaml_files = sorted(source_dir.glob("*/metadata/*.yaml"))
    if not yaml_files:
        print(f"No YAML metadata files found under {source_dir}", file=sys.stderr)
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for yaml_path in yaml_files:
        metadata = load_yaml_metadata(yaml_path)
        if not metadata:
            continue
        # TODO: Map metadata fields to FIELDNAMES
        row = {field: metadata.get(field, "") for field in FIELDNAMES}
        rows.append(row)

    with output_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Written {len(rows)} records to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
