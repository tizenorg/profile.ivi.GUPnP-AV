# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       gupnp-av
Summary:    GUPnP-AV is a collection of helpers for building UPnP AV applications
Version:    0.10.3
Release:    0
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gupnp.org/
Source0:    http://download.gnome.org/sources/%{name}/0.10/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gupnp-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)


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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -rf  $RPM_BUILD_ROOT%{_datadir}/gtk-doc
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/gupnp-av-1.0/libgupnp-av
%{_libdir}/*.so
%{_libdir}/pkgconfig/gupnp-av-1.0.pc
# << files devel
