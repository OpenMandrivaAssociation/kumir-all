%define distsuffix edm
# norootforbuild

# Spec for:
# -- openSUSE 11.0
# -- openSUSE 11.1
# -- openSUSE 11.2
# -- openSUSE Factory
# -- Mandriva 2010.0
# -- Fedora 12

# --------------- К О Н Ф И Г У Р А Ц И Я      С Б О Р К И --------------------
# relno -- номер сборки
# packager -- кто собрал пакет
# is_buildservice -- 1, если сборка через openSUSE BuildService,
#                    0 в противном случае
# ---------------

%define relno 1
%define packager Victor Yacovlev <victor@lpm.org.ru>
%define is_buildservice 0

# -----------------------------------------------------------------------------


%define release unknown
%define kum_release rc4

%if %{is_buildservice}
    %define is_suse %{defined suse_version}
    %define is_mandriva %{defined mdkversion}
    %define is_fedora %{defined fedora}
%else
    %define is_suse %(if [ -f /etc/SuSE-release ] ; then echo -n 1; else echo -n 0; fi)
    %define is_mandriva %(if [ -f /etc/mandriva-release ] ; then echo -n 1; else echo -n 0; fi)
    %define is_fedora %(if [ -f /etc/fedora-release ] ; then echo -n 1; else echo -n 0; fi)
%endif

%if %{is_suse}
    %define release %{relno}.suse%{suse_version}
%endif

%if %{is_mandriva}
    %define release %mkrel %{relno}
%endif

%if %{is_fedora}
    %define release %{relno}.fc%{fedora}
%endif

Name:		kumir-all
Summary:	KUMIR education system
License:	GPL
Group:		Education
Version:	1.7.1.%{kum_release}
Release:	%{release}
BuildRoot:	%{_tmppath}/kumir-%{version}
BuildRequires:	python >= 2.5
%if %{is_suse}
BuildRequires:	libqt4-devel >= 4.5.0
%if %{is_buildservice}
BuildRequires:	-post-build-checks -rpmlint-Factory
%endif
Requires:	libqt4 >= 4.5.0
Requires:	libqt4-x11 >= 4.5.0
%endif
%if %{is_mandriva}
BuildRequires:	libqt4-devel >= 4.5.0
Requires:	libqtcore4 >= 4.5.0
Requires:	libqtgui4 >= 4.5.0
Requires:	libqtnetwork4 >= 4.5.0
Requires:	libqtscript4 >= 4.5.0
Requires:	libqtsvg4 >= 4.5.0
Requires:	libqtxml4 >= 4.5.0
%endif
%if %{is_fedora}
BuildRequires:	gcc-c++
BuildRequires:	qt-devel >= 4.5.0
Requires:	qt >= 4.5.0
Requires:	qt-x11 >= 4.5.0
%endif
PreReq:		shared-mime-info
Vendor:		NIISI RAS
Source:		kumir-1.7.1-%{kum_release}.tar.gz
Packager:	%{packager}
URL:		http://lpm.org.ru/kumir/

%description
Complete KUMIR education system

%description -l ru_RU.UTF-8
Комплект Учебных МИРов

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
Summary(ru_RU.UTF-8): Реализация системы КуМир (текущая версия)
Group:		Education

%description -n kumir
Implementation of Kumir programming language, designed by academic Ershov.
Includes compiler, runtime, IDE, Robot and Draw.

%description -n kumir -l ru_RU.UTF-8
Реализация системы КУМИР в соответствии с учебником Анатолия Георгиевича Кушниренко.
Включает в себя среду программирования на русском алгоритмическом языке а также
канонические исполнители: Робот и Чертёжник.

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
Summary(ru_RU.UTF-8): Система запуска Миров без помощи Кумира
Group:		Education

%description -n kumir-pluginstarter
Starter to use Kumir Worlds without Kumir

%description -n kumir-pluginstarter -l ru_RU.UTF-8
Система запуска Миров без помощи Кумира

%files -n kumir-pluginstarter
%defattr(-,root,root)
/usr/libexec/kumir/pluginstarter
/usr/bin/kumpluginstarter

%package -n kumir-worlds-turtle
Summary:	Tutle for Kumir and Pictomir
Summary(ru_RU.UTF-8): Черепаха для Кумира и Пиктомира
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-turtle
Turtle for Kumir anf Pictomir

%description -n kumir-worlds-turtle -l ru_RU.UTF-8
Черепаха для Кумира и Пиктомира

%files -n kumir-worlds-turtle
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libturtle.so

%package -n kumir-worlds-kuznechik
Summary:	Grasshopper for Kumir and Pictomir
Summary(ru_RU.UTF-8): Кузнечик для Кумира и Пиктомира
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-kuznechik
Grasshopper for Kumir and Pictomir

%description -n kumir-worlds-kuznechik -l ru_RU.UTF-8
Кузнечик для Кумира и Пиктомира

%files -n kumir-worlds-kuznechik
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libkuznechik.so

%package -n kumir-worlds-vodoley
Summary:	Aquarius for Kumir and Pictomir
Summary(ru_RU.UTF-8): Водолей для Кумира и Пиктомира
Requires:	kumir-pluginstarter >= %{version}
Group:		Education

%description -n kumir-worlds-vodoley
Aquarius for Kumir anf Pictomir

%description -n kumir-worlds-vodoley -l ru_RU.UTF-8
Водолей для Кумира и Пиктомира

%files -n kumir-worlds-vodoley
%defattr(-,root,root)
/usr/libexec/kumir/Addons/libvodoley.so
/usr/libexec/kumir/Addons/vodoley/*
