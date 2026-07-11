%global tl_name guitarchordschemes
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Guitar Chord and Scale Tablatures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/guitarchordschemes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides two commands (\chordscheme and \scales). With
those commands it is possible to draw schematic diagrams of guitar chord
tablatures and scale tablatures. Both commands know a range of options
that allow wide customization of the output. The package's drawing is
done with the help of TikZ.

