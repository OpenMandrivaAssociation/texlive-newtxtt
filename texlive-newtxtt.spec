%global tl_name newtxtt
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.059
Release:	%{tl_revision}.1
Summary:	Enhancement of typewriter fonts from newtx
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newtxtt
License:	gpl3 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides enhanced fonts with LaTeX support files providing
access to the typewriter fonts from newtx. Regular and bold weights,
slanted variants and a choice of four different styles for zero.

