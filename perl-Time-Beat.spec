%include	/usr/lib/rpm/macros.perl
Summary:	Time-Beat perl module
Summary(pl):	Modu³ perla Time-Beat
Name:		perl-Time-Beat
Version:	1.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/Time-Beat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-Beat allows to convert from standard time to swatch 'beat' time.

%description -l pl
Time-Beat pozwala na konwersjê czasu w sandardowym formacie na format
'swatcha'.

%prep
%setup -q -n Time-Beat-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Time/Beat.pm
%{_mandir}/man3/*
