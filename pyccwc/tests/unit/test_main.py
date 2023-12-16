from pathlib import Path

import pytest

from pyccwc.main import process_file

def test_number_of_lines_is_correct(files_and_results: tuple[Path, str]):
    for file, result in files_and_results:
        assert process_file(file, count_lines=True) == result


@pytest.fixture
def files_and_results(tmp_path: Path):
    values = []

    file = tmp_path / "test1.txt"
    file.write_text("A \n piece \n of text.")
    values.append((file, f"3 {file}"))
    return values