#include <pybind11/pybind11.h>

namespace py = pybind11;

static bool is_palindrome(const std::string& str)
{
  for (std::size_t i = 0; i < str.length() / 2; i++) {
    if (str[i] != str[str.length() - i - 1]) {
      return false;
    }
  }

  return true;
}

PYBIND11_MODULE(_kyle_hello_impl, m) {
  m.def("is_palindrome", is_palindrome, "Check to see if a string is a palindrome");
}
