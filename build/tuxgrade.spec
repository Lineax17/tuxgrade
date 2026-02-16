Name:           tuxgrade
Version:        3.0.1
Release:        1%{?dist}
Summary:        Automated system upgrade script for several Linux distributions

License:        MIT
URL:            https://github.com/Lineax17/tuxgrade
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3 >= 3.10
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Automated system upgrade script for several Linux distributions with support 
for APT, DNF, Flatpak, Snap, Homebrew and NVIDIA akmods. Provides both silent mode
(default with ASCII animation) and verbose mode (--verbose flag) for
detailed output.

Alternative commands: fedora-update, fedora-upgrade, fuck

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/tuxgrade
%{_bindir}/fedora-update
%{_bindir}/fedora-upgrade
%{_bindir}/fuck