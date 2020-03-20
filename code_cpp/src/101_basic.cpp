#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	cout << "Enigma_10001";
	cout << "This is far too long \nas long as there.\n";
	cout << "...............................\n"

	//declaracion de variables
    int numero1 = 0;
    int numero2 = 0;
    int suma = 0, resta= 0,
         produc_=1, division, modulo;

    cout << "escriba el primer numero: ";//std::cout<<..
    cin >> numero1;

    cout << "escriba el segundo numero: ";
    cin >> numero2;

    suma = numero1 + numero2;
    resta = numero1 -numero2;
    produc_ = numero1 * numero2;
    division = numero1 / numero2;
    modulo = numero1 % numero2;
    cout <<"la suma es " << suma << endl;
    cout <<"resta :: " << resta <<endl;
    cout <<"producto:: " << produc_ << endl;
    cout <<"division:: " << division << endl;
    cout <<"modulo:: "<< modulo << endl;
	return 0;
}