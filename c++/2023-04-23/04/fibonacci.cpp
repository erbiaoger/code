#include <iostream>
using namespace std;

// int fibonacci(int n) {
//     int a = 0, b = 0, sum = 1;
//     for (int i = 0; i < n; i++) {
//         a = b; b = sum; sum = a + b;
//         cout << sum << " ";
//     }
//     return sum;
// }

// int main() {
//     fibonacci(10);

//     return 0;
// }

int fibonacci(int a, int b, int n) {
    int sum;
    while(n--) {
        cout << a << " ";
        sum = a + b; a = b; b = sum; 
        //cout << n << " ";    
        fibonacci(a, b, n);
        //cout << n << " ";
        break;
    }
    return 0;
}

int main() {
    fibonacci(0, 1, 10);

    return 0;
}