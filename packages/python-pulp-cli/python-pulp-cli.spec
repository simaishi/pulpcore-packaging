%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.6
%global pypi_name pulp-cli

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.11.0
Release:        3%{?dist}
Summary:        Command line interface to talk to pulpcore's REST API

License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML < 6.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click < 9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click >= 7.1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click-shell < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click-shell >= 2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygments
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.24
Requires:       %{?scl_prefix}python%{python3_pkgversion}-schema = 0.7.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-toml = 0.10.2
%if 0%{?!scl:1}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp
%{python3_sitelib}/pulp_cli
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pytest_pulp_cli
%{python3_sitelib}/pulp_cli-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Sep 29 2021 Evgeni Golov - 0.11.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 13 2021 Evgeni Golov - 0.11.0-2
- Build against Python 3.8

* Wed Aug 11 2021 Evgeni Golov - 0.11.0-1
- Release python-pulp-cli 0.11.0

* Wed Jun 30 2021 Evgeni Golov - 0.10.1-1
- Initial package.

