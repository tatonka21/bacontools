.PHONY: all install

all: httpdf

httpdf:
	go build httpdf.go

install: httpdf
	install httpdf $PREFIX/bin
