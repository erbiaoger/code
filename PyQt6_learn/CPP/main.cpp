#include <iostream>
#include "forA.h"
using namespace std;


int main() {
    cout << "Hello, World!" << endl;
    // auto aa {10};
    // auto sum {0.0};
    int aa = 10;
    float sum = 0.0;
    sum = forA(aa);
    cout << "aa: " << aa << endl;
    cout << "sum: " << sum << endl;
    return 0;
    }