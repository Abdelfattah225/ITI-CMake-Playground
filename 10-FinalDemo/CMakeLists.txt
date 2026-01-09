cmake_minimum_required(VERSION 3.20)

project(FinalDemo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)



find_program(GIT_EXECUTABLE NAMES git)

if(GIT_EXECUTABLE)
    message(STATUS "Git Found: ${GIT_EXECUTABLE}")
else()
    message(STATUS "Git NOT found")
endif()



find_package(Threads REQUIRED)
message(STATUS "Threads found")

find_package(ZLIB)

if(ZLIB_FOUND)
    message(STATUS "ZLIB FOUND")
else()
    message(STATUS "NOT FOUND")
endif()


add_executable(app main.cpp)


target_link_libraries(app PRIVATE Threads::Threads)


if(ZLIB_FOUND)
    target_link_libraries(app PRIVATE ZLIB::ZLIB)
    target_compile_definitions(app PRIVATE HAS_ZLIB)
endif()

