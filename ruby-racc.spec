%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby yACC
Summary(pl):	yACC dla jêzyka Ruby
Name:		ruby-Racc
Version:	1.4.4
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://i.loveruby.net/archive/racc/racc-%{version}-all.tar.gz
# Source0-md5:	4a7453b056bf71dc55899607316a56fb
URL:		http://i.loveruby.net/en/racc.html
BuildRequires:	ruby
Obsoletes:	ruby-racc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RACC is a Ruby clone of YACC, to generate LALR(1) parsers in Ruby.

%description -l pl
RACC to klon YACC-a dla jêzyka Ruby, s³u¿±cy do generowania
analizatorów LALR(1) w Rubym.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{ruby_rubylibdir}/racc
%{ruby_rubylibdir}/racc/compat.rb
%{ruby_rubylibdir}/racc/compiler.rb
%{ruby_rubylibdir}/racc/grammar.rb
%{ruby_rubylibdir}/racc/grammarfilescanner.rb
%{ruby_rubylibdir}/racc/info.rb
%{ruby_rubylibdir}/racc/iset.rb
%{ruby_rubylibdir}/racc/output.rb
%{ruby_rubylibdir}/racc/rubyloader.rb
%{ruby_rubylibdir}/racc/state.rb
%{ruby_rubylibdir}/racc/usercodeparser.rb
%{ruby_rubylibdir}/racc/grammarfileparser.rb
