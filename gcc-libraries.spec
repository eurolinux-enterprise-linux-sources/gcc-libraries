%global DATE 20190223
%global DATE7 20180303
%global SVNREV 269162
%global gcc_version 8.3.1
%global gcc7_version 7.3.1
%global gcc_major 8
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 2
%global mpc_version 0.8.1
%global _unpackaged_files_terminate_build 0
%global multilib_64_archs sparc64 ppc64 ppc64p7 s390x x86_64
%ifarch %{ix86} x86_64 ia64 ppc %{power64} alpha s390x %{arm} aarch64
%global build_ada 0
%else
%global build_ada 0
%endif
%global build_objc 0
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 %{mips}
%global build_go 0
%else
%global build_go 0
%endif
%if 0%{?rhel} == 7
%ifarch %{ix86} x86_64 ia64 ppc ppc64 ppc64le
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%endif
%if 0%{?rhel} == 6
%ifarch %{ix86} x86_64 ia64 ppc64le
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%endif
%if 0%{?rhel} == 7
# libquadmath is present via system gcc on x86_64 and i686.
%ifarch ppc ppc64 ppc64le
%global package_libquadmath 1
%else
%global package_libquadmath 0
%endif
%endif
%if 0%{?rhel} == 6
%ifarch %{ix86} x86_64 ppc64le
%global package_libquadmath 1
%else
%global package_libquadmath 0
%endif
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global build_libasan 0
%else
%global build_libasan 0
%endif
%ifarch x86_64 ppc64 ppc64le aarch64
%global build_libtsan 0
%else
%global build_libtsan 0
%endif
%ifarch x86_64 ppc64 ppc64le aarch64
%global build_liblsan 0
%else
%global build_liblsan 0
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global build_libubsan 0
%else
%global build_libubsan 0
%endif
%ifarch aarch64
%if 0%{?rhel} >= 7
%global build_libatomic 1
%else
%global build_libatomic 0
%endif
%endif
%ifnarch aarch64
%if 0%{?rhel} >= 7
%global build_libatomic 0
%else
%global build_libatomic 1
%endif
%endif
%if 0%{?rhel} >= 7
%global build_libitm 0
%else
%global build_libitm 1
%endif
%global build_isl 0
%global build_libstdcxx_docs 0
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 %{mips}
%global attr_ifunc 1
%else
%global attr_ifunc 0
%endif
%ifarch s390x
%global multilib_32_arch s390
%endif
%ifarch sparc64
%global multilib_32_arch sparcv9
%endif
%ifarch ppc64 ppc64p7
%global multilib_32_arch ppc
%endif
%ifarch x86_64
%global multilib_32_arch i686
%endif
Summary: GCC runtime libraries
Name: gcc-libraries
Provides: libatomic libitm libgfortran4 libgfortran5
%if %{package_libquadmath}
Provides: libquadmath
%endif
Obsoletes: libitm
Version: %{gcc_version}
Release: %{gcc_release}.1.1%{?dist}
# libgcc, libgfortran, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: System Environment/Libraries
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-8-branch@%%{SVNREV} gcc-%%{version}-%%{DATE}
# tar cf - gcc-%%{version}-%%{DATE} | xz -9e > gcc-%%{version}-%%{DATE}.tar.xz
Source0: gcc-%{version}-%{DATE}.tar.xz
Source1: http://www.multiprecision.org/mpc/download/mpc-%{mpc_version}.tar.gz
Source2: gcc-%{gcc7_version}-%{DATE7}.tar.bz2
URL: http://gcc.gnu.org
# Need binutils with -pie support >= 2.14.90.0.4-4
# Need binutils which can omit dot symbols and overlap .opd on ppc64 >= 2.15.91.0.2-4
# Need binutils which handle -msecure-plt on ppc >= 2.16.91.0.2-2
# Need binutils which support .weakref >= 2.16.91.0.3-1
# Need binutils which support --hash-style=gnu >= 2.17.50.0.2-7
# Need binutils which support mffgpr and mftgpr >= 2.17.50.0.2-8
# Need binutils which support --build-id >= 2.17.50.0.17-3
# Need binutils which support %%gnu_unique_object >= 2.19.51.0.14
# Need binutils which support .cfi_sections >= 2.19.51.0.14-33
BuildRequires: binutils >= 2.19.51.0.14-33
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, /usr/bin/pod2man
BuildRequires: gcc, gcc-c++, gcc-gfortran
%if 0%{?rhel} >= 7
BuildRequires: texinfo-tex
%endif
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
%ifarch %{multilib_64_archs} sparcv9 ppc
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif
%ifarch ia64
BuildRequires: libunwind >= 0.98
%endif
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
# On ppc64, need omit dot symbols support and --non-overlapping-opd
# Need binutils that owns /usr/bin/c++filt
# Need binutils that support .weakref
# Need binutils that supports --hash-style=gnu
# Need binutils that support mffgpr/mftgpr
# Need binutils that support --build-id
# Need binutils that support %%gnu_unique_object
# Need binutils that support .cfi_sections
Requires: binutils >= 2.19.51.0.14-33
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
Requires: glibc >= 2.3.90-35
%endif
Requires: libgcc >= 4.1.2-43
Requires: libgomp >= 4.4.4-13
BuildRequires: gmp-devel >= 4.1.2-8
BuildRequires: mpfr-devel >= 2.2.1
%if 0%{?rhel} >= 7
BuildRequires: libmpc-devel >= 0.8.1
%endif
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
ExclusiveArch: %{ix86} x86_64 ppc ppc64 ppc64le s390 s390x aarch64

%global oformat %{nil}
%global oformat2 %{nil}
%ifarch %{ix86}
%global oformat OUTPUT_FORMAT(elf32-i386)
%endif
%ifarch x86_64
%global oformat OUTPUT_FORMAT(elf64-x86-64)
%global oformat2 OUTPUT_FORMAT(elf32-i386)
%endif
%ifarch ppc
%global oformat OUTPUT_FORMAT(elf32-powerpc)
%global oformat2 OUTPUT_FORMAT(elf64-powerpc)
%endif
%ifarch ppc64
%global oformat OUTPUT_FORMAT(elf64-powerpc)
%global oformat2 OUTPUT_FORMAT(elf32-powerpc)
%endif
%ifarch s390
%global oformat OUTPUT_FORMAT(elf32-s390)
%endif
%ifarch s390x
%global oformat OUTPUT_FORMAT(elf64-s390)
%global oformat2 OUTPUT_FORMAT(elf32-s390)
%endif
%ifarch ia64
%global oformat OUTPUT_FORMAT(elf64-ia64-little)
%endif
%ifarch ppc64le
%global oformat OUTPUT_FORMAT(elf64-powerpcle)
%endif
%ifarch aarch64
%global oformat OUTPUT_FORMAT(elf64-littleaarch64)
%endif

Patch0: gcc8-hack.patch
Patch2: gcc8-i386-libgomp.patch
Patch3: gcc8-sparc-config-detection.patch
Patch4: gcc8-libgomp-omp_h-multilib.patch
Patch5: gcc8-libtool-no-rpath.patch
Patch8: gcc8-no-add-needed.patch
Patch9: gcc8-foffload-default.patch
Patch10: gcc8-Wno-format-security.patch
Patch11: gcc8-rh1512529-aarch64.patch
Patch12: gcc8-mcet.patch

Patch1001: gcc8-alt-compat-test.patch
Patch1003: gcc8-rh1118870.patch
Patch1100: gcc8-htm-in-asm.patch

# Support for more DEC extensions in libgfortran runtime
# BZ1554429
Patch2001: 0022-Default-values-for-certain-field-descriptors-in-form.patch

# We'll be building GCC 7 in order to ship libgfortran4.
Patch7000: gcc7-hack.patch
Patch7002: gcc7-i386-libgomp.patch
Patch7003: gcc7-sparc-config-detection.patch
Patch7004: gcc7-libgomp-omp_h-multilib.patch
Patch7005: gcc7-libtool-no-rpath.patch
Patch7006: gcc7-isl-dl.patch
Patch7008: gcc7-no-add-needed.patch
Patch7009: gcc7-aarch64-async-unw-tables.patch
Patch7010: gcc7-foffload-default.patch
Patch7011: gcc7-Wno-format-security.patch
Patch7013: gcc7-rh1512529-aarch64.patch
Patch7014: gcc7-pr84524.patch
Patch7015: gcc7-pr84128.patch
Patch7016: gcc7-rh1570967.patch
Patch7102: gcc7-alt-compat-test.patch
Patch7105: gcc7-rh1118870.patch
Patch7100: gcc7-htm-in-asm.patch

# Support for more DEC extensions in libgfortran runtime
# BZ1554429
Patch7200: gcc7-0000-infrastructure.patch
Patch7201: gcc7-0022-Default-values-for-certain-field-descriptors-in-form.patch

%global _gnu %{nil}
%ifarch sparcv9
%global gcc_target_platform sparc64-%{_vendor}-%{_target_os}%{?_gnu}
%endif
%ifarch ppc ppc64p7
%global gcc_target_platform ppc64-%{_vendor}-%{_target_os}%{?_gnu}
%endif
%ifnarch sparcv9 ppc ppc64p7
%global gcc_target_platform %{_target_platform}
%endif

%description
This package contains various GCC runtime libraries, such as libatomic,
or libitm.

%package -n libitm
Summary: The GNU Transactional Memory library
Group: System Environment/Libraries
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description -n libitm
This package contains the GNU Transactional Memory library
which is a GCC transactional memory support runtime library.

%package -n libatomic
Summary: The GNU Atomic library
Group: System Environment/Libraries
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description -n libatomic
This package contains the GNU Atomic library
which is a GCC support runtime library for atomic operations not supported
by hardware.

%package -n libgfortran4
Summary: Fortran runtime v4
Group: System Environment/Libraries
Autoreq: true
%if %{build_libquadmath}
Requires: libquadmath
%endif

%description -n libgfortran4
This package contains Fortran shared library v4 which is needed to run
Fortran dynamically linked programs.

%package -n libgfortran5
Summary: Fortran runtime v5
Group: System Environment/Libraries
Autoreq: true
%if %{build_libquadmath}
Requires: libquadmath
%endif

%description -n libgfortran5
This package contains Fortran shared library v5 which is needed to run
Fortran dynamically linked programs.

%package -n libquadmath
Summary: GCC __float128 shared support library
Group: System Environment/Libraries
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description -n libquadmath
This package contains GCC shared support library which is needed
for __float128 math support and for Fortran REAL*16 support.

%prep
# Also unpack GCC 7 sources.
%if 0%{?rhel} >= 7
%setup -q -n gcc-%{version}-%{DATE} -a 2
%else
%setup -q -n gcc-%{version}-%{DATE} -a 1 -a 2
%endif
%patch0 -p0 -b .hack~
%patch2 -p0 -b .i386-libgomp~
%patch3 -p0 -b .sparc-config-detection~
%patch4 -p0 -b .libgomp-omp_h-multilib~
%patch5 -p0 -b .libtool-no-rpath~
%patch8 -p0 -b .no-add-needed~
%patch9 -p0 -b .foffload-default~
%patch10 -p0 -b .Wno-format-security~
%patch11 -p0 -b .rh1512529-aarch64~

%ifarch %{ix86} x86_64
%if 0%{?rhel} < 7
# On i?86/x86_64 there are some incompatibilities in _Decimal* as well as
# aggregates containing larger vector passing.
%patch1001 -p0 -b .alt-compat-test~
%endif
%endif

%patch1003 -p0 -b .rh1118870~
%patch1100 -p0 -b .gcc8-htm-in-asm~

%patch2001 -p1 -b .dec-extensions-2~

%if 0%{?rhel} == 6
# Default to -gdwarf-3 rather than -gdwarf-4
sed -i '/UInteger Var(dwarf_version)/s/Init(4)/Init(3)/' gcc/common.opt
sed -i 's/\(may be either 2, 3 or 4; the default version is \)4\./\13./' gcc/doc/invoke.texi
%endif

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h
cp -a libstdc++-v3/config/cpu/i{4,3}86/opt
echo 'TM_H += $(srcdir)/config/rs6000/rs6000-modes.h' >> gcc/config/rs6000/t-rs6000

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt

%ifarch ppc
if [ -d libstdc++-v3/config/abi/post/powerpc64-linux-gnu ]; then
  mkdir -p libstdc++-v3/config/abi/post/powerpc64-linux-gnu/64
  mv libstdc++-v3/config/abi/post/powerpc64-linux-gnu/{,64/}baseline_symbols.txt
  mv libstdc++-v3/config/abi/post/powerpc64-linux-gnu/{32/,}baseline_symbols.txt
  rm -rf libstdc++-v3/config/abi/post/powerpc64-linux-gnu/32
fi
%endif
%ifarch sparc
if [ -d libstdc++-v3/config/abi/post/sparc64-linux-gnu ]; then
  mkdir -p libstdc++-v3/config/abi/post/sparc64-linux-gnu/64
  mv libstdc++-v3/config/abi/post/sparc64-linux-gnu/{,64/}baseline_symbols.txt
  mv libstdc++-v3/config/abi/post/sparc64-linux-gnu/{32/,}baseline_symbols.txt
  rm -rf libstdc++-v3/config/abi/post/sparc64-linux-gnu/32
fi
%endif

# This test causes fork failures, because it spawns way too many threads
rm -f gcc/testsuite/go.test/test/chan/goroutines.go

# Apply GCC 7 patches.
pushd gcc-%{gcc7_version}-%{DATE7}
%patch7000 -p0 -b .hack~
%patch7002 -p0 -b .i386-libgomp~
%patch7003 -p0 -b .sparc-config-detection~
%patch7004 -p0 -b .libgomp-omp_h-multilib~
%patch7005 -p0 -b .libtool-no-rpath~
%patch7008 -p0 -b .no-add-needed~
%patch7009 -p0 -b .aarch64-async-unw-tables~
%patch7010 -p0 -b .foffload-default~
%patch7011 -p0 -b .Wno-format-security~
%patch7013 -p0 -b .rh1512529-aarch64~
%patch7014 -p0 -b .pr84524~
%patch7015 -p0 -b .pr84128~
%patch7016 -p0 -b .rh1570967~

sed -i -e 's/ -Wl,-z,nodlopen//g' gcc/ada/gcc-interface/Makefile.in

%ifarch %{ix86} x86_64
%if 0%{?rhel} < 7
# On i?86/x86_64 there are some incompatibilities in _Decimal* as well as
# aggregates containing larger vector passing.
%patch7102 -p0 -b .alt-compat-test~
%endif
%endif

%patch7105 -p0 -b .rh1118870~
%patch7100 -p0 -b .gcc7-htm-in-asm~

%patch7200 -p1 -b .dec-extensions~
%patch7201 -p1 -b .dec-extensions-2~
popd

%build

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

rm -fr obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}


%if 0%{?rhel} < 7
mkdir mpc mpc-install
cd mpc
../../mpc-%{mpc_version}/configure --disable-shared \
  CFLAGS="${CFLAGS:-%optflags} -fPIC" CXXFLAGS="${CXXFLAGS:-%optflags} -fPIC" \
  --prefix=`cd ..; pwd`/mpc-install
make %{?_smp_mflags}
make install
cd ..
%endif

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
%ifarch sparc
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mcpu=ultrasparc/-mtune=ultrasparc/g;s/-mcpu=v[78]//g'`
%endif
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-shared --enable-threads=posix --enable-checking=release \
%ifarch ppc64le
	--enable-targets=powerpcle-linux \
%endif
%ifarch ppc64le %{mips} riscv64
	--disable-multilib \
%else
	--enable-multilib \
%endif
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
%ifnarch %{mips}
	--with-linker-hash-style=gnu \
%endif
	--enable-plugin --enable-initfini-array \
	--without-isl \
	--disable-libmpx \
	--disable-libsanitizer \
%if 0%{?rhel} < 7
	--with-mpc=%{buildroot}/obj-%{gcc_target_platform}/mpc-install \
%endif
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%if %{attr_ifunc}
	--enable-gnu-indirect-function \
%endif
%endif
%ifarch %{arm}
	--disable-sjlj-exceptions \
%endif
%ifarch ppc ppc64 ppc64le ppc64p7
	--enable-secureplt \
%endif
%ifarch sparc sparcv9 sparc64 ppc ppc64 ppc64le ppc64p7 s390 s390x alpha
	--with-long-double-128 \
%endif
%ifarch sparc
	--disable-linux-futex \
%endif
%ifarch sparc64
	--with-cpu=ultrasparc \
%endif
%ifarch sparc sparcv9
	--host=%{gcc_target_platform} --build=%{gcc_target_platform} --target=%{gcc_target_platform} --with-cpu=v7
%endif
%ifarch ppc ppc64 ppc64p7
%if 0%{?rhel} >= 7
	--with-cpu-32=power7 --with-tune-32=power7 --with-cpu-64=power7 --with-tune-64=power7 \
%endif
%if 0%{?rhel} == 6
	--with-cpu-32=power4 --with-tune-32=power6 --with-cpu-64=power4 --with-tune-64=power6 \
%endif
%endif
%ifarch ppc64le
	--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%ifarch ppc
	--build=%{gcc_target_platform} --target=%{gcc_target_platform} --with-cpu=default32
%endif
%ifarch %{ix86} x86_64
	--with-tune=generic \
%endif
%if 0%{?rhel} >= 7
%ifarch %{ix86}
	--with-arch=x86-64 \
%endif
%ifarch x86_64
	--with-arch_32=x86-64 \
%endif
%else
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%endif
%ifarch s390 s390x
%if 0%{?rhel} >= 7
%if 0%{?rhel} >= 8
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z196 --with-tune=zEC12 \
%endif
%else
%if 0%{?fedora} >= 26
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z9-109 --with-tune=z10 \
%endif
%endif
	--enable-decimal-float \
%endif
%ifarch armv7hl
	--with-tune=generic-armv7-a --with-arch=armv7-a \
	--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux \
%endif
%ifarch mips mipsel
	--with-arch=mips32r2 --with-fp-32=xx \
%endif
%ifarch mips64 mips64el
	--with-arch=mips64r2 --with-abi=64 \
%endif
%ifnarch sparc sparcv9 ppc
	--build=%{gcc_target_platform} \
%endif
	"

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --disable-bootstrap \
	--enable-languages=c,c++,fortran,lto \
	$CONFIGURE_OPTS

%ifarch sparc sparcv9 sparc64
make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS"
%else
make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS"
%endif


# Copy various doc files here and there
cd ..
mkdir -p rpm.doc/libquadmath rpm.doc/gfortran rpm.doc/libatomic rpm.doc/libitm

(cd libgfortran; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/gfortran/$i.libgfortran
done)
%if %{build_libquadmath}
(cd libquadmath; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/libquadmath/$i.libquadmath
done)
%endif
%if %{build_libitm}
(cd libitm; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/libitm/$i.libitm
done)
%endif
%if %{build_libatomic}
(cd libatomic; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/libatomic/$i.libatomic
done)
%endif

rm -f rpm.doc/changelogs/gcc/ChangeLog.[1-9]
find rpm.doc -name \*ChangeLog\* | xargs bzip2 -9

# Handle GCC 7.  We'll not bootstrap as we're only interested in
# libgfortran.so.4.
cd gcc-%{gcc7_version}-%{DATE7}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --disable-bootstrap \
	--enable-languages=c,c++,fortran,lto \
	$CONFIGURE_OPTS
make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS"

%install
rm -rf %{buildroot}

cd obj-%{gcc_target_platform}

# Make sure libcilkrts can use system libgcc_s.so.1.
rm -f gcc/libgcc_s.so
echo '/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
%{oformat}
GROUP ( /%{_lib}/libgcc_s.so.1 libgcc.a )' > gcc/libgcc_s.so

mkdir -p %{buildroot}%{_prefix}/%{_lib}
mkdir -p %{buildroot}%{_infodir}

# Use make install DESTDIR trick to avoid bogus RPATHs.
%if %{build_libitm}
cd %{gcc_target_platform}/libitm/
mkdir temp
make install DESTDIR=`pwd`/temp
cp -a temp/usr/%{_lib}/libitm.so.1* %{buildroot}%{_prefix}/%{_lib}/
cp -a libitm.info %{buildroot}%{_infodir}/
cd ../..
%endif

%if %{build_libatomic}
cd %{gcc_target_platform}/libatomic/
mkdir temp
make install DESTDIR=`pwd`/temp
cp -a temp/usr/%{_lib}/libatomic.so.1* %{buildroot}%{_prefix}/%{_lib}/
cd ../..
%endif

%if %{build_libquadmath}
cd %{gcc_target_platform}/libquadmath/
mkdir temp
make install DESTDIR=`pwd`/temp
%if %{package_libquadmath}
cp -a temp/usr/%{_lib}/libquadmath.so.0* %{buildroot}%{_prefix}/%{_lib}/
%endif
cd ../..
%endif

cd %{gcc_target_platform}/libgfortran/
mkdir temp
%if %{build_libquadmath}
# It needs to find libquadmath.so.
export LIBRARY_PATH=`pwd`/../../%{gcc_target_platform}/libquadmath/temp/usr/%{_lib}
%endif
make install DESTDIR=`pwd`/temp
cp -a temp/usr/%{_lib}/libgfortran.so.5* %{buildroot}%{_prefix}/%{_lib}/
cd ../..


# Remove binaries we will not be including, so that they don't end up in
# gcc-libraries-debuginfo.
%if 0%{?rhel} >= 7
# None.
%endif

rm -f gcc/libgcc_s.so
ln -sf libgcc_s.so.1 gcc/libgcc_s.so


# GCC 7.  Up to my old tricks again.
cd ../gcc-%{gcc7_version}-%{DATE7}/obj-%{gcc_target_platform}

%if %{build_libquadmath}
cd %{gcc_target_platform}/libquadmath/
mkdir temp
make install DESTDIR=`pwd`/temp
cd ../..
%endif

cd %{gcc_target_platform}/libgfortran/
mkdir temp
%if %{build_libquadmath}
# It needs to find libquadmath.so.
export LIBRARY_PATH=`pwd`/../../%{gcc_target_platform}/libquadmath/temp/usr/%{_lib}
%endif
make install DESTDIR=`pwd`/temp
cp -a temp/usr/%{_lib}/libgfortran.so.4* %{buildroot}%{_prefix}/%{_lib}/
cd ../..

%check
cd obj-%{gcc_target_platform}

# run the tests.
make %{?_smp_mflags} -k check RUNTESTFLAGS="--target_board=unix/'{,-fstack-protector}'" || :
( LC_ALL=C ../contrib/test_summary -t || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}' > testresults
echo ====================TESTING=========================
cat testresults
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | bzip2 -9c \
  | uuencode testlogs-%{_target_platform}.tar.bz2 || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

# GCC 7.  Only test Fortran.
cd ../gcc-%{gcc7_version}-%{DATE7}/obj-%{gcc_target_platform}
make %{?_smp_mflags} -C gcc check-gfortran || :
( LC_ALL=C ../contrib/test_summary -t || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}' > testresults
echo ====================TESTING 7========================
cat testresults
echo ====================TESTING 7 END====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | bzip2 -9c \
  | uuencode testlogs-%{_target_platform}.tar.bz2 || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

%post -n libitm
/sbin/ldconfig
if [ -f %{_infodir}/libitm.info.gz ]; then
  /sbin/install-info \
    --info-dir=%{_infodir} %{_infodir}/libitm.info.gz || :
fi

%post -n libatomic
/sbin/ldconfig
if [ -f %{_infodir}/libatomic.info.gz ]; then
  /sbin/install-info \
    --info-dir=%{_infodir} %{_infodir}/libatomic.info.gz || :
fi

%post -n libgfortran4
/sbin/ldconfig
if [ -f %{_infodir}/libgfortran.info.gz ]; then
  /sbin/install-info \
    --info-dir=%{_infodir} %{_infodir}/libgfortran.info.gz || :
fi
%post -n libgfortran5
/sbin/ldconfig
if [ -f %{_infodir}/libgfortran.info.gz ]; then
  /sbin/install-info \
    --info-dir=%{_infodir} %{_infodir}/libgfortran.info.gz || :
fi

%post -n libquadmath
/sbin/ldconfig
if [ -f %{_infodir}/libquadmath.info.gz ]; then
  /sbin/install-info \
    --info-dir=%{_infodir} %{_infodir}/libquadmath.info.gz || :
fi

%preun -n libitm
if [ $1 = 0 -a -f %{_infodir}/libitm.info.gz ]; then
  /sbin/install-info --delete \
    --info-dir=%{_infodir} %{_infodir}/libitm.info.gz || :
fi

%preun -n libatomic
if [ $1 = 0 -a -f %{_infodir}/libatomic.info.gz ]; then
  /sbin/install-info --delete \
    --info-dir=%{_infodir} %{_infodir}/libatomic.info.gz || :
fi

%preun -n libgfortran4
if [ $1 = 0 -a -f %{_infodir}/libgfortran.info.gz ]; then
  /sbin/install-info --delete \
    --info-dir=%{_infodir} %{_infodir}/libgfortran.info.gz || :
fi

%preun -n libgfortran5
if [ $1 = 0 -a -f %{_infodir}/libgfortran.info.gz ]; then
  /sbin/install-info --delete \
    --info-dir=%{_infodir} %{_infodir}/libgfortran.info.gz || :
fi

%preun -n libquadmath
if [ $1 = 0 -a -f %{_infodir}/libquadmath.info.gz ]; then
  /sbin/install-info --delete \
    --info-dir=%{_infodir} %{_infodir}/libquadmath.info.gz || :
fi

%postun -n libitm -p /sbin/ldconfig

%postun -n libatomic -p /sbin/ldconfig

%postun -n libgfortran4 -p /sbin/ldconfig

%postun -n libgfortran5 -p /sbin/ldconfig

%postun -n libquadmath -p /sbin/ldconfig

%if %{build_libitm}
%files -n libitm
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libitm.so.1*
%{_infodir}/libitm.info*

%doc gcc/COPYING3 COPYING.RUNTIME rpm.doc/libitm/*
%endif

%if %{build_libatomic}
%files -n libatomic
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libatomic.so.1*

%doc gcc/COPYING3 COPYING.RUNTIME rpm.doc/libatomic/*
%endif

%files -n libgfortran4
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libgfortran.so.4*

%doc gcc/COPYING3 COPYING.RUNTIME rpm.doc/gfortran/*

%files -n libgfortran5
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libgfortran.so.5*

%doc gcc/COPYING3 COPYING.RUNTIME rpm.doc/gfortran/*

%if %{package_libquadmath}
%files -n libquadmath
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libquadmath.so.0*

%doc gcc/COPYING3 COPYING.RUNTIME rpm.doc/libquadmath/*
%endif

%changelog
* Mon Feb 25 2019 Marek Polacek <polacek@redhat.com> 8.3.1-2.1.1
- update from Fedora 8.3.1-2 gcc (#1551629)

* Mon Aug 27 2018 Marek Polacek <polacek@redhat.com> 8.2.1-1.3.1
- update 0022-Default-values-for-certain-field-descriptors-in-form.patch

* Fri Jul 27 2018 Marek Polacek <polacek@redhat.com> 8.2.1-1.2.1
- add %preun for libgfortran4

* Fri Jul 27 2018 Marek Polacek <polacek@redhat.com> 8.2.1-1.1.1
- update from gcc-8.2.1-1

* Wed Jul 25 2018 Marek Polacek <polacek@redhat.com> 8.1.1-5.2.1
- also package libgfortran4 (#1600265)

* Tue Jul 10 2018 Marek Polacek <polacek@redhat.com> 8.1.1-5.1.1
- update from gcc-8.1.1-5

* Tue Jul 10 2018 Marek Polacek <polacek@redhat.com> 8.1.1-4.1.1
- update from gcc-8.1.1-4

* Wed Jun 13 2018 Marek Polacek <polacek@redhat.com> 7.3.1-5.1.1
- update from devtoolset-7-gcc-7.3.1-5.10

* Tue Apr  3 2018 Marek Polacek <polacek@redhat.com> 7.2.1-1.2.1
- Add support for DEC formatting extensions (#1554430)

* Thu Oct 19 2017 Marek Polacek <polacek@redhat.com> 7.2.1-1.1.1
- update from gcc-7.2.1-1 (#1477224)

* Tue Jun 20 2017 Marek Polacek <polacek@redhat.com> 7.1.1-2.2.1
- don't run make check with -fstack-protector on ppc64le

* Thu Jun 15 2017 Marek Polacek <polacek@redhat.com> 7.1.1-2.1.1
- bump gcc_release (DTS7 gcc-gfortran requires libgfortran4 >= 7.1.1-2)

* Mon Jun 12 2017 Marek Polacek <polacek@redhat.com> 7.1.1-1.2.1
- remove libquadmath.so.* so that it doesn't end up in debuginfo

* Mon Jun  5 2017 Marek Polacek <polacek@redhat.com> 7.1.1-1.1.1
- rename libgfortran2 to libgfortran4
- update from Fedora gcc-7.1.1-2.fc27
 
* Wed May 24 2017 Marek Polacek <polacek@redhat.com> 7.0.1-4.2.1
- also build on ppc64le

* Mon Mar 20 2017 Marek Polacek <polacek@redhat.com> 7.0.1-4.1.1
- also build on aarch64
- drop libitm
- only enable libatomic for aarch64

* Fri Mar 17 2017 Marek Polacek <polacek@redhat.com> 7.0.1-3.1.1
- drop libquadmath and rename libgfortran to libgfortran2

* Wed Mar 15 2017 Marek Polacek <polacek@redhat.com> 7.0.1-2.1.1
- also include the libquadmath subpackage

* Tue Mar 14 2017 Marek Polacek <polacek@redhat.com> 7.0.1-1.1.1
- update from Fedora 7.0.1-0.12.fc26 (#1412815)
- add the libgfortran subpackage

* Wed Oct 19 2016 Marek Polacek <polacek@redhat.com> 6.2.1-1.1.1
- update from DTS 6.2.1 (#1265255)

* Tue Oct 18 2016 Marek Polacek <polacek@redhat.com> 5.3.1-1.1.1
- update from DTS 5.3.1 (#1265255)
- run the whole testsuite (because of Cilk+)

* Tue Dec 15 2015 Marek Polacek <polacek@redhat.com> 5.2.1-2.1.1
- update from DTS 5.2.1-2 (#1265253)
- drop libmpx (#1275357)

* Fri Apr 10 2015 Marek Polacek <polacek@redhat.com> 5.0.0-1.1.1
- update from Fedora gcc-5.0.0-0.21.fc22
- add libmpx subpackage on x86

* Mon Jun 02 2014 Marek Polacek <polacek@redhat.com> 4.9.0-6.1.1
- make sure libcilkrts can use system libgcc_s.so.1 (#1101277)
- update from DTS gcc-4.9.0-6

* Fri May 23 2014 Marek Polacek <polacek@redhat.com> 4.9.0-5.2.1
- prevent bogus RPATHs

* Wed May 14 2014 Marek Polacek <polacek@redhat.com> 4.9.0-5.1.1
- update from DTS gcc-4.9.0-5
- add libcilkrts

* Mon Apr 28 2014 Marek Polacek <polacek@redhat.com> 4.8.2-12.1.1
- update from DTS gcc-4.8.2-12

* Wed Aug 14 2013 Marek Polacek <polacek@redhat.com> 4.8.1-4.2.1
- always build HTM bits in libitm (#996683, #996682)

* Fri Jul 19 2013 Marek Polacek <polacek@redhat.com> 4.8.1-4.1.1
- update from DTS gcc-4.8.1-4

* Wed May 29 2013 Marek Polacek <polacek@redhat.com> 4.8.0-5.1.1
- update from DTS gcc-4.8.0-5
- build libitm even for s390{,x}

* Thu May 02 2013 Marek Polacek <polacek@redhat.com> 4.8.0-3.1.1
- new package
