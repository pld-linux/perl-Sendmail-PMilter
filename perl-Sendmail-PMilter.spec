#
%bcond_without	tests		# do not perform "make test"

%define	pdir	Sendmail
%define	pnam	PMilter
Summary:	Sendmail::PMilter - Perl binding of Sendmail Milter protocol
Summary(pl):	Sendmail::PMilter - moduł Perla do obsługi protokołu Milter
Name:		perl-Sendmail-PMilter
Version:	1.28
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/G/GW/GWHAYWOOD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1e1cf850935beba24462802450c466b
URL:		http://search.cpan.org/dist/Sendmail-PMilter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sendmail::PMilter is a mail filtering API implementing the Sendmail
milter protocol in pure Perl. This allows Sendmail servers (and
perhaps other MTAs implementing milter) to filter and modify mail in
transit during the SMTP connection, all in Perl.

It should be noted that PMilter 0.90 and later is NOT compatible with
scripts written for PMilter 0.5 and earlier. The API has been reworked
significantly, and the enhanced APIs and rule logic provided by
PMilter 0.5 and earlier has been factored out for inclusion in a
separate package to be called Mail::Milter.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
PERL_MM_USE_DEFAULT=1 %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ABOUT ACKNOWLEDGEMENTS CONTRIBUTING README README.1.28 TODO
%{perl_vendorlib}/Sendmail/*.pm
%{perl_vendorlib}/Sendmail/PMilter
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
