Summary:	Tamagotchi emulator
Summary(pl):	Emulator tamagotchi
Name:		ktamaga
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		Games
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	84e02759e7ab549993f8b68a7509c8de
URL:		http://ktamaga.sourceforge.net/		
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTamaga is a FREE Tamagotchi emulator for X-Window systems with KDE.

%description -l pl
Ktamaga to emulator Tamagotchi dla KDE.

%prep
%setup -q

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ktamaga
#%{_desktopdir}/ktamaga.desktop
/usr/share/applnk/Games/ktamaga.desktop
%{_iconsdir}/*/*/*/ktamaga*
