%define upstream_name	 Net-NBName
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	NetBIOS Name Service Requests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Net-NBName-0.25-shellbang.diff

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::NBName is a class that allows you to perform simple NetBIOS Name
Service Requests in your Perl code. It performs these NetBIOS operations over
TCP/IP using Perl's built-in socket support.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's/\r\n$/\n/' bin/* README Changes
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/namequery.pl
%{_bindir}/nodescan.pl
%{_bindir}/nodestat.pl
%{perl_vendorlib}/Net
%{_mandir}/man3/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 404099
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.26-3mdv2009.0
+ Revision: 241786
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Jun 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2007.0
- New version 0.26
- spec cleanup
- fix directory ownership
- use perl instead of dos2unix to fix EOLs

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.25-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL

* Mon Jan 30 2006 Oden Eriksson <oeriksson@mandriva.com> 0.25-1mdk
- initial Mandriva package

