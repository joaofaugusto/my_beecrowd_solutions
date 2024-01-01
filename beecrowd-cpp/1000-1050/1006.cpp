#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>

using namespace std;

int main() {
    double a;
    double b;
    double c;
    double media;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    double step1 = a / 10;
    step1 = step1 * 2;
    double step2 = b / 10;
    step2 = step2 * 3;
    double step3 = c / 10;
    step3 = step3 * 5;
    media = step1 + step2;
    media = media + step3;  
    std::cout << std::fixed << std::setprecision(1);
    std::cout << "MEDIA = " << media << std::endl;
    return 0;
}