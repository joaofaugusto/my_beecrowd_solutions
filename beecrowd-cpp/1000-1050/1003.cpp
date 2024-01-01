#include <stdio.h>
#include <iostream>
// Lib que usa para determinar a quantidade de casas decimais
using namespace std;

int main() {
    int a;
    int b;
    int soma;
    std::cin >> a;
    std::cin >> b;
    soma = a + b;
    std::cout << "SOMA = " << soma << std::endl;
    return 0;
}