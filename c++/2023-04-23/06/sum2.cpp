// sum2.cpp
/*
将值转换为 Python 对象，然后返回
C++ 函数可以将计算结果转换为 Python 对象，并将其作为返回值返回。可以使用 Boost.Python 库来实现这个过程。以下是一个例子：
*/
#include <boost/python.hpp>

int sum2(int n) {
	int result = 1;
	for (int i = 1; i <= n; ++i) {
		result *= i;
	}
	return result;
}

BOOST_PYTHON_MODULE(sum2)
{
	using namespace boost::python;
	def("sum2", sum2);
}
