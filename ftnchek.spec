%define name ftnchek
%define	version 3.3.1
%define release	%mkrel 6

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-6mdv2011.0
+ Revision: 618365
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.3.1-5mdv2010.0
+ Revision: 428961
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.3.1-4mdv2009.0
+ Revision: 245444
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3.1-2mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ftnchek


* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 3.3.1-2mdv2007.0
- rebuild

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 3.3.1-1mdk
- 3.3.1

* Tue May 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-2mdk
- buildrequires

* Fri Jan 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Thu Feb 07 2002 Giuseppe Ghibò <ghibo@mandrakesoft.com> 3.1.2-2mdk
- added URL.

* Thu Feb 07 2002 Giuseppe Ghibò <ghibo@mandrakesoft.com> 3.1.2-1mdk
- updated to 3.1.2.
- added test.
- added dcl2inc.awk.
- fixed license (MIT).

* Thu Jul 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.1.1-1mdk
- added by Pierre-Michel Theveny <pmt@mnhn.fr> :
	- Update version to 3.1.1
	- Port to Mandrake 8.0

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Fri Nov 10 2000 Than Ngo <than@redhat.com>
- update to 3.0.0
- use %%configure and %%makeinstall
- update ftp site

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- use RPMS macros

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun May 21 2000 Ngo Than <than@redhat.de>
- update to 2.12.0
- put man pages in /usr/share/man/*

* Thu Nov 18 1999 Ngo Than <than@redhat.de>
- initial RPM
