.PHONY: all install

all: build/maybe

build/maybe:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/maybe
	cd build && make install
