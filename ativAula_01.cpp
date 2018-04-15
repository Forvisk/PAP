#include <iostream>
#include <cstring>

struct Parada{
	double latitude, longitude;
	float carga;
};

void getParada(struct Parada *stPar){
	double dIn1;
	int iIn1;
	std::cout << "latitude: ";
	std::cin >> stPar->latitude;
	//stPar.latitude = dIn1;
	//std::cout << stPar.latitude << std::endl;
	std::cout << "Longitude: ";
	std::cin >> stPar->longitude;
	//stPar.longitude = 15;
	std::cout << "Quantidade(Kg)(negativo para descarga): ";
	std::cin >> stPar->carga;
	//stPar.carga = 6;
}

void relatorio(struct Parada stPar[]){
	int total = 0;
	for( int i = 0; i < 3; i++){
		std::cout << "Parada " << i+1 << ":\n" << std::endl;
		std::cout << "\tlat: " << stPar[i].latitude << "\tlong: " << stPar[i].longitude << std::endl;
		if( stPar[i].carga < 0)
			std::cout << "\tDescarga(Kg): " << -( stPar[i].carga) << std::endl;
		else
			std::cout << "\tCarga(Kg): " << stPar[i].carga << std::endl;
		total += stPar[i].carga;
	}
	std::cout << "Total(Kg): " << total << std::endl;
}

int main(){
	struct Parada stPar[3];
	for( int i = 0; i < 3; i++){
		getParada(&stPar[i]);
	}
	relatorio( stPar);
	return 0;
}

