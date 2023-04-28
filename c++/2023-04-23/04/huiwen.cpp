#include <iostream>
using namespace std;

bool is_huiwen(long int num) {
    string str;
    str = to_string(num);
    int len = size(str);
    for (int i = 0; i < len; i++) {
        if (str[i] != str[len-1-i])
            return false;
    }
    return true;
}

int main() {
    long int num = 10101;
    cin >> num;
    if (is_huiwen(num)) 
        cout << num << " is huiwen." << endl;
    else
        cout << num << " is not huiwen." << endl;

    return 0;
}