Summary:	Open source implementation of a 16-bit x86 BIOS
Summary(pl.UTF-8):	Implementacja 16-bitowego BIOS-u x86 o otwartych źródłach
Name:		seabios
Version:	1.16.3
Release:	1
License:	LGPL v3
Group:		Applications/System
Source0:	https://www.seabios.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9f854ca1ae32bfdc081377717a18e1b3
URL:		https://www.seabios.org/SeaBIOS
BuildRequires:	acpica
%ifnarch %{ix86} %{x8664} x32
# i386 crosscompiler could be used as well, but we have only x86_64 as more universal
BuildRequires:	crossx8664-binutils
BuildRequires:	crossx8664-gcc
%endif
BuildRequires:	python3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

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
	V=1 PYTHON=%{__python3} \
%ifnarch %{ix86} %{x8664} x32
	CROSS_PREFIX=x86_64-pld-linux
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install out/bios.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/bios.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{Debugging.md,Mailinglist.md,Memory_Model.md,Releases.md,Runtime_config.md,SeaBIOS.md,SeaVGABIOS.md}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bios.bin
