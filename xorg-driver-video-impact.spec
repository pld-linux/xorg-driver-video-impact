Summary:	X.org video driver for SGI Indigo2 and Octane
Summary(pl.UTF-8):   Sterownik obrazu X.org dla SGI Indigo2 i Octane
Name:		xorg-driver-video-impact
Version:	0.2.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-impact-%{version}.tar.bz2
# Source0-md5:	07c9557f6529a88845b01924313e5763
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
ExclusiveArch:	mips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for SGI Indigo2 and Octane.

%description -l pl.UTF-8
Sterownik obrazu X.org dla SGI Indigo2 i Octane.

%prep
%setup -q -n xf86-video-impact-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog XF86Config.impact
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/impact_drv.so
%{_mandir}/man4/impact.4*
