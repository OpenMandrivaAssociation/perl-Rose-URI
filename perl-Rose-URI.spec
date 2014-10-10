%define upstream_name	 Rose-URI
%define upstream_version 1.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An alternative to URI
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Rose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(overload)
BuildRequires:	perl(Rose::Object) >= 0.015
BuildRequires:	perl(URI)
## scottk ##
## perl(URI::Escape) is provided by perl-URI, which requirement is
## satisfied when the perl(URI) requirement is satisfied
##BuildRequires:	perl(URI::Escape)
BuildArch:	noarch

%description
Rose::URI is a standalone URI class allowing easy and efficient
manipulation of query parameters and other URI components.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/Rose


%changelog
* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 523960
- update to 1.00

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 406381
- rebuild using %%perl_convert_version

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdv2009.1
+ Revision: 333412
- update to new version 0.50

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 0.022-1mdv2008.1
+ Revision: 163390
- update to new version 0.022

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.021-3mdv2008.0
+ Revision: 86826
- rebuild


* Fri Jun 16 2006 Scott Karns <scottk@mandriva.org> 0.021-2mdv2007.0
- Fixed "redundant" BuildRequires perl(URI::Escape) for automated builds

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 0.021-1mdk
- Initial MDV package

