%define name ftnchek
%define	version 3.3.1
%define release	%mkrel 2

Summary: Fortran 77 program checker
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group:		Development/Other
License: 	MIT
Url:		http://www.dsm.fordham.edu/~ftnchek
Source: 	ftp://ftp.dsm.fordham.edu/pub/ftnchek/%{name}-%{version}.tar.bz2
Buildrequires:	groff groff-for-man 
BuildRoot:	%{_tmppath}/%name-%version-root

%description
Ftnchek (short for Fortran checker) is designed to detect certain errors in a
Fortran program that a compiler usually does not.

Ftnchek is not primarily intended to detect syntax errors.
Its purpose is to assist the user in finding semantic errors.
Semantic errors are legal in the Fortran language but are wasteful or may
cause incorrect operation.

%prep

%setup -q
touch `find . -type f`

%build
%configure
%make "OPTIONS=$RPM_OPT_FLAGS"
(cd test; make)

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__mkdir_p $RPM_BUILD_ROOT%_mandir/man1
%__mkdir_p $RPM_BUILD_ROOT%_datadir/emacs/site-lisp
%makeinstall

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README PATCHES INSTALL FAQ LICENSE dcl2inc.ps ftnchek.ps html
%attr (0755,root,root) %_bindir/*
%attr (0644,root,root) %_mandir/man1/*
%attr (0644,root,root) %_datadir/emacs/site-lisp/*
%_libdir/*.awk

