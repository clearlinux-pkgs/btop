#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : btop
Version  : 1.3.0
Release  : 8
URL      : https://github.com/aristocratos/btop/archive/v1.3.0/btop-1.3.0.tar.gz
Source0  : https://github.com/aristocratos/btop/archive/v1.3.0/btop-1.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: btop-bin = %{version}-%{release}
Requires: btop-data = %{version}-%{release}
Requires: btop-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ![btop++](Img/logo.png)
<a href="https://repology.org/project/btop/versions">
<img src="https://repology.org/badge/vertical-allrepos/btop.svg" alt="Packaging status" align="right">
</a>

%package bin
Summary: bin components for the btop package.
Group: Binaries
Requires: btop-data = %{version}-%{release}
Requires: btop-license = %{version}-%{release}

%description bin
bin components for the btop package.


%package data
Summary: data components for the btop package.
Group: Data

%description data
data components for the btop package.


%package license
Summary: license components for the btop package.
Group: Default

%description license
license components for the btop package.


%prep
%setup -q -n btop-1.3.0
cd %{_builddir}/btop-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704725735
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1704725735
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/btop
cp %{_builddir}/btop-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/btop/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/btop-%{version}/include/fmt/LICENSE.rst %{buildroot}/usr/share/package-licenses/btop/1606b4a09dd264124a044831841a83c68a2b9126 || :
pushd clr-build-avx2
%make_install_v3 PREFIX=/usr || :
popd
pushd clr-build
%make_install PREFIX=/usr
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/btop
/usr/bin/btop

%files data
%defattr(-,root,root,-)
/usr/share/applications/btop.desktop
/usr/share/btop/themes/HotPurpleTrafficLight.theme
/usr/share/btop/themes/adapta.theme
/usr/share/btop/themes/adwaita.theme
/usr/share/btop/themes/ayu.theme
/usr/share/btop/themes/dracula.theme
/usr/share/btop/themes/dusklight.theme
/usr/share/btop/themes/elementarish.theme
/usr/share/btop/themes/everforest-dark-hard.theme
/usr/share/btop/themes/flat-remix-light.theme
/usr/share/btop/themes/flat-remix.theme
/usr/share/btop/themes/greyscale.theme
/usr/share/btop/themes/gruvbox_dark.theme
/usr/share/btop/themes/gruvbox_dark_v2.theme
/usr/share/btop/themes/gruvbox_material_dark.theme
/usr/share/btop/themes/horizon.theme
/usr/share/btop/themes/kyli0x.theme
/usr/share/btop/themes/matcha-dark-sea.theme
/usr/share/btop/themes/monokai.theme
/usr/share/btop/themes/night-owl.theme
/usr/share/btop/themes/nord.theme
/usr/share/btop/themes/onedark.theme
/usr/share/btop/themes/paper.theme
/usr/share/btop/themes/solarized_dark.theme
/usr/share/btop/themes/solarized_light.theme
/usr/share/btop/themes/tokyo-night.theme
/usr/share/btop/themes/tokyo-storm.theme
/usr/share/btop/themes/tomorrow-night.theme
/usr/share/btop/themes/whiteout.theme
/usr/share/icons/hicolor/48x48/apps/btop.png
/usr/share/icons/hicolor/scalable/apps/btop.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/btop/1606b4a09dd264124a044831841a83c68a2b9126
/usr/share/package-licenses/btop/2b8b815229aa8a61e483fb4ba0588b8b6c491890
