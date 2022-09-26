%define date 20220926
Summary:    Audio Editing Package
Name:       rezound
Version:    0.13.2
Release:    %{?date:0.%{date}.}1
License:    GPLv2+
Group:      Sound
URL:        http://rezound.sourceforge.net/
Source0:    https://github.com/ddurham2/rezound/archive/refs/heads/dev/qt.tar.gz#/%{name}-%{date}.tar.gz
BuildRequires:  libvorbis-devel
BuildRequires:	qmake-qt6
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  audiofile-devel
BuildRequires:	flex
BuildRequires:  pkgconfig(jack)
BuildRequires:  fftw-devel
BuildRequires:  flac++-devel
BuildRequires:  soundtouch-devel
BuildRequires:  bison >= 1.875-3mdk
BuildRequires:	gettext-devel
BuildRequires:	boost-devel
BuildRequires:	cmake qt6-cmake ninja

%description
ReZound aims to be a stable, open source, and graphical audio file editor
primarily for but not limited to the Linux operating system.

%prep
%autosetup -p1 -n %name%{?date:-dev-qt}%{!?date:-%{version}}
%cmake -G Ninja \
	-DBUILD_GMOCK:BOOL=OFF \
	-DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON

%build
export LD_LIBRARY_PATH=`pwd`/build/lib:$LD_LIBRARY_PATH
%ninja_build -C build

%install
%ninja_install -C build

# No point in packaging the google test stuff that's just
# built to run autotests
rm -rf %{buildroot}%{_includedir}/gmock \
	%{buildroot}%{_includedir}/gtest \
	%{buildroot}%{_libdir}/cmake/GTest \
	%{buildroot}%{_libdir}/libgmock.so* \
	%{buildroot}%{_libdir}/libgmock_main.so* \
	%{buildroot}%{_libdir}/libgtest.so* \
	%{buildroot}%{_libdir}/libgtest_main.so* \
	%{buildroot}%{_libdir}/pkgconfig/gmock*.pc \
	%{buildroot}%{_libdir}/pkgconfig/gtest*.pc

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


%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/rezound
%_datadir/applications/mandriva-%name.desktop
%_docdir/%name-%version
