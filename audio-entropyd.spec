# TODO: init script
Summary:	Audio-entropyd - generating entropy-data for the /dev/random device
Summary(pl.UTF-8):	Audio-entropyd - generowanie danych entropii dla urządzenia /dev/random
Name:		audio-entropyd
Version:	2.0.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.vanheusden.com/aed/%{name}-%{version}.tgz
# Source0-md5:	44d355a0e61b6f291922fe99462d47e8
URL:		http://www.vanheusden.com/aed/
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small program to reseed the Linux kernel random number
generator with data from soundcard.

**** This is an alpha release intended for peer review.
**** DO NOT use this on a production server.

%description -l pl.UTF-8
Jest to mały program karmiący generator liczb losowych w jądrze
Linuksa danymi z karty dźwiękowej.

UWAGA: jest to wersja alpha, nie należy używać jej na produkcyjnym
serwerze.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags} -ffast-math" \
	LFLAGS="%{rpmldflags} -lm -lasound"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install audio-entropyd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_sbindir}/audio-entropyd
