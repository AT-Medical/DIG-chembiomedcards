from __future__ import annotations
"""Generate QR codes from a card registry CSV.

Usage:
    python3 generate_qr_codes.py --csv cards/registry/cards.master.csv \
        --output-dir exports/qr --base-url https://chembiomed-cards.de/c/

Requires the 'qrcode' library (pip install qrcode[pil]).
"""

import argparse
import csv
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate QR codes from card registry CSV."
    )
    parser.add_argument(
        "--csv",
        required=True,
        metavar="FILE",
        help="Path to the card registry CSV file (cards.master.csv).",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        metavar="DIR",
        help="Output directory for generated QR code images.",
    )
    parser.add_argument(
        "--base-url",
        default="https://chembiomed-cards.de/c/",
        metavar="URL",
        help="Base URL prefix for QR redirect targets (default: https://chembiomed-cards.de/c/).",
    )
    return parser.parse_args()


def generate_qr_for_card(card_id: str, url: str, output_dir: Path) -> None:
    """Generate a single QR code PNG for the given card ID and URL.

    TODO: Replace this stub with actual qrcode library call:
        import qrcode
        img = qrcode.make(url)
        img.save(output_dir / f"{card_id}.png")
    """
    print(f"[TODO] Generate QR for {card_id} \u2192 {url} \u2192 {output_dir / card_id}.png")


def main() -> int:
    args = parse_args()

    try:
        import qrcode  # noqa: F401
    except ImportError:
        print(
            "ERROR: 'qrcode' library not installed. Run: pip install qrcode[pil]",
            file=sys.stderr,
        )
        return 1

    csv_path = Path(args.csv)
    if not csv_path.is_file():
        print(f"ERROR: CSV file not found: {csv_path}", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            card_id = row.get("card_id", "").strip()
            if not card_id:
                continue
            url = f"{args.base_url.rstrip('/')}/{card_id}"
            generate_qr_for_card(card_id, url, output_dir)
            count += 1

    print(f"Processed {count} cards.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
