from ._kyle_hello_impl import is_palindrome


def check_palindrome(s):
    if not is_palindrome(s):
        raise ValueError(f"String \"{s}\" is not a palindrome")
