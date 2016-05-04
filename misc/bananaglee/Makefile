.PHONY: all bananaglee install

all: bananaglee

bananaglee:
	runghc Setup.hs configure && runghc Setup.hs build

install: bananaglee
	runghc Setup.hs install
