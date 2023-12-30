#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>

int main() {
    int numero;
    int horas;
    float valor_hora;
    std::cin >> numero;
    std::cin >> horas;
    std::cin >> valor_hora;
    float salario = horas * valor_hora;
    std::cout << "NUMBER = " << numero << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "SALARY = U$ " << salario << std::endl;
    return 0;
}