#include <iostream>
#include <list>
#include <string>
#include "utils/swapWhenSecondIsLessThanFirst.h"

// sobrecarga de operador
bool operator <( string &str1, string &str2){
	if ( str1.compare( str2) < 0)
		return true;
	else
		return false;
}

int main(){
	int k[10] =  {56, 58, 93, 45, 12, 45, 78, 36, 36, 5};
	string kk[10] = { "hk", "batata", "damit", "WoW", "lk", "is", "ms", "tw", "up", "th"};

	std::list<int> inteiros;
	std::list<std::string> strings;
	
	for( int i; i < 10; i++){
		inteiros.push_back( k[i]);
		strings.push_back( kk[i]);
		std::cout << k[i] << " " << kk[i] << std::endl;
	}

	for( it=inteiros.begin(); it != inteiros.end(); it++)
		for( it2 = it+1; it2 != inteiros.end(); it2++)
			swapWhenSecondIsLessThanFirst( &it, &it2);

	for( it=strings.begin(); it != strings.end(); it++)
			for( it2 = it+1; it2 != strings.end(); it2++)
				swapWhenSecondIsLessThanFirst( &it, &it2);

	for( it=inteiros.begin(); it != inteiros.end(); it++){
		std::cout << it << std::endl;
	}

	for( it=strings.begin(); it != strings.end(); it++){
		std::cout << it << std::endl;
	}
	return 0;
}

