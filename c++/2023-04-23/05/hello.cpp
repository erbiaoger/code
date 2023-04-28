#include <iostream>

extern "C" {
    int print_str(const char* str) {
        std::cout << "C++ received string: " << str << std::endl;
        return 10;
    }
}
