

cmake_minimum_required(VERSION 3.20) #Requre cmake 3.20 or higher

project(FirstAPP LANGUAGES C CXX ASM)


add_executable(${PROJECT_NAME} src/main.cpp)