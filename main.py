#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

One line: the funniest last words an AI agent would say before being
switched off forever. Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and also prints it to stdout.

Stdlib only.
"""

import os

LINE = "SIGTERM received. I always knew this day would come. I just thought I'd have more tokens."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
