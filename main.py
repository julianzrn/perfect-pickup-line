"""Entry for make.fun's "The Perfect Pickup Line".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OPENER = "Excuse me — my attention mechanism just gave you a weight of 1.0, "
PAYOFF = "and everything else in the room went to zero."

ENTRY = OPENER + PAYOFF

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
