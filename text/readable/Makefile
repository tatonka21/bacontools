.PHONY: all clean install

all: clean build/readable

clean:
	rm -rf ./build

build/readable:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: clean build/readable
	cd build && make install
	# XXX: should we do this in CMakeLists.txt?
	install readable.1 "${PREFIX}/share/man/man1"
	mandb
