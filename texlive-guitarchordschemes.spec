Name:		texlive-guitarchordschemes
Version:	54512
Release:	2
Summary:	Guitar Chord and Scale Tablatures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/guitarchordschemes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitarchordschemes.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
