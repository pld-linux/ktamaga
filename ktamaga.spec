Summary:	Tamagotchi emulator
Summary(pl):	Emulator tamagotchi
Name:		ktamaga
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ktamaga/%{name}-%{version}.tar.gz
# Source0-md5:	84e02759e7ab549993f8b68a7509c8de
Patch0:		%{name}-desktop.patch
URL:		http://ktamaga.sourceforge.net/
BuildRequires:	kdebase-devel >= 3.3.2
BuildRequires:	qt-devel  >= 3.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTamaga is a FREE Tamagotchi emulator for X-Window systems with KDE.

%description -l pl
Ktamaga to emulator Tamagotchi dla KDE.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_kdedocdir}
mv -f $RPM_BUILD_ROOT{%{_docdir}/HTML/*,%{_kdedocdir}}
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Games,%{_desktopdir}}/ktamaga.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ktamaga
%{_desktopdir}/ktamaga.desktop
%{_iconsdir}/*/*/*/ktamaga*
%{_kdedocdir}
