%define name	rezound
%define version 0.12.3
%define release %mkrel 6

Summary:	Audio Editing Package
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPLv2+
Group: 		Sound
URL: 		http://rezound.sourceforge.net/
Source0: 	http://prdownloads.sourceforge.net/rezound/%{name}-%{version}beta.tar.bz2
Patch:		rezound-0.12.2beta-64bit.patch
Patch1:		rezound-flac-1.2.patch
# patch from Debian
Patch2:		11_gcc_4.3.patch
#
Patch3:		rezound-0.12.3beta-fix-gcc44.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libvorbis-devel 
BuildRequires:  fox1.6-devel
BuildRequires:  libaudiofile-devel flex
BuildRequires:  libjack-devel
BuildRequires:  fftw2-devel
BuildRequires:  libflac++-devel
BuildRequires:  soundtouch-devel
BuildRequires:  bison >= 1.875-3mdk

%description
ReZound aims to be a stable, open source, and graphical audio file editor 
primarily for but not limited to the Linux operating system.

%prep
rm -rf $RPM_BUILD_ROOT 

%setup -q -n %name-%{version}beta
%patch -p1
%patch1 -p1
%patch2 -p1 -b .gcc43
%patch3 -p1 -b .gcc44

%build
%configure2_5x --disable-portaudio
%make

%install
%makeinstall
mkdir -p %buildroot/%{_docdir}/%name-%version
mv %buildroot%_prefix/doc/* %buildroot/%{_docdir}/%name-%version

# Menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Rezound
Comment=Digital audio editor
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideoEditing;Recorder;
EOF

%find_lang %name

%clean
rm -rf %buildroot/

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/rezound
%_datadir/applications/mandriva-%name.desktop
%_docdir/%name-%version


