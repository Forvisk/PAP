#include <string>
#include <list>
#include <iostream>
using namespace std;

class Forma{
	string cor;
	virtual long area() = 0;
	public:
		void show(){
			cout << area() << endl;
		}
};

class TrianguloRet: public Forma{
	long cateto1, cateto2, hipotenusa;
	long area() {
		return (cateto1 * cateto2) / 2;
	};
};

class Circulo: public Forma{
	long raio;
	long area() {
		return 0;
	};
};

int main(){
	list<Forma*> formas;
	formas.push_back(new Circulo());
	formas.push_back(new TrianguloRet());
	return 0;
}
