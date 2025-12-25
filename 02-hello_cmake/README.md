
# Hello CMake - First Project

## 📚 Concepts Covered
- Minimum CMakeLists.txt structure
- `cmake_minimum_required()` - version requirement
- `project()` - project declaration
- `add_executable()` - create executable

## 📁 Structure
```
02-hello_cmake/
├── CMakeLists.txt
├── main.cpp
└── build/
```

## 📌 Minimal CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(HelloCMake LANGUAGES CXX)
add_executable(hello_app main.cpp)
```

## 🔧 Build & Run
```bash
cmake -S . -B build
cmake --build build
./build/hello_app
```