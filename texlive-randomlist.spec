Name:		texlive-randomlist
Version:	45281
Release:	2
Summary:	Deal with database, loop, and random in order to build personalized exercises
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/randomlist
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomlist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomlist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomlist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main aim of this package is to work on lists, especially
with random operations. The hidden aim is to build a personnal
collection of exercises with different data for each pupil.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/randomlist
%{_texmfdistdir}/tex/generic/randomlist
%doc %{_texmfdistdir}/doc/generic/randomlist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
