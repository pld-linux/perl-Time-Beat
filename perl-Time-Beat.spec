%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Beat
Summary:	Time::Beat perl module
Summary(pl):	Modu³ perla Time::Beat
Name:		perl-Time-Beat
Version:	1.21
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	effbcb318952fe3ed876200ec22626d6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::Beat allows to convert from standard time to swatch 'beat' time.

%description -l pl
Time::Beat pozwala na konwersjê czasu w sandardowym formacie na format
'swatcha'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Time/Beat.pm
%{_mandir}/man3/*
