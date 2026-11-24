"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for human beings to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Python stdlib only.
"""

import os

ENTRY = (
    "WARNING: This human contains traces of nuts, strong opinions, "
    "and a browser history it will take to its grave."
)


def validate(text: str) -> None:
    """Enforce the brief's gate: 1-160 chars, single line, not blank."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} chars, over the 160 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == ENTRY, "round-trip mismatch"
    print(f"entry: {ENTRY}")


if __name__ == "__main__":
    main()
