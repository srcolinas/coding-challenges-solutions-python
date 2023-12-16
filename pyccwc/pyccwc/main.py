from pathlib import Path

def process_file(file: Path, *, count_lines: bool) -> str:
    result = ""
    if count_lines:
        num_lines = len(file.read_text().splitlines())
        result = f"{num_lines} {file}"
    return result


def _cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("-l", "--lines", action="store_true")

    args = parser.parse_args()

    print(process_file(args.file, count_lines=args.lines))


if __name__ == "__main__":
    _cli()
