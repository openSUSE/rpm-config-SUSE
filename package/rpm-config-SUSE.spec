#
# spec file for package rpm-config-SUSE
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/openSUSE/rpm-config-SUSE/
#


Name:           rpm-config-SUSE
Version:        0
Release:        0
Summary:        SUSE specific RPM configuration files
License:        GPL-2.0+
Group:          System/Packages
URL:            https://github.com/openSUSE/rpm-config-SUSE
Source:         %{name}-%{version}.tar.gz

# Generic Provides for distribution RPM configuration
Provides:       distribution-rpm-config = %{version}-%{release}
Provides:       system-rpm-config = %{version}-%{release}

%if 0%{?is_opensuse}
# This is the vendor configuration for the openSUSE Linux distribution
Provides:       rpm-config-openSUSE = %{version}-%{release}
%endif

# This is only for SUSE-based distributions
Requires:       suse-release

# RPM owns the directories we need
Requires:       rpm

BuildArch:      noarch

%description
This package contains the RPM configuration data for the SUSE Linux
distribution family.

%prep
%setup -q

%build
# Set up the SUSE Linux version macros
sed -e 's/@suse_version@/%{?suse_version}%{!?suse_version:0}/' \
    -e 's/@sles_version@/%{?sles_version}%{!?sles_version:0}/' \
    -e 's/@ul_version@/%{?ul_version}%{!?ul_version:0}/' \
    -e '/@is_opensuse@%{?is_opensuse:nomatch}/d' \
    -e 's/@is_opensuse@/%{?is_opensuse}%{!?is_opensuse:0}/' \
    -e '/@leap_version@%{?leap_version:nomatch}/d' \
    -e 's/@leap_version@/%{?leap_version}%{!?leap_version:0}/' \
%if 0%{?is_opensuse}
    -e '/@sle_version@%{?sle_version:nomatch}/d' \
    -e 's/@sle_version@/%{?sle_version}%{!?sle_version:0}/' \
%else
    -e '/@sle_version@/d' \
%endif
  < macros.d/suse_dist_macros.in > macros.d/macros.dist


%install
# Install SUSE vendor macros and rpmrc
mkdir -p %{buildroot}%{_rpmconfigdir}
cp -a suse %{buildroot}%{_rpmconfigdir}

# Install vendor dependency generators
cp -a fileattrs %{buildroot}%{_rpmconfigdir}
cp -a scripts/* %{buildroot}%{_rpmconfigdir}

# Install extra macros (omitting the templated macro file)
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp -a macros.d/macros.* %{buildroot}%{_rpmconfigdir}/macros.d


%files
%license COPYING
%doc README.md
%{_rpmconfigdir}/suse/
%{_rpmconfigdir}/macros.d/macros.*
%{_rpmconfigdir}/fileattrs/*
%{_rpmconfigdir}/brp-suse
%{_rpmconfigdir}/find-supplements
%{_rpmconfigdir}/firmware.prov
%{_rpmconfigdir}/sysvinitdeps.sh
# kmod deps
%{_rpmconfigdir}/find-provides.ksyms
%{_rpmconfigdir}/find-requires.ksyms
%{_rpmconfigdir}/find-supplements.ksyms

%changelog

