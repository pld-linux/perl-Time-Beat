%define	pdir	Time
%define	pnam	Beat
%include	/usr/lib/rpm/macros.perl
Summary:	Time-Beat perl module
Summary(pl):	Modu� perla Time-Beat
Name:		perl-Time-Beat
Version:	1.02
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-Beat allows to convert from standard time to swatch 'beat' time.

%description -l pl
Time-Beat pozwala na konwersj� czasu w sandardowym formacie na format
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
