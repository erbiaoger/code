#include <iostream>
using namespace std;

class Employee {
    public:
        int id;
        string name;
        float salary;
        Employee(int id, string name, float salary) {
            this->id = id;
            this->name = name;
            this->salary = salary;
        }
        void disploy() {
            cout << id << "\t" << name << "\t" << salary << endl;
        }
};

int main() {
    Employee e1 = Employee(101, "Hema", 890000);
    Employee e2 = Employee(102, "Calf", 59000);
    e1.disploy();
    e2.disploy();

    return 0;
}