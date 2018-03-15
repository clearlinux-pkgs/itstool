#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : itstool
Version  : 2.0.4
Release  : 18
URL      : http://files.itstool.org/itstool/itstool-2.0.4.tar.bz2
Source0  : http://files.itstool.org/itstool/itstool-2.0.4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: itstool-bin
Requires: itstool-data
Requires: itstool-doc
Requires: libxml2-python
BuildRequires : libxml2-dev
BuildRequires : libxml2-python3
BuildRequires : llvm-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description


%package bin
Summary: bin components for the itstool package.
Group: Binaries
Requires: itstool-data

%description bin
bin components for the itstool package.


%package data
Summary: data components for the itstool package.
Group: Data

%description data
data components for the itstool package.


%package doc
Summary: doc components for the itstool package.
Group: Documentation

%description doc
doc components for the itstool package.


%prep
%setup -q -n itstool-2.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521081659
export CC=clang
export CXX=clang++
export LD=ld.gold
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1521081659
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
