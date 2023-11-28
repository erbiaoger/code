#include <iostream>

using namespace std;

int func1(int &a, int const &b = 20, int &c = 30) {
    return a + b + c;
}

int main() {

    cout << func1(10, 40) << endl;

    return 0;
}