#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : itstool
Version  : 2.0.6
Release  : 32
URL      : http://files.itstool.org/itstool/itstool-2.0.6.tar.bz2
Source0  : http://files.itstool.org/itstool/itstool-2.0.6.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: itstool-bin = %{version}-%{release}
Requires: itstool-data = %{version}-%{release}
Requires: itstool-license = %{version}-%{release}
Requires: itstool-man = %{version}-%{release}
Requires: libxml2-python
BuildRequires : buildreq-distutils3
BuildRequires : libxml2-dev
BuildRequires : libxml2-python3
BuildRequires : llvm

%description


%package bin
Summary: bin components for the itstool package.
Group: Binaries
Requires: itstool-data = %{version}-%{release}
Requires: itstool-license = %{version}-%{release}

%description bin
bin components for the itstool package.


%package data
Summary: data components for the itstool package.
Group: Data

%description data
data components for the itstool package.


%package license
Summary: license components for the itstool package.
Group: Default

%description license
license components for the itstool package.


%package man
Summary: man components for the itstool package.
Group: Default

%description man
man components for the itstool package.


%prep
%setup -q -n itstool-2.0.6
cd %{_builddir}/itstool-2.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604443086
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604443086
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/itstool
cp %{_builddir}/itstool-2.0.6/COPYING %{buildroot}/usr/share/package-licenses/itstool/48703751ffc7d48dc3aa9609be19dd542cf9776b
cp %{_builddir}/itstool-2.0.6/COPYING.GPL3 %{buildroot}/usr/share/package-licenses/itstool/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/itstool

%files data
%defattr(-,root,root,-)
/usr/share/itstool/its/docbook.its
/usr/share/itstool/its/docbook5.its
/usr/share/itstool/its/its.its
/usr/share/itstool/its/mallard.its
/usr/share/itstool/its/ttml.its
/usr/share/itstool/its/xhtml.its

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/itstool/48703751ffc7d48dc3aa9609be19dd542cf9776b
/usr/share/package-licenses/itstool/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/itstool.1
