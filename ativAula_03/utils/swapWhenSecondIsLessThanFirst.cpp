#include "swapWhenSecondIsLessThanFirst.h"
#include "swap.h"
#include <string>


void swapWhenSecondIsLessThanFirst(int *t1, int *t2){
	bool ret = false;
	if ( *t2 < *t1){
		swap< int>( &t1, &t2);
		ret = true;
	}
	return ret;
}

void swapWhenSecondIsLessThanFirst(string *t1, string *t2){
	bool ret = false;
	if ( *t2 < *t1){
		swap< string>( &t1, &t2);
		ret = true;
	}
	return ret;
}

template <typename T>
void swapWhenSecondIsLessThanFirst(T *t1, T *t2){
	bool ret = false;
	if ( *t2 < *t1){
		swap< T>( &t1, &t2);
		ret = true;
	}
	return ret;
}
