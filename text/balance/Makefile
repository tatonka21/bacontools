.PHONY: all install

all: build/balance

build/balance:
	mkdir -p build && cd build && cmake .. && $(MAKE)

install: build/balance
	install build/balance "${PREFIX}/bin"
