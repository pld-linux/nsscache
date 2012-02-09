Summary:	Asynchronously synchronise local NSS databases with remote directory services
Name:		nsscache
Version:	0.21.14
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	https://nsscache.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8f6c77599425e0f4dc1029f9185416e1
URL:		https://code.google.com/p/nsscache/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nsscache is a Python library and a commandline frontend to that
library that synchronises a local NSS cache against a remote directory
service, such as LDAP.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc THANKS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nsscache.conf
%attr(755,root,root) %{_bindir}/nsscache
%{py_sitescriptdir}/nss_cache
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info
%endif
