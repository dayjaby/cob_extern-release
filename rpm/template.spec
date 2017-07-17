Name:           ros-kinetic-libconcorde-tsp-solver
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS libconcorde_tsp_solver package

Group:          Development/Libraries
License:        free for academic research, for further licensing contact Wiliam Cook
URL:            http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-libqsopt
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-libqsopt

%description
Wrapper for the concorde traveling salesman problem solver. The code was
obtained from http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm
all rights of it go to the corresponding authors David Applegate, Robert Bixby,
Vasek Chvatal and William Cook. The library doesn't give a specific license, but
is provided free for academic research use, for further licensing options
contact William Cook.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 17 2017 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.11-0
- Autogenerated by Bloom

