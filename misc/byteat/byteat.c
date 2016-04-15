#include <stdio.h>
#include <string.h>

#define PROGRAM_NAME "byteat"

#define HELP_TEXT "Usage: cat file | " PROGRAM_NAME " 10\n"\
"Print value of the byte at index, starting from 0.\n"
#define INVOPT_MESSAGE PROGRAM_NAME ": invalid option %s\n"

void normalize(const signed char in, char *result) {
	switch (in) {
		case EOF: sprintf(result, "<EOF>");   break;
		case 0:   sprintf(result, "<NUL>");   break;
		case 1:   sprintf(result, "<SOH>");   break;
		case 2:   sprintf(result, "<STX>");   break;
		case 3:   sprintf(result, "<ETX>");   break;
		case 4:   sprintf(result, "<EOT>");   break;
		case 5:   sprintf(result, "<ENQ>");   break;
		case 6:   sprintf(result, "<ACK>");   break;
		case 7:   sprintf(result, "<BEL>");   break;
		case 8:   sprintf(result, "<BS>");    break;
		case 9:   sprintf(result, "<TAB>");   break;
		case 10:  sprintf(result, "<LF>");    break;
		case 11:  sprintf(result, "<VT>");    break;
		case 12:  sprintf(result, "<FF>");    break;
		case 13:  sprintf(result, "<CR>");    break;
		case 14:  sprintf(result, "<SO>");    break;
		case 15:  sprintf(result, "<SI>");    break;
		case 16:  sprintf(result, "<DLE>");   break;
		case 17:  sprintf(result, "<DC1>");   break;
		case 18:  sprintf(result, "<DC2>");   break;
		case 19:  sprintf(result, "<DC3>");   break;
		case 20:  sprintf(result, "<DC4>");   break;
		case 21:  sprintf(result, "<NAK>");   break;
		case 22:  sprintf(result, "<SYN>");   break;
		case 23:  sprintf(result, "<ETB>");   break;
		case 24:  sprintf(result, "<CAN>");   break;
		case 25:  sprintf(result, "<EM>");    break;
		case 26:  sprintf(result, "<SUB>");   break;
		case 27:  sprintf(result, "<ESC>");   break;
		case 28:  sprintf(result, "<FS>");    break;
		case 29:  sprintf(result, "<GS>");    break;
		case 30:  sprintf(result, "<RS>");    break;
		case 31:  sprintf(result, "<US>");    break;
		case 32:  sprintf(result, "<Space>"); break;
		case 127: sprintf(result, "<DEL>");   break;
		// case EOF: sprintf(result, "<EOF>");   break;
		default:  break;
	};

	if (in > 32 && in < 127) sprintf(result, "%c", in);
	if ((unsigned)in > 127) sprintf(result, "<?>");
}

// TODO: Implement intervals
void byteat(/*FILE *f, */unsigned long pos) {
	int c = 0;
	char s[8];
	unsigned long i = 0;

	// fseek(f, pos, SEEK_SET);
	// c = getc(f);

	if (pos == 0) {c = getchar();} else {
		for (i = 0; i <= pos; i++) {
			c = getchar();
			if (c == EOF) {sprintf(s, "<EOF>"); goto pr;};
		};
	};

	normalize(c, s);
	pr: printf("%-8s 0x%2X\n", s, c & 0xFF);
}

void print_help() {
	printf(HELP_TEXT);
}

void print_invalid_option(char *s) {
	printf(INVOPT_MESSAGE, s);
}

int main(int argc, char **argv) {
	unsigned long pos = 0;

	if (argc != 2) {print_help(); return 0;};

	if (!sscanf(argv[1], "%lu", &pos)) {
		print_invalid_option(argv[1]);
		return 1;
	};

	byteat(pos);

	return 0;
}
