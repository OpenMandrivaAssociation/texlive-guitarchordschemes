# revision 31524
# category Package
# catalog-ctan /macros/latex/contrib/guitarchordschemes
# catalog-date 2013-08-25 22:09:38 +0200
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-guitarchordschemes
Version:	0.4
Release:	7
Summary:	Guitar Chord and Scale Tablatures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/guitarchordschemes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides two commands (\chordscheme and \scales).
With those commands it is possible to draw schematic diagrams
of guitar chord tablatures and scale tablatures. Both commands
know a range of options that allow wide customization of the
output. The package's drawing is done with the help of TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/guitarchordschemes/guitarchordschemes.sty
%doc %{_texmfdistdir}/doc/latex/guitarchordschemes/README
%doc %{_texmfdistdir}/doc/latex/guitarchordschemes/guitarchordschemes_en.pdf
%doc %{_texmfdistdir}/doc/latex/guitarchordschemes/guitarchordschemes_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
