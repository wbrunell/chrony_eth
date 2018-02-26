Name:           {{ stream_feed }}
Version:        {{ latest_tag.stdout[1:] }}
Release:        0
Summary:        Pseudo Stream/Feed for testing RPM build

Group:          DSF Feeds and Streams
License:        GPL
URL:            http://www.github.com
Source0:        %{name}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-buildroot
#Requires:

%description
Pseudo Stream/Feed for testing RPM build. Required for Feed and Stream Deployment.

%prep
#%setup -q
%setup -n %{name}               # This needs to be set to the main DIR of the tar.gz File. %{name}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/dwp_root/      # Either the tar.gz has the structure or you do it here
cp -R * ${RPM_BUILD_ROOT}/dwp_root/       # Either the tar.gz has the structure or you do it here

%files
/dwp_root/
%defattr(-,root,root,-)

%clean
rm -rf ${RPM_BUILD_ROOT}

%changelog
* Sun Jan 14 2018       Walter Brunelli <walter.brunelli@ubs.com> - 1.0.0
- First version
