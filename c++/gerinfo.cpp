#include <iostream>

int main()
{
	using namespace std;

	int carrots;

	cout <<	"How many carrots do you have?" << endl;
	cin >>	carrots;
	cout << "Here are two more. ";
	carrots = carrots + 2;
	
	cout << "Now you hace " << carrots << " carrots." << endl;

	return 0;
}
