
# Calculator V3 - Subdirectories

## 📚 Concepts Covered
- Multi-directory project structure
- `add_subdirectory()` command
- `CMAKE_SOURCE_DIR` vs `CMAKE_CURRENT_SOURCE_DIR`
- Each folder has its own CMakeLists.txt

## 📁 Structure
```
05-calculator_V3/
├── CMakeLists.txt              # Root
├── libs/
│   ├── CMakeLists.txt          # Libs handler
│   └── calc/
│       ├── CMakeLists.txt      # Library
│       ├── include/
│       │   └── calculator.hpp
│       └── src/
│           └── calculator.cpp
├── src/
│   ├── CMakeLists.txt          # App
│   └── main.cpp
└── build/
```

## 📌 Key Variables
| Variable | Meaning |
|----------|---------|
| `CMAKE_SOURCE_DIR` | Always root folder |
| `CMAKE_CURRENT_SOURCE_DIR` | Current CMakeLists.txt folder |

## 📌 Root CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(CalculatorV3 VERSION 3.0.0 LANGUAGES CXX)

add_subdirectory(libs)
add_subdirectory(src)
```

## 🔧 Build & Run
```bash
cmake -S . -B build
cmake --build build
./build/src/calc_app
```