%define relno 1
%define kum_release 2565
%define ver 1.8.0

Name:		kumir-all
Summary:	KUMIR education system
License:	GPL
Group:		Education
Version:	%{ver}.%{kum_release}
Release:	%mkrel %{relno}
BuildRoot:	%{_tmppath}/kumir-%{version}
BuildRequires:	python >= 2.5
BuildRequires:	libqt4-devel >= 4.6.0
Requires:	libqtcore4 >= 4.6.0
Requires:	libqtgui4 >= 4.6.0
Requires:	libqtnetwork4 >= 4.6.0
Requires:	libqtscript4 >= 4.6.0
Requires:	libqtsvg4 >= 4.6.0
Requires:	libqtxml4 >= 4.6.0
Requires:	libqtwebkit4 >= 4.6.0
Source:		http://lpm.org.ru/kumir2/files/%{ver}/kumir-%{ver}.%{kum_release}.tar.gz
Patch0:		kumir-ege-desktop.patch
Patch1:		kumir-configure.patch
#Patch2:		kumir-install-script.patch
URL:		http://www.niisi.ru/kumir/

%description
Complete KUMIR education system

%prep
%setup -q -n kumir-%{ver}
%patch0 -p0
%patch1 -p0
#%patch2 -p0

%build
python ./configure --prefix=%{buildroot}/usr
make
strip -s kumir
strip -s pluginstarter
#cd Kumir-EGE/src
#%qmake_qt4 -config release
#make
#cd ..
#strip -s bin/ckumir
#cd ..

%install
rm -rf %{buildroot}
KUMIR_DIR=%{buildroot}%{_datadir}/kumir make install
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/vodoley/resources/
mkdir -p %{buildroot}%{_datadir}/kumir/Addons/painter/resources/

cp Addons/libpainter.so %{buildroot}%{_datadir}/kumir/Addons/
cp Addons/turtle.ini %{buildroot}%{_datadir}/kumir/Addons/
cp Addons/vodoley/resources/*.* %{buildroot}%{_datadir}/kumir/Addons/vodoley/resources/
cp Addons/painter/resources/*.* %{buildroot}%{_datadir}/kumir/Addons/painter/resources/
cp kumir-ege.desktop $RPM_BUILD_ROOT/usr/share/applications/
#cp -R Kumir-EGE/bin Kumir-EGE/share %{buildroot}/usr

%clean
rm -rf %{buildroot}

%package -n kumir
Summary:	Kumir Language Implementation (development version)
Group:	Education

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
%defattr(-,root,root)
%defattr(-,root,root)
%{_datadir}/kumir/Kumir/*
%{_datadir}/kumir/kumir
%{_bindir}/kumir
%{_datadir}/applications/kumir.desktop
%{_datadir}/applications/kumir-ege.desktop
%{_datadir}/pixmaps/kumir.png

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
%defattr(-,root,root)
%{_datadir}/kumir/pluginstarter
%{_bindir}/kumpluginstarter

%package -n kumir-worlds-turtle
Summary:	Tutle for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-turtle
Turtle for Kumir anf Pictomir

%files -n kumir-worlds-turtle
%defattr(-,root,root)
%{_datadir}/kumir/Addons/libturtle.so

%package -n kumir-worlds-kuznechik
Summary:	Grasshopper for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-kuznechik
Grasshopper for Kumir and Pictomir

%files -n kumir-worlds-kuznechik
%defattr(-,root,root)
%{_datadir}/kumir/Addons/libkuznechik.so

%package -n kumir-worlds-vodoley
Summary:	Aquarius for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-vodoley
Aquarius for Kumir anf Pictomir

%files -n kumir-worlds-vodoley
%defattr(-,root,root)
%{_datadir}/kumir/Addons/libvodoley.so
%{_datadir}/kumir/Addons/vodoley/*

%package -n kumir-worlds-painter
Summary:	Painter for Kumir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-painter
Painter for Kumir

%files -n kumir-worlds-painter
%defattr(-,root,root)
/usr/kumir/Addons/libpainter.so
/usr/kumir/Addons/painter/*
