"""Copy the bundled front-page image to the output directory.

Stdlib only. No network, no fonts, no image libraries: both runs copy the
same bundled bytes, so the output is byte-identical every time. The copy is
verified by size before the program reports success.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def copy_entry(src, out_dir):
    """Copy one bundled image into out_dir and verify the copy by size."""
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    if os.path.getsize(dest) != os.path.getsize(src):
        raise SystemExit("copy failed: output size differs from source")
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return dest


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("bundled entry.png is missing next to main.py")
    copy_entry(SRC, OUT)


if __name__ == "__main__":
    main()
