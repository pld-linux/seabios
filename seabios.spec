Summary:	Open source implementation of a 16-bit x86 BIOS
Summary(pl.UTF-8):	Implementacja 16-bitowego BIOS-u x86 o otwartych źródłach
Name:		seabios
Version:	1.9.0
Release:	1
License:	LGPL v3
Group:		Applications/System
#Source0Download: http://code.coreboot.org/p/seabios/downloads/
Source0:	http://code.coreboot.org/p/seabios/downloads/get/%{name}-%{version}.tar.gz
# Source0-md5:	c3fea87e731e396bd4e7e2c478ba39d9
URL:		http://seabios.org/
BuildRequires:	acpica
%ifnarch %{ix86} %{x8664} x32
# i386 crosscompiler could be used as well, but we have only x86_64 as more universal
BuildRequires:	crossx8664-binutils
BuildRequires:	crossx8664-gcc
%endif
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SeaBIOS is an open source implementation of a 16-bit X86 BIOS. SeaBIOS
can run in an emulator or it can run natively on X86 hardware with the
use of coreboot.

SeaBIOS is the default BIOS for QEMU, KVM and Xen HVM.

%description -l pl.UTF-8
SeaBIOS to mająca otwarte źródła implementacją 16-bitowego BIOS-u X86.
SeaBIOS może działać pod kontrolą emulatora lub natywnie na sprzęcie
X86 przy użyciu bootloadera coreboot.

SeaBIOS to domyślny BIOS dla narzędzi QEMU, KVM i Xen HVM.

%prep
%setup -q

%build
%{__make} \
	V=1 \
%ifnarch %{ix86} %{x8664} x32
	CROSS_PREFIX=x86_64-pld-linux
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install out/bios.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/bios.bin
install out/src/fw/*.aml $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{Debugging.md,Mailinglist.md,Memory_Model.md,Releases.md,Runtime_config.md,SeaBIOS.md,SeaVGABIOS.md}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bios.bin
%{_datadir}/%{name}/*.aml
