from pathlib import Path

def _cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("-l", "--lines", action="store_true")

    args = parser.parse_args()

    if args.lines:
        num_lines = len(args.file.read_text().splitlines())
        print(f"{num_lines} {args.file}")

if __name__ == "__main__":
    _cli()