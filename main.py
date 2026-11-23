"""One Emoji, One Smile — entry writer.

Writes exactly one emoji, the hugging face (U+1F917), to entry.txt in the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default /output). The file holds the emoji alone: UTF-8, no trailing
newline, nothing else.

End-to-end check: verified by running — the written file decodes as UTF-8,
is exactly 1 character and 4 bytes (f0 9f a4 97), is not whitespace-only,
and has no trailing newline.
"""

import os

EMOJI = "\U0001F917"  # hugging face


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(EMOJI)


if __name__ == "__main__":
    main()
