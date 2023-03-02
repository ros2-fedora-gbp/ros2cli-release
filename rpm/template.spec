%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2topic
Version:        0.23.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2topic package

License:        Apache License 2.0 and BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-yaml
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-ros2cli
Requires:       ros-rolling-rosidl-runtime-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ros2cli
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ament-xmllint
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-launch-testing
BuildRequires:  ros-rolling-launch-testing-ros
BuildRequires:  ros-rolling-rosgraph-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-test-msgs
%endif

%description
The topic command for ROS 2 command line tools.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Mar 02 2023 Audrow Nash <audrow@openrobotics.org> - 0.23.0-1
- Autogenerated by Bloom

* Tue Feb 14 2023 Audrow Nash <audrow@openrobotics.org> - 0.22.0-1
- Autogenerated by Bloom

* Wed Nov 02 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.21.0-1
- Autogenerated by Bloom

* Tue Sep 13 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.20.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.19.0-1
- Autogenerated by Bloom

* Fri Apr 08 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.3-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.2-1
- Autogenerated by Bloom

* Mon Mar 28 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.1-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.18.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.17.1-2
- Autogenerated by Bloom

