.PHONY: all install

all: build/n7m

build/n7m:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/n7m
	install build/n7m "${PREFIX}/bin"
