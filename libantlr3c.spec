#
Summary:	C language runtime for antlr3
Summary(pl.UTF-8):	Biblioteka C dla antlr3
Name:		libantlr3c
Version:	3.2
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://www.antlr.org/download/C/%{name}-%{version}.tar.gz
# Source0-md5:	674646e1d1bf5c6015435480cead725a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C runtime for antlr3

%description -l pl.UTF-8
Biblioteki C dla antlr3

%package devel
Summary:	Header files for libantlr3c library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libantlr3c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libantlr3c library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libantlr3c.

%package static
Summary:	Static libantlr3c library
Summary(pl.UTF-8):	Statyczna biblioteka libantlr3c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
