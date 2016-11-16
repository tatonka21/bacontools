.PHONY: all clean install

all: clean build/readable

clean:
	rm -rf ./build

build/readable:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/readable
	install build/readable "${PREFIX}/bin"
	install readable.1 "${PREFIX}/share/man/man1"
