# ITI CMake Playground 🛠️

A hands-on learning repository for mastering CMake - from fundamentals to advanced usage.

## 📖 Description

This repository contains progressive exercises and examples for learning CMake, the cross-platform build system generator. Each folder builds upon the previous one, introducing new concepts while reinforcing earlier lessons.

**Learning Approach:**
- Step-by-step concept explanations
- Quick knowledge checks
- Practical tasks with real code
- Code review and feedback

---

## 📊 Progress Roadmap

### ✅ Completed

| # | Folder | Topic | Concepts |
|---|--------|-------|----------|
| 1 | `01-getting_start` | CMake Basics | Meta-build system, configure & build phases |
| 2 | `02-hello_cmake` | First Project | cmake_minimum_required, project, add_executable |
| 3 | `03-calculator` | Multiple Files | Multiple sources, target_include_directories, PRIVATE |
| 4 | `04-calculatorV2` | Static Libraries | add_library, STATIC vs SHARED, target_link_libraries, PUBLIC vs PRIVATE |
| 5 | `05-calculator_V3` | Subdirectories | add_subdirectory, CMAKE_SOURCE_DIR vs CMAKE_CURRENT_SOURCE_DIR |
| 6 | `06-calculator_V4` | Custom Commands | add_custom_command, add_custom_target, POST_BUILD |
| 7 | `07-CustomProject` | Advanced Custom Commands | Python scripts, generate headers, build info |
| 8 | `08-Demo1` | find_program | Finding executables (git, python) |
| 9 | `09-Demo2` | find_package Basics | Finding packages (Threads) |
| 10 | `10-FinalDemo` | find_package Advanced | Threads, ZLIB, optional dependencies, compile definitions |

### 📅 Upcoming Topics

| # | Topic | Description |
|---|-------|-------------|
| 11 | FetchContent | Downloading dependencies automatically |
| 12 | Generator Expressions | Build-time conditional expressions |
| 13 | Interface Libraries | Header-only libraries |
| 14 | Options & Configuration | User-configurable build options with option() |
| 15 | Toolchain Files | Cross-compilation setup |
| 16 | CTest | Testing integration |
| 17 | Installation Rules | install() command and targets |
| 18 | CPack | Creating distributable packages |
| 19 | Debugging CMake | Troubleshooting configuration issues |
| 20 | Code Review & Patterns | Best practices and anti-patterns |

---

## 📁 Repository Structure

```
iti-cmake-playground/
├── README.md
├── 01-getting_start/        # CMake basics
├── 02-hello_cmake/          # First CMake project
├── 03-calculator/           # Multiple source files
├── 04-calculatorV2/         # Static libraries
├── 05-calculator_V3/        # Subdirectories
├── 06-calculator_V4/        # Custom commands & targets
├── 07-CustomProject/        # Advanced custom commands
├── 08-Demo1/                # find_program
├── 09-Demo2/                # find_package basics
├── 10-FinalDemo/            # find_package advanced
└── ...                      # More to come!
```

---

## 🔧 Quick Reference

### Essential Commands

```bash
# Configure project
cmake -S . -B build

# Build project
cmake --build build

# Build specific target
cmake --build build --target <target_name>

# Clean build
rm -rf build/
```

### Common CMake Commands

| Command | Purpose |
|---------|---------|
| `cmake_minimum_required()` | Set minimum CMake version |
| `project()` | Declare project name and language |
| `add_executable()` | Create executable target |
| `add_library()` | Create library target |
| `target_include_directories()` | Set include paths |
| `target_link_libraries()` | Link libraries to target |
| `add_subdirectory()` | Include subdirectory |
| `add_custom_command()` | Add custom build step |
| `add_custom_target()` | Create custom target |
| `find_program()` | Find executable on system |
| `find_package()` | Find and use external library |

### Visibility Keywords

| Keyword | Used by Target | Propagated to Consumers |
|---------|----------------|------------------------|
| PRIVATE | ✅ Yes | ❌ No |
| PUBLIC | ✅ Yes | ✅ Yes |
| INTERFACE | ❌ No | ✅ Yes |

---

## 📚 Key Concepts Summary

### 1. CMake is a Meta-Build System
CMake doesn't compile code - it generates build files for other tools (Make, Ninja, Visual Studio).

### 2. Targets are Central
Everything revolves around targets (executables, libraries). Modern CMake is target-based.

### 3. Two-Phase Process
```
Configure (cmake -S . -B build) → Build (cmake --build build)
```

### 4. Out-of-Source Builds
Always build in a separate `build/` directory to keep source clean.

### 5. Finding External Dependencies
```cmake
find_program(GIT NAMES git)           # Find executables
find_package(Threads REQUIRED)         # Find libraries
target_link_libraries(app Threads::Threads)  # Link using imported targets
```

---

## 🛠️ Prerequisites

- CMake 3.20 or higher
- C++ compiler (GCC, Clang, or MSVC)
- Basic C++ knowledge
