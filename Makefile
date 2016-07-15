export PREFIX ?= /usr/local

.PHONY: all install

all:
	patches/apply
	$(MAKE) -C linux
	$(MAKE) -C media
	$(MAKE) -C misc
	$(MAKE) -C text
	$(MAKE) -C web

install:
	$(MAKE) -C linux install
	$(MAKE) -C media install
	$(MAKE) -C misc install
	$(MAKE) -C text install
	$(MAKE) -C web install
