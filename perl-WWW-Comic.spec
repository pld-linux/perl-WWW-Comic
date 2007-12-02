#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test" (uses network)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Comic
Summary:	WWW::Comic - Retrieve comic strip images
#Summary(pl.UTF-8):	
Name:		perl-WWW-Comic
Version:	1.06
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	211826fbbdf07e8448145c6a7a33f621
URL:		http://search.cpan.org/dist/WWW-Comic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(WWW::Dilbert) >= 1.18
BuildRequires:	perl(WWW::VenusEnvy) >= 1.06
BuildRequires:	perl-libwww
BuildRequires:	perl-Module-Pluggable >= 2.96
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will download cartoon comic strip images from various
websites and return a binary blob of the image, or write it to
disk. Multiple comic strips can be supported through subclassed
plugin modules.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
AUTOMATED_TESTING=1
export AUTOMATED_TESTING
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL TODO
%{perl_vendorlib}/WWW/*.pm
%{perl_vendorlib}/WWW/Comic
%{_mandir}/man3/*
