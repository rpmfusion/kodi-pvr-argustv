%global kodi_addon pvr.argustv
%global kodi_version 18.0
%global kodi_codename Matrix

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        7.1.2
Release:        1%{?dist}
Summary:        ArgusTV PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  pkgconfig(jsoncpp)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
# https://gitlab.kitware.com/cmake/cmake/issues/17555#note_355574
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.1.2-1
- Update to 7.1.2

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.1.0-1
- Update to 7.1.0

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.0.0-1
- Update to 7.0.0

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Leigh Scott <leigh123linux@gmail.com> - 1:6.0.1-1
- Update to 6.0.1

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.4-1
- Update to 3.5.4

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.2-2
- Enable arm build

* Thu Aug 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.2-1
- Update to 3.5.2
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.1-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.5.9-1
- Update to 2.5.9

* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.5.6-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.15-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.11-1
- Initial RPM release
