#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>

using namespace std;

int main() {
    double a;
    double b;
    double media;
    std::cin >> a;
    std::cin >> b;
    media = (a / 11 * 3.5) + (b / 11 * 7.5);
    std::cout << std::fixed << std::setprecision(5);
    std::cout << "MEDIA = " << media << std::endl;
    return 0;
}