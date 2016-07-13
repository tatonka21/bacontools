.PHONY: all install

all:
	$(MAKE) -C bananaglee
	$(MAKE) -C bitcount
	$(MAKE) -C bitdiff
	$(MAKE) -C byteat
	$(MAKE) -C corrupt
	$(MAKE) -C maybe

install: all
	$(MAKE) -C apdiff install
	$(MAKE) -C bananaglee install
	$(MAKE) -C baconplaylist install
	$(MAKE) -C bitcount install
	$(MAKE) -C bitdiff install
	$(MAKE) -C byteat install
	$(MAKE) -C corrupt install
	$(MAKE) -C git-ls install
	$(MAKE) -C maybe install
	$(MAKE) -C pip-upgrade-all install
	$(MAKE) -C stopwatch install
	$(MAKE) -C tasktags install
	$(MAKE) -C termdraw install
	$(MAKE) -C update-all install
