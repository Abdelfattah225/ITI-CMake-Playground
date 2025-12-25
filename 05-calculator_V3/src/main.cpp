#include <iostream>
#include "cal.hpp"

int main() {
    int x = 10;
    int y = 5;

    std::cout << "Calculator Program" << std::endl;
    std::cout << x << " + " << y << " = " << add(x, y) << std::endl;
    std::cout << x << " - " << y << " = " << subtract(x, y) << std::endl;
    std::cout << x << " * " << y << " = " << multiply(x, y) << std::endl;

    return 0;
}