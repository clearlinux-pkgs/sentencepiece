#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : sentencepiece
Version  : 0.1.97
Release  : 2
URL      : https://github.com/google/sentencepiece/archive/refs/tags/v0.1.97.tar.gz
Source0  : https://github.com/google/sentencepiece/archive/refs/tags/v0.1.97.tar.gz
Summary  : Unsupervised text tokenizer and detokenizer for Neural Network-based text generation.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: sentencepiece-bin = %{version}-%{release}
Requires: sentencepiece-lib = %{version}-%{release}
Requires: sentencepiece-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : icu4c-dev
BuildRequires : protobuf-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# SentencePiece
[![Build C++](https://github.com/google/sentencepiece/actions/workflows/cmake.yml/badge.svg)](https://github.com/google/sentencepiece/actions/workflows/cmake.yml)
[![Build Wheels](https://github.com/google/sentencepiece/actions/workflows/wheel.yml/badge.svg)](https://github.com/google/sentencepiece/actions/workflows/wheel.yml)
[![GitHub Issues](https://img.shields.io/github/issues/google/sentencepiece.svg)](https://github.com/google/sentencepiece/issues)
[![PyPI version](https://badge.fury.io/py/sentencepiece.svg)](https://badge.fury.io/py/sentencepiece)
[![PyPi downloads](https://img.shields.io/pypi/dm/sentencepiece?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/sentencepiece/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://opensource.org/licenses/Apache-2.0)

%package bin
Summary: bin components for the sentencepiece package.
Group: Binaries
Requires: sentencepiece-license = %{version}-%{release}

%description bin
bin components for the sentencepiece package.


%package dev
Summary: dev components for the sentencepiece package.
Group: Development
Requires: sentencepiece-lib = %{version}-%{release}
Requires: sentencepiece-bin = %{version}-%{release}
Provides: sentencepiece-devel = %{version}-%{release}
Requires: sentencepiece = %{version}-%{release}

%description dev
dev components for the sentencepiece package.


%package lib
Summary: lib components for the sentencepiece package.
Group: Libraries
Requires: sentencepiece-license = %{version}-%{release}

%description lib
lib components for the sentencepiece package.


%package license
Summary: license components for the sentencepiece package.
Group: Default

%description license
license components for the sentencepiece package.


%prep
%setup -q -n sentencepiece-0.1.97
cd %{_builddir}/sentencepiece-0.1.97

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683661816
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1683661816
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sentencepiece
cp %{_builddir}/sentencepiece-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/sentencepiece/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/sentencepiece-%{version}/third_party/absl/LICENSE %{buildroot}/usr/share/package-licenses/sentencepiece/d5cf6efc97d21fa5e1ffd14abe61d6382c9e4701 || :
cp %{_builddir}/sentencepiece-%{version}/third_party/darts_clone/LICENSE %{buildroot}/usr/share/package-licenses/sentencepiece/1995e90082fbabd8ed1ed097878c6518ba7d826e || :
cp %{_builddir}/sentencepiece-%{version}/third_party/esaxx/LICENSE %{buildroot}/usr/share/package-licenses/sentencepiece/53af945b18e0917715623bf2ebdd6daef4c59bc2 || :
cp %{_builddir}/sentencepiece-%{version}/third_party/protobuf-lite/LICENSE %{buildroot}/usr/share/package-licenses/sentencepiece/1b5a14d06dd784e88dadc5c68344be2dc13875b6 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/spm_decode
/V3/usr/bin/spm_encode
/V3/usr/bin/spm_export_vocab
/V3/usr/bin/spm_normalize
/V3/usr/bin/spm_train
/usr/bin/spm_decode
/usr/bin/spm_encode
/usr/bin/spm_export_vocab
/usr/bin/spm_normalize
/usr/bin/spm_train

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libsentencepiece.so
/V3/usr/lib64/libsentencepiece_train.so
/usr/include/sentencepiece_processor.h
/usr/include/sentencepiece_trainer.h
/usr/lib64/libsentencepiece.so
/usr/lib64/libsentencepiece_train.so
/usr/lib64/pkgconfig/sentencepiece.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsentencepiece.so.0
/V3/usr/lib64/libsentencepiece.so.0.0.0
/V3/usr/lib64/libsentencepiece_train.so.0
/V3/usr/lib64/libsentencepiece_train.so.0.0.0
/usr/lib64/libsentencepiece.so.0
/usr/lib64/libsentencepiece.so.0.0.0
/usr/lib64/libsentencepiece_train.so.0
/usr/lib64/libsentencepiece_train.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sentencepiece/1995e90082fbabd8ed1ed097878c6518ba7d826e
/usr/share/package-licenses/sentencepiece/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/sentencepiece/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/sentencepiece/53af945b18e0917715623bf2ebdd6daef4c59bc2
/usr/share/package-licenses/sentencepiece/d5cf6efc97d21fa5e1ffd14abe61d6382c9e4701
