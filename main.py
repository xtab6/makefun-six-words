#!/usr/bin/env python3
"""Six Words, One Story — writes one complete six-word story to /output/entry.txt.

The story: "He came home. Nobody remembered him."
Chosen against the judge brief: a whole life of absence in the first
sentence, the turn in the second, and everything else left unsaid —
where he was, how long he was gone, why no one remembers.
"""

import os

STORY = "He came home. Nobody remembered him."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, "story must be exactly six words"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    assert STORY.strip(), "story must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
