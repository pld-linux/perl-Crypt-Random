%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Random
Summary:	Crypt::Random perl module
Summary(pl):	Modu³ perla Crypt::Random
Name:		perl-Crypt-Random
Version:	1.11
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Random perl module.

%description -l pl
Modu³ perla Crypt::Random.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Crypt/Random.pm
%{perl_sitelib}/Crypt/Random/Generator.pm
%{_mandir}/man3/*
