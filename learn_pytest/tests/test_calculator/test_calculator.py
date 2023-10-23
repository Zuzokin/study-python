import pytest

from calculator_app.calc import simple_calculator


@pytest.mark.parametrize(
    "num_1, num_2, operation, expected_result",
    [
        (3, 3, "+", 6),
        (3, 3, "-", 0),
        (3, 3, "*", 9),
        (3, 3, "/", 1),
    ],
)
def test_simple_calculator(num_1, num_2, operation, expected_result):
    result = simple_calculator(num_1, num_2, operation)
    assert result == expected_result
