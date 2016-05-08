.PHONY: all clean install

all: clean build/readable

clean:
	rm -rf ./build

build/readable:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: clean build/readable
	cd build && make install
