export PREFIX ?= /usr/local

.PHONY: all install patch linux media misc text web linux-install media-install misc-install text-install web-install

all: linux media misc text web
install: patch linux-install media-install misc-install text-install web-install

patch:
	patches/apply

linux:
	$(MAKE) -C linux

media:
	$(MAKE) -C media

misc:
	$(MAKE) -C misc

text:
	$(MAKE) -C text

web:
	$(MAKE) -C web

linux-install:
	$(MAKE) -C linux install

media-install:
	$(MAKE) -C media install

misc-install:
	$(MAKE) -C misc install

text-install:
	$(MAKE) -C text install

web-install:
	$(MAKE) -C web install
