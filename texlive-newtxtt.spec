Name:		texlive-newtxtt
Version:	1.055
Release:	2
Summary:	Enhancement of typewriter fonts from newtx
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/newtxtt
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides enhanced fonts with LaTeX support files
providing access to the typewriter fonts from newtx. Regular
and bold weights, slanted variants and a choice of four
different styles for zero.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/newtxtt
%{_texmfdistdir}/fonts/map/dvips/newtxtt
%{_texmfdistdir}/fonts/tfm/public/newtxtt
%{_texmfdistdir}/fonts/type1/public/newtxtt
%{_texmfdistdir}/tex/latex/newtxtt
%doc %{_texmfdistdir}/doc/fonts/newtxtt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
