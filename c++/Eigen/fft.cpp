#include <complex>
#include <vector>
#include <cmath>
#include <iostream>

const double PI = 3.14159265358979323846;

// 使用递归实现FFT算法
void fft(std::vector<std::complex<double>>& a, bool invert) {
    int n = a.size();
    if (n == 1) return;

    std::vector<std::complex<double>> a0(n / 2), a1(n / 2);
    for (int i = 0; i < n / 2; i++) {
        a0[i] = a[2*i];
        a1[i] = a[2*i + 1];
    }

    fft(a0, invert);
    fft(a1, invert);

    double ang = 2 * PI / n * (invert ? -1 : 1);
    std::complex<double> w(1), wn(cos(ang), sin(ang));
    for (int i = 0; i < n / 2; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n / 2] = a0[i] - w * a1[i];
        if (invert) {
            a[i] /= 2;
            a[i + n / 2] /= 2;
        }
        w *= wn;
    }
}

int main() {
    std::vector<std::complex<double>> data = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 
                                              8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 
                                              14.0, 15.0, 16.0};

    fft(data, false); // 进行FFT
    // 处理FFT结果
    fft(data, true); // 进行逆FFT（如果需要）
    
    // 处理逆FFT结果
    return 0;
}
