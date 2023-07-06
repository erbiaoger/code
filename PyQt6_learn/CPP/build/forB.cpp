
#include <iostream>
using namespace std;


// int forB() {
//     int n = 1;
//     cout << n;
//     return 0;
// }


float forA(int n)
{
    float sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += 1.0 / i;
    }
    return sum;
}