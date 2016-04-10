#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define bool int
#define true 1
#define false 0

#define NO_SKIP_SPACES_FLAG "--no-skip-spaces"
#define OPTION_LIST_END "--"
#define HELP_FLAG "--help"
#define HELP_FLAG_SHORT "-h"
// #define READ_FROM_STDIN "-"

#define HELP_TEXT "Usage: n7m word1 word2 word3\n"\
"Convert words to numeronyms, like i18n or l10n.\n"\
"\n"\
"  --no-skip-spaces  Don't ignore whitespace. 'Hello world' becomes 'H9d'.\n"\
"  --help, -h        Print this text.\n"

void numeronymize(const char* string, char* result,
		const bool skip_spaces) {
	int strl = (int)strlen(string);
	int i = 0;
	int length = 0;
	char c = '\0';

	if (strl <= 3) {
		strcpy(result, string);
		return;
	};

	while ((c = string[i++]) != '\0')
		if (!((c == ' ' || c == '\t') && skip_spaces)) length++;

	sprintf(result, "%c%d%c", string[0], length-2, string[strl-1]);
}

bool is_flag(const char* string) {
	return !(
		strcmp(string, NO_SKIP_SPACES_FLAG) &&
		strcmp(string, OPTION_LIST_END) &&
		strcmp(string, HELP_FLAG) &&
		strcmp(string, HELP_FLAG_SHORT)
	);
}

void print_help() {
	printf("%s", HELP_TEXT);
}

int main(int argc, char** argv) {
	bool skip_spaces = true;
	int i = 0;
	char* current_string = 0;

	if (argc <= 1) {
		print_help();
		return 0;
	};

	for (i = 1; i < argc; i++) {
		if (!strcmp(argv[i], NO_SKIP_SPACES_FLAG)) skip_spaces = false;
		if (!strcmp(argv[i], OPTION_LIST_END)) break;
		if (!strcmp(argv[i], HELP_FLAG)) {print_help(); return 0;};
		if (!strcmp(argv[i], HELP_FLAG_SHORT)) {print_help(); return 0;};
	};

	for (i = 1; i < argc; i++) {
		if (is_flag(argv[i])) continue;
		current_string = (char*)malloc(sizeof(char)*strlen(argv[i]));
		numeronymize(argv[i], current_string, skip_spaces);
		printf("%s\n", current_string);
		free(current_string);
	};

	return 0;
};
