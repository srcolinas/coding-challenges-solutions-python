import string
from typing import NamedTuple, TextIO


class Counts(NamedTuple):
    lines: int
    words: int
    characters: int
    bytes: int


def count(
    file: TextIO,
    /,
    count_lines: bool = False,
    count_bytes: bool = False,
    count_words: bool = False,
    count_characters: bool = False,
) -> Counts:
    default = (
        not count_lines and not count_bytes and not count_words and not count_characters
    )
    num_bytes = 0 if count_bytes or default else -1
    num_words = 0 if count_words or default else -1
    num_characters = 0 if count_characters else -1
    i = -1
    for i, line in enumerate(file):
        if count_bytes or default:
            num_bytes += len(line.encode())
            num_bytes += 1
        if count_words or default:
            num_words += len(line.split())
        if count_characters:
            old = line
            for w in string.whitespace:
                new = old.replace(w, "")
                old = new
            num_characters += len(new)

    num_lines = -1 if not count_lines and not default else i + 1
    return Counts(num_lines, num_words, num_characters, num_bytes)


def format(filename: str, counts: Counts) -> str:
    result = ""
    for c in counts:
        if c != -1:
            result += f"{c} "
    result += f"{filename}"
    return result


def _cli():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-c", "--bytes", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-m", "--chars", action="store_true")

    args = parser.parse_args()
    print(
        format(
            args.file.name if args.file.name != "<stdin>" else "",
            count(
                args.file,
                count_lines=args.lines,
                count_bytes=args.bytes,
                count_words=args.words,
                count_characters=args.chars,
            ),
        )
    )


if __name__ == "__main__":
    _cli()
