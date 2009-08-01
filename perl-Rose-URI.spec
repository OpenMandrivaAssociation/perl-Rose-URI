%define upstream_name	Rose-URI
%define upstream_version	0.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	An alternative to URI
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Rose/%{upstream_name}-%{upstream_version}.tar.bz2

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Rose::URI is a standalone URI class allowing easy and efficient
manipulation of query parameters and other URI components.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Rose
