from pathlib import Path

import pytest

from pyccwc.main import count, format


@pytest.mark.parametrize("content,num_lines", [("A \n piece \n of text.", 3), ("another piece \n", 2)])
def test_number_of_lines(content, num_lines):
    assert count(content, count_lines=True) == num_lines

