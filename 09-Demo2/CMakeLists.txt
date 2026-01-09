cmake_minimum_required(VERSION 3.20)
project(FindPackageDemo LANGUAGES CXX)





find_package(Threads REQUIRED)

add_executable(app main.cpp)


target_link_libraries(app PRIVATE Threads::Threads)