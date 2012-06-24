%include	/usr/lib/rpm/macros.perl
Summary:	Time-Beat perl module
Summary(pl):	Modu� perla Time-Beat
Name:		perl-Time-Beat
Version:	1.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/Time-Beat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Time/Beat
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Time/Beat.pm
%{perl_sitearch}/auto/Time/Beat

%{_mandir}/man3/*
