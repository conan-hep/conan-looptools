cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX Fortran)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test_cmake_fortran test_looptools.F)
target_link_libraries(test_cmake_fortran CONAN_PKG::LoopTools)

add_executable(test_cmake_cpp test_looptools.cpp)
target_link_libraries(test_cmake_cpp CONAN_PKG::LoopTools)
