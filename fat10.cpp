#include<iostream>

int main(){
	int k = 2;
	int res = 1;
	do{
		std::cout << res << "\n";
		res = res * k;
		k++;
	}while( k <= 10);
	
	std::cout << "Resp: " <<  res << "\n";
	
	return 0;
}
