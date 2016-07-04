#include <stdio.h>

int main(int argc, char **argv) {
	unsigned long long int total_bits = 0;
	unsigned long long int count[] = {0, 0, 0, 0, 0, 0, 0, 0};
	int c = 0;

	while ((c = getchar()) != EOF) {
		count[0] += (c >> 7) & 1l; total_bits += (c >> 7) & 1l;
		count[1] += (c >> 6) & 1l; total_bits += (c >> 6) & 1l;
		count[2] += (c >> 5) & 1l; total_bits += (c >> 5) & 1l;
		count[3] += (c >> 4) & 1l; total_bits += (c >> 4) & 1l;
		count[4] += (c >> 3) & 1l; total_bits += (c >> 3) & 1l;
		count[5] += (c >> 2) & 1l; total_bits += (c >> 2) & 1l;
		count[6] += (c >> 1) & 1l; total_bits += (c >> 1) & 1l;
		count[7] += c & 1l;        total_bits += c & 1l;
	};

	printf("total: %lld\n", total_bits);

	printf("dist: MSB %lld %lld %lld %lld %lld %lld %lld %lld LSB\n",
		count[0],
		count[1],
		count[2],
		count[3],
		count[4],
		count[5],
		count[6],
		count[7]);

	printf("norm: MSB %f %f %f %f %f %f %f %f LSB\n",
		(double)count[0]/total_bits/8,
		(double)count[1]/total_bits/8,
		(double)count[2]/total_bits/8,
		(double)count[3]/total_bits/8,
		(double)count[4]/total_bits/8,
		(double)count[5]/total_bits/8,
		(double)count[6]/total_bits/8,
		(double)count[7]/total_bits/8);

	return 0;
};
