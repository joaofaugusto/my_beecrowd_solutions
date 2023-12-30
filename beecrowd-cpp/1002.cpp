#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double raio;
    std::cin >> raio;
    double area;
    area = 3.14159 * std::pow(raio, 2);
    // Função que determina a precisão das casas decimais
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "A=" << area << std::endl;
    return 0;
}