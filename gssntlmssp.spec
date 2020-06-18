Summary:	GSSAPI NTLMSSP Mechanism
Name:		gssntlmssp
Version:	0.9.0
Release:	1
Group:		System/Libraries
License:	LGPLv3+
URL:		https://github.com/gssapi/gss-ntlmssp/
Source0:	https://github.com/gssapi/gss-ntlmssp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	xsltproc
BuildRequires:	libxml2
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd44-xml
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(krb5) >= 1.11.2
BuildRequires:	pkgconfig(gssrpc)
BuildRequires:	pkgconfig(libunistring)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(wbclient)
BuildRequires:	pkgconfig(zlib)

%description
A GSSAPI Mechanism that implements NTLMSSP.

%package devel
Summary:	Development header for GSSAPI NTLMSSP
Group:		Development/C++
Requires:	%{name} >= %{EVRD}

%description devel
Adds a header file with definition for custom GSSAPI extensions
for NTLMSSP.

%prep
%autosetup -p1

%build

%configure \
    --with-wbclient \
    --without-zlib \
    --disable-static

%make_build all

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

mkdir -p %{buildroot}%{_sysconfdir}/gss/mech.d
install -pm644 examples/mech.ntlmssp %{buildroot}%{_sysconfdir}/gss/mech.d/ntlmssp.conf

%check
make test_gssntlmssp

%files -f %{name}.lang
%doc COPYING
%config(noreplace) %{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{_libdir}/gssntlmssp/
%{_mandir}/man8/gssntlmssp.8*

%files devel
%{_includedir}/gssapi/gssapi_ntlmssp.h
