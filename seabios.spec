Summary:	Open source implementation of a 16-bit x86 BIOS
Summary(pl.UTF-8):	Implementacja 16-bitowego BIOS-u x86 o otwartych źródłach
Name:		seabios
Version:	1.8.0
Release:	1
License:	LGPL v3
Group:		Applications/System
Source0:	http://code.coreboot.org/p/seabios/downloads/get/%{name}-%{version}.tar.gz
# Source0-md5:	a4bbfa4139ae0b7f31cb11674080e1ed
# binary for non-x86 archs
Source1:	http://code.coreboot.org/p/seabios/downloads/get/bios.bin-%{version}.gz
# Source1-md5:	0d224123289f68db9087873dd61e9c18
URL:		http://seabios.org/
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
%ifarch %{ix86} %{x8664}
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%ifarch %{ix86} %{x8664}
install out/bios.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/bios.bin
install out/src/fw/*.aml $RPM_BUILD_ROOT%{_datadir}/%{name}
%else
gunzip -c %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/%{name}/bios.bin
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bios.bin
%ifarch %{ix86} %{x8664}
%{_datadir}/%{name}/*.aml
%endif
