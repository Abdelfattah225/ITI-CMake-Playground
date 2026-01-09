add_executable(calc_app main.cpp )

target_link_libraries(calc_app PRIVATE calc_lib)


add_custom_command(
    TARGET calc_app
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_SOURCE_DIR}/bin
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:calc_app> ${CMAKE_SOURCE_DIR}/bin
    COMMENT "Copying calc_app to bin/"    
)


