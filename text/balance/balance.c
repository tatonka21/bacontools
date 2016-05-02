#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define bool int
#define true 1
#define false 0

#define LEFT_CHARS_OPTION "--left"
#define RIGHT_CHARS_OPTION "--right"
#define IGNORE_EXTRAS_OPTION "--ignore-extras"
#define READ_FROM_STDIN "-"
#define HELP_OPTION "--help"

#define HELP_TEXT ""\
"Usage: balance [input] --left ({ --right )}\n"\
"Detect if string containing matching left and right characters is balanced.\n"\
"\n"\
"  --left           Define left (opening) characters to match, "\
"({[< by default\n"\
"  --right          Define right (closing) characters to match respectively, "\
")}]> by default\n"\
"  --ignore-extras  Skip all unspecified characters, false by default\n"\
"  --help           Print this text\n"\
"  -                Ignore argument input, read stdin\n"

#define IS_BALANCED_MESSAGE "balanced: %s\n"
#define IS_NOT_BALANCED_MESSAGE "not balanced: %s\n"
#define INVALID_CHARACTER_MESSAGE "unspecified character %c at index %d: "\
"%s\n"
#define INVALID_FLAG_MESSAGE "invalid option %s\n"
#define NO_INPUT_MESSAGE "no input provided\n"

#define NOPE -1

struct node {
	char value;
	int initial;
	struct node *prev;
	struct node *next;
};

struct charstream {
	int ptr;
	char *string;
	bool is_stdin;
};

char get_char(struct charstream *s) {
	if (s->is_stdin) {s->ptr++; return getchar();}
	else return s->string[s->ptr++];
}

void free_stack(struct node *last) {
	struct node *prev;

	if (!last->initial) {
		prev = last->prev;
		free(last);
		free_stack(prev);
	};
}

char peek(struct node *last) {
	if (last == 0 || last->initial) return NOPE;

	return last->value;
}

char pop(struct node **last) {
	struct node *prev;
	char value;

	if ((*last)->initial) return NOPE;

	value = (*last)->value;
	prev = (*last)->prev;
	free(*last);
	(*last) = prev;

	return value;
}

void push(struct node **last, char value) {
	struct node *tmp;
	if (last == 0 || (*last) == 0) return;

	tmp = *last;

	(*last)->next = (struct node*)malloc(sizeof(struct node));
	memset((*last)->next, 0, sizeof(struct node));

	(*last) = (*last)->next;
	(*last)->prev = tmp;
	(*last)->value = value;
}

bool is_terminal(char c) {
	return (
		c == '\0' ||
		c == EOF
	);
}

int getpos(const char character, const char *string) {
	int i = 0;

	while (!is_terminal(string[i]))
		if (character == string[i++]) return i;

	return -1;
}

void print_help() {
	printf(HELP_TEXT);
}

bool is_flag(char *string) {
	return !(
		strcmp(string, LEFT_CHARS_OPTION) &&
		strcmp(string, RIGHT_CHARS_OPTION) &&
		strcmp(string, IGNORE_EXTRAS_OPTION) &&
		strcmp(string, HELP_OPTION) &&
		strcmp(string, READ_FROM_STDIN)
	);
}

void print_result(int result, char *string) {
	if (result == 1) printf(IS_BALANCED_MESSAGE, string);
	if (result == 0) printf(IS_NOT_BALANCED_MESSAGE, string);
}

int is_balanced(struct charstream *s, char *left, char *right, bool ignore) {
	struct node first = {true, 0, 0, 0};
	first.initial = true;
	struct node *last = &first;
	bool is_match = false;
	int getpos_left = -1;
	int getpos_right = -1;
	char current_char = '\0';
	int pos = -1;

	while(pos++, !is_terminal(current_char = get_char(s))) {
		getpos_left = getpos(current_char, left);
		getpos_right = getpos(current_char, right);

		is_match = (getpos_left != -1 || getpos_right != -1);

		if (!is_match) {
			if (ignore) {continue;} else {
				printf(INVALID_CHARACTER_MESSAGE, current_char, pos, s->string);
				free_stack(last);
				return -1;
			};
		};

		if (getpos_right != -1) {
			if (getpos(pop(&last), left) != getpos_right) {
				free_stack(last);
				return 0;
			} else continue;
		}
		else push(&last, current_char);
	};

	return last->initial;
	free_stack(last);
}

int main(int argc, char **argv) {
	struct charstream cs = {false, 0, 0};
	bool read_from_stdin = false;
	bool ignore_extras = false;
	bool *argument_input_mask; // which args are input data and which are opts
	char *left = "({[<";
	char *right = ")}]>";
	int result = 0;
	int i = 0;
	int retval = 0;

	if (argc < 2) {
		printf(NO_INPUT_MESSAGE);
		print_help();
		return 1;
	} else {
		argument_input_mask = (bool*)malloc(sizeof(bool)*argc);
		memset(argument_input_mask, 0, sizeof(bool)*argc);

		for (i = 1; i < argc; i++) {
			if (argument_input_mask[i] == true)
				{argument_input_mask[i] = false;}
			else if (!is_flag(argv[i])) argument_input_mask[i] = true;

			if (!strcmp(argv[i], HELP_OPTION)) {
				print_help();
				goto rt;
			};

			if (!strcmp(argv[i], IGNORE_EXTRAS_OPTION)) {
				ignore_extras = true;
			};

			if (!strcmp(argv[i], LEFT_CHARS_OPTION)) {
				if (i+1 < argc) {
					argument_input_mask[i+1] = true; // bear with me
					left = argv[i+1];
				} else {
					printf(INVALID_FLAG_MESSAGE, argv[i]);
				};
			};

			if (!strcmp(argv[i], RIGHT_CHARS_OPTION)) {
				if (i+1 < argc) {
					argument_input_mask[i+1] = true; // bear with me
					right = argv[i+1];
				} else {
					printf(INVALID_FLAG_MESSAGE, argv[i]);
				};
			};

			if (!strcmp(argv[i], READ_FROM_STDIN)) {
				read_from_stdin = true;
			};
		};
	};

	if (read_from_stdin) {
		cs.is_stdin = true;
		cs.ptr = 0;
		cs.string = "<stdin>";

		result = is_balanced(&cs, left, right, ignore_extras);
		print_result(result, cs.string);
	} else {
		for (i = 1; i < argc; i++) {
			if (argument_input_mask[i]) {
				cs.is_stdin = false;
				cs.ptr = 0;
				cs.string = argv[i];
				result = is_balanced(&cs, left, right, ignore_extras);
				print_result(result, cs.string);
			};
		};
	};

	rt: free(argument_input_mask);
	return retval;
}
