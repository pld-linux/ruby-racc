%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby yACC
Name:		ruby-racc
Version:	1.4.4
Release:	1
License:	GPL
Source0:		http://i.loveruby.net/archive/racc/racc-%{version}-all.tar.gz
# Source0-md5:	4a7453b056bf71dc55899607316a56fb
Group:		Development/Libraries
URL: http://i.loveruby.net/en/racc.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ruby

%description
RACC is a Ruby clone of YACC, to generate LALR(1) parsers in Ruby.

%prep
%setup -q -n racc-%{version}-all

%build
ruby setup.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ruby_rubylibdir}
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

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
%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT
