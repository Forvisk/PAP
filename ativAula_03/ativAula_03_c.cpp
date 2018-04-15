#include <iostream>
#include <list>
#include <string>
#include "utils/swapWhenSecondIsLessThanFirst.h"

class Student {
	string nome;
public:
	void set_values ( string);
	string get_nome(void);
}

bool operator <(Student &st1, Student &st2){
	return st1.get_nome() < st2.get_nome();
}

// sobrecarga de operador
bool operator <( string &str1, string &str2){
	if ( str1.compare( str2) < 0)
		return true;
	else
		return false;
}

int main(){
	
	string kk[10] = { "Anduin", "Sylvanas", "Jaina", "Malfurion", "Thrall", "Baine", "Nathanos", "Genn", "Alleria", "Turalion"};

	std::list<Student> alunos;
	
	for( int i; i < 10; i++){
		Student novo;
		novo.set_values(kk[i]);
		strings.push_back( novo);
	}

	for( it=alunos.begin(); it != alunos.end(); it++)
			for( it2 = it+1; it2 != alunos.end(); it2++)
				swapWhenSecondIsLessThanFirst( &it, &it2);

	for( it=alunos.begin(); it != alunos.end(); it++){
		std::cout << it.get_nome() << std::endl;
	}
	return 0;
}