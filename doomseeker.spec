%global debug_package %{nil}

Name:		doomseeker
Version:	1.3
Release:	1%{?dist}

Group:		Amusements/Games
Summary:	Cross-platform server browser for Doom.
License:	GPLv2+
URL:		https://doomseeker.drdteam.org

Source0:	https://doomseeker.drdteam.org/files/doomseeker-%{version}.tar.xz
BuildRequires: gcc-c++ cmake bzip2-devel
BuildRequires:	qt5-devel

%description
Doomseeker is a cross-platform server browser for Doom.
The goal of Doomseeker is to provide a smooth, consistant
experience for Doom players regardless of port or platform.
Doomseeker provides support for Chocolate Doom, Odamex,
Sonic Robo Blast 2, Turok 2 Remaster, and Zandronum. With
its plugin system support for even more can be added.

Using the Qt Toolkit, Doomseeker can run on wide variety
of platforms including Linux, Mac OS X, and Windows. In
addition the browser is open source and licensed under the
GNU Public License v2.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr
make

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/doomseeker
%{_datadir}/icons/doomseeker.png
%{_datadir}/doomseeker/translations/*.qm
%{_datadir}/doomseeker/translations/translations.def
%{_datadir}/applications/org.drdteam.Doomseeker.desktop
%{_datadir}/doc/doomseeker/LICENSE.json
%{_libdir}/doomseeker/engines/*.so
%{_libdir}/libwadseeker.so*
%{_docdir}/wadseeker/LICENSE.json
%{_includedir}/wadseeker/*.h
%{_includedir}/wadseeker/entities/*.h
%{_includedir}/wadseeker/protocols/networkreplytimeouter.h
%{_includedir}/wadseeker/zip/unarchive.h

%changelog
* Sun Sep 08 2019 vain <nibbler at vain.cz> - 1.2-1
- Doomseeker 1.3 release

* Thu Jan 10 2019 vain <nibbler at vain.cz> - 1.2-1
- Initial release
