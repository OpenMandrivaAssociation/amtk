%global api	5
%global major	0
%define libname %mklibname amtk %api %major
%define girname	%mklibname amtk-gir %{api}
%define devname %mklibname -d amtk %api

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:           amtk
Version:	5.9.0
Release:	1
Summary:        Text editor product line
Group:		System/Libraries

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Amtk
#Source0:        https://download.gnome.org/sources/amtk/%{url_ver}/amtk-%{version}.tar.xz
# New name, new source.
#Source0:        https://gedit-technology.net/tarballs/libgedit-amtk/libgedit-amtk-%{version}.tar.xz
Source0:        https://gitlab.gnome.org/World/gedit/libgedit-amtk/-/archive/%{version}/libgedit-amtk-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uchardet)

Obsoletes:	%{name} < %{EVRD}

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.

%package        -n %{libname}
Summary:        Libraries for %{name}
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Provides:       libgedit-amtk = %{version}-%{release}
Obsoletes:	%{_lib}amtk5 < 4.99.1-2
Obsoletes:	%{libname} < %{EVRD}

%description    -n %{libname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for Amtk
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{name} < 4.99.1-2
Obsoletes:	%{girname} < %{EVRD}

%description -n %{girname}
GObject Introspection interface description for Amtk.

%package        -n %{devname}
Summary:        Development files for %{name}
Group:		Development/Other
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:       libgedit-amtk-devel = %{version}-%{release}
Obsoletes:	%{_lib}amtk-devel < 4.99.1-2
Obsoletes:	%{devname} < %{EVRD}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libgedit-amtk-%{version} -p1

%build
%meson  \
        -Dgtk_doc=true
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang libgedit-amtk-%{api}

%files -f libgedit-amtk-%{api}.lang
%doc NEWS README.md

%files -n %{girname}
%{_libdir}/girepository-1.0/Amtk-%{api}.typelib

%files -n %libname
%{_libdir}/libgedit-amtk-%{api}.so.%{major}*

%files -n %devname
%doc %{_datadir}/gtk-doc/html/libgedit-amtk-%{api}/
%{_includedir}/libgedit-amtk-%{api}/amtk/
%{_libdir}/libgedit-amtk-%{api}.so
%{_libdir}/pkgconfig/libgedit-amtk-%{api}.pc
%{_datadir}/gir-1.0/Amtk-%{api}.gir
