#include <iostream>
#include <cstring>
#include "utils/swapWhenSecondIsLessThanFirst.h"



struct Parada{
	double latitude, longitude;
	float carga;
};

void getParada(struct Parada *stPar);

void relatorio(struct Parada stPar[]);

template <typename Type>
void swap( Type *a, Type *b);

// sobrecarga de função
bool operator <( struct Parada& p1, struct Parada& p2){
	return p1.latitude < p2.latitude;
}

void ordena( struct Parada *stPar, int nPar);

int main(){
	struct Parada stPar[3];
	for( int i = 0; i < 3; i++){
		getParada(&stPar[i]);
	}
	relatorio( stPar);
	ordena( stPar, 3);
	relatorio(stPar);
	return 0;
}

void getParada(struct Parada *stPar){
	double dIn1;
	int iIn1;
	std::cout << "latitude: ";
	std::cin >> stPar->latitude;
	std::cout << "Longitude: ";
	std::cin >> stPar->longitude;
	std::cout << "Quantidade(Kg)(negativo para descarga): ";
	std::cin >> stPar->carga;
}

void relatorio(struct Parada stPar[]){
	int total = 0;
	std::cout << "\n---------------------------\n";
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


void ordena( struct Parada *stPar, int nPar){
	// dumb bubble
	for( int i = 0; i < nPar; i++){
		for( int j = i+1; j < nPar; j++){
			//swap < struct Parada>( &stPar[i], &stPar[j]);
			swapWhenSecondIsLessThanFirst<struct Parada>( &stPar[i], &stPar[j]);
		}
	}
}


