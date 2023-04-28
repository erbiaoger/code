// #include <iostream>
// using namespace std;

// class Account {
//     public:
//         int accno;
//         string name;
//         static float rate0fInterest;
//         Account(int accno, string name) {
//             this->accno = accno;
//             this->name = name;
//         }
//         void display() {
//             cout << accno << "\t" << name << "\t" << rate0fInterest << endl;
//         }
// };

// float Account::rate0fInterest = 6.5;

// int main() {
//     Account a1 = Account(201, "Samjay");
//     Account a2 = Account(202, "Calf");
//     a1.display();
//     a2.display();
//     return 0;
// }

#include <iostream>
using namespace std;

class Account {
    public:
        int accno;
        string name;
        static int count;
        Account(int accno, string name) {
            this->accno = accno;
            this->name = name;
            count++;
        }
        void disploy() {
            cout << accno << "\t" << name << endl;
        }
};

int Account::count = 0;

int main() {
    Account a1 = Account(201, "Sanjay");
    Account a2 = Account(202, "Calf");
    Account a3 = Account(203, "Ranjana");
    a1.disploy();
    a2.disploy();
    a3.disploy();

    cout << "Account::count = " << Account::count << endl;

    return 0;
}