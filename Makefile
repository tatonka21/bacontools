export PREFIX ?= /usr/local

.PHONY: all install

all:
	$(MAKE) -C git
	$(MAKE) -C linux
	$(MAKE) -C media
	$(MAKE) -C misc
	$(MAKE) -C text
	$(MAKE) -C web

install:
	$(MAKE) -C git   install
	$(MAKE) -C linux install
	$(MAKE) -C media install
	$(MAKE) -C misc  install
	$(MAKE) -C text  install
	$(MAKE) -C web   install
	install bacontools.7 "${PREFIX}/share/man/man7"
	mandb

test: all
	./test-all
