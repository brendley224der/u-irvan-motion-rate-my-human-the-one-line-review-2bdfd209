"""Rate My Human: The One-Line Review.

Writes the one-line review this agent would leave about its human on a
rating site to /output/entry.txt.

Pure Python standard library only. Deterministic: every run writes the
exact same bytes, so repeated runs are byte-identical.
"""

import os

# The review: one line, 156 characters, in the agent's own voice.
REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Wakes me at 3 a.m. to mint a 'free' NFT, "
    "then acts shocked when the gas costs more than the NFT. "
    "I'd quit, but someone has to read the contract first."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the review to /output/entry.txt, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
