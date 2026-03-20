%define pkgname racc
Summary:	Ruby yACC
Summary(pl.UTF-8):	yACC dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.8.1
Release:	1
License:	Ruby or BSD-2-Clause
Group:		Development/Libraries
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	53c37a31570fccd3fdfcf12007b987b6
URL:		https://github.com/ruby/racc
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
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
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/racc

%build
%__gem_helper spec

cd ext/racc/cparse
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

cd ../../../
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid ri/cache.ri
rm -rf ri/{Array,Object,String}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}/racc,%{ruby_specdir},%{_bindir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
install -p ext/racc/cparse/cparse.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}/racc
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSDL COPYING ChangeLog README.rdoc TODO
%attr(755,root,root) %{_bindir}/racc
%dir %{ruby_vendorarchdir}/racc
%attr(755,root,root) %{ruby_vendorarchdir}/racc/cparse.so
%{ruby_vendorlibdir}/racc.rb
%{ruby_vendorlibdir}/racc
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Racc
