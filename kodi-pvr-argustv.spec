%global commit 9040b1447bd622bcbae3f8944e7b84d933037644
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170324

%global kodi_addon pvr.argustv
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.5.6
Release:        1%{?dist}
Summary:        Kodi's ARGUS TV client addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Fix jsoncpp library detection
Patch1:         %{name}-2.5.6-jsoncpp.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Kodi frontend for the ARGUS TV PVR (http://www.argus-tv.com/). Supports
streaming of live TV & recordings, listening to radio channels, EPG and
schedules.


%prep
%autosetup -n %{kodi_addon}-%{commit}

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.5.6-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.15-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.11-1
- Initial RPM release
