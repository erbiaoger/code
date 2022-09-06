#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	char animal[20] = "bear";
	const char * bird = "wrem";
	char * ps;

	cout << animal << " and " << bird << "\n";
	cout <<	"Enter a kind of animal: ";
	cin >> animal;
	ps = animal;
	cout << ps << "!\n";

	cout << animal << " at " << (int *) animal << endl;
	cout << ps << " at " <<	(int *) ps << endl;
	
	ps = new char[strlen(animal) + 1];
	strcpy(ps, animal);
	
	cout << animal << " at " << (int *) animal << endl;
	cout << ps << " at " <<	(int *) ps << endl;

	return 0;
}
