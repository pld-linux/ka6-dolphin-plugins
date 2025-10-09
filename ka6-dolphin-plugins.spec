#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		dolphin-plugins
Summary:	Dolphin plugins
Name:		ka6-%{kaname}
Version:	25.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cea6e7d5ff64dd73a482e5cc5daf7d22
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-dolphin-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-ktexteditor-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Dolphin.

%description -l pl.UTF-8
Wtyczki do Dolphina.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/plugins/dolphin/vcs
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphin/vcs/fileviewbazaarplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphin/vcs/fileviewdropboxplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphin/vcs/fileviewgitplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphin/vcs/fileviewhgplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphin/vcs/fileviewsvnplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/makefileactions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/mountisoaction.so
%{_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_datadir}/metainfo/org.kde.dolphin-plugins.metainfo.xml
%{_datadir}/qlogging-categories6/dolphingit.categories
