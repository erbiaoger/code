#include <iostream>
using namespace std;

int main()
{
	double wages[3] = {10000.0, 20000.0, 30000.0};
	short stacks[3] = {3, 2, 1};

	double* p_wages = wages;
	short* p_stacks = &stacks[0];

	cout << "p_wages = " <<	p_wages << endl;
	cout << "*p_wagtes = " << *p_wages << endl;
	cout << "p_stacks = " << p_stacks << endl;
	cout << "*p_stacks = " << *p_stacks << endl;
	cout << endl;

	cout << "p_wages = " <<	p_wages << endl;
	cout << "*p_wagtes = " << *++p_wages << endl;
	cout << "p_stacks = " << p_stacks << endl;
	cout << "*p_stacks = " << *++p_stacks << endl;

	cout << "p_wages = " <<	p_wages << endl;
	cout << "*p_wagtes = " << *++p_wages << endl;
	cout << "p_stacks = " << p_stacks << endl;
	cout << "*p_stacks = " << *++p_stacks << endl;

	return 0;
} 
