#include <iostream>
using namespace std;
const int Max = 5;

int main()
{
	double fish[Max];
	cout << "Please Enter the weights of your fish.\n";
	cout << "You may enter up to " << Max
		<< " fish <q to terminate>.\n";
	cout << "fish #1 ";
	int i = 0;
	while (i < Max && cin >> fish[i])
	{
		if (++i < Max)
			cout << "fish # " << i+1 << ":";
	}
	double total = 0.0;
	for (int j = 0; j < i; i++)
		total += fish[i];
	if (i == 0)
		cout <<	"No fish!" << endl;
	else
		cout << total / i << " average weight of "
			<< i <<	" fish \n";
	cout << "Done.\n";



	return 0;
}
