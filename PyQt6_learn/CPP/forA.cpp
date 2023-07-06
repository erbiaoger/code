#include <iostream>
using namespace std;

//#includeint forA(int n);

float forA(int n)
{
    float sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += 1.0 / i;
    }
    return sum;
}