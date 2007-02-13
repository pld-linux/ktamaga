Summary:	Tamagotchi emulator
Summary(pl.UTF-8):	Emulator tamagotchi
Name:		ktamaga
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ktamaga/%{name}-%{version}.tar.gz
# Source0-md5:	84e02759e7ab549993f8b68a7509c8de
Patch0:		%{name}-desktop.patch
URL:		http://ktamaga.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.3.2
BuildRequires:	qt-devel >= 3.3.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTamaga is a FREE Tamagotchi emulator for X-Window systems with KDE.

%description -l pl.UTF-8
Ktamaga to emulator Tamagotchi dla KDE.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_datadir}/apps/ktamaga/Makefile*

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ktamaga
%{_desktopdir}/ktamaga.desktop
%{_iconsdir}/*/*/*/ktamaga*
