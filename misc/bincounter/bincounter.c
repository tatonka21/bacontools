#include <stdio.h>

int main(int argc, char **argv) {
	unsigned long int count[] = {0, 0, 0, 0, 0, 0, 0, 0};
	int c = 0;

	while ((c = getchar()) != EOF) {
		count[0] += (c >> 7) & 1l;
		count[1] += (c >> 6) & 1l;
		count[2] += (c >> 5) & 1l;
		count[3] += (c >> 4) & 1l;
		count[4] += (c >> 3) & 1l;
		count[5] += (c >> 2) & 1l;
		count[6] += (c >> 1) & 1l;
		count[7] += c & 1l;
	};

	printf("%ld %ld %ld %ld %ld %ld %ld %ld\n", count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7]);

	return 0;
};
