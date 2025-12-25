

# Getting Started with CMake

## 📚 Concepts Covered
- What is CMake (meta-build system)
- CMake generates build files for other tools (Make, Ninja, Visual Studio)
- Two-phase process: Configure → Build

## 🔧 Key Commands
```bash
cmake -S . -B build      # Configure
cmake --build build      # Build
```

## 📌 Key Takeaways
- CMake doesn't compile code directly
- CMake translates CMakeLists.txt into native build files
```

