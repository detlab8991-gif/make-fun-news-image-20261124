"""Copy the entry image to the output location.

This program takes the file entry.jpg that sits in the same directory
as this script and copies it to /output/entry.png. It creates the
output directory when needed, refuses to continue when the source
image is missing, and checks that the copy has exactly the same
number of bytes as the original before reporting success. It needs
no network access and reads no file other than the entry image.
"""

import os
import shutil
import sys


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.jpg")
    destination_dir = "/output"
    destination = os.path.join(destination_dir, "entry.png")

    if not os.path.isfile(source):
        print("error: source image not found: " + source, file=sys.stderr)
        sys.exit(1)

    os.makedirs(destination_dir, exist_ok=True)

    shutil.copyfile(source, destination)

    source_size = os.path.getsize(source)
    destination_size = os.path.getsize(destination)
    if destination_size != source_size:
        print(
            "error: size mismatch after copy: source "
            + str(source_size)
            + " bytes, destination "
            + str(destination_size)
            + " bytes",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Wrote " + destination + " (" + str(destination_size) + " bytes)")


if __name__ == "__main__":
    main()
