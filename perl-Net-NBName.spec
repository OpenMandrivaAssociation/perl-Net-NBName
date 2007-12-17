%define module	Net-NBName
%define name	perl-%{module}
%define version 0.26
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary:	NetBIOS Name Service Requests
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
Patch0:		Net-NBName-0.25-shellbang.diff
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
Net::NBName is a class that allows you to perform simple NetBIOS Name
Service Requests in your Perl code. It performs these NetBIOS operations over
TCP/IP using Perl's built-in socket support.

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's/\r\n$/\n/' bin/* README Changes
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/namequery.pl
%{_bindir}/nodescan.pl
%{_bindir}/nodestat.pl
%{perl_vendorlib}/Net
%{_mandir}/man3/*

