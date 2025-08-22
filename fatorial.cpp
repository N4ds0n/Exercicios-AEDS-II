#include <iostream>

using namespace std;

int calcular_fatorial_laco(int numero){
    int fatorial;

    fatorial = 1;

    for (int i = 1; i <= numero; i++) {
        fatorial = fatorial*i;
    }

    return fatorial;
}

int calcular_fatorial_rec(int numero){
    int fatorial;
    //Caso base
    if(numero == 1)
        return 1;
    //Caso recursivo
    else{
        fatorial = numero * calcular_fatorial_rec(numero-1);
        return fatorial;
    }

}

int main()
{

    int numero, fatorial;

    cout << "Digite um numero inteiro: " << endl;

    cin >> numero;

    //fatorial = calcular_fatorial_laco(numero);
    fatorial = calcular_fatorial_rec(numero);

    cout << "O fatorial de " << numero << " eh " << fatorial << endl;

    return 0;
}