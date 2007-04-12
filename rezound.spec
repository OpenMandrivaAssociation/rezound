%define name	rezound
%define version 0.12.3
%define release %mkrel 2

Summary:	Audio Editing Package
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Sound
URL: 		http://rezound.sourceforge.net/
Source0: 	http://prdownloads.sourceforge.net/rezound/%{name}-%{version}beta.tar.bz2
Patch: rezound-0.12.2beta-64bit.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libvorbis-devel 
BuildRequires:  fox1.4-devel
BuildRequires:  libaudiofile-devel flex
BuildRequires:  libjack-devel
BuildRequires:  fftw2-devel
BuildRequires:  libflac++-devel
BuildRequires:  SoundTouch-devel
BuildRequires:  bison >= 1.875-3mdk
BuildRequires:  automake1.8

%description
ReZound aims to be a stable, open source, and graphical audio file editor 
primarily for but not limited to the Linux operating system.

%prep
rm -rf $RPM_BUILD_ROOT 

%setup -q -n %name-%{version}beta
%patch -p1

%build
%configure2_5x --disable-portaudio
%make

%install
%makeinstall
mkdir -p %buildroot/%{_docdir}/%name-%version
mv %buildroot%_prefix/doc/* %buildroot/%{_docdir}/%name-%version

# Menu
mkdir -p %buildroot/%{_menudir}
cat > %buildroot/%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="sound_section.png" section="Multimedia/Sound" \
title="Rezound" longtitle="Digital audio editor" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
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

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_menudir}/*
%{_datadir}/rezound
%_datadir/applications/mandriva-%name.desktop
%_docdir/%name-%version


