#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s1 = "penguin";
	string s2, s3;

	cout <<	"You can assign one sring object to another: s2 = s1\n";
	s2 = s1;
	cout << "s1: " << s1 << ", s2: " << s2 << endl;
	cout << "You can assign a C-stype to a string object.\n";
	cout <<	"s2 = \"buzzard\"";

	s2 = "buzzard";
	cout <<	"s2: " << s2 << endl;



	return 0;
}

