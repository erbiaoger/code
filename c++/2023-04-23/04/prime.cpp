#include <iostream>
using namespace std;

bool is_prime(int number) {
    static int i = number/2 + 1;
    while (i-- != 2) {
        cout << i ;
        if (number % i == 0)
            return false;
    }
    return true;
}

int prime() {
    int number;

    cout << "Please a number." << endl;
    while (number != 0) {
        cout << "Please a number. Or quit enter 0" << endl;
        cin >> number;
        if (is_prime(number) == true)
            cout << number << "is prime" << endl;
        else
            cout << number << "is not prime" << endl;
    }
    return 0;
}


int main() {
    prime();
    
    return 0;
}