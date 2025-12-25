cmake_minimum_required(VERSION 3.20)

project(CalculatorV3 VERSION 3.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


add_subdirectory(libs)
add_subdirectory(src)

set(OUTLOCATION ${CMAKE_BINARY_DIR}/generatedFiles/build_info.txt)

add_custom_command(
    OUTPUT ${OUTLOCATION}
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_BINARY_DIR}/generatedFiles
    COMMAND ${CMAKE_COMMAND} -E echo
        "Project name ${PROJECT_NAME}\nProject version ${PROJECT_VERSION}\nBuild time ${data}" > ${OUTLOCATION}
    COMMENT "DISPLAY INFO Generated"
)