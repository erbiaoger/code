//
// Created by fuhong on 20-7-12.
//

#include <iostream>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

int main() {
    MatrixXd m = MatrixXd::Random(3, 3);            //初始化动态矩阵m,使用Random函数,初始化的值在[-1,1]区间内,矩阵大小3X3
    m = (m + MatrixXd::Constant(3, 3, 1.2)) * 50;   // MatrixXd::Constant(3, 3, 1.2)初始化3X3矩阵,矩阵里面的数值为常量,全部为1.2
    // Eigen重载了+ 运算符，两个矩阵有相同的行数和列数即可相加,对应位置上的值相加
    cout << "m =" << endl << m << endl;
    VectorXd v(3);
    v << 1, 2, 3;                                   //逗号初始化，英文：comma-initializer,Eigen未提供c++11 的{}初始化方式
    cout << "m * v =" << endl << m * v << endl;
}
