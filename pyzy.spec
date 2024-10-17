%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	The Chinese PinYin and Bopomofo conversion library
Name:		pyzy
Version:	0.1.0
Release:	2
License:	LGPLv2+
Group:		System/Internationalization
Url:		https://code.google.com/p/pyzy
Source0:	http://pyzy.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://pyzy.googlecode.com/files/pyzy-database-1.0.0.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(opencc)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	sqlite3-tools
Requires:	pyzy-db

%description
The Chinese Pinyin and Bopomofo conversion library.

%files
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/db/*.db

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for pyzy
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
The Chinese Pinyin and Bopomofo conversion library.

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libpyzy-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development tools for pyzy
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The pyzy-devel package contains the header files for pyzy.

%files -n %{devname}
%{_libdir}/libpyzy-%{api}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

#----------------------------------------------------------------------------

%package db-open-phrase
Summary:	The open phrase database for pyzy
Group:		System/Internationalization
Provides:	pyzy-db = %{EVRD}
BuildArch:	noarch

%description db-open-phrase
The phrase database for pyzy from open-phrase project.

%files db-open-phrase
%{_datadir}/%{name}/db/open-phrase.db

#----------------------------------------------------------------------------

%package db-android
Summary:	The android phrase database for pyzy
Group:		System/Internationalization
Provides:	pyzy-db = %{EVRD}
BuildArch:	noarch

%description db-android
The phrase database for pyzy from android project.

%files db-android
%{_datadir}/%{name}/db/android.db

#----------------------------------------------------------------------------

%prep
%setup -q
cp %{SOURCE1} data/db/open-phrase

%build
%configure2_5x \
	--disable-static \
	--enable-db-open-phrase \
	--enable-opencc

%make

%install
%makeinstall_std NO_INDEX=true

