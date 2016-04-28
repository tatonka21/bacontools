.PHONY: all install

all: build/corrupt

build/corrupt:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/corrupt
	cd build && make install
