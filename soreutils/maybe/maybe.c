#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define YES_MESSAGE "y"
#define NO_MESSAGE "n"

// TODO: Help text
// TODO: Like coreutils yes, allow custom options

int main(int argc, char** argv) {
	srand(time(NULL));

	while (1)
		printf("%s\n", rand() % 2 ? YES_MESSAGE : NO_MESSAGE);

	return 0;
}
