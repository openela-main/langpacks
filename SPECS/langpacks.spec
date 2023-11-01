Name:      langpacks
Version:   1.0
Release:   12%{?dist}
Summary:   Langpacks meta-package

License:   GPLv2+
BuildArch: noarch
Source0:   https://people.freedesktop.org/~hughsient/temp/org.fedoraproject.LangPacks.xml

# to split up the AppStream file
BuildRequires: libappstream-glib >= 0.5.10

%description
Langpack meta-package to provide individual langpacks packages.

# mk_pkg (langcode langname)
# we are using macro to auto-generate subpackages which is
# defined below with %%define so no %%global here
%define mk_pkg() \
%package -n %{name}-%1\
Summary: %{?2:%(echo %* | sed -e "s/%1 //")} langpacks meta-package\
\
%description -n %{name}-%1\
This package provides %{?2:%(echo %* | sed -e "s/%1 //")} langpacks meta-package.\
\
%files -n %{name}-%1 \
%{_datadir}/metainfo/org.fedoraproject.LangPack-%1.metainfo.xml

# The following language list is generated based on
# 1) take the languages where anaconda translations are available
# ls /usr/share/locale/*/LC_MESSAGES/anaconda.mo
# Then pick those languages which provides at least a single langpack
# 2) Added br ga he nn nr ss tn ts ve xh
# as per requested in https://bugzilla.redhat.com/show_bug.cgi?id=1310538
# 3) Enabled en langpack https://bugzilla.redhat.com/show_bug.cgi?id=1312890

%mk_pkg af Afrikaans
%mk_pkg am Amharic
%mk_pkg ar Arabic
%mk_pkg as Assamese
%mk_pkg ast Asturian
%mk_pkg be Belarusian
%mk_pkg bg Bulgarian
%mk_pkg bn Bengali
%mk_pkg br Breton
%mk_pkg bs Bosnian
%mk_pkg ca Catalan
%mk_pkg cs Czech
%mk_pkg cy Welsh
%mk_pkg da Danish
%mk_pkg de German
%mk_pkg el Greek
%mk_pkg en English
%mk_pkg en_GB English \(United Kingdom\)
%mk_pkg es Spanish
%mk_pkg et Estonian
%mk_pkg eu Basque
%mk_pkg fa Persian
%mk_pkg fi Finnish
%mk_pkg fr French
%mk_pkg ga Irish
%mk_pkg gl Galician
%mk_pkg gu Gujarati
%mk_pkg he Hebrew
%mk_pkg hi Hindi
%mk_pkg hr Croatian
%mk_pkg hu Hungarian
%mk_pkg ia Interlingua
%mk_pkg id Indonesian
%mk_pkg is Icelandic
%mk_pkg it Italian
%mk_pkg ja Japanese
%mk_pkg kk Kazakh
%mk_pkg kn Kannada
%mk_pkg ko Korean
%mk_pkg lt Lithuanian
%mk_pkg lv Latvian
%mk_pkg mai Maithili
%mk_pkg mk Macedonian
%mk_pkg ml Malayalam
%mk_pkg mr Marathi
%mk_pkg ms Malay
%mk_pkg nb Norwegian Bokmål
%mk_pkg ne Nepali
%mk_pkg nl Dutch
%mk_pkg nn Nynorsk
%mk_pkg nr Southern Ndebele
%mk_pkg nso Northern Sotho
%mk_pkg or Oriya
%mk_pkg pa Punjabi
%mk_pkg pl Polish
%mk_pkg pt Portuguese
%mk_pkg pt_BR Portuguese \(Brazil\)
%mk_pkg ro Romanian
%mk_pkg ru Russian
%mk_pkg si Sinhala
%mk_pkg sk Slovak
%mk_pkg sl Slovenian
%mk_pkg sq Albanian
%mk_pkg ss Swati
%mk_pkg sr Serbian
%mk_pkg sv Swedish
%mk_pkg ta Tamil
%mk_pkg te Telugu
%mk_pkg th Thai
%mk_pkg tn Tswana
%mk_pkg tr Turkish
%mk_pkg ts Tsonga
%mk_pkg uk Ukrainian
%mk_pkg ur Urdu
%mk_pkg ve Venda
%mk_pkg vi Vietnamese
%mk_pkg xh Xhosa
%mk_pkg zh_CN Simplified Chinese
%mk_pkg zh_TW Traditional Chinese
%mk_pkg zu Zulu

%prep
# nothing to prep

%build
# nothing to build

%install
# Explode the metainfo files into the subpackages so they get added to the
# distro-specific AppStream metadata
mkdir -p %{buildroot}/usr/share/metainfo
DESTDIR=%{buildroot} appstream-util split-appstream %{SOURCE0}

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.0-11
- Added description in appdata metainfo files (rh#1538105)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Richard Hughes <richard@hughsie.com> - 1.0-8
- Use a specific AppStream component type of localization.

* Mon Feb 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-7
- Resolves:rh#1312890: langpacks-en should be added

* Fri Feb 26 2016 Richard Hughes <richard@hughsie.com> - 1.0-6
- Explode the metainfo files into the subpackages so they get added to the
  distro-specific AppStream metadata.
- This allows us to add and remove languages in GNOME Software.

* Tue Feb 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-5
- Resolves:rh#1310538: Added br ga he nn nr ss tn ts ve xh languages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-3
- Removed %%files to disable langpacks.noarch package

* Tue Jan 26 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-2
- Changed metapackage -> meta-package
- Added information about how we chose language list

* Thu Jan 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-1
- Initial packaging

