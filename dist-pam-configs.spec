Name     : dist-pam-configs
Version  : 1
Release  : 7
Source0  : pam-su
Source1  : pam-login
Summary  : A set of pam configuration files
Group    : Development/Tools
License  : MIT

%description
A set of pam configuration files.

%prep

%build

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d
install -m  0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/pam.d/su
install -m  0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/login

%files
%defattr(-,root,root,-)
%{_sysconfdir}/pam.d/*
