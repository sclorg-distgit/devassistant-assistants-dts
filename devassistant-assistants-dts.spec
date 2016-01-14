%{?scl:%scl_package devassistant-assistants-dts}
%{!?scl:%global pkg_name %{name}}

%global release 4
%global prerel ad45baa
%global instdir %{_datadir}/devassistant

Name:           %{?scl_prefix}devassistant-assistants-dts
Version:        3.0.0
Release:        %{?prerel:0.}%{release}%{?prerel:.%{prerel}}%{?dist}
Summary:        Collection of assistants that work with DTS 3 packages

License:        GPLv2+
Source0:        %{pkg_name}-%{version}%{?prerel:.%{prerel}}.tar.gz

Requires:       %{?scl_prefix}devassistant

BuildArch:      noarch

%description
Collection of assistants that set up projects based on packages
shipped by DTS 3 and also base RHEL.

%prep
%setup -q -n %{pkg_name}-%{version}%{?prerel:.%{prerel}}

%build

%install
mkdir -p %{buildroot}%{instdir}
cp -pR assistants files icons snippets %{buildroot}%{instdir}

%files
%doc LICENSE NOTICE
%{instdir}/assistants/crt/*
%{instdir}/files/crt/*
%{instdir}/files/snippets/*
%{instdir}/icons/crt/*
%{instdir}/snippets/*

%changelog
* Tue Jun 03 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.0-0.4.ad45baa
- Fix release number.

* Tue Jun 03 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.0-0.3.ad45baa
- Use new source that properly includes all .gitignore files.

* Mon Jun 02 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.0-0.2.3f02f80
- Add .classpath file for maven eclipse projects.

* Thu May 29 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.0-0.1.c3a8f76
- Initial package.
