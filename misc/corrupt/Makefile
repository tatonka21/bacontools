.PHONY: all install

all: build/corrupt

build/corrupt:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/corrupt
	install build/corrupt "${PREFIX}/bin"
