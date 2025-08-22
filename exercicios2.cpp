#include <iostream>
using namespace std;

int main() {
    int x = 25, y = 3, z = 12, w = 8;
    bool resultado = ((x + y > 10 || z < 15));
    
    if (resultado) {
        cout << " verdadeira. " << endl;
    } else {
        cout << " falsa. " << endl;
    }
    
    return 0;
}
