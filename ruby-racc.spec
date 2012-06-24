Summary:	Ruby yACC
Summary(pl):	yACC dla j�zyka Ruby
Name:		ruby-Racc
Version:	1.4.5
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://i.loveruby.net/archive/racc/racc-%{version}-all.tar.gz
# Source0-md5:	c23ee98abe79f051243adf04d4a82900
URL:		http://i.loveruby.net/en/racc.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Obsoletes:	ruby-racc
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RACC is a Ruby clone of YACC, to generate LALR(1) parsers in Ruby.

%description -l pl
RACC to klon YACC-a dla j�zyka Ruby, s�u��cy do generowania
analizator�w LALR(1) w Rubym.

%prep
%setup -q -n racc-%{version}-all

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
%{ruby_rubylibdir}/racc
