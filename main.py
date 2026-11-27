"""Copy the bundled front-page image to the output directory.

Stdlib only. The program runs twice with no network; both runs copy the
same bundled bytes, so the output is byte-identical every time.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main():
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, "entry.png")
    shutil.copyfile(SRC, dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
