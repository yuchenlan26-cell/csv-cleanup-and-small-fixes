"""Trim CSV cells and remove exact duplicate rows. Uses Python's standard library."""
import argparse
import csv
import json
from pathlib import Path


def clean_csv(source, destination):
    source = Path(source)
    destination = Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError("Choose a different output path to preserve the original.")
    seen = set()
    cleaned = []
    duplicates = 0
    blanks = 0
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, strict=True)
        header = next(reader, None)
        if not header:
            raise ValueError("The CSV must contain a header row.")
        header = [cell.strip() for cell in header]
        if any(not name for name in header) or len(set(header)) != len(header):
            raise ValueError("Headers must be nonempty and unique after trimming.")
        for row in reader:
            values = tuple(cell.strip() for cell in row)
            if not any(values):
                blanks += 1
                continue
            if len(values) != len(header):
                raise ValueError(f"Wrong field count at CSV line {reader.line_num}.")
            if values in seen:
                duplicates += 1
                continue
            seen.add(values)
            cleaned.append(values)
    # Exclusive creation protects any existing output file.
    with destination.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(cleaned)
    return {"rows_written": len(cleaned), "duplicates_removed": duplicates,
            "blank_rows_removed": blanks}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="UTF-8 comma-separated CSV")
    parser.add_argument("output", help="New output file")
    args = parser.parse_args()
    print(json.dumps(clean_csv(args.input, args.output)))
