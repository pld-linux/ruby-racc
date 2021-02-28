%define pkgname racc
Summary:	Ruby yACC
Summary(pl.UTF-8):	yACC dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.4.6
Release:	10
License:	GPL
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c61adac8cd59877e6abe37f5fc12e9a5
URL:		http://i.loveruby.net/en/racc.html
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1-6
Provides:	ruby-Racc
Obsoletes:	ruby-Racc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RACC is a Ruby clone of YACC, to generate LALR(1) parsers in Ruby.

%description -l pl.UTF-8
RACC to klon YACC-a dla języka Ruby, służący do generowania
analizatorów LALR(1) w Rubym.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--site-ruby=%{ruby_vendorlibdir} \
	--so-dir=%{ruby_vendorarchdir}

ruby setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Array,Object,String}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/racc
%attr(755,root,root) %{_bindir}/racc2y
%attr(755,root,root) %{_bindir}/y2racc
%dir %{ruby_vendorarchdir}/racc
%attr(755,root,root) %{ruby_vendorarchdir}/racc/cparse.so
%{ruby_vendorlibdir}/racc.rb
%{ruby_vendorlibdir}/racc

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Racc
