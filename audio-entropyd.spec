Summary:	Audio-entropyd - generating entropy-data for the /dev/random device
Summary(pl):	Audio-entropyd - generowanie danych entropii dla urz±dzenia /dev/random
Name:		audio-entropyd
Version:	0.0.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.vanheusden.com/aed/%{name}-%{version}.tgz
# Source0-md5:	ef014b233c08a0f6eb12d2a75c3041b9
Patch0:		%{name}-ncurses.patch
URL:		http://www.vanheusden.com/aed/
#BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small program to reseed the Linux kernel random number
generator with data from soundcard.

**** This is an alpha release intended for peer review.
**** DO NOT use this on a production server.

%description -l pl
Jest to ma³y program karmi±cy generator liczb losowych w j±drze
Linuksa danymi z karty d¼wiêkowej.

UWAGA: jest to wersja alpha, nie nale¿y u¿ywaæ jej na produkcyjnym
serwerze.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags} -DVERSION=\"\$(VERSION)\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install audio-entropyd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* TODO
%attr(755,root,root) %{_sbindir}/*
