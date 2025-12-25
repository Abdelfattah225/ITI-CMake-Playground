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

### ⏳ In Progress

| # | Topic | Description |
|---|-------|-------------|
| 7 | Options & Configuration | User-configurable build options with option() |

### 📅 Upcoming Topics

| # | Topic | Description |
|---|-------|-------------|
| 8 | find_package | Finding and using external libraries |
| 9 | FetchContent | Downloading dependencies automatically |
| 10 | Generator Expressions | Build-time conditional expressions |
| 11 | Interface Libraries | Header-only libraries |
| 12 | Toolchain Files | Cross-compilation setup |
| 13 | CTest | Testing integration |
| 14 | Installation Rules | install() command and targets |
| 15 | CPack | Creating distributable packages |
| 16 | Debugging CMake | Troubleshooting configuration issues |
| 17 | Build Optimization | Improving build performance |
| 18 | Code Review & Patterns | Best practices and anti-patterns |

---

## 📁 Repository Structure
iti-cmake-playground/
├── README.md
├── 01-getting_start/ # CMake basics
├── 02-hello_cmake/ # First CMake project
├── 03-calculator/ # Multiple source files
├── 04-calculatorV2/ # Static libraries
├── 05-calculator_V3/ # Subdirectories
├── 06-calculator_V4/ # Custom commands & targets
└── ... # More to come!
