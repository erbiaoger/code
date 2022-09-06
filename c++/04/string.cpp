#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    const int Size = 15;
    char name1[Size];
    char name2[Size] = "c++owboy";

    cout << "howdy I'm " << name2;
    cout << "!\nWhat's your name?\n";
    cin >> name1;
    cout << "Well! " << name1 << " your name has ";
    cout << strlen(name1) << endl;
    cout << sizeof(name1) << endl;
    cout << sizeof(name1) / sizeof(char) << endl;

    return 0;
}

