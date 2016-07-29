# TODO: conform to AUR packaging standards
# Maintainer: Ilya Terentyev <bacondropped at gmail dot com>
pkgname=bacontools
pkgver=$(date +%Y-%M-%d)
pkgrel=1
pkgdesc="Collection of small, unrelated utilities"
arch=('i686' 'x86_64')
license=('MIT')
url='https://github.com/bacondropped/bacontools'
makedepends=('cmake' 'ruby-bundler' 'go' 'ghc')
source=(bacontools-dev-main.tar.gz::https://github.com/bacondropped/bacontools/archive/dev/main.tar.gz)
sha1sums=('SKIP')

build() {
	cd "${srcdir}"/bacontools-dev-main
	patches/apply
	cd misc/bananaglee
	sed -i 's/configure/configure --user/' Makefile
	cd ../../
	make
}

package_bacontools() {
	pkgdesc='Collection of small, unrelated utilities'
	depends=('python3' 'ruby')

	mkdir -p "${pkgdir}"/usr/share/man/man1
	mkdir -p "${pkgdir}"/usr/bin

	cd "${srcdir}"/bacontools-dev-main

	# There are problems with installation at the moment; perhaps, termdraw
	# should be adapted for a standalone installation?
	# Do not install termdraw for the moment.
	rm -r misc/termdraw
	sed -i '/termdraw/d' **/Makefile

	# imgur-dl installs imgur-dl.1 to ${PREFIX}/man/man1 instead of
	# ${PREFIX}/share/man/man1. It needs to be fixed or installation fails.
	sed -i 's/{PREFIX}\/man/{PREFIX}\/share\/man/g' web/imgur-dl/Makefile

	make DESTDIR="${pkgdir}" PREFIX="${pkgdir}"/usr install
}
