#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void swap(unsigned char* a, unsigned char* b) {
	unsigned char tmp = *a;
	*a = *b;
	*b = tmp;
}

unsigned char* KSA(unsigned char* key) {
	unsigned char* S = malloc(0x100);
	for (int i = 0; i < 0x100; ++i) {
		S[i] = i;
	}
	int j = 0;
	for (int i = 0; i < 0x100; ++i) {
		j = (j + S[i] + key[i % strlen(key)]) % 0x100;
		swap(&S[i], &S[j]);
	}
	return S;
}

void RC4(unsigned char* data, unsigned char* key, int len) {
	unsigned char* S = KSA(key);
	int i = 0, j = 0;
	for (int k = 0; k < len; ++k) {
		i = (i + 1) % 0x100;
		j = (j + S[i]) % 0x100;
		swap(&S[i], &S[j]);
		data[k] ^= S[(S[i] + S[j]) % 0x100];
	}
}

int main(void) {
	unsigned char input_password[0x100];
	printf("PASSWORD: ");
	scanf("%s", input_password);
	if (strcmp(input_password, "sUp3r_s3Cr37_P4s5w0Rd") != 0) {
		puts("Invalid password.");
		return 1;
	}
	// nitic_ctf{hardcode_s3cret}
	char s[] = "\xa9\x4c\x67\x42\xba\x5d\x7e\xe1\xba\x9d\xcb\xb9\xf0\xc7\x27\x40\x87\x44\x68\x02\x7e\x7c\xd9\x30\x00\x1d";
	RC4(s, input_password, 26);
	puts(s);
	return 0;
}