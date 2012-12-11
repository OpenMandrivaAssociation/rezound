%define name    rezound
%define version 0.12.3
%define release %mkrel 6

Summary:    Audio Editing Package
Name:       rezound
Version:    0.12.3
Release:    7
License:    GPLv2+
Group:      Sound
URL:        http://rezound.sourceforge.net/
Source0:    http://prdownloads.sourceforge.net/rezound/%{name}-%{version}beta.tar.bz2
Patch:      rezound-0.12.2beta-64bit.patch
Patch1:     rezound-flac-1.2.patch
# patch from Debian
Patch2:     11_gcc_4.3.patch
#
Patch3:     rezound-0.12.3beta-fix-gcc44.patch
BuildRequires:  libvorbis-devel
BuildRequires:  fox1.6-devel
BuildRequires:  libaudiofile-devel flex
BuildRequires:  pkgconfig(jack)
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

#perl -pi -e 's/AM_PATH_AUDIOFILE\(0.2.2/AM_PATH_AUDIOFILE\(0.3.4/g' configure.ac
perl -pi -e 's/setNewFilterKernel\(convert/this->setNewFilterKernel\(convert/g' src/backend/DSP/Convolver.h
perl -pi -e 's/push_back/this->push_back/g' src/misc/auto_array.h
perl -pi -e 's/overflowWrite/this->overflowWrite/g' src/PoolFile/TPoolAccesser.cpp

%build
LDFLAGS="-lX11 -ldl"%configure2_5x --disable-portaudio
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




%changelog
* Tue Jun 02 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.12.3-6mdv2010.0
+ Revision: 382099
- fix build with gcc 4.3 (patch from Debian)
- fix build with gcc 4.4
- fix license (GPLv2+)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Emmanuel Andry <eandry@mandriva.org> 0.12.3-3mdv2008.0
+ Revision: 82475
- Drop old menu
- build against fox 1.6
- add sourceforge patch to fix build with flac >= 1.1.3

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.3-2mdv2007.0
+ Revision: 108624
- bot rebuild
- Import rezound

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.12.3-1mdv2007.1
- xdg menu
- unpack patch
- disable portaudio
- new version

* Tue Feb 14 2006 Götz Waschk <waschk@mandriva.org> 0.12.2-2mdk
- patch to make it build on 64 bit

* Tue Sep 06 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.2-1mdk
- New release 0.12.2

* Mon Sep 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.1-1mdk
- New release 0.12.1

* Tue May 03 2005 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdk
- drop the patch
- New release 0.12.0

* Fri Apr 22 2005 Lenny Cartier <lenny@mandriva.com> 0.11.1-3mdk
- rebuild for dependencies

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.11.1-2mdk
- fix buildrequires
- build with the new fox

* Thu Oct 28 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.11.1-1mdk
- New release 0.11.1

* Mon Oct 25 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.11.0-1mdk
- New release 0.11.0

* Tue Aug 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.10.0-2mdk
- rebuild for new flac

* Wed Jul 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.10.0-1mdk
- 0.10.0beta

* Tue Jun 29 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.1-0.20040628.1mdk
- fix buildrequires, use fox 1.2
- upgrade to CVS snapshot

