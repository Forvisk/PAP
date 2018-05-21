#include <iostream>
#include <string>
#include <cstdlib>
#include <time.h>
#include <cstdio>
//#include <pqxx/pqxx>

//using namespace pqxx;
using namespace std;


typedef struct {

	double latitude;
	double longitude;
	int peso;
} Aviao;


int main(int argc, char* argv[]){

		srand(time(NULL));
		FILE *arquivo = NULL; // CRIANDO O ARQUIVO
		int pesoTotal=0;
		char nameArquivo[] = "voos.txt";

		if (argc < 2){  //VERIFICACAO NA HORA DA COMPILACAO
		  printf("ERRO!FALTAM ARGUMENTOS\n");
		  //return 0;
		}

		//VERIFICACAO DE ARQUIVO
		if( (arquivo = fopen (nameArquivo, "w+")) == NULL){ // VERIFICACAO PARA ABRIR O ARQUIVO PARA ESCRITA E LEITURA
		  printf("ERRO AO ABRIR O ARQUIVO\n");
		  return 0;
		}
		//CRIANDO SO UM AVIAO
		Aviao aviao;
		for(int i=0 ; i<100 ; i++){
			aviao.latitude = rand() % 1800000 -900000;
			aviao.longitude = rand() % 3600000 -1800000;
			aviao.peso = rand() % 1000 + (-500);
			if( pesoTotal + aviao.peso < 0){
				aviao.peso = -1 * pesoTotal;
				pesoTotal = 0;
			}else
				pesoTotal += aviao.peso;
			printf("%.0lf %.0lf %d %d\n", aviao.latitude, aviao.longitude, aviao.peso, pesoTotal);
			fprintf( arquivo, "%0.lf %0.lf %d %d\n", aviao.latitude, aviao.longitude, aviao.peso, pesoTotal);
		}

		cout << "IMPRESSAO NO TXT FEITA COM SUCESSO\nPESO ACUMULADADO DO AVIAO = " << pesoTotal << endl;


}