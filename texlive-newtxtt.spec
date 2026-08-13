%global tl_name newtxtt
%global tl_revision 79618
%global tl_version 1.059

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Enhancement of typewriter fonts from newtx
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newtxtt
License:	gpl3 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxtt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides enhanced fonts with LaTeX support files providing
access to the typewriter fonts from newtx. Regular and bold weights,
slanted variants and a choice of four different styles for zero.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from newtxtt:
Map newtxtt.map
TL_DROPIN_EOF
