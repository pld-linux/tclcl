Summary:	Tcl/C++ interface
Summary(pl):	Interfejs Tcl/C++
Name:		tclcl
Version:	1.0b13
Release:	1
License:	MIT
Group:		Development/Languages/Tcl
Source0:	http://www.isi.edu/nsnam/dist/%{name}-src-%{version}.tar.gz
# Source0-md5:	40af5da9720e029a0fc7afa13f17a74f
URL:		http://otcl-tclcl.sourceforge.net/otcl/
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-tcl-8.4.patch
BuildRequires:	autoconf
BuildRequires:	otcl-devel
BuildRequires:	tcl-devel = 8.4.4
BuildRequires:	tk-devel = 8.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TclCL (Tcl with classes) is a Tcl/C++ interface used by Mash, vic,
vat, rtp_play, ns, and nam. It provides a layer of C++ glue over OTcl.

%description -l pl
TclCL (Tcl z klasami) jest interfejsem Tcl/C++ u¿ywanym prezz Mash,
vic, vat, rtp_play, ns oraz nam. Zapewnia warstwê C++ nad OTcl.

%package devel
Summary:	TclCL header files
Summary(pl):	Pliki nag³ówkowe TclCL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
TclCL header files.

%description devel -l pl
Pliki nag³ówkowe TclCL.

%package static
Summary:	TclCL static library
Summary(pl):	Statyczna biblioteka TclCL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
TclCL static library.

%description static -l pl
Statyczna biblioteka TclCL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
./configure \
	--with-tcl-ver=8.4.4 \
	--with-tk-ver=8.4.4
%{__make} CCOPT="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

install tcl2c++ $RPM_BUILD_ROOT%{_bindir}
install *.h $RPM_BUILD_ROOT%{_includedir}
install libtclcl.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.html
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
