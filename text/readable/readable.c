#include <getopt.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define READABLE_VERSION "1"

const char *short_options = "hc:";

struct option long_options[] = {
	{"help",   no_argument,       0, 'h'},
	{"cutoff", required_argument, 0, 'c'},
	{0,        0,                 0,  0 }
};

const char *help_text = ""\
"bacontools readable v" READABLE_VERSION "\n"
"Usage: strings some_file | readable [options...]\n"\
"Filter out unreadable (garbage) lines.\n\n"\
"COMMAND LINE OPTIONS:\n"\
" -h, --help                   Print this help text.\n"\
" -c, --cutoff                 Set the minimum readability value (default 0.5).\n"\
"";

double compute_r_index(
	const char *string
);

double compute_r_index(const char *string) {
	double result = 0;

	unsigned int lowcases = 0;
	unsigned int upcases  = 0;
	unsigned int digits   = 0;
	unsigned int others   = 0;

	unsigned int i = 0;
	unsigned int total = (unsigned int)strlen(string);

	for (i = 0; i < total - 1; i++) {
		char cur = string[i];

		// TODO: Smarter algorithm, with sequential vowels/consonants,
		// mixing of upper and lower case, spacing, etc.
		if (cur >= 'a' && cur <= 'z') {lowcases++;}
		else if (cur >= 'A' && cur <= 'Z') {upcases++;}
		else if (cur >= '0' && cur <= '9') {digits++;}
		else others++;
	};

	// BUG: Doesn't produce exact results, maybe due to IEEE754 error
	// accumulation, or maybe I just fucked this one up
	result = (2.0*lowcases
	          + 1*upcases
	        - 0.8*digits
	          - 2*others)
	/total/4+0.5;

	return result;
};

int main(int argc, char **argv) {
	char *line = NULL;
	size_t size;
	int c = 0;

	double cutoff = 0.5;

	while(1) {
		int opt_index = 0;
		c = getopt_long(argc, argv, short_options, long_options, &opt_index);
		if (c == -1) break;

		switch(c) {
		case 'h':
			printf("%s", help_text);
			exit(EXIT_SUCCESS);
		case 'c':
			cutoff = strtod(optarg, NULL);
			break;
		};
	};

	if (optind < argc) {
		fprintf(stderr, "readable: unexpected non-option "\
		                "argument %s\n", argv[optind]);
		exit(EXIT_FAILURE);
	};

	while (getline(&line, &size, stdin) != -1) {
		double r_index = compute_r_index(line);
		if (r_index >= cutoff) printf("%s", line);
	};

	return EXIT_SUCCESS;
};
