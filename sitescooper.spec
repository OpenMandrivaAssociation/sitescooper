%define version	3.1.2
%define release	%mkrel 10
%define name	sitescooper

Name:		%{name}
Summary:	Convert websites for reading on a Palm
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sitescooper.org/
Source:		%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	perl-DB_File

%define _requires_exceptions perl(in)\\|perl(to)\\|perl(Win32::Process)\\|perl(MacPerl)\\|perl(Win32::TieRegistry)
%define _provides_exceptions perl(Algorithm::Diff)

%description
Sitescooper automatically retrieves the stories from several news websites,
trims off extraneous HTML, and converts them into formats you can read on your
Palm computing device later, on-the-move.  Even if you don't have a Palm
handheld, it's still handy for simple website-to-text conversion. 


%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
%make PREFIX=$RPM_BUILD_ROOT/%{_prefix} RAW_PREFIX=%{_prefix} ETC=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} install || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/sitescooper
%{_datadir}/sitescooper/*
%config(noreplace) %{_sysconfdir}/sitescooper.cf
%doc	README.txt CHANGES.txt
%doc	doc/*

