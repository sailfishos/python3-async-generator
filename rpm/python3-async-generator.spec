# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-async-generator
Summary:    Async generators for Python3
Version:    1.10
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/async_generator/
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-setuptools

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/async_generator

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/async_generator
%{python3_sitearch}/async_generator-*.egg-info
