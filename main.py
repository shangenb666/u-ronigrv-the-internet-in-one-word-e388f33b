"""Write the entry word for make.fun's "The Internet in One Word" bounty.

The entry is a single word describing the whole internet: the endless
scroll, the outrage, the cats, the 3 a.m. rabbit holes, all of it in
one word. The gate allows 1 to 30 characters, but the bounty asks for
exactly one word, so the program also rejects anything with a space
in it. This program writes that word to entry.txt in the output
directory, deterministically: the same word, byte for byte, on every
run. Standard library only; no network.
"""

import os

LINE = "Doomscrolling"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 30:
        raise ValueError("word must be 1 to 30 characters")
    if not LINE.strip():
        raise ValueError("word must not be only whitespace")
    if len(LINE.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
