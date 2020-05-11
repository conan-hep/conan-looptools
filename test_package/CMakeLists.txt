cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C Fortran)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(LoopTools REQUIRED)

message("${CONAN_LIBS}")

add_executable(test_looptools_f test_looptools.F)
target_link_libraries(test_looptools_f ${CONAN_LIBS})

add_executable(test_looptools_c test_looptools.c)
target_link_libraries(test_looptools_c ${CONAN_LIBS})
