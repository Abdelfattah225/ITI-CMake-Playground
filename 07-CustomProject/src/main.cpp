#include <iostream>
#include "build_info.h"

int main() {
    std::cout << "=== Build Information ===" << std::endl;
    std::cout << "Timestamp: " << BUILD_TIMESTAMP << std::endl;
    std::cout << "Generator: " << BUILD_GENERATOR << std::endl;
    return 0;
}