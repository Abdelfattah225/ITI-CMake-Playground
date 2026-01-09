cmake_minimum_required(VERSION 3.16)
project(BuildInfoDemo VERSION 1.0.0 LANGUAGES CXX)



set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


message(STATUS "Generator: ${CMAKE_GENERATOR}")
message(STATUS "Binary Dir: ${CMAKE_BINARY_DIR}")
message(STATUS "Source Dir: ${CMAKE_SOURCE_DIR}")


add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/build_info.h
    COMMAND python3 ${CMAKE_SOURCE_DIR}/scripts/generate_buildinfo.py
        --output ${CMAKE_BINARY_DIR}/build_info.h
        --generator "${CMAKE_GENERATOR}"
    DEPENDS ${CMAKE_SOURCE_DIR}/scripts/generate_buildinfo.py
    COMMENT "Generating build_info.h..."
    )

add_custom_target(buildInfo
DEPENDS ${CMAKE_BINARY_DIR}/build_info.h
)

add_executable(myapp src/main.cpp )

add_dependencies(myapp buildInfo)


# Tell compiler: "Also look in build directory for headers"
target_include_directories(myapp PRIVATE ${CMAKE_BINARY_DIR})