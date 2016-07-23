.PHONY: all install

all: build/bitdiff

build/bitdiff:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/bitdiff
	install build/bitdiff "${PREFIX}/bin"
