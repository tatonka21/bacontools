#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>

#define byte char
#define bool char
#define true 1
#define false 0

#define PROGRAM_NAME "corrupt"

// TODO: Add actions for bytes and bits separately; like drop bit or flip byte
#define DROP_BYTES_ACTION "drop"
#define FLIP_BITS_ACTION "flip"
#define RATIO_OPTION "--ratio"

#define HELP_TEXT "Usage: cat file1 | " PROGRAM_NAME " drop --ratio 0.01 "\
">> file2\n"\
"Corrupt data by flipping random bits or dropping random bytes.\n"\
"\n"\
"Actions (required first argument):\n"\
"  drop       Remove random bytes\n"\
"  flip       Flip random bits\n"\
"Options:\n"\
"  --ratio f  Real number between 0 and 1 (exclusive); equals ratio of"\
" elements (bits or bytes) affected\n"\
"  --help     Print this text\n"

#define INVALID_PARAMETER_MESSAGE PROGRAM_NAME ": invalid argument %s\n"

struct charstream {
	bool is_stdin;
	char *string;
	int ptr;
};

bool get_bit(byte source, int pos) {
	return ((source & 0xFF) >> pos) & 1U;
}

void set_bit(byte *source, int pos, bool value) {
	// Dark magic; tread with care
	*source ^= (-value ^ (*source & 0xFF)) & (1U << pos) & 0xFF;
}

void swap_bits(byte *source, int pos1, int pos2) {
	bool tmp = get_bit(*source, pos1);
	bool tmp2 = get_bit(*source, pos2);
	set_bit(source, pos1, tmp2);
	set_bit(source, pos2, tmp);
}

int rand_in(int min, int max) {
	return rand() % (1 + max - min) + min;
}

byte mask_left(int bits) {
	byte nums[] = {0x00, 0x80, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF};
	return nums[bits];
}

byte mask_right(int bits) {
	byte nums[] = {0x00, 0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF};
	return nums[bits];
}

// Flip 'number_of_bits' randomly chosen bits in the 'source' byte,
// return result
byte corrupt_byte(byte source, int number_of_bits) {
	int i = 0;
	int newpos = 0;
	byte mask = mask_right(number_of_bits);

	int num = (number_of_bits > CHAR_BIT ? CHAR_BIT :
		(number_of_bits < 0U ? 0U : number_of_bits));

	for (i = 0; i < num; i++) {
		newpos = rand_in(i, 7);
		swap_bits(&mask, i, newpos);
	};

	return source ^ mask;
}

char read_char(struct charstream *cs) {
	if (cs->is_stdin) {return getchar();} else return cs->string[cs->ptr++];
}

void print_help() {
	printf(HELP_TEXT);
}

void print_invopt(char *opt) {
	printf(INVALID_PARAMETER_MESSAGE, opt);
}

bool is_action(char *string) {
	return !(
		strcmp(string, DROP_BYTES_ACTION) &&
		strcmp(string, FLIP_BITS_ACTION)
	);
}

bool is_terminal(char c) {
	return
		c == '\0' ||
		c == EOF;
}

bool select_action(char *string) {
	if (!strcmp(string, DROP_BYTES_ACTION)) return false;
	return true;
}

// TODO: Revamp these
void corrupt_drop_bytes_stdout(struct charstream *cs, double ratio) {
	int consec = 0;
	// prob of dropping a byte
	double current_p = ratio;
	char c = '\0';

	while (!is_terminal(c = read_char(cs))) {
		current_p = 1.0-pow(1.0-ratio, consec++ +1);

		if (rand() < current_p * RAND_MAX) {
			consec = 0;
			continue;
		}
		else
			printf("%c", c);
	};
}


// TODO: This frequentist approach doesn't work; fix it
void corrupt_flip_bits_stdout(struct charstream *cs, double ratio) {
	int consec = 0;
	double current_p = ratio;
	char c = '\0';
	int i = 0;
	int in_current_byte = 0;

	while (!is_terminal(c = read_char(cs))) {
		in_current_byte = 0;

		for (i = 0; i < 8; i++) {
			current_p = 1.0-pow(1.0-ratio, consec++ + 1);
			if (rand() < current_p * RAND_MAX) {
				consec = 0;
				in_current_byte++;
			};
		};

		printf("%c", corrupt_byte(c, in_current_byte));
	};
}

int main(int argc, char **argv) {
	bool is_flip_action = true; // Should be an enum probably
	double ratio = 0.1;
	int i = 0;
	struct charstream cs = {true, "<stdin>", 0};

	srand(time(NULL));

	if (argc == 1 || !is_action(argv[1])) {print_help(); return 0;};

	is_flip_action = select_action(argv[1]);

	if (argc > 2)
	for (i = 2; i < argc; i++) {
		if (!strcmp(argv[i], RATIO_OPTION)) {
			if (!(i+1 < argc)) {
				print_invopt(argv[i]);
				return 1;
			};

			if (!sscanf(argv[i+1], "%lf", &ratio)) {
				printf("no scan for you\n");
				print_invopt(argv[i+1]);
				//return 1;
			};

			i++;
		};
	};

	is_flip_action ? corrupt_flip_bits_stdout(&cs, ratio) : corrupt_drop_bytes_stdout(&cs, ratio);

	return 0;
}
