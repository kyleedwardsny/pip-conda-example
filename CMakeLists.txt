cmake_minimum_required(VERSION 3.27)
project(kyle_hello CXX)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 REQUIRED)

python3_add_library(_kyle_hello_impl MODULE WITH_SOABI impl.cxx)
target_link_libraries(_kyle_hello_impl PRIVATE pybind11::pybind11)
install(TARGETS _kyle_hello_impl DESTINATION kyle_hello)
