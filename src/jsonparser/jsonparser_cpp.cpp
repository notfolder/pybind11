#include <pybind11/pybind11.h>
#include <iostream>

using namespace std;

int add(int a, int b)
{
    cout << "Hello world." << endl;
    return a + b;
}

PYBIND11_MODULE(_jsonparser_cpp, m)
{
    m.doc() = "my test module";
    m.def("add", &add, "add two numbers");
}
