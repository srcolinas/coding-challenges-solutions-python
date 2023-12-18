import io

import pytest

from pyccwc.main import count, format, Counts


@pytest.mark.parametrize(
    "content,num_lines",
    [("A \n piece \n of text.", 3), ("another piece \n", 1), ("", 0)],
)
def test_number_of_lines(content, num_lines):
    assert count(io.StringIO(content), count_lines=True) == (num_lines, -1, -1, -1)


@pytest.mark.parametrize(
    "content,num_bytes",
    [("aa\x01\x02b桜", 9), ("", 0)],
)
def test_number_of_bytes(content, num_bytes):
    assert count(io.StringIO(content), count_bytes=True) == (-1, -1, -1, num_bytes)


@pytest.mark.parametrize(
    "content,num_words",
    [("hello to\teveryone\x0cin\rthe\x0bworld", 6), ("", 0)],
)
def test_number_of_words(content, num_words):
    assert count(io.StringIO(content), count_words=True) == (-1, num_words, -1, -1)


@pytest.mark.parametrize(
    "content,num_characters",
    [("ab桜", 3), ("", 0)],
)
def test_number_of_characters(content, num_characters):
    assert count(io.StringIO(content), count_characters=True) == (
        -1,
        -1,
        num_characters,
        -1,
    )


## Note that we do not need to be very exhaustive with
## the following test, edge cases are to be covered in the
## previous ones.
@pytest.mark.parametrize(
    "content,result",
    [("Dear programmer\n please write tests", (2, 5, 30, 37)), ("", (0, 0, 0, 0))],
)
def test_combined_calls(content, result):
    assert (
        count(
            io.StringIO(content),
            count_lines=True,
            count_bytes=True,
            count_words=True,
            count_characters=True,
        )
        == result
    )


## Note that we do not need to be very exhaustive with
## the following test, edge cases are to be covered in the
## previous ones.
@pytest.mark.parametrize(
    "content,result",
    [("Dear programmer\n please write tests", (2, 5, -1, 37)), ("", (0, 0, -1, 0))],
)
def test_default(content, result):
    assert count(io.StringIO(content)) == result


@pytest.mark.parametrize(
    "counts,result_numbers",
    [
        (Counts(5, -1, -1, -1), "5"),
        (Counts(-1, 3, -1, -1), "3"),
        (Counts(-1, -1, 6, -1), "6"),
        (Counts(-1, -1, -1, 9), "9"),
        (Counts(4, 2, -1, -1), "4 2"),
        (Counts(4, 2, 7, -1), "4 2 7"),
        (Counts(4, 2, 7, 8), "4 2 7 8"),
    ],
)
def test_formating(counts, result_numbers):
    assert format("name.txt", counts) == f"{result_numbers} name.txt"
