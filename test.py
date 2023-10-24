from kyle_hello import is_palindrome, check_palindrome
import pytest


def test_is_palindrome():
    assert is_palindrome("")
    assert is_palindrome("abcba")
    assert is_palindrome("abccba")
    assert not is_palindrome("abbc")


def test_check_palindrome():
    check_palindrome("")
    check_palindrome("abcba")
    check_palindrome("abccba")
    with pytest.raises(ValueError):
        check_palindrome("abbc")
