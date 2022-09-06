//******************************************#
//Author:		erbiaoger
//Email:		643747954@qq.com
//Date:			2022-07-27
//FileName:		structur.cpp
//Description:	The purpose of the script is
//Copyright(C):	2022 All rights reserved
//******************************************#
#include <iostream>
#include <string>
using namespace std;
struct inflatable
{
	string name;
	float volume;
	double price;
};

int main(void)
{
	inflatable guest = 
	{
		"Glorious Gloria",
		1.88,
		29.99
	};
	inflatable pal = 
	{
		"Audacious Arthur",
		3.12,
		32.99
	};
	cout << "Expand your guest list with " << guest.name;
	cout << " and " << pal.name << "!\n";
	cout <<	"You can have both for $";
	cout << guest.price + pal.price << "!\n";

	system("pause");
	return 0;
}
