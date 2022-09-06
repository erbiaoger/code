#include <iostream>
#include <cstring>
using namespace std;

char * getname(void);

int main()
{
	char * name;

	name = getname();
	cout <<	name << " at " << (int *) name << endl;
	delete [] name;

	name = getname();
	cout <<	name << " at " << (int *) name << endl;
	delete [] name;

	return 0;
}

char * getname(void)
{
	char temp[80];
	cout << "Enter last name: ";
	cin >> temp;
	char * p_name = new char [strlen(temp) + 1];
	strcpy(p_name, temp);

	return p_name;
}
