.PHONY: all install

all: build/bincounter

build/bincounter:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/bincounter
	cd build && make install
