%define relno 1

%define release unknown
%define kum_release rc4

Name:		kumir-all
Summary:	KUMIR education system
License:	GPL
Group:		Education
Version:	1.7.1.%{kum_release}
Release:	%mkrel %{relno}
BuildRoot:	%{_tmppath}/kumir-%{version}
BuildRequires:	python >= 2.5
BuildRequires:	libqt4-devel >= 4.5.0
Requires:	libqtcore4 >= 4.5.0
Requires:	libqtgui4 >= 4.5.0
Requires:	libqtnetwork4 >= 4.5.0
Requires:	libqtscript4 >= 4.5.0
Requires:	libqtsvg4 >= 4.5.0
Requires:	libqtxml4 >= 4.5.0
Source:		kumir-1.7.1-%{kum_release}.tar.gz
URL:		http://lpm.org.ru/kumir/

%description
Complete KUMIR education system

%prep
%setup -q -n kumir-1.7.1-%{kum_release}


%build
python ./configure --prefix=$RPM_BUILD_ROOT/usr
make
strip -s kumir
strip -s pluginstarter

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%package -n kumir
Summary:	Kumir Language Implementation (development version)

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
/usr/libexec/kumir/Kumir/*
/usr/libexec/kumir/kumir
/usr/bin/kumir
/usr/share/applications/kumir.desktop
/usr/share/mime/application/x-kumir-program.xml
/usr/share/mimelnk/application/x-kumir-program.desktop
/usr/share/pixmaps/kumir.png
/usr/share/pixmaps/x-kumir-program.png

%package -n kumir-pluginstarter
Summary:	Starter to use Kumir Worlds without Kumir
Group:		Education

%description -n kumir-pluginstarter
Starter to use Kumir Worlds without Kumir


%files -n kumir-pluginstarter
%defattr(-,root,root)
/usr/libexec/kumir/pluginstarter
/usr/bin/kumpluginstarter

%package -n kumir-worlds-turtle
Summary:	Tutle for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-turtle
Turtle for Kumir anf Pictomir

%files -n kumir-worlds-turtle
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libturtle.so

%package -n kumir-worlds-kuznechik
Summary:	Grasshopper for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-kuznechik
Grasshopper for Kumir and Pictomir

%files -n kumir-worlds-kuznechik
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libkuznechik.so

%package -n kumir-worlds-vodoley
Summary:	Aquarius for Kumir and Pictomir
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-vodoley
Aquarius for Kumir anf Pictomir

%files -n kumir-worlds-vodoley
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libvodoley.so
/usr/libexec/kumir/Addons/vodoley/*
