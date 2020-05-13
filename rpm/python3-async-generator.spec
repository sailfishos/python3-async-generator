Name:       python3-async-generator
Summary:    Async generators for Python3
Version:    1.10
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/async_generator/
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/async_generator

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitearch}/async_generator
%{python3_sitearch}/async_generator-*.egg-info
