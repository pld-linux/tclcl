Summary:	Tcl/C++ interface
Summary(pl.UTF-8):	Interfejs Tcl/C++
Name:		tclcl
Version:	1.17
Release:	1
License:	MIT
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/otcl-tclcl/%{name}-%{version}.tar.gz
# Source0-md5:	39574568176c138f5d2f7fe8fba85a9c
URL:		http://otcl-tclcl.sourceforge.net/tclcl/
Patch0:		tcl-lib.patch
Patch1:		%{name}-tcl-8.4.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	otcl-devel
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TclCL (Tcl with classes) is a Tcl/C++ interface used by Mash, vic,
vat, rtp_play, ns, and nam. It provides a layer of C++ glue over OTcl.

%description -l pl.UTF-8
TclCL (Tcl z klasami) jest interfejsem Tcl/C++ używanym prez Mash,
vic, vat, rtp_play, ns oraz nam. Zapewnia warstwę C++ nad OTcl.

%package devel
Summary:	TclCL header files
Summary(pl.UTF-8):	Pliki nagłówkowe TclCL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tclcl-static

%description devel
TclCL header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe TclCL.

%package static
Summary:	TclCL static library
Summary(pl.UTF-8):	Statyczna biblioteka TclCL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
TclCL static library.

%description static -l pl.UTF-8
Statyczna biblioteka TclCL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
./configure \
	--with-tcl-ver=8.4 \
	--with-tk-ver=8.4
%{__make} \
	CCOPT="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

install tcl2c++ $RPM_BUILD_ROOT%{_bindir}
install *.h $RPM_BUILD_ROOT%{_includedir}
install libtclcl.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.html
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a

#%files static
#%defattr(644,root,root,755)
