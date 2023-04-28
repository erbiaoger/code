#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

void printArray(vector<int> vec);

int main() {
    int arr1[5] = {10, 20, 30, 40, 50};
    int arr2[5] = {5, 15, 25, 35, 45};
    vector<int> vec{5, 15, 25, 35, 45};
    printArray(vec);

    return 0;
}

void printArray(vector<int> vec) {
    cout << "Printing array elements: " << endl;
    for (int i :  vec) {
        cout << i << endl;
    }

}
