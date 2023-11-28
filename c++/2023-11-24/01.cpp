#include <iostream>

using namespace std;

void swapValue(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

void swapReference(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void swapPointer(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {

    int a = 10, b = 20;
    cout << "a = " << a << " b = " << b << endl;
    
    // call by value
    swapValue(a, b);
    cout << "a = " << a << " b = " << b << endl;
     
    // call by reference
    swapReference(a, b);
    cout << "a = " << a << " b = " << b << endl;

    // call by pointer
    swapPointer(&a, &b);
    cout << "a = " << a << " b = " << b << endl;

    
    return 0;
}
