#include <iostream>
using namespace std;

int main()
{
	long long mul = 1LL;

	for (int i = 0; i < 17; i++)
	{
		if (i == 0)
			mul = mul;
		else
			mul *= i;
		cout << i << "! = " << mul << endl;
	}

	return 0;
}
