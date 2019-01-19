Name:           myscript
Version:        1.0
Release:        1
Summary:        Simple shell script 

Group:          Utilities
License:        GPL
URL:            http://www.sadashivhb.com
Source0:        myscript-%{version}.tar.gz

BuildRequires: bash  
Requires:       bash

%description
This is my First rpm package 
To test simple shell script


%prep
%setup -n myscript-1.0 


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/myscript
install myscript.sh $RPM_BUILD_ROOT/opt/myscript/myscript.sh


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/myscript/myscript.sh
%doc



%changelog
