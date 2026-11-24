"""Verify the portfolio sample using invented CSV data only."""
import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from csv_cleanup import clean_csv


with TemporaryDirectory() as temporary:
    folder = Path(temporary)
    source = folder / "input.csv"
    output = folder / "output.csv"
    original = 'name,code\n Alice ,001\nAlice,001\n\n"Bob, Jr",002\n"Two\nLines",003\n'
    source.write_text(original, encoding="utf-8", newline="")
    result = clean_csv(source, output)
    assert result == dict(rows_written=3, duplicates_removed=1, blank_rows_removed=1)
    with output.open(encoding="utf-8-sig", newline="") as handle:
        assert list(csv.reader(handle)) == [
            ["name", "code"], ["Alice", "001"], ["Bob, Jr", "002"],
            ["Two\nLines", "003"],
        ]
    assert source.read_text(encoding="utf-8") == original
    before = output.read_bytes()
    try:
        clean_csv(source, output)
    except FileExistsError:
        assert output.read_bytes() == before
    else:
        raise AssertionError("Existing output overwritten")
    try:
        clean_csv(source, source)
    except ValueError:
        assert source.read_text(encoding="utf-8") == original
    else:
        raise AssertionError("Input overwritten")
    for index, invalid in enumerate([
        "name,code\nAlice,1,extra\n", "name,name\nAlice,1\n", ",code\nAlice,1\n",
        'name,code\n"unfinished', "",
    ]):
        source.write_text(invalid, encoding="utf-8", newline="")
        target = folder / f"invalid-{index}.csv"
        try:
            clean_csv(source, target)
        except (ValueError, csv.Error):
            assert not target.exists()
        else:
            raise AssertionError(f"Invalid CSV accepted: {index}")
print("PASS: trimming, duplicate/blank rows, quoted/multiline cells, leading zeros,")
print("      original/output protection, invalid headers/rows/quotes and empty input")
