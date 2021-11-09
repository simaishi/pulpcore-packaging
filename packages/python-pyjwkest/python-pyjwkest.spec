%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pyjwkest

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.4.2
Release:        5%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK

License:        Apache 2.0
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-future
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pycryptodomex
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six


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
%doc README.rst
%exclude %{_bindir}/gen_symkey.py
%exclude %{_bindir}/jwdecrypt.py
%exclude %{_bindir}/jwenc.py
%exclude %{_bindir}/jwk_create.py
%exclude %{_bindir}/jwk_export.py
%exclude %{_bindir}/jwkutil.py
%exclude %{_bindir}/peek.py
%{python3_sitelib}/jwkest
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Nov 05 2021 Satoe Imaishi - 1.4.2-5
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 1.4.2-4
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 1.4.2-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.4.2-1
- Initial package.
