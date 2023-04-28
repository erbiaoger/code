#include <iostream>
using namespace std;

int main() {
    int test[3][3] = {{5, 10, 15}, 
                      {20, 25, 30}, 
                      {35, 40, 45}};
    
    for (int i: test[1]) {
        cout << i << endl;
    }

    return 0;
}