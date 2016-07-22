pkgname=bacontools
pkgver=2016.07.15
pkgrel=1
arch=('i686' 'x86_64')
license=('mit')
url='https://github.com/bacondropped/bacontools'
makedepends=('cmake' 'ruby-bundler' 'go' 'ghc')
#source=()
source=(bacontools-$pkgver.tar.gz::https://github.com/bacondropped/bacontools/archive/$pkgver.tar.gz)
sha1sums=('SKIP')

prepare() {
	true
}

build() {
	cd "${srcdir}"/bacontools-$pkgver
	patches/apply
	cd misc/bananaglee
	sed -i 's/configure/configure --user/' Makefile
	cd ../../
	make
}

check() {
	true
}

package_bacontools() {
	pkgdesc='A collection of small, unrelated utilities'
	depends=('python2' 'python3' 'ruby' 'go' 'ghc')

	mkdir -p "${pkgdir}"/usr/share/man/man1
	mkdir -p "${pkgdir}"/usr/share/man/man3
	mkdir -p "${pkgdir}"/usr/bin

	cd "${srcdir}"/bacontools-$pkgver

	# There are problems with installation at the moment; perhaps, termdraw
	# should be adapted for a standalone installation?
	rm -r misc/termdraw
	sed -i '/termdraw/d' **/Makefile

	# imgur-dl installs imgur-dl.1 to ${PREFIX}/man/man1 instead of
	# ${PREFIX}/share/man/man1. It needs to be fixed or installation fails.
	sed -i 's/{PREFIX}\/man/{PREFIX}\/share\/man/g' web/imgur-dl/Makefile

	make DESTDIR="${pkgdir}" PREFIX="${pkgdir}"/usr install
}
