
# Calculator V4 - Custom Commands & Targets

## 📚 Concepts Covered
- `add_custom_command()` - generate files or post/pre build actions
- `add_custom_target()` - create manual tasks
- CMake cross-platform commands (`${CMAKE_COMMAND} -E`)
- POST_BUILD, PRE_BUILD, PRE_LINK keywords

## 📁 Structure
```
06-calculator_V4/
├── CMakeLists.txt
├── libs/
│   └── calc/
│       ├── CMakeLists.txt
│       ├── include/
│       └── src/
├── src/
│   ├── CMakeLists.txt
│   └── main.cpp
├── bin/                        # Created by POST_BUILD
└── build/
```

## 📌 add_custom_command vs add_custom_target
| Feature | add_custom_command | add_custom_target |
|---------|-------------------|-------------------|
| Runs | Automatically when needed | Manually by user |
| Use case | Generate files, post-build | Named tasks (format, run) |

## 📌 Key Commands
```cmake
# Generate file
add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/version.h
    COMMAND ${CMAKE_COMMAND} -E echo "..." > version.h
)

# Post-build copy
add_custom_command(
    TARGET calc_app POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:calc_app> ${CMAKE_SOURCE_DIR}/bin/
)

# Custom target
add_custom_target(run
    COMMAND $<TARGET_FILE:calc_app>
    DEPENDS calc_app
)
```

## 🔧 Build & Run
```bash
cmake -S . -B build
cmake --build build
cmake --build build --target run    # Run custom target
cmake --build build --target info   # Show info
```