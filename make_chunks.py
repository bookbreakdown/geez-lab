#!/usr/bin/env python3
"""Index and optionally download Ma IX 1 images for Ge'ez Lab.

Project: https://ethiopiancanon.com
Code: MIT. Images retain the library's source terms; see docs/SOURCES.md.
Book allocations are provisional catalogue labels, not text identifications.
"""

import argparse
import csv
import sys
import urllib.error
import urllib.request
from pathlib import Path

LAB = Path(__file__).resolve().parent
IIIF = "https://opendigi.ub.uni-tuebingen.de/opendigi/image/MaIX1/MaIX1_{c}.jp2/full/{w},/0/default.jpg"
BOOKS = [
    ("IV", 152, "r", 205, "v"),
    ("V", 206, "r", 216, "r"),
    ("VI", 216, "v", 241, "r"),
    ("VII", 241, "r", 276, "r"),
]


def canvas(folio, side):
    return (folio - 1) * 2 + 7 + (1 if side.lower() == "v" else 0)


def sides(first, first_side, last, last_side):
    current = (first, first_side)
    while True:
        yield current
        if current == (last, last_side):
            return
        folio, side = current
        current = (folio, "v") if side == "r" else (folio + 1, "r")


def build_index(width=1700):
    records = {}
    for book, first, first_side, last, last_side in BOOKS:
        for folio, side in sides(first, first_side, last, last_side):
            code = f"MAIX1-{folio}{side.upper()}"
            if code in records:
                records[code]["catalogue_books"] += ";" + book
                continue
            number = canvas(folio, side)
            records[code] = {
                "code": code,
                "catalogue_books": book,
                "folio": f"{folio}{side}",
                "canvas": number,
                "image_url": IIIF.format(c=number, w=width),
            }
    return list(records.values())


def jpeg_transport_ok(data):
    """Catch empty, truncated and HTML responses; not a full image decoder."""
    return len(data) > 4 and data.startswith(b"\xff\xd8\xff") and data.endswith(b"\xff\xd9")


def fetch_image(url, destination, opener=urllib.request.urlopen):
    temporary = destination.with_suffix(".jpg.part")
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "GeezLab/preview (https://ethiopiancanon.com)"})
        with opener(request, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
            if content_type != "image/jpeg":
                raise ValueError(f"expected image/jpeg, received {content_type or 'no content type'}")
            data = response.read()
        if not jpeg_transport_ok(data):
            raise ValueError("response is empty, truncated, or not a JPEG")
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary.write_bytes(data)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def write_csv(path, records):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", type=int, default=0, metavar="N", help="attempt at most N new downloads (default: index only)")
    parser.add_argument("--width", type=int, default=1700, help="requested image width, in pixels")
    parser.add_argument("--only", metavar="CODE", help="download only this manuscript side")
    args = parser.parse_args(argv)
    if args.download < 0 or args.width < 1:
        parser.error("--download must be nonnegative and --width must be positive")
    rows = build_index(args.width)
    if args.only and args.only not in {r["code"] for r in rows}:
        parser.error("--only must name a side from MAIX1-152R through MAIX1-276R")

    # Width-specific directories prevent resuming a different-resolution trial.
    out = LAB / "chunks" / str(args.width)
    attempted = failed = 0
    for row in rows:
        destination = out / (row["code"] + ".jpg")
        present = destination.exists() and jpeg_transport_ok(destination.read_bytes())
        row["status"] = "have" if present else "pending"
        if present or attempted >= args.download or (args.only and row["code"] != args.only):
            continue
        attempted += 1
        try:
            fetch_image(row["image_url"], destination)
            row["status"] = "have"
        except (OSError, urllib.error.URLError, ValueError) as exc:
            failed += 1
            row["status"] = "FAILED"
            print(f"{row['code']}: {exc}", file=sys.stderr)
        else:
            print(f"{row['code']}: downloaded")
    write_csv(LAB / "chunks-index.csv", rows)
    have = sum(row["status"] == "have" for row in rows)
    print(f"{len(rows)} unique sides indexed; {have} images present at {args.width}px; {failed} failed requests")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
