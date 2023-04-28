#include <iostream>
using namespace std;   

int main() {
    int arr[5] = {10, 0, 20, 0, 30};
    for (int i: arr) {
        cout << i << endl;
    }
    return 0;
}