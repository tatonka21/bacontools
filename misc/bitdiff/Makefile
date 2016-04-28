.PHONY: all install

all: build/bitdiff

build/bitdiff:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/bitdiff
	cd build && make install
