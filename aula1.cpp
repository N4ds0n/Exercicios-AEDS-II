#include<iostream>
using namespace std;

int calcularfat(int numero){
    int fatorial = 1;
    for (int i=1; i<=numero; i++){
    fatorial *= i;
}
return fatorial;
}

int main(){ 
    int numero;
    
    cout << "Digite o numero: " << endl;
    cin >> numero;

    if (numero < 0){
        cout << "Impossivel calcular fatorial.";
   } else {
    int resultado = calcularfat(numero);
    cout << "O fatorial de " << numero << " eh: " << resultado << endl;
   }

return 0; 
}