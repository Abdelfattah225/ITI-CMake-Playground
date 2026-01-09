cmake_minimum_required(VERSION 3.20)
project(FindProgramDemo)

find_program(GIT_EXECUTABLE NAMES git)

# Find Python

find_program(PYTHON_EXECUTABLE NAMES python python3)

find_program(CLANG_FORMAT NAMES clang-format)


message(STATUS "git : ${GIT_EXECUTABLE}")

message(STATUS "python : ${PYTHON_EXECUTABLE}")

message(STATUS "format : ${CLANG_FORMAT}")