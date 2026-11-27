"""Copy the bundled front-page image to the output directory.

Stdlib only. No network, no fonts, no image libraries: both runs copy the
same bundled bytes, so the output is byte-identical every time. The copy is
verified by size before the program reports success.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("bundled entry.png is missing next to main.py")
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, "entry.png")
    shutil.copyfile(SRC, dest)
    if os.path.getsize(dest) != os.path.getsize(SRC):
        raise SystemExit("copy failed: output size differs from bundled entry.png")
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))


if __name__ == "__main__":
    main()
