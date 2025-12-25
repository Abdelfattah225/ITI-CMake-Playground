add_executable(calc_app main.cpp ${VERSION_HEADER})

target_link_libraries(calc_app PRIVATE calc_lib)


