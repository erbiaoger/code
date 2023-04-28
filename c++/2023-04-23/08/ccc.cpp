#include <iostream>
#include <valarray>
#include <complex>
#include <algorithm>
#include <fstream>
using namespace std;

typedef valarray<double> Signal;
typedef valarray<complex<double>> ComplexSignal;

int main()
{
    Signal signal1(1, 1000);
    Signal signal2(1, 1000);
    
    for (auto x: signal1) {
        static int i = 0;
        signal1[i] = sin(i*2*3.1415926/1000.0);
        signal2[i] = cos(i*2*3.1415926/1000.0);
        i++;
    }

    cout << signal1.size();

    // 执行FFT变换
    ComplexSignal spectrum1(signal1.size());
    transform(begin(signal1), end(signal1), begin(spectrum1), [](double x) { return complex<double>(x, 0); });
    valarray<complex<double>> spectrum2(signal2.size());
    transform(begin(signal2), end(signal2), begin(spectrum2), [](double x) { return complex<double>(x, 0); });

    // 计算互相关
    valarray<complex<double>> correlation(spectrum1.size());
    transform(begin(spectrum1), end(spectrum1), begin(spectrum2), begin(correlation), multiplies<complex<double>>());

    // 执行IFT变换
    Signal result(correlation.size());
    transform(begin(correlation), end(correlation), begin(result), [](complex<double> x) { return x.real(); });

    ofstream fp("plot.dat");
    if (fp.is_open()) {
        static int j = 0;
        for (auto s : result) { 
            fp << signal1[j] << "\t" << signal2[j] << "\t" << s << endl;
            j++;
        }

        fp.close();
    }

    system("python3 plot.py");
    return 0;
}
