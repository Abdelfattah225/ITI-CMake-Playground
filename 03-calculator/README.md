

# Calculator - Multiple Source Files

## 📚 Concepts Covered
- Multiple source files in one target
- Include directories with `target_include_directories()`
- Project organization (src/, include/ folders)
- PRIVATE keyword for include directories

## 📁 Structure
```
03-calculator/
├── CMakeLists.txt
├── include/
│   └── calculator.hpp
├── src/
│   ├── main.cpp
│   └── calculator.cpp
└── build/
```

## 📌 Key Commands
```cmake
add_executable(calc src/main.cpp src/calculator.cpp)
target_include_directories(calc PRIVATE ${PROJECT_SOURCE_DIR}/include)
```

## 🔧 Build & Run
```bash
cmake -S . -B build
cmake --build build
./build/calc
```