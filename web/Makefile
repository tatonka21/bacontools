.PHONY: all install httpdf httpdf-install imgur-dl-install myzuka-dl-install respcode-install

all: httpdf

install: httpdf-install imgur-dl-install myzuka-dl-install respcode-install

httpdf:
	$(MAKE) -C httpdf

httpdf-install:
	$(MAKE) -C httpdf install

imgur-dl-install:
	$(MAKE) -C imgur-dl install

myzuka-dl-install:
	$(MAKE) -C myzuka-dl install

respcode-install:
	$(MAKE) -C respcode install
