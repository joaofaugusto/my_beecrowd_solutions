#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
#include <iomanip>

int main() {
    std::string nome;
    double salario;
    double ajuste = 0.15;
    double vendas;
    std::cin >> nome;
    std::cin >> salario;
    std::cin >> vendas;
    double reajuste = vendas * ajuste;
    reajuste = reajuste + salario;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "TOTAL = R$ " << reajuste << std::endl;
    return 0;
}