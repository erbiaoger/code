#include <iostream>
using namespace std;

class Student {
    public:
        int id;
        string name;  
        void insert(int i, string n) {
            id = i;
            name = n;
        }
        void display() {
            cout << id << "\t" << name << endl;
        }
};


int main() {

    Student s1, s2;
    s1.id = 201;
    s1.name = "xiaoming";
    cout << s1.id << "\t" << s1.name << endl;
    s2.insert(301, "al;skjdl;f");
    s1.display();
    s2.display();

    return 0;
}