
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Random
Summary:	Crypt::Random - cryptographically secure, true random number generator
Summary(pl):	Crypt::Random - bezpieczny kryptograficznie, prawdziwy generator liczb losowych
Name:		perl-Crypt-Random
Version:	1.13
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e01bb787041c52557698a03fd801098
%if %{with tests}
BuildRequires:	perl-Class-Loader >= 2.00
BuildRequires:	perl-Math-Pari >= 2.001804
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Random is an interface module to the /dev/random device found
on most modern Unix systems. The /dev/random driver gathers
environmental noise from various non-deterministic sources including
inter-keyboard timings and inter-interrupt timings that occur within
the operating system environment.

%description -l pl
Modu³ Perla Crypt::Random stanowi interfejs do urz±dzenia /dev/random
znajduj±cego siê w wiêkszo¶ci wspó³czesnych systemów uniksowych.
Sterownik /dev/random gromadzi szum pochodz±cy z ró¿nych
niedeterministycznych ¼róde³, w³±czaj±c w to: przebiegi czasowe
klawiatury i przerwañ wystêpuj±ce w systemie operacyjnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Crypt/Random.pm
%{perl_vendorlib}/Crypt/Random
#%%{perl_vendorlib}/Crypt/Random/Generator.pm
%{_mandir}/man3/*
