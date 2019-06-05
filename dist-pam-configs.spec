Name     : dist-pam-configs
Version  : 1
Release  : 27
Source0  : pam-su
Source1  : pam-login
Source2  : pam-system-auth
Source3  : pam-su-l
Source4  : pam-sudo
Source5  : pam-sshd
Summary  : A set of pam configuration files
Group    : Development/Tools
License  : MIT

%description
A set of pam configuration files.

%prep

%build

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/pam.d
install -m  0644 %{SOURCE0} %{buildroot}%{_datadir}/pam.d/su
install -m  0644 %{SOURCE1} %{buildroot}%{_datadir}/pam.d/login
install -m  0644 %{SOURCE2} %{buildroot}%{_datadir}/pam.d/system-auth
install -m  0644 %{SOURCE3} %{buildroot}%{_datadir}/pam.d/su-l
install -m  0644 %{SOURCE4} %{buildroot}%{_datadir}/pam.d/sudo
install -m  0644 %{SOURCE5} %{buildroot}%{_datadir}/pam.d/sshd

%files
%defattr(-,root,root,-)
%{_datadir}/pam.d/*
