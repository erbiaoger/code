#include <iostream>
using namespace std;

int main()
{
    const int ArSize = 20;
    char Name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name:\n";
    cin.getline(Name, ArSize);
    cout << "Enter your favorite dessert:\n";
    cin.getline(dessert, ArSize);

    cout << "I have some delicious " << dessert;
    cout << " for your, " << Name;

    cout << "Enter your name:\n";
    cin.get(Name, ArSize).get();
    cin.clear();
    cout << "Enter your favorite dessert:\n";
    cin.get(dessert, ArSize).get();
    cin.clear();

    cout << "I have some delicious " << dessert;
    cout << " for your, " << Name;


    return 0;
}
