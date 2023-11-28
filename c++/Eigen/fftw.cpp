#include <iostream>
#include <fftw3.h>
#include <cmath>
#define PI 3.14


int main() {
    int N = 1024; // 数据的大小
    fftw_complex *in, *out;
    fftw_plan p;

    // 分配输入和输出数组
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    // 创建计划
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // 填充输入数据
    for (int i = 0; i < N; i++) {
        in[i][0] = sin(2 * PI * i / N); /* 实部数据 */ // 例如：sin(2 * PI * i / N)
        in[i][1] = 0;                   /* 虚部数据 */ // 通常为0，除非您处理的是复数
    }

    // 执行FFT
    fftw_execute(p);

    // 打印FFT结果
    for (int i = 0; i < N; i++) {
        std::cout << "out[" << i << "] = " << out[i][0] << " + " << out[i][1] << "i" << std::endl;
    }

    // 清理
    fftw_destroy_plan(p);
    fftw_free(in); 
    fftw_free(out);

    return 0;
}
