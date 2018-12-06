#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Size
Version  : 0.82
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/Devel-Size-0.82.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/Devel-Size-0.82.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-Size-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
=pod
Devel::Size - Perl extension for finding the memory usage of Perl variables

%package dev
Summary: dev components for the perl-Devel-Size package.
Group: Development
Requires: perl-Devel-Size-lib = %{version}-%{release}
Provides: perl-Devel-Size-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-Size package.


%package lib
Summary: lib components for the perl-Devel-Size package.
Group: Libraries

%description lib
lib components for the perl-Devel-Size package.


%prep
%setup -q -n Devel-Size-0.82

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Devel/Size.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Size.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Devel/Size/Size.so
