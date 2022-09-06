#include <iostream>
using namespace std;

int main()
{
	double* p = new double [3];
	p[0] = 0.2;
	p[1] = 0.3;
	p[2] = 0.4;
	cout << R"(p[0] = )" << *p << endl;
	cout << R"(p[1] = )" << *(++p) << endl;
	cout << R"(p[2] = )" << *(++p) << endl;

	p = p - 2;
	delete [] p;


	return 0;
}
