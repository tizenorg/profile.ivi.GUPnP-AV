Name:       gupnp-av
Summary:    GUPnP-AV is a collection of helpers for building UPnP AV applications
Version:    0.12.4
Release:    0
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gupnp.org/
Source0:    http://download.gnome.org/sources/%{name}/0.12/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gupnp-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala


%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video)
applications using GUPnP.

%package devel
Summary:    Development package for gupnp-av
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files for development with gupnp-av.


%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -rf  $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%{_datadir}/gupnp-av/*.xsd

%files devel
%defattr(-,root,root,-)
%{_includedir}/gupnp-av-1.0/libgupnp-av
%{_libdir}/*.so
%{_libdir}/pkgconfig/gupnp-av-1.0.pc
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi

