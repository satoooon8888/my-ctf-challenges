#include <stdio.h>
#include <stdlib.h>

int randtbl[31];
int* fptr = &randtbl[3];
int* rptr = &randtbl[0];
int* state = &randtbl[0];
int* end_ptr = &randtbl[31];

int rand(void) {
		int result;
		unsigned int val;
		val = *fptr += (unsigned int) *rptr;
		result = val >> 1;
		++fptr;
		if (fptr >= end_ptr) {
			fptr = state;
			++rptr;
		} else {
			++rptr;
			if (rptr >= end_ptr)
				rptr = state;
		}
		return result;
}

int main(int argc, char* argv[]) {
	long long flags = 0, i;
	for (int i = 0; i < 31; i++) {
		randtbl[i] = atoi(argv[i+1]);
	}
	for(i=0;;++i) {
			flags <<= 1;
			flags += (rand() % 6 == 0);
			if ((flags & ((1 << 9) - 1)) == ((1 << 9) - 1)) {
					break;
			}
	}
	printf("%d\n", i-8);
}