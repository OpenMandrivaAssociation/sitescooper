%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32::(.*)\\)'
%define __noautoprov 'perl\\(Algorithm::Diff\\)'
%else
%define _requires_exceptions perl(in)\\|perl(to)\\|perl(Win32::Process)\\|perl(MacPerl)\\|perl(Win32::TieRegistry)
%define _provides_exceptions perl(Algorithm::Diff)
%endif

Name:		sitescooper
Summary:	Convert websites for reading on a Palm
Version:	3.1.2
Release:	12
License:	GPL
Group:		Networking/WWW
URL:		http://sitescooper.org/
Source:		%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	perl-DB_File

%description
Sitescooper automatically retrieves the stories from several news websites,
trims off extraneous HTML, and converts them into formats you can read on your
Palm computing device later, on-the-move.  Even if you don't have a Palm
handheld, it's still handy for simple website-to-text conversion. 


%prep
%setup -q

%build

%install
%make PREFIX=%{buildroot}%{_prefix} RAW_PREFIX=%{_prefix} ETC=%{buildroot}%{_sysconfdir} \
	MANDIR=%{buildroot}%{_mandir} install || :

%files
%doc README.txt CHANGES.txt
%doc doc/*
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/sitescooper
%{_datadir}/sitescooper/*
%config(noreplace) %{_sysconfdir}/sitescooper.cf

