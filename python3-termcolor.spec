Summary:	ANSI Color formatting for output in terminal
Summary(pl.UTF-8):	Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI
Name:		python3-termcolor
Version:	3.1.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
# Source0-md5:	877fe6650412d9cea0384600870f0161
URL:		https://pypi.org/project/termcolor/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling >= 1.27
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSI Color formatting for output in terminal.

%description -l pl.UTF-8
Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI.

%prep
%setup -q -n termcolor-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYING.txt README.md
%{py3_sitescriptdir}/termcolor
%{py3_sitescriptdir}/termcolor-%{version}.dist-info
