#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Beat
Summary:	Time::Beat perl module
Summary(pl.UTF-8):	Moduł perla Time::Beat
Name:		perl-Time-Beat
Version:	1.21
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	effbcb318952fe3ed876200ec22626d6
Source1:	cc-license.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::Beat allows to convert from standard time to swatch 'beat' time.

%description -l pl.UTF-8
Time::Beat pozwala na konwersję czasu w standardowym formacie na format
'swatcha'.

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
install %{SOURCE1} LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{perl_vendorlib}/Time/Beat.pm
%{_mandir}/man3/*
