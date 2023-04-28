#include <iostream>
using namespace std;   

int jiecheng(int *chengji, int n) {
    if (n >= 1) {
        *chengji *= n;
        n--;
        jiecheng(chengji, n);
    }

    return *chengji;
}

int main() {
    auto n = 10;
    auto sum = 0;
    auto chengji = 1;
    sum = jiecheng(&chengji, n);

    cout << sum << endl;
    return 0;
}