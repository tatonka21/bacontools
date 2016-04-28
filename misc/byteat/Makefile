.PHONY: all install

all: build/byteat

build/byteat:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/byteat
	cd build && make install
