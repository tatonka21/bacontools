.PHONY: all install linux media web linux-install media-install misc-install web-install

all: linux media misc web
install: linux-install media-install misc-install web-install

linux:
	$(MAKE) -C "linux"

media:
	$(MAKE) -C "media"

misc:
	$(MAKE) -C "misc"

web:
	$(MAKE) -C "web"

linux-install:
	$(MAKE) -C "linux" install

media-install:
	$(MAKE) -C "media" install

misc-install:
	$(MAKE) -C "misc" install

web-install:
	$(MAKE) -C "web" install
