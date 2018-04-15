#include "swapWhenSecondIsLessThanFirst.h"
#include "swap.h"

template <typename T>
void swapWhenSecondIsLessThanFirst(T *t1, T *t2){
	bool ret = false;
	if ( *t2 < *t1){
		swap( &t1, &t2);
		ret = true;
	}
	return ret;
}
