#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main()
{
	char charr1[20];
	char charr2[20] = "jujar";
	string str1;
	string str2 = "panther";

	str1 =	str2;
	strcpy(charr1, charr2);
	cout << str1 <<	endl;
	cout << charr1 << endl;
	str1 += " aaaaa";
	strcat(charr1, " bbbbb");
	cout << str1 <<	endl;
	cout << charr1 << endl;
	cout << str1.size() << endl;
	cout << strlen(charr1) << endl;
	


	return 0;
}


