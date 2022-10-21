import pytest
from exercise import *


def test_validate_number__return_true__when_calling_with_valid_string():
    input_string = '43032780'
    assert(validate_number(input_string))
