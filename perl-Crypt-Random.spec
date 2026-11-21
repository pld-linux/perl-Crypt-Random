#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Crypt
%define		pnam	Random
Summary:	Crypt::Random - cryptographically secure, true random number generator
Summary(pl.UTF-8):	Crypt::Random - bezpieczny kryptograficznie, prawdziwy generator liczb losowych
Name:		perl-Crypt-Random
Version:	1.57
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/T/TI/TIMLEGGE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7e704688eb08211de0e6885617e8982
Patch0:		%{name}-itv-real.patch
URL:		https://metacpan.org/dist/Crypt-Random
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Loader >= 2.00
BuildRequires:	perl-Crypt-URandom
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-Statistics-ChiSquare >= 1.0000
%endif
Requires:	perl-Class-Loader >= 2.00
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Random is an interface module to the /dev/random device found
on most modern Unix systems. The /dev/random driver gathers
environmental noise from various non-deterministic sources including
inter-keyboard timings and inter-interrupt timings that occur within
the operating system environment.

%description -l pl.UTF-8
Moduł Perla Crypt::Random stanowi interfejs do urządzenia /dev/random
znajdującego się w większości współczesnych systemów uniksowych.
Sterownik /dev/random gromadzi szum pochodzący z różnych
niedeterministycznych źródeł, włączając w to: przebiegi czasowe
klawiatury i przerwań występujące w systemie operacyjnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README SECURITY.md
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Crypt/Random.pm
%{perl_vendorlib}/Crypt/Random
%{_mandir}/man3/*
