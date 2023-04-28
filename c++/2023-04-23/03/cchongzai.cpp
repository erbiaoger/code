#include <iostream>
using namespace std;

class Cal {
    public:
        static int add(int a, int b) {
            return a + b;
        }
        static int add(int a, int b, int c) {
            return a + b + c;
        }
};

class Test {
    private:
        int num;
    public:
        Test(): num(8) {}
        void operator ++() {
            num = num + 2;
        }  
        void Print() {
            cout << "The Count is: " << num;
        }
};

int main() {
    Cal c1;
    cout << c1.add(10, 20) << endl; 
    cout << c1.add(2, 3, 4) << endl;

    Test t1;
    ++t1;
    t1.Print();
    return 0;
}