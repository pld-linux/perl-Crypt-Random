%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Random
Summary:	Crypt::Random perl module
Summary(pl):	Modu³ perla Crypt::Random
Name:		perl-Crypt-Random
Version:	1.12
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Class-Loader >= 2.00
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Random Perl module - Cryptographically Secure, True Random
Number Generator.

%description -l pl
Modu³ Perla Crypt::Random - Bezpieczny Kryptograficznie, Prawdziwy
Generator Liczb Losowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Crypt/Random.pm
%{perl_sitelib}/Crypt/Random
#%%{perl_sitelib}/Crypt/Random/Generator.pm
%{_mandir}/man3/*
