#include <iostream>
using namespace std;

class Student {
    public:
        Student(string name, int age, int score, int Id) {
            this->name = name;
            this->age = age;
            this->score = score;
            this->Id = Id;
        }

        string name;
        int Id;
        int age;
        int score;

        void show() {
            cout << "name: " << name << endl;
            cout << "Id: " << Id << endl;
            cout << "age: " << age << endl;
            cout << "score: " << score << endl;
        }
};



int main() {

    Student student1("张三", 18, 100, 1);
    Student student2("李四", 19, 99, 2);

    student1.show();
    student2.show();

    student1.name = "王五";
    student1.show();

    system("pause");
    return 0;
}