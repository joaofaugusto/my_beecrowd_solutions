#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
using namespace std;

int main() {
    int a;
    int b;
    int prod;
    std::cin >> a;
    std::cin >> b;
    prod = a * b;
    std::cout << "PROD = " << prod << std::endl;
    return 0;
}