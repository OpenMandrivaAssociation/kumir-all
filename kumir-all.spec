%define kum_release 2565
%define ver 1.8.0

Name:		kumir-all
Summary:	KUMIR education system
License:	GPL
Group:		Education
Version:	%{ver}.%{kum_release}
Release:	4
URL:		http://www.niisi.ru/kumir/
Source:		http://lpm.org.ru/kumir2/files/%{ver}/kumir-%{ver}.%{kum_release}.tar.gz
Source1:	kumir-alt-icons.tar.bz2
Source2:	test.vod
Source10:	%{name}.rpmlintrc
#patch from SUSE
Patch0:		kumir-ege-desktop.patch
Patch1:		kumir-configure.patch
#patch from ALT
Patch2:		kumir-1.7.1-desktop.patch
Patch3:		kumir-1.7.90-x-kumir-program.desktop.patch
Patch4:		kumir-1.7.1-x-kumir-program.xml.patch
# Rosa patches
Patch10:	kumir-1.8.0-gcc4.7.patch

BuildRequires:	python
BuildRequires:	qt4-devel
Requires:	libqtcore4
Requires:	libqtgui4
Requires:	libqtnetwork4
Requires:	libqtscript4
Requires:	libqtsvg4
Requires:	libqtxml4
Requires:	libqtwebkit4

%description
Complete KUMIR education system.

%prep
%setup -q -n kumir-%{ver} -a 1
#aplly patch from SUSE
%patch0 -p0
%patch1 -p0
#apply patch from ALT
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1
cp %{SOURCE2} .

# Disable build of some plugins
sed -i "s/dwunog//" Addons/Addons.pro
sed -i "s/isometricRobot//" Addons/Addons.pro
sed -i "s/convertor//" Addons/Addons.pro
sed -i "s/Robotor3D//" Addons/Addons.pro

%build
python ./configure --prefix=%{buildroot}/usr
make
#strip -s kumir
#strip -s pluginstarter
#cd Kumir-EGE/src
#%qmake_qt4 -config release
#make
#cd ..
#strip -s bin/ckumir
#cd ..

%install
KUMIR_DIR=%{buildroot}%{_datadir}/kumir make install
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/vodoley/resources/
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/painter/resources/

cp Addons/libpainter.so %{buildroot}%{_datadir}/kumir/Addons/
cp Addons/turtle.ini %{buildroot}%{_datadir}/kumir/Addons/
cp Addons/vodoley/resources/*.* %{buildroot}%{_datadir}/kumir/Addons/vodoley/resources/
cp Addons/painter/resources/*.* %{buildroot}%{_datadir}/kumir/Addons/painter/resources/
cp kumir-ege.desktop %{buildroot}%{_datadir}/applications/
#cp -R Kumir-EGE/bin Kumir-EGE/share %{buildroot}/usr

#install -m 644 -D Kumir/X-Desktop/%name.desktop %buildroot%_desktopdir/%name.desktop
install -m 644 -D Kumir/X-Desktop/x-kumir-program.xml %buildroot/%_datadir/mime/packages/x-kumir-program.xml
install -m 644 -D Kumir/X-Desktop/x-kumir-program.desktop  %buildroot/%_datadir/mimelnk/application/x-kumir-program.desktop

# Install icons

mkdir -p %buildroot%_icons16dir/ %buildroot%{_iconsbasedir}/32x32/apps %buildroot%_liconsdir/ %buildroot%_iconsdir/hicolor/64x64/apps/ %buildroot%_iconsdir/hicolor/128x128/apps/
install -m 644 alt-icons/16x16/*.png %buildroot%_icons16dir/
install -m 644 alt-icons/32x32/*.png %buildroot%{_iconsbasedir}/32x32/apps
install -m 644 alt-icons/48x48/*.png %buildroot%_liconsdir/
install -m 644 alt-icons/64x64/*.png %buildroot%_iconsdir/hicolor/64x64/apps/
#install -m 644 alt-icons/128x128/*.png %buildroot%_iconsdir/hicolor/128x128/apps/

#rm %buildroot%_iconsdir/hicolor/128x128/apps/kumir.png
#rm %buildroot%_iconsdir/hicolor/*/apps/pictomir.png

install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/16x16/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/16x16/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/22x22/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/22x22/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/32x32/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/32x32/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/48x48/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/48x48/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/64x64/application-x-kumir-program.png %buildroot%_iconsdir/crystalsvg/64x64/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/crystalsvg/mimetypes/scalable/application-x-kumir-program.svg %buildroot%_iconsdir/crystalsvg/scalable/mimetypes/application-x-kumir-program.svg
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/16x16/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/16x16/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/22x22/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/22x22/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/32x32/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/32x32/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/48x48/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/48x48/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/64x64/application-x-kumir-program.png %buildroot%_iconsdir/oxygen/64x64/mimetypes/application-x-kumir-program.png
install -m 644 -D Kumir/Images/mime/oxygen/mimetypes/scalable/application-x-kumir-program.svg %buildroot%_iconsdir/oxygen/scalable/mimetypes/application-x-kumir-program.svg

# Install TaskControl plugin
install -m 644 -D TaskControl/libtaskControl.so  %{buildroot}%{_datadir}/kumir/TaskControl/libtaskControl.so

# Fix paths to help files
cd %{buildroot}%{_datadir}/kumir/Kumir
ln -s Help help

# Rename kumir.png to correct name
cd %{buildroot}%{_datadir}/pixmaps
mv kumir.png application-x-kumir-program.png

# make link in /usr/bin/kumir
#cd %buildroot%_bindir
#rm kumir kumpluginstarter
#ln -s ../..%_libdir/kumir/kumir kumir
#ln -s ../..%_libdir/kumir/pluginstarter kumpluginstarter

# Fix permissions
find %{buildroot} -perm 0666 -exec chmod 0644 '{}' \;
find %{buildroot} -perm 0777 -exec chmod 0755 '{}' \;

%package -n kumir
Summary:	Kumir Language Implementation (development version)
Group:	Education
Suggests:	kumir-pluginstarter kumir-worlds-kuznechik kumir-worlds-painter kumir-worlds-turtle kumir-worlds-vodoley

%description -n kumir
Implementation of Kumir programming language, designed by academic Ershov.
Includes compiler, runtime, IDE, Robot and Draw.

%post -n kumir
cd /usr/share/mime
rm -f XMLnamespaces aliases globs magic subclasses
update-mime-database /usr/share/mime > /dev/null

%postun -n kumir
cd /usr/share/mime
rm -f XMLnamespaces aliases globs magic subclasses application/x-kumir-program.xml
update-mime-database /usr/share/mime > /dev/null

%files -n kumir
%{_datadir}/kumir/Kumir/*
%{_datadir}/kumir/kumir
%{_bindir}/kumir
%{_datadir}/applications/kumir.desktop
%{_datadir}/applications/kumir-ege.desktop
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/x-kumir-program.xml
%{_datadir}/mimelnk/application/x-kumir-program.desktop
%{_datadir}/kumir/TaskControl
%{_iconsdir}/*

#%package -n ckumir
#Requires:	libqtcore4 >= 4.6.0
#Summary:	Console version of Kumir core 
#Group:		Education

#%description -n ckumir
#Non-gui version of Kumir core system.
#Operates in two modes:
#    1. Correctness check of program
#    2. Evaluation of program
#I/O operations are mapped to stdin/stdout, error messages - to stderr.
#Use of any modules (including non-GUI) is prohibited.
#For usage information type "ckumir --help" in terminal.

#%files -n ckumir
#%defattr(-,root,root)
#%{_bindir}/ckumir
#%{_datadir}/kumir/*

%package -n kumir-pluginstarter
Summary:	Starter to use Kumir Worlds without Kumir
Group:		Education

%description -n kumir-pluginstarter
Starter to use Kumir Worlds without Kumir

%files -n kumir-pluginstarter
%{_datadir}/kumir/pluginstarter
%{_bindir}/kumpluginstarter

%package -n kumir-worlds-turtle
Summary:	Tutle for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-turtle
Turtle for Kumir anf Pictomir

%files -n kumir-worlds-turtle
%{_datadir}/kumir/Addons/libturtle.so
%{_datadir}/kumir/Addons/turtle.ini

%package -n kumir-worlds-kuznechik
Summary:	Grasshopper for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-kuznechik
Grasshopper for Kumir and Pictomir

%files -n kumir-worlds-kuznechik
%{_datadir}/kumir/Addons/libkuznechik.so

%package -n kumir-worlds-vodoley
Summary:	Aquarius for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-vodoley
Aquarius for Kumir anf Pictomir

%files -n kumir-worlds-vodoley
%{_datadir}/kumir/Addons/libvodoley.so
%{_datadir}/kumir/Addons/vodoley/*

%package -n kumir-worlds-painter
Summary:	Painter for Kumir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-painter
Painter for Kumir

%files -n kumir-worlds-painter
%{_datadir}/kumir/Addons/libpainter.so
%{_datadir}/kumir/Addons/painter/*


%changelog
* Tue Apr 26 2011 Александр Казанцев <kazancas@mandriva.org> 1.8.0.2565-3mdv2011.0
+ Revision: 659414
+ rebuild (emptylog)

* Sun Apr 17 2011 Александр Казанцев <kazancas@mandriva.org> 1.8.0.2565-2
+ Revision: 653967
+ rebuild (emptylog)

* Sun Apr 17 2011 Александр Казанцев <kazancas@mandriva.org> 1.8.0.2565-1
+ Revision: 653918
- new version 1.8.0. Add new addons - painter

* Tue Jan 25 2011 Александр Казанцев <kazancas@mandriva.org> 1.7.3.2369-1
+ Revision: 632495
- version 1.7.3

* Wed Dec 29 2010 Александр Казанцев <kazancas@mandriva.org> 1.7.1.rc4-1mdv2011.0
+ Revision: 625872
- import kumir-all


