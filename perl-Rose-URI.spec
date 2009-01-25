%define module	Rose-URI
%define	modprefix Rose

%define version	0.50

%define	rel	1
%define release	%mkrel %{rel}

Summary:	An alternative to URI
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}

