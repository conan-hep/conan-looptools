cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C Fortran)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test_looptools_f test_looptools.F)
target_link_libraries(test_looptools_f CONAN_PKG::LoopTools)

add_executable(test_looptools_c test_looptools.c)
target_link_libraries(test_looptools_c CONAN_PKG::LoopTools)
