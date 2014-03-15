Summary:    Audio Editing Package
Name:       rezound
Version:    0.13.1
Release:    1
License:    GPLv2+
Group:      Sound
URL:        http://rezound.sourceforge.net/
Source0:    http://prdownloads.sourceforge.net/rezound/%{name}-%{version}beta.tar.gz
BuildRequires:  libvorbis-devel
BuildRequires:  fox1.6-devel
BuildRequires:  audiofile-devel
BuildRequires:	flex
BuildRequires:  pkgconfig(jack)
BuildRequires:  fftw2-devel
BuildRequires:  flac++-devel
BuildRequires:  soundtouch-devel
BuildRequires:  bison >= 1.875-3mdk

%description
ReZound aims to be a stable, open source, and graphical audio file editor
primarily for but not limited to the Linux operating system.

%prep

%setup -q -n %name-%{version}beta

%build
LDFLAGS="-lX11 -ldl" %configure2_5x --disable-portaudio
%make

%install
%makeinstall_std
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

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/rezound
%_datadir/applications/mandriva-%name.desktop
%_docdir/%name-%version

