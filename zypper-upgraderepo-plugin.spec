#
# spec file for package rubygem-zypper-upgraderepo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-upgraderepo-plugin
Version:        1.6.0
Release:        0
%define mod_name zypper-upgraderepo
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       rubygem(zypper-upgraderepo)
Requires:       zypper >= 1.13.10
Url:            https://github.com/fabiomux/zypper-upgraderepo-plugin
Source:         zypper-upgraderepo.tgz
Summary:        Zypper addon to check and upgrade repositories
License:        GPL-3.0
Group:          System/Packages

%description
This is just a complement to zypper command which helps to upgrading the
repositories before launching zypper dup.

%prep
%setup -q -n %{mod_name}

%build

%install
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 755 zypper-upgraderepo %{buildroot}/usr/lib/zypper/commands/
install -m 644 zypper-upgraderepo.8 %{buildroot}/%{_mandir}/man8/

%files
%defattr(-,root,root,-)
/usr/lib/zypper
/usr/lib/zypper/commands
%{_mandir}/man8/*


%changelog
