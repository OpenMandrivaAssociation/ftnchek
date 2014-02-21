Summary:	Fortran 77 program checker
Name:		ftnchek
Version:	3.3.1
Release:	7
License:	MIT
Group:		Development/Other
Url:		http://www.dsm.fordham.edu/~ftnchek
Source:		ftp://ftp.dsm.fordham.edu/pub/ftnchek/%{name}-%{version}.tar.bz2
Buildrequires:	groff
Buildrequires:	groff-for-man

%description
Ftnchek (short for Fortran checker) is designed to detect certain errors in a
Fortran program that a compiler usually does not.

Ftnchek is not primarily intended to detect syntax errors.
Its purpose is to assist the user in finding semantic errors.
Semantic errors are legal in the Fortran language but are wasteful or may
cause incorrect operation.

%files
%doc README PATCHES FAQ LICENSE dcl2inc.ps ftnchek.ps html
%attr (0755,root,root) %{_bindir}/*
%attr (0644,root,root) %{_mandir}/man1/*
%attr (0644,root,root) %{_datadir}/emacs/site-lisp/*
%{_libdir}/*.awk

#----------------------------------------------------------------------------

%prep
%setup -q
touch `find . -type f`

%build
%configure2_5x
%make "OPTIONS=%{optflags}"
cd test
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
%makeinstall STRIP=true

