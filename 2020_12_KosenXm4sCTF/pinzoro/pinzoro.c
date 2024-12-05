#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>

int dice(void) {
	return rand() % 6 + 1;
}

void init_seed(void) {
	int seed;
	FILE *fp = fopen("/dev/urandom", "r");
	fread(&seed, sizeof(seed), 1, fp);
	srand(seed);
	fclose(fp);
	// seedはクリアしてるので乱数予測は不可能でしょう！
	seed = 0;
}

void challenge(void) {
	int results[8];
	bool pinzoro = true;

	for (int i = 0; i < 8; ++i) {
		results[i] = dice();
		if (results[i] != 1) pinzoro = false;
	}
	
	printf("8d6 => ");
	for (int i = 0; i < 8; ++i) {
		printf("%d ", results[i]);
	}
	printf("\n");
	
	if (!pinzoro) {
		puts("FAILED TO CHALLENGE...");
		return;
	}

	puts("OH!!!! YOU ARE LUCKY!!!!!!");
	system("/bin/sh");
}

void roll_dices(void) {
	char count[128];
	printf("NUMBER: ");
	scanf("%127s%*c", count);
	if (atoi(count) > 100000000) {
		puts("Sorry, that's too big.");
		return;
	}
	for (int i = 0; i < atoi(count); ++i) {
		dice();
	}
	printf("FINISH ROLLING ");
	printf(count);
	printf(" DICES.\n");
	sleep(1);
}

int menu(void) {
	int select;
	printf(
		"1. ROLL DICES (PRACTICE)\n"
		"2. PINZORO CHALLENGE\n"
		"SELECT: "
	);
	scanf("%d%*c", &select);
	return select;
}

void setup(void) {
	alarm(60);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main(void) {
	int select;
	setup();
	init_seed();
	while (1) {
		select = menu();
		if (select == 1) roll_dices();
		if (select == 2) {
			challenge();
			break;
		}
	}
}
