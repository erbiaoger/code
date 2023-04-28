// #include <iostream>
// using namespace std;

// struct Rectangle {
//     int width, height;
// };

// int main() {
//     struct Rectangle rec;
//     rec.width = 8;
//     rec.height = 5;
//     cout << "Area of Rectangle is: " << rec.width * rec.height << endl;
//     return 0;
// }
#include <iostream>
using namespace std;

struct Rectangle {
    int width, height;
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }
    void area0fRectangle() {
        cout << "Area of Rectangle is: " << width * height << endl;
    }
};

int main() {
    struct Rectangle rec = Rectangle(4, 6);
    rec.area0fRectangle();
    
    return 0;
}