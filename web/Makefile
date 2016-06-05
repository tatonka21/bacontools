.PHONY: all install imgur-dl-install myzuka-dl-install respcode-install

all: httpdf

install: imgur-dl-install myzuka-dl-install httpdf-install respcode-install

httpdf:
	$(MAKE) -C httpdf

imgur-dl-install:
	$(MAKE) -C imgur-dl install

myzuka-dl-install:
	$(MAKE) -C myzuka-dl install

httpdf-install:
	$(MAKE) -C httpdf install

respcode-install:
	$(MAKE) -C respcode install
