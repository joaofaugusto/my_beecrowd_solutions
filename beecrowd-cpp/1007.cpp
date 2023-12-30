#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>

using namespace std;


int main() {
    int a;
    int b;
    int c;
    int d;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    std::cin >> d;
    int step1 = a * b;
    int step2 = c * d;
    int diferenca = step1 - step2;
    std::cout << "DIFERENCA = " << diferenca << std::endl;
    return 0;
}