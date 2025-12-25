cmake_minimum_required(VERSION 3.20)

project(HelloCMake VERSION 1.0.0 LANGUAGES CXX)


# Set C++ standard

set(CMAKE_CXX_STANDARD 17) #use c++17
set(CMAKE_CXX_STANDARD_REQUIRED ON) #fail if the compiler does not supported it
set(CMAKE_CXX_EXTENSIONS OFF) # Don't use compiler specific extenstions

set(AUTHER_NAME "Abdo")


message(STATUS "Project name : ${PROJECT_NAME}")
message(STATUS "Project version : ${PROJECT_VERSION}")
message(STATUS "Author name : ${AUTHER_NAME}")
message(STATUS "Source directory : ${PROJECT_SOURCE_DIR}")
message(STATUS "Build directory : ${PROJECT_BINARY_DIR}")




add_executable(hello_app main.cpp)