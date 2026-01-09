cmake_minimum_required(VERSION 3.20)

project(CalculatorV4 VERSION  4.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


add_subdirectory(libs)
add_subdirectory(src)


# TODO: Add custom target "info" that prints:
#   - Project name
#   - Project version

add_custom_target(info
    COMMAND ${CMAKE_COMMAND} -E echo "============================="
    COMMAND ${CMAKE_COMMAND} -E echo "Project Name: ${PROJECT_NAME}" 
    COMMAND ${CMAKE_COMMAND} -E echo "Project Version: ${PROJECT_VERSION}"
    COMMAND ${CMAKE_COMMAND} -E echo "============================="
    COMMENT  "Showing Project info"
)
# TODO: Add custom target "run" that:
#   - Depends on calc_app
#   - Runs calc_app

add_custom_target(run

    COMMAND $<TARGET_FILE:calc_app>
    DEPENDS calc_app
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Running my calc_app"
)