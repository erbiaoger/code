#include <iostream>

using namespace std;


class Circle {
    private:
        double radius;
    public:
        Circle(double r) {
            this->radius = r;
        }
        double getRadius() {
            cout << "半径为：" << this->radius << endl;
            return this->radius;
        }
};

int main() {
    Circle c1(10);
    c1.getRadius();
    
    system("pause");
    return 0;
}