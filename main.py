"""Write the 24 November 2026 news image to the grader's output path.

The entry image lives in this repository as entry.jpg. This program
copies it byte for byte to /output/entry.png, creating the output
directory first if it is missing. It makes no network requests, reads
no other file, and produces identical bytes on every run. The copy is
checked by comparing the byte counts of source and destination.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.jpg"
DESTINATION = Path("/output/entry.png")


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing: {SOURCE}")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    written = DESTINATION.stat().st_size
    if written != SOURCE.stat().st_size:
        raise SystemExit(f"copy incomplete: wrote {written} bytes")
    print(f"wrote {DESTINATION} ({written} bytes)")


if __name__ == "__main__":
    main()
