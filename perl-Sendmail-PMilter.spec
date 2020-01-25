#
%bcond_without	tests		# do not perform "make test"

%define	pdir	Sendmail
%define	pnam	PMilter
Summary:	Sendmail::PMilter - Perl binding of Sendmail Milter protocol
Summary(pl):	Sendmail::PMilter - moduł Perla do obsługi protokołu Milter
Name:		perl-Sendmail-PMilter
Version:	1.00
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AV/AVAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	18f8fd3b69ef98014a1a5d55fbefd3d9
URL:		http://search.cpan.org/dist/Sendmail-PMilter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sendmail-devel >= 8.13.6-3.1
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
%doc Changes doc README
%{perl_vendorlib}/Sendmail/*.pm
%{perl_vendorlib}/Sendmail/PMilter
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
