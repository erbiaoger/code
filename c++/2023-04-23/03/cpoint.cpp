#include <iostream>
using namespace std;

// int main() {
//     int number = 30;
//     int *p;
//     p = &number;
//     cout << "number: \t" << number << endl;
//     cout << "&number: \t" << &number << endl;
//     cout << "p: \t\t" << p << endl;
//     cout << "*p: \t\t" << *p << endl;
//     return 0;
// }

int main() {
    int a = 20, b = 10, *p1 = &a, *p2 = &b;
    cout << a << b << *p1 << *p2 << endl;
    *p1 = *p2 + *p1;
    cout << *p1 << endl;
    cout << a << endl;
    
    return 0;
}