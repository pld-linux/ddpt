Summary:	A variant of the standard Unix command dd
Summary(pl.UTF-8):	Alternatywna implementacja standardowej uniksowej komendy dd
Name:		ddpt
Version:	0.97
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tar.xz
# Source0-md5:	5217a3a2f316b8d1e5ea6e4645cd8ec6
URL:		http://sg.danny.cz/sg/ddpt.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	sg3_utils-devel >= 1.38
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	sg3_utils >= 1.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ddpt utility is a variant of the standard Unix command dd which
copies files. The ddpt utility specializes in files that are block
devices. For block devices that understand the SCSI command set, finer
grain control over the copy may be available via a SCSI pass-through
interface.

The types of block devices that are supported are disks (known as
direct access devices in SCSI) and cd/dvd/bd devices. Tape drives are
not supported. It is becoming more common for ATA disks (especially
SATA) to be accessed by an operating system using SCSI commands. ATA
disks are not always directly connected and transports such as USB,
IEEE1394 (FireWire) and iSCSI use SCSI commands. Protocol translation
from SCSI to ATA (SAT standard) has been around for several years and
many implementations are now reliable.

The ddpt utility is a more generic version of the Linux specific sg_dd
utility found in the sg3_utils package.

%description -l pl.UTF-8
ddpt jest implementacją standardowej komendy Uniksa dd, służącej do
kopiowania plików. ddpt zostało napisane szczególnie z myślą o
plikach będących urządzeniami blokowymi. Dla urządzeń blokowych, które
rozumieją zestaw komend SCSI, jest dostępna bardziej szczegółowa
kontrola nad procesem kopiowania poprzez interface SCSI pass-through.

Obsługiwane urządzenia blokowe to dyski (znane jako urządzenia SCSI
o bezpośrednim dostępnie) oraz urządzenia cd/dvd/bd. Napędy taśmowe
nie są obsługiwane. Coraz bardziej popularny jest dostęp poprzez
polecenia SCSI do dysków ATA (zwłaszcza SATA). Dyski ATA nie zawsze są
podłączone bezpośrednio, a transporty takie jak USB, IEEE1394
(FireWire) oraz iSCSI używają poleceń SCSI. Tłumaczenie protokołu z
SCSI na ATA (standard SAT) istnieje od kilku lat i dostępne jest wiele
implementacji.

Narzędzie ddpt jest bardziej ogólną wersją specyficznego dla Linuksa
narzędzia sg_dd, które można znaleźć w pakiecie sg3_utils.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/ddpt
%attr(755,root,root) %{_bindir}/ddpt_sgl
%attr(755,root,root) %{_bindir}/ddptctl
%{_mandir}/man8/ddpt.8*
%{_mandir}/man8/ddpt_sgl.8*
%{_mandir}/man8/ddptctl.8*
