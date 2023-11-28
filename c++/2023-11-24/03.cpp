#include <iostream>
#define PI 3.14
using namespace std;

class Circle {
    private:
        // 属性
        double radius;
    
    // 公共权限
    public:
        Circle(double radius) {
            this->radius = radius;
        }
        double getRadius() {
            return radius;
        }
        void setRadius(double radius) {
            this->radius = radius;
        }
        double getArea() {
            return 3.14 * radius * radius;
        }
        double getCalculate() {
            return 2 * PI * radius;
        }
};

int main() {

    Circle c1(10); 
    cout << "c1的半径为：" << c1.getRadius() << endl;
    cout << "c1的周长为：" << c1.getCalculate() << endl;

    system("pause");
    return 0;
}