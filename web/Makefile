.PHONY: all install imgur-dl-install myzuka-dl-install

all: webdf

install: imgur-dl-install myzuka-dl-install webdf-install

webdf:
	$(MAKE) -C webdf

imgur-dl-install:
	$(MAKE) -C imgur-dl install

myzuka-dl-install:
	$(MAKE) -C myzuka-dl install

webdf-install:
	$(MAKE) -C webdf install
