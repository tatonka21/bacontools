.PHONY: all install checkreboot-install devbup-install devrestore-install netinfo-install userls-install

all:

install: checkreboot-install devbup-install devrestore-install netinfo-install userls-install

checkreboot-install:
	$(MAKE) -C checkreboot install

devbup-install:
	$(MAKE) -C devbup install

devrestore-install:
	$(MAKE) -C devrestore install

netinfo-install:
	$(MAKE) -C netinfo install

userls-install:
	$(MAKE) -C userls install
