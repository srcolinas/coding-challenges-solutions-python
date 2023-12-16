from pathlib import Path


def count(content: str, *, count_lines: bool) -> int:
    result = -1
    if count_lines:
        result = len(content.splitlines())
    return result


def format(file: Path, count: int) -> str:
    return f"{count} {file}"


def _cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("-l", "--lines", action="store_true")

    args = parser.parse_args()
    print(format(args.file, count(args.file.read_text(), count_lines=args.lines)))


if __name__ == "__main__":
    _cli()
