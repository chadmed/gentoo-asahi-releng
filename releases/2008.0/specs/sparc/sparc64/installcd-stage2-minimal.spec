subarch: sparc64
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/sparc/2008.0
snapshot: 2008.0
source_subpath: default/livecd-stage1-sparc64-2008.0

livecd/fstype: squashfs
livecd/cdtar: /home/armin76/tmp/silo-1.4.13-sparc-cdtar-2008.0.tar.bz2

livecd/type: gentoo-release-minimal
livecd/volid: Gentoo Linux SPARC64 2008.0
livecd/iso: /var/tmp/catalyst/builds/default/install-sparc64-minimal-2008.0.iso

boot/kernel: gentoo
boot/kernel/gentoo/sources: ~sys-kernel/gentoo-sources-2.6.23
boot/kernel/gentoo/config: ../../../kconfig/sparc/installcd-2.6.23.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb -qt3 -qt4 -X
boot/kernel/gentoo/packages:
	sys-fs/ntfs3g

livecd/unmerge:
	autoconf
	automake
	binutils
	bison
	busybox
	ccache
	flex
	gcc
	gcc-sparc64
	gettext
	groff
	kgcc64
	libtool
	linux-headers
	m4
	make
	man
	man-pages
	patch
	sandbox
	texinfo

livecd/empty:
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/rsync
	/etc/skel
	/root/.ccache
	/tmp
	/usr/lib/binutils
	/usr/lib/gcc
	/usr/lib/gconv
	/usr/lib/perl5
	/usr/lib/portage
	/usr/lib/python2.4/test
	/usr/local
	/usr/portage
	/usr/share/man
	/usr/share/info
	/usr/share/unimaps
	/usr/include
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/gcc-data
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/libtool
	/usr/share/locale
	/usr/share/man
	/usr/share/perl
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/zoneinfo
	/usr/sparc-unknown-linux-gnu
	/usr/src
	/usr/X11R6
	/var/cache
	/var/db
	/var/empty
	/var/lib/portage
	/var/lock
	/var/log
	/var/run
	/var/tmp

livecd/rm:
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/genkernel.conf
	/etc/make.conf
	/etc/make.conf.example
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/lib/*.a
	/sbin/fsck.cramfs
	/sbin/fsck.minix
	/sbin/mkfs.bfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
	/usr/bin/addr2line
	/usr/bin/ar
	/usr/bin/as
	/usr/bin/audioctl
	/usr/bin/c++*
	/usr/bin/cc
	/usr/bin/cjpeg
	/usr/bin/cpp
	/usr/bin/djpeg
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
	/usr/bin/gprof
	/usr/bin/jpegtran
	/usr/bin/libpng*
	/usr/bin/ld
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback
	/usr/bin/piggyback64
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
	/usr/bin/sparc-unknown-linux-gnu-*
	/usr/bin/sparc64-unknown-linux-gnu-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/lib/*.a
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
