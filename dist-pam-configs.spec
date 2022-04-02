Name     : dist-pam-configs
Version  : 1
Release  : 31
Source0  : pam-su
Source1  : pam-login
Source2  : pam-system-auth
Source3  : pam-su-l
Source4  : pam-sudo
Source5  : pam-sshd
Source6  : pam-runuser
Source7  : pam-runuser-l
Summary  : A set of pam configuration files
Group    : Development/Tools
License  : MIT

%description
A set of pam configuration files.

%prep

%build

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/usr/share/pam.d
install -m  0644 %{SOURCE0} %{buildroot}/usr/share/pam.d/su
install -m  0644 %{SOURCE1} %{buildroot}/usr/share/pam.d/login
install -m  0644 %{SOURCE2} %{buildroot}/usr/share/pam.d/system-auth
install -m  0644 %{SOURCE3} %{buildroot}/usr/share/pam.d/su-l
install -m  0644 %{SOURCE4} %{buildroot}/usr/share/pam.d/sudo
install -m  0644 %{SOURCE5} %{buildroot}/usr/share/pam.d/sshd
install -m  0644 %{SOURCE6} %{buildroot}/usr/share/pam.d/runuser
install -m  0644 %{SOURCE7} %{buildroot}/usr/share/pam.d/runuser-l

%files
%defattr(-,root,root,-)
/usr/share/pam.d/su
/usr/share/pam.d/login
/usr/share/pam.d/system-auth
/usr/share/pam.d/su-l
/usr/share/pam.d/sudo
/usr/share/pam.d/sshd
/usr/share/pam.d/runuser
/usr/share/pam.d/runuser-l
