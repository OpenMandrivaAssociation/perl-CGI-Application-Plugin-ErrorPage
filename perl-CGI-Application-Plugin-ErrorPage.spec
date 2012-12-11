%define upstream_name    CGI-Application-Plugin-ErrorPage
%define upstream_version 1.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A simple error page plugin for CGI::Application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin provides a shortcut for the common need of returning a simple
error message to the user. 

You are encouraged to provide a template file so that the error messages
can be presented with a design consistent with the rest of your
application. 

A simple design is provided below to get to you started. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/CGI


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.210.0-2mdv2011.0
+ Revision: 680680
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 405774
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2010.0
+ Revision: 390324
- update to new version 1.21

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 307089
- import perl-CGI-Application-Plugin-ErrorPage


* Wed Nov 26 2008 cpan2dist 1.20-1mdv
- initial mdv release, generated with cpan2dist

