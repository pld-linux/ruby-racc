%define pkgname racc
Summary:	Ruby yACC
Summary(pl.UTF-8):	yACC dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.4.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c61adac8cd59877e6abe37f5fc12e9a5
URL:		http://i.loveruby.net/en/racc.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Provides:	ruby-Racc
Obsoletes:	ruby-Racc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RACC is a Ruby clone of YACC, to generate LALR(1) parsers in Ruby.

%description -l pl.UTF-8
RACC to klon YACC-a dla języka Ruby, służący do generowania
analizatorów LALR(1) w Rubym.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer ChangeLog -o -print | xargs touch --reference %{SOURCE0}

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{ruby_rubylibdir}/racc/parser.rb
rm -f $RPM_BUILD_ROOT%{ruby_archdir}/racc/cparse.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/racc.rb
%{ruby_rubylibdir}/racc
