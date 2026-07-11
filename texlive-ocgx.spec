%global tl_name ocgx
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Use OCGs within a PDF document without JavaScript
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ocgx
License:	lppl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocgx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the ocg package, which allows you to create OCGs
(Optional Content Groups) in PDF documents. (The ocg package is
distributed as part of Asymptote.) Every OCG includes TeX material into
a layer of the PDF file. Each of these layers can be displayed or not.
Links can enable or disable the display of OCGs. The ocgx package does
not use Javascript embedded in the PDF document to enable (to show) or
disable (to hide) OCGs.

