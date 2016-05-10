.PHONY: all install checkreboot-install devbup-install netinfo-install userls-install

all:

install: checkreboot-install devbup-install netinfo-install userls-install

checkreboot-install:
	$(MAKE) -C "checkreboot" install

devbup-install:
	$(MAKE) -C "devbup" install

netinfo-install:
	$(MAKE) -C "netinfo" install

userls-install:
	$(MAKE) -C "userls" install
