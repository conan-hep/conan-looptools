cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C Fortran)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test_looptools test_looptools.F)
target_link_libraries(test_looptools ${CONAN_LIBS})
