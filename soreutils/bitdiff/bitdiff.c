#include <stdio.h>
#include <string.h>

#define byte char
#define bool char
#define true 1
#define false 0

// Comment out to ignore different sizes but compare only the minimal available
// intersection
#define DIFFERENT_SIZES

#define DIFFERENT_SIZE_WARNING "bitdiff: files have different sizes %ld and "\
"%ld; comparing minimal intersection\n"
#define DIFF_MESSAGE "at index %lX: %02X^%02X = %02X, "\
"diff %d\n"
#define HELP_OPTION "--help"
#define HELP_TEXT "Usage: bitdiff file1 file2\n"\
"Compare files byte-wise; print indices, different bytes, their XOR, "\
"and number of differing bits\n"\
"\n"\
"  --help  Print this text\n"
#define FOPEN_ERROR_MESSAGE "bitdiff: failed to open file for reading: %s\n"
#define TALLY_MESSAGE "total differing bits: %ld\n"

bool get_bit(byte source, int pos) {
	return ((source & 0xFF) >> pos ) & 1U;
}

int bits_on(byte source) {
	int result = 0;
	for (int i = 0; i < 8; i++)
		if (get_bit(source, i)) result++;

	return result;
}

void compare_files(FILE *f1, FILE *f2) {
	long s1 = 0;
	long s2 = 0;
	long min = 0;
	long i = 0;
	long diffs = 0;
	char c1 = '\0';
	char c2 = '\0';

	fseek(f1, 0, SEEK_END);
	fseek(f2, 0, SEEK_END);
	s1 = ftell(f1);
	s2 = ftell(f2);
	fseek(f1, 0, SEEK_SET);
	fseek(f2, 0, SEEK_SET);
	min = (s1 > s2 ? s2 : s1);

	#ifdef DIFFERENT_SIZES
	if (s1 != s2) {
		printf(DIFFERENT_SIZE_WARNING, s1, s2);
	};
	#endif

	for (i = 0; i < min; i++) {
		c1 = fgetc(f1);
		c2 = fgetc(f2);
		if (c1 != c2) {
			printf(DIFF_MESSAGE, i, c1 & 0xFFU, c2 & 0xFFU, (c1 ^ c2) & 0xFFU,
					bits_on(((c1 ^ c2) & 0xFFU)));
			diffs += bits_on((c1 ^ c2) & 0xFFU);
		};
	};

	if (diffs > 0) {
		printf(TALLY_MESSAGE, diffs);
	};
}

int main(int argc, char **argv) {
	if (argc != 3) {
		printf(HELP_TEXT);
		return 0;
	};

	for (int i = 0; i < argc; i++) {
		if(!strcmp(argv[i], HELP_OPTION)) {
			printf(HELP_TEXT);
			return 0;
		};
	};

	FILE *f1 = fopen(argv[1], "rb");
	FILE *f2 = fopen(argv[2], "rb");

	if(!f1) {
		printf(FOPEN_ERROR_MESSAGE, argv[1]);
		return 1;
	};

	if(!f2) {
		printf(FOPEN_ERROR_MESSAGE, argv[2]);
		return 1;
	};

	compare_files(f1, f2);

	fclose(f1);
	fclose(f2);

	return 0;
}
