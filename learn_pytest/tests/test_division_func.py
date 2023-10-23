from my_funcs.utils import division
import pytest

xfail = pytest.mark.xfail


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (10, 2, 5),
        (20, 10, 2),
        (30, -3, -10),
        (5, 2, 2.5),
        (3, 4, 0.75),
    ],
)
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize(
    "expected_exception, a, b",
    [
        (ZeroDivisionError, 4, 0),
        (TypeError, "4", 2),
        (TypeError, 4, "2"),
        # (None, 4, 2),
    ],
)
def test_division_with_error(expected_exception, a, b):
    with pytest.raises(expected_exception):
        division(a, b)


@pytest.mark.xfail
@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (10, 2, 3),
        (20, 10, 1),
        (30, -3, -19),
        (5, 2, 2.3),
        (4, 0, 0),
        ("4", 2, 2),
        (4, "2", 2),
    ],
)
def test_division_bad(a, b, expected_result):
    assert division(a, b) == expected_result
