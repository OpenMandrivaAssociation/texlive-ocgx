Name:		texlive-ocgx
Version:	54512
Release:	2
Summary:	Use OCGs within a PDF document without JavaScript
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ocgx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the ocg package, which allows you to create
OCGs (Optional Content Groups) in PDF documents. (The ocg
package is distributed as part of Asymptote.) Every OCG
includes TeX material into a layer of the PDF file. Each of
these layers can be displayed or not. Links can enable or
disable the display of OCGs. The ocgx package does not use
Javascript embedded in the PDF document to enable (to show) or
disable (to hide) OCGs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ocgx/ocgx.sty
%{_texmfdistdir}/tex/latex/ocgx/tikzlibraryocgx.code.tex
%doc %{_texmfdistdir}/doc/latex/ocgx/README
%doc %{_texmfdistdir}/doc/latex/ocgx/demo-ocgx.pdf
%doc %{_texmfdistdir}/doc/latex/ocgx/ocgx-manual-en.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ocgx/demo-ocgx.tex
%doc %{_texmfdistdir}/source/latex/ocgx/ocgx-example-1.tex
%doc %{_texmfdistdir}/source/latex/ocgx/ocgx-manual-en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
