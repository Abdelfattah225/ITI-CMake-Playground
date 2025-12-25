

# Calculator V2 - Static Libraries

## 📚 Concepts Covered
- Creating static libraries with `add_library()`
- STATIC vs SHARED libraries
- Linking libraries with `target_link_libraries()`
- PUBLIC vs PRIVATE keywords
  - PUBLIC: propagates to consumers
  - PRIVATE: only for this target

## 📁 Structure
```
04-calculatorV2/
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
add_library(calc_lib STATIC src/calculator.cpp)
target_include_directories(calc_lib PUBLIC ${PROJECT_SOURCE_DIR}/include)

add_executable(calc_app src/main.cpp)
target_link_libraries(calc_app PRIVATE calc_lib)
```

## 📌 STATIC vs SHARED
| Type | Extension | Code Location |
|------|-----------|---------------|
| STATIC | .a / .lib | Copied INTO executable |
| SHARED | .so / .dll | Stays SEPARATE |

## 🔧 Build & Run
```bash
cmake -S . -B build
cmake --build build
./build/calc_app
```