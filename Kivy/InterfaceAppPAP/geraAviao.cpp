#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <time.h>
#include <cstdio>
//#include <pqxx/pqxx>

//using namespace pqxx;
using namespace std;


typedef struct {
	float latitude;
	float longitude;
	int peso;
} Aviao;

typedef struct {
	int indice;
	string name;
	string modelo;
	string codigo;
} Voo;

int geraParadas( string nameArquivo){
	FILE *arquivo = NULL; // CRIANDO O ARQUIVO
	int pesoTotal=0;
	char *cNome = new char[nameArquivo.length() +1]; 
	strcpy( cNome, nameArquivo.c_str());
	int quant = rand() % 200 + 20;

	//VERIFICACAO DE ARQUIVO
	if( (arquivo = fopen (cNome, "w+")) == NULL){ // VERIFICACAO PARA ABRIR O ARQUIVO PARA ESCRITA E LEITURA
		printf("ERRO AO ABRIR O ARQUIVO\n");
		return 0;
	}
	//CRIANDO SO UM AVIAO
	Aviao aviao;
	for(int i=0 ; i<quant ; i++){
		aviao.latitude = rand() % 1800000 -900000;
		aviao.longitude = rand() % 3600000 -1800000;
		aviao.peso = rand() % 1000 + (-500);
		if( pesoTotal + aviao.peso < 0){
			aviao.peso = -1 * pesoTotal;
			pesoTotal = 0;
		}else
			pesoTotal += aviao.peso;
		//printf("%.0lf %.0lf %d %d\n", aviao.latitude, aviao.longitude, aviao.peso, pesoTotal);
		fprintf( arquivo, "%0.lf %0.lf %d %d\n", aviao.latitude, aviao.longitude, aviao.peso, pesoTotal);
	}
	printf("\tArquivo %s criado com sucesso\n", cNome);
	fclose( arquivo);
	return 1;
}

int geraListaVoo( string nameArquivo){
	FILE *arquivo = NULL; // CRIANDO O ARQUIVO
	char *cNome = new char[nameArquivo.length() +1]; 
	strcpy( cNome, nameArquivo.c_str());
	string modelos[] = {"Antonov An-225", "Airbus A300-600ST", "Airbus A380-800", "Airbus A340-600", "Antonov An-124"};
	int quant = rand() % 5 + 1;
	int indice = 0;

	//VERIFICACAO DE ARQUIVO
	if( (arquivo = fopen (cNome, "r+")) == NULL){ // VERIFICACAO PARA ABRIR O ARQUIVO PARA ESCRITA E LEITURA
		printf("Criando arquivo\n");
		if( (arquivo = fopen (cNome, "w+")) == NULL){ // VERIFICACAO PARA ABRIR O ARQUIVO PARA ESCRITA E LEITURA
			printf("Erro ao criar o arquivo\n");
			return 0;
		}
	}else{
		char c;
		while(fread (&c, sizeof(char), 1, arquivo)) {
            if(c == '\n') {
                indice++;
            }
        }
	}
	Voo voo;
	for( int i = indice; i < indice + quant; i++){
		voo.codigo = to_string( rand() % 100) + to_string( i);
		char *cCodigo = new char[voo.codigo.length() +1]; 
		strcpy( cCodigo, voo.codigo.c_str());

		voo.name = "voo" + voo.codigo;
		char *cNome = new char[voo.name.length() +1]; 
		strcpy( cNome, voo.name.c_str());

 		int mol = rand() % 5;
		voo.modelo = modelos[ mol];
		char *cModelo = new char[voo.modelo.length() +1]; 
		strcpy( cModelo, voo.modelo.c_str());

		printf("%i %s %s %s\n", i+1, cNome, cCodigo, cModelo);
		fprintf(arquivo, "%i--%s--%s--%s\n", i+1, cNome, cCodigo, cModelo);
		
		string newArqParadas = "arquivos/"+voo.name+".txt";
		geraParadas( newArqParadas);
	}

	fclose( arquivo);
	printf("Arquivo %s criado/modificado com sucesso\n", cNome);

	return 1;
}


int main(int argc, char* argv[]){

		srand(time(NULL));
		string arqVoos = "arquivos/listaVoo.txt";

		geraListaVoo( arqVoos);

		return 0;
}