cmake_minimum_required(VERSION 3.20)

project(CalculatorLib VERSION 2.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(calc_lib STATIC src/cal.cpp)

target_include_directories(calc_lib PUBLIC ${PROJECT_SOURCE_DIR}/inc)

add_executable(calc_app src/main.cpp)

target_link_libraries(calc_app PRIVATE calc_lib)
