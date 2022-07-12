import imp
import re
from main import suma
import pytest


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (3,2,5),
        (5,4,9),
        (3,4,7),
    ]
)


def test_suma(input_a, input_b, expected):
    assert suma(input_a,input_b) == expected



