Summary:	C run-time support for ANTLR-generated parsers
Summary(pl.UTF-8):	Biblioteka C dla antlr3
Name:		libantlr3c
Version:	3.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.antlr.org/download/C/%{name}-%{version}.tar.gz
# Source0-md5:	08b1420129d5dccd0f4461cedf2a0d7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C run-time support for ANTLR-generated parsers.

%description -l pl.UTF-8
Biblioteki C dla antlr3

%package devel
Summary:   Header files for the C bindings for ANTLR-generated parsers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libantlr3c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the C bindings for ANTLR-generated parsers

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libantlr3c.

%package static
Summary:	Static libantlr3c library
Summary(pl.UTF-8):	Statyczna biblioteka libantlr3c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libantlr3c library.

%description static -l pl.UTF-8
Statyczna biblioteka libantlr3c.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

# even there's no SONAME symlink, run ldconfig to get library into ld.so.cache
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/libantlr3c.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libantlr3c.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libantlr3c.a
