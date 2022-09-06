#include <iostream>
#include <string>
using namespace std;

int main()
{
	int nights = 1001;
	int* p_nights = new int;
	*p_nights = 1001;

	cout << R"(nights = )" << nights << endl;
	cout << R"(&nights = )" << &nights << endl;
	cout << R"(p_nights = )" << p_nights << endl;
	cout << R"(*p_nights = )" << *p_nights << endl;


	return 0;
}
