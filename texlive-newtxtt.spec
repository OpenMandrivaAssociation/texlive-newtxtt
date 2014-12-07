# revision 33819
# category Package
# catalog-ctan /fonts/newtxtt
# catalog-date 2014-05-04 12:01:16 +0200
# catalog-license gpl3
# catalog-version 1.00
Name:		texlive-newtxtt
Version:	1.00
Release:	3
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
%{_texmfdistdir}/fonts/enc/dvips/newtxtt/txttAec.enc
%{_texmfdistdir}/fonts/enc/dvips/newtxtt/txttBec.enc
%{_texmfdistdir}/fonts/enc/dvips/newtxtt/txttCec.enc
%{_texmfdistdir}/fonts/enc/dvips/newtxtt/txttDec.enc
%{_texmfdistdir}/fonts/map/dvips/newtxtt/newtxtt.map
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbtta.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttd.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttsca.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttscb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttscc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttscd.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttsla.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttslb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttslc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxbttsld.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxtt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxtta.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttd.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttsca.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttscb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttscc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttscd.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttsla.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttslb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttslc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtxtt/newtxttsld.tfm
%{_texmfdistdir}/fonts/type1/public/newtxtt/newtxbtt.pfb
%{_texmfdistdir}/fonts/type1/public/newtxtt/newtxbttsc.pfb
%{_texmfdistdir}/fonts/type1/public/newtxtt/newtxtt.pfb
%{_texmfdistdir}/fonts/type1/public/newtxtt/newtxttsc.pfb
%{_texmfdistdir}/tex/latex/newtxtt/newtxtt.sty
%{_texmfdistdir}/tex/latex/newtxtt/t1newtxtt.fd
%{_texmfdistdir}/tex/latex/newtxtt/ts1newtxtt.fd
%doc %{_texmfdistdir}/doc/fonts/newtxtt/README
%doc %{_texmfdistdir}/doc/fonts/newtxtt/newtxtt-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/newtxtt/newtxtt-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
