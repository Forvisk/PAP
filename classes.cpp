#include <string>
#include <list>
#include <cmath>
#include <iostream>

using namespace std;

class Forma{
	string cor;
	virtual long area() = 0;
	public:
		void show(){
			cout << area() << endl;
		}
		void set_values();
};

class TrianguloRet: public Forma{
	long cateto1, cateto2, hipotenusa;
	long area() {
		return (cateto1 * cateto2) / 2;
	};
	public:
		void set_values(long, long);
};

void TrianguloRet::set_values(long inCat1, long inCat2){
	cateto1 = inCat1;
	cateto2 = inCat2;
	hipotenusa = sqrt( pow(inCat1, 2) + pow( inCat2, 2));
}

class Circulo: public Forma{
	long raio;
	long area() {
		return 0;
	};
	public:
		void set_values(long);
};

void Circulo::set_values(long inRaio){
	raio = inRaio;
}

int main(){
	list<Forma*> formas;
	formas.push_back(new Circulo());
	formas.push_back(new TrianguloRet());
	return 0;
}
