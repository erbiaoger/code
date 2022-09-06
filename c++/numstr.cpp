#include <iostream>
using namespace std;

int main()
{
    cout << "What year was your house build?\n";
    int year;
    (cin >> year).get();
    cout << "What is its street address?\n";
    char address[80];
    cin.get(address, 80).get();
    cout << "Year build: " << year << endl;
    cout << "Address: " << address << endl;
    cout << "Done!\n";

    return 0;
}
