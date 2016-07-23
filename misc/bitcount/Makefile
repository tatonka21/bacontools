.PHONY: all install

all: build/bitcount

build/bitcount:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/bitcount
	install build/bitcount "${PREFIX}/bin"
