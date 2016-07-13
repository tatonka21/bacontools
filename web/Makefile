.PHONY: all install httpdf

all: httpdf

httpdf:
	$(MAKE) -C httpdf

install: all
	$(MAKE) -C curl-tt install
	$(MAKE) -C httpdf install
	$(MAKE) -C imgur-dl install
	$(MAKE) -C myzuka-dl install
	$(MAKE) -C respcode install
	$(MAKE) -C wget-page install
