from __future__ import annotations
"""Export a batch of printable card files from a registry CSV and HTML/SVG template.

Usage:
    python3 export_print_batch.py --csv cards/registry/cards.master.csv \
        --template card-system/templates/card-template-front.html \
        --output-dir exports/pdf --format pdf

Supported formats: html, svg, pdf (PDF requires weasyprint or equivalent).
"""

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export printable card files for a batch from the registry."
    )
    parser.add_argument(
        "--csv",
        required=True,
        metavar="FILE",
        help="Path to the card registry CSV (cards.master.csv).",
    )
    parser.add_argument(
        "--template",
        required=True,
        metavar="FILE",
        help="Path to the HTML or SVG card template file.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        metavar="DIR",
        help="Directory to write exported files into.",
    )
    parser.add_argument(
        "--format",
        choices=["html", "svg", "pdf"],
        default="pdf",
        help="Output format: html, svg, or pdf (default: pdf).",
    )
    return parser.parse_args()


def export_card(
    card_id: str,
    template_path: Path,
    output_dir: Path,
    fmt: str,
) -> None:
    """Export a single card using the provided template.

    TODO: Implement template variable substitution and rendering:
      1. Load template from template_path
      2. Replace placeholders ({{card_id}}, {{title}}, {{module}}, ...)
      3. Write rendered HTML/SVG to output_dir / f"{card_id}.{fmt}"
      4. If fmt == 'pdf', convert via weasyprint or headless chromium
    """
    output_file = output_dir / f"{card_id}.{fmt}"
    print(f"[TODO] Export {card_id} \u2192 {output_file}")


def main() -> int:
    args = parse_args()

    csv_path = Path(args.csv)
    if not csv_path.is_file():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        return 1

    template_path = Path(args.template)
    if not template_path.is_file():
        print(f"ERROR: Template not found: {template_path}", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    import csv

    count = 0
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            card_id = row.get("card_id", "").strip()
            if not card_id:
                continue
            export_card(card_id, template_path, output_dir, args.format)
            count += 1

    print(f"Exported {count} cards to {output_dir} (format: {args.format})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
