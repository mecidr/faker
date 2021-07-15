from .. import Provider as PersonProvider


def translit(text):
    translit_dict = {
        'Ə': 'E', 'I': 'I', 'Ü': 'U', 'Ş': 'SH', 'Ç': 'CH', 'Ğ': 'G', 'Ö': 'O',
        'ə': 'e', 'ı': 'i', 'ü': 'u', 'ş': 's', 'ç': 'c', 'ğ': 'g', 'ö': 'o',
    }
    for letter in text:
        if letter.isalpha():
            text = text.replace(letter, translit_dict[letter])
    return text


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name_female}}',
        '{{first_name_female}} {{first_name_male}}',
        '{{first_name_female}} {{last_name_unisex}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name_male}}',
        '{{first_name_male}} {{first_name_male}}',
        '{{first_name_male}} {{last_name_unisex}}',
    )

    formats = formats_male + formats_female

    first_names_female = ('Adilə',
                          'Afaq',
                          'Afət',
                          'Ağca',
                          'Aidə',
                          'Akifə',
                          'Aliyə',
                          'Almaz',
                          'Arifə',
                          'Arzu',
                          'Asilə',
                          'Aybəniz',
                          'Ayan',
                          'Ayçiçək',
                          'Aydan',
                          'Aygül',
                          'Aygün',
                          'Ayla',
                          'Aynur',
                          'Aynurə',
                          'Aysu',
                          'Aysel',
                          'Aytən',
                          'Aytəkin',
                          'Balaxanım',
                          'Bənövşə',
                          'Brilyant',
                          'Cahan',
                          'Ceyran',
                          'Ceyhunə',
                          'Ceyla',
                          'Cəmalə',
                          'Cəmilə',
                          'Çimnaz',
                          'Çinarə',
                          'Çiçək',
                          'Dilarə',
                          'Dilşad',
                          'Dünya',
                          'Durna',
                          'Dürdanə',
                          'Dürnisə',
                          'Elmira',
                          'Elnarə',
                          'Elnurə',
                          'Esmira',
                          'Əcəbnaz',
                          'Ədibə',
                          'Əminə',
                          'Əntiqə',
                          'Əsmər',
                          'Familə',
                          'Fatimə',
                          'Fatihə',
                          'Fatma',
                          'Fəridə',
                          'Fərqanə',
                          'Fəxriyyə',
                          'Fidan',
                          'Fimar',
                          'Firəngiz',
                          'Firuzə',
                          'Fizzə',
                          'Flora',
                          'Gülarə',
                          'Gülay',
                          'Gülər',
                          'Güllər',
                          'Gülçöhrə',
                          'Gülçin',
                          'Gülnar',
                          'Gülnarə',
                          'Gülnaz',
                          'Gülnur',
                          'Gülmira',
                          'Gültac',
                          'Gülşən',
                          'Gülsüm',
                          'Gültəkin',
                          'Gülüstan',
                          'Gülüş',
                          'Gülxar',
                          'Gülzar',
                          'Günay',
                          'Həcər',
                          'Hicran',
                          'Hökümə',
                          'Hüsniyyə',
                          'İlhamə',
                          'İlkanə',
                          'İlqarə',
                          'İlnarə',
                          'İlahə',
                          'İnarə',
                          'İnayət',
                          'İntizar',
                          'İradə',
                          'Jalə',
                          'Kamilə',
                          'Kəmalə',
                          'Kifayət',
                          'Könül',
                          'Kövsər',
                          'Laçın',
                          'Lamiyə',
                          'Lalə',
                          'Laləzar',
                          'Leyla',
                          'Leyli',
                          'Ləman',
                          'Lətifə',
                          'Lətafət',
                          'Lütfiyyə',
                          'Mahirə',
                          'Mahizər',
                          'Maisə',
                          'Mehbarə',
                          'Mehin',
                          'Meyransa',
                          'Mədinə',
                          'Məhru',
                          'Məlahət',
                          'Məleykə',
                          'Mənsurə',
                          'Məryəm',
                          'Mərziyyə',
                          'Məsmə',
                          'Mətanət',
                          'Minurə',
                          'Münəvvər',
                          'Müşkünaz',
                          'Mülayim',
                          'Nahidə',
                          'Narıngül',
                          'Naibə',
                          'Nailə',
                          'Nanə',
                          'Natella',
                          'Natəvan',
                          'Nazilə',
                          'Nazimə',
                          'Nazlı',
                          'Nəfisə',
                          'Nərgiz',
                          'Nərmin',
                          'Nərminə',
                          'Nəzakət',
                          'Nəzrin',
                          'Nigar',
                          'Nihal',
                          'Nisə',
                          'Növrəstə',
                          'Nurlana',
                          'Nuranə',
                          'Nübar',
                          'Nüşabə',
                          'Ofeliya',
                          'Pakizə',
                          'Pərvanə',
                          'Pərvinə',
                          'Pəri',
                          'Pərişan',
                          'Qaratel',
                          'Qənirə',
                          'Qızbəs',
                          'Qönçə',
                          'Qumru',
                          'Raifə',
                          'Ramilə',
                          'Rasimə',
                          'Raziyə',
                          'Reyhan',
                          'Reyhanə',
                          'Rəfiqə',
                          'Rəhilə',
                          'Rəmziyyə',
                          'Rəna',
                          'Rəqsanə',
                          'Rəsmiyyə',
                          'Rəxşəndə',
                          'Roza',
                          'Rövşanə',
                          'Röya',
                          'Röyal',
                          'Röyalə',
                          'Ruhəngiz',
                          'Ruhiyyə',
                          'Ruqiyyə',
                          'Ruxsarə',
                          'Rübeyda',
                          'Rübabə',
                          'Sabirə',
                          'Sacidə',
                          'Sahibə',
                          'Samirə',
                          'Sayalı',
                          'Sara',
                          'Selcan',
                          'Sevil',
                          'Sevinc',
                          'Seyran',
                          'Səadət',
                          'Səbinə',
                          'Səbirə',
                          'Sədaqət',
                          'Səfurə',
                          'Səhər',
                          'Səidə',
                          'Səlimə',
                          'Səmayə',
                          'Səma',
                          'Sənubər',
                          'Səriyyə',
                          'Sidiqə',
                          'Sima',
                          'Simuzər',
                          'Sitarə',
                          'Solmaz',
                          'Sona',
                          'Suğra',
                          'Sürəyya',
                          'Südabə',
                          'Şahnaz',
                          'Şeyda',
                          'Şəfa',
                          'Şəfiqə',
                          'Şəhrəbanu',
                          'Şəmsiyyə',
                          'Şəlalə',
                          'Şəhla',
                          'Şərafət',
                          'Şükufə',
                          'Şövkət',
                          'Tamara',
                          'Tamilla',
                          'Tamaşa',
                          'Təhminə',
                          'Təranə',
                          'Tovuz',
                          'Tomris',
                          'Turan',
                          'Turanə',
                          'Tutu',
                          'Tükəzban',
                          'Tünzalə',
                          'Türkan',
                          'Türkanə',
                          'Ulduz',
                          'Ülkər',
                          'Ülviyyə',
                          'Vahidə',
                          'Validə',
                          'Vəfa',
                          'Vüsalə',
                          'Xalidə',
                          'Xalisə',
                          'Xanım',
                          'Xatirə',
                          'Xavər',
                          'Xəyalə',
                          'Xumar',
                          'Yasəmən',
                          'Yaqub',
                          'Yazgül',
                          'Yeganə',
                          'Zarəngiz',
                          'Zemfira',
                          'Zeynəb',
                          'Zeynəgül',
                          'Zəhra',
                          'Zəminə',
                          'Zəkəriyyə',
                          'Zərif',
                          'Zərifə',
                          'Zərnigar',
                          'Ziba',
                          'Zibeydə',
                          'Zinət',
                          'Zöhrə',
                          'Züleyxa',
                          'Zülfiyyə',
                          'Zümrüd',
                          )

    first_names_male = ('Adil',
                        'Adnan',
                        'Afiq',
                        'Afil',
                        'Ağa',
                        'Ağahadi',
                        'Ağaxan',
                        'Ağamalı',
                        'Ağamusa',
                        'Ağasəfa',
                        'Akif',
                        'Aqil',
                        'Allahverdi',
                        'Anar',
                        'Arif',
                        'Asif',
                        'Asəf',
                        'Asiman',
                        'Aslan',
                        'Atabala',
                        'Atamoğlan',
                        'Aydın',
                        'Azad',
                        'Azər',
                        'Baba',
                        'Bahadır',
                        'Bayram',
                        'Behbud ',
                        'Bəhlul',
                        'Bəhram',
                        'Bəhruz',
                        'Bəkir',
                        'Bəşir',
                        'Bilal',
                        'Cabbar',
                        'Cahangir',
                        'Cavad',
                        'Cavid',
                        'Ceyhun',
                        'Cəlal',
                        'Cəlil',
                        'Cəmil',
                        'Coşqun',
                        'Cümşüd',
                        'Çingiz',
                        'Dadaş ',
                        'Dilavər',
                        'Dönməz',
                        'Dünyamalı',
                        'Elvin',
                        'Elariz',
                        'Elçin',
                        'Eldar',
                        'Eldəniz',
                        'Elgün',
                        'Elman',
                        'Elmir',
                        'Elmidar',
                        'Elmar',
                        'Elməddin',
                        'Elnur',
                        'Elton',
                        'Elturan',
                        'Elsevər',
                        'Elxan',
                        'Elşən',
                        'Elşad',
                        'Emin',
                        'Emil',
                        'Etibar',
                        'Etiqad',
                        'Eyyub',
                        'Əbdül',
                        'Ədalət',
                        'Əflatun',
                        'Əhməd',
                        'Əhliman',
                        'Əhəd',
                        'Əkbər',
                        'Ələkbər',
                        'Ələsgər',
                        'Əli',
                        'Əliəkrəm',
                        'Əliş',
                        'Əmin',
                        'Əmir',
                        'Ənvər',
                        'Əkrəm',
                        'Ərtoğrul',
                        'Əsgər',
                        'Əşrəf',
                        'Əyyub',
                        'Əjdər',
                        'Faiq',
                        'Famil ',
                        'Fazil',
                        'Fariz',
                        'Fərhad',
                        'Fərid',
                        'Fərda',
                        'Fərman',
                        'Fəxri',
                        'Fəxrəddin',
                        'Fəyyaz',
                        'Fərrux',
                        'Fərahim',
                        'Fimar',
                        'Fikrət',
                        'Firudin',
                        'Firdovsi',
                        'Fəhmin',
                        'Fəzail',
                        'Fuad ',
                        'Füzuli',
                        'Gəray',
                        'Gülağa',
                        'Gülbala',
                        'Gündüz',
                        'Habil',
                        'Hafiz',
                        'Hakim',
                        'Hacıbəy',
                        'Heydər',
                        'Həci',
                        'Həmid',
                        'Həsən',
                        'Həsənağa',
                        'Həzi',
                        'Hikmət',
                        'Hilal',
                        'Hümbət',
                        'Hüseyn',
                        'Hüseynqulu',
                        'İbiş',
                        'İbrahim',
                        'İlham',
                        'İlkin',
                        'İlqar',
                        'İlyas',
                        'İmam',
                        'İmran',
                        'İnqilab',
                        'İntiqam',
                        'İsa',
                        'İsgəndər',
                        'İslam',
                        'İsmayıl',
                        'İsmət',
                        'İsrafil',
                        'İxtiyar',
                        'İzzət',
                        'Kamal',
                        'Kamil',
                        'Kamran',
                        'Kazım',
                        'Kəmaləddin',
                        'Kənan',
                        'Kərim',
                        'Kəramət',
                        'Laçın',
                        'Lazım',
                        'Lətif',
                        'Mahir',
                        'Mahmud',
                        'Maqsud',
                        'Manaf',
                        'Mehdi',
                        'Mehdiqulu',
                        'Mehman',
                        'Məhəmməd',
                        'Məhərrəm',
                        'Məmməd',
                        'Mənsur',
                        'Mikayıl',
                        'Mirəli',
                        'Mirzə',
                        'Musa',
                        'Murad',
                        'Muxtar',
                        'Mübariz',
                        'Mümtaz',
                        'Münəvvər',
                        'Müntəzir',
                        'Mürsəl',
                        'Müslüm',
                        'Müzəffər',
                        'Nadir',
                        'Nağı',
                        'Namiq',
                        'Natiq',
                        'Nazim',
                        'Nazir',
                        'Nakif',
                        'Nəcəf',
                        'Nəriman',
                        'Nəsib',
                        'Nəsimi',
                        'Nicat',
                        'Nihal',
                        'Nihad',
                        'Niyaz',
                        'Niyazi',
                        'Novruz',
                        'Nurşən',
                        'Nurlan',
                        'Nuru',
                        'Nurulla',
                        'Nurşərəf ',
                        'Nuşirəvan',
                        'Nürəddin',
                        'Nüsrət',
                        'Oqtay',
                        'Orxan',
                        'Orduxan',
                        'Osman',
                        'Paşa',
                        'Pərvin',
                        'Pərviz',
                        'Polad',
                        'Pünhan',
                        'Qabil',
                        'Qadir',
                        'Qalib',
                        'Qasım',
                        'Qələndər',
                        'Qədir',
                        'Qəşəm ',
                        'Qəzənfər',
                        'Qiyas',
                        'Qoşqar',
                        'Qulam',
                        'Qulu',
                        'Qüdrət',
                        'Rafael',
                        'Rafiq',
                        'Ramil',
                        'Ramid',
                        'Ramiz ',
                        'Rasim',
                        'Razi',
                        'Rəis',
                        'Rəsul',
                        'Rəşad',
                        'Rəşid',
                        'Riyad',
                        'Rizvan',
                        'Roman',
                        'Rövşən',
                        'Ruslan',
                        'Rüfət',
                        'Rza',
                        'Sabir',
                        'Sadıq',
                        'Sadiq',
                        'Saleh',
                        'Salman ',
                        'Samir',
                        'Sarvan',
                        'Seyfulla',
                        'Seyfəddin',
                        'Seymur',
                        'Seyran',
                        'Səbuhi',
                        'Sədaqət',
                        'Səfər',
                        'Səlahəddin',
                        'Səlim',
                        'Səməd',
                        'Sənan',
                        'Sərəncam',
                        'Sərvər ',
                        'Sərxan',
                        'Səxavət',
                        'Sirac',
                        'Sübhan',
                        'Süleyman',
                        'Sücəddin',
                        'Şahin ',
                        'Şamil',
                        'Şamxal',
                        'Şahvələd',
                        'Şahlar',
                        'Şahmar',
                        'Şakir',
                        'Şaban',
                        'Şərəfəddin',
                        'Şirin',
                        'Şirzad',
                        'Şıxı',
                        'Şükür',
                        'Tahir ',
                        'Talıb',
                        'Tariyel',
                        'Teymur',
                        'Teymuraz',
                        'Teymurçin',
                        'Telman',
                        'Tərlan',
                        'Tofiq',
                        'Toğrul',
                        'Tunar',
                        'Tural',
                        'Turan',
                        'Turxan',
                        'Urfan',
                        'Uğur',
                        'Ülfət',
                        'Ülvi',
                        'Ümid',
                        'Üzeyir',
                        'Vahid',
                        'Vaqif ',
                        'Valeh',
                        'Valid',
                        'Vasif',
                        'Vazeh',
                        'Vidadi',
                        'Vilayət',
                        'Veysəl',
                        'Vəfadar',
                        'Vəli',
                        'Vurğun',
                        'Vüqar',
                        'Vüsal',
                        'Xamis',
                        'Xalid',
                        'Xaləddin',
                        'Xaliq',
                        'Xankişi',
                        'Xanlar',
                        'Xəlil',
                        'Xəyyam',
                        'Xəyal',
                        'Xudu',
                        'Xudayar',
                        'Xudaverdi',
                        'Xosrov',
                        'Yadigar',
                        'Yamən',
                        'Yasin',
                        'Yaşar',
                        'Yalçın',
                        'Yaqub',
                        'Yavər',
                        'Yasəf',
                        'Yəhya',
                        'Yunis',
                        'Yusif',
                        'Zakir',
                        'Zaman',
                        'Zamin',
                        'Zamiq',
                        'Zamir',
                        'Zahid',
                        'Zahir',
                        'Zaur',
                        'Zeynal',
                        'Zeynulla',
                        'Zərdüşt',
                        'Ziya',
                        )

    first_names = first_names_male + first_names_female

    last_names_male = ['Əlibəyov', 'Məhərrəmoğlu', 'Əlləzoğlu', 'Şükürov', 'Arifcanov', 'Qurbanov', 'Əlioğlu',
                       'Nərimanov', 'Kərimov', 'Bağırov', 'Hüseynoğlu', 'İbrahimbəyov', 'Atakişioğlu', 'Camalov',
                       'Şamiloğlu', 'Rəhimov', 'Vəzirov', 'Cəbrayılov', 'Tapdıqoğlu', 'Hümmətov', 'İldırımoğlu',
                       'Xəlilov', 'Əmirov', 'Eminov', 'Mahmudov', 'Qabiloğlu', 'Bəşiroğlu', 'Talıbov', 'Süleymanov',
                       'Ağaoğlu', 'Axundov', 'Musabəyov', 'Əhmədov', 'Orucov', 'Vəlixanov', 'Hacıbəyov', 'Pənahov',
                       'Şamilov', 'Cəfəroğlu', 'İbrahimoğlu', 'Vəziroğlu', 'Gözəlov', 'Hüseynov', 'Yusifoğlu',
                       'Nəbioğlu', 'Həsənov', 'Fikrətoğlu', 'Xakimov', 'Sadıxov', 'İdrisoğlu', 'Salamoğlu', 'Yaqubov',
                       'Sadiqov', 'Əsgəroğlu', 'Bayramov', 'Qasımov', 'Vəlioğlu', 'Sultanov', 'Vilayətoğlu',
                       'Abdullaoğlu', 'Muxtaroğlu', 'Bakıxanov', 'Nağıoğlu', 'Mirələmov', 'Ədiloğlu', 'Məcnunbəyov',
                       'Mirəhmədov', 'Qafarov', 'Səmədoğlu', 'Abbasov', 'Sədaqətoğlu', 'Əsgərov', 'Çingizoğlu',
                       'Fərəcov', 'Rövşənov', 'İbrahimov']

    last_names_female = ['Aslanova', 'İsmayılqızı', 'Səlimova', 'İbrahimova', 'Nəzirova', 'Əsgərova', 'Nəsibova',
                         'Şərifova', 'Bağırova', 'Anarqızı', 'Abdullayeva', 'Rəhmanova', 'Babayeva', 'Cəfərova',
                         'Sadıxova', 'Mürvətqızı', 'Kərimova', 'Nəbiqızı', 'Əmirova', 'Əfəndiyeva', 'Mahmudova',
                         'Abbasova', 'Axundova', 'Hüseynova', 'Musabəyova', 'Yusifqızı', 'Nərimanova', 'Əkbərova',
                         'Əliyeva', 'Ağayeva', 'Vəliyeva']

    last_names_unisex = ['Şahbuzlu', 'Tağızadə', 'Əlibəyli', 'Baharlı', 'Talıblı', 'Ələkbərli',
                         'Abdullazadə', 'Çəmənzəminli', 'İmanzadə', 'Nurəli',
                         'Seyidbəyli', 'Şirvanzadə', 'Lətifxanlı', 'Əbdülrəhmanlı', 'Cabbarlı',
                         'Cəfərzadə', 'Süleymanlı', 'Kərimli', 'Abbaszadə', 'Məhərrəmzadə', 'Tapdıqoğlu',
                         'Məmmədquluzadə', 'Nəbibəyli', 'Məmmədxanlı', 'Qənizadə', 'Budaqlı', 'Hacızadə',
                         'Nəsirli', 'Məhərrəmli', 'Əzimzadə', 'Makulu',
                         'Yusifzadə', 'Qutqaşınlı', 'Rzaquluzadə', 'Nəzərli', 'Qurbanlı',
                         'Şeyxzadə', 'Qoşalı', 'Hüseynbəyli', 'Məmmədzadə',
                         'Əhmədli', 'Tahirzadə', 'Əlixanlı', 'Cuvarlı', 'Dağlı', 'Şahsuvarlı',
                         'İsaxanlı', 'Bünyadzadə', 'Həsənzadə', 'Turallı', 'Gəncəli',
                         'Əfəndizadə', 'Məlikzadə', 'Qoçulu', 'Arzulu', 'İbrahimli',
                         'Abbaslı', 'Arazlı', 'Sultanlı', 'Vəziroğlu', 'Musaxanlı', 'Nəbioğlu', 'Qarabağlı', 'İdrisli',
                         'Axundlu', 'Elatlı', 'Salamoğlu', 'Əhmədzadə',
                         'Rəsulzadə', 'Vəfalı', 'Əlizadə', 'Səfərli', 'Hüseynli', 'Məmmədli', 'Əsgərli', 'Uğurlu',
                         'Vəlizadə', 'Şükürlü', 'Şıxlı', 'Muğanlı', 'Eyvazlı', 'Əylisli', 'Qəhrəmanlı', 'Əkbərzadə',
                         'Köçərli', 'Musazadə',
                         'Sədalı', 'Təhmasibli', 'Eyvazalı', 'Kərimzadə', 'Babanlı', 'Veysəlli', 'Dəmirbəyli',
                         'Tapdıqlı', 'Nəzirli',
                         'Rəhimli', 'Seyidzadə', 'Axundzadə', 'İsabəyli', 'Çəmənli', 'Heydərli',
                         'Qədirzadə', 'Hacıbəyli', 'Qafurbəyli', 'Əmirli', 'Ələkbərzadə']
    prefixes_female = ('Xanım',)
    prefixes_male = ('Cənab', 'Bəy', 'Müəllim')

    prefixes = prefixes_female + prefixes_male

    def last_name_male(self):
        return self.random_element(self.last_names_male)

    def last_name_female(self):
        return self.random_element(self.last_names_female)

    def last_name_unisex(self):
        return self.random_element(self.last_names_unisex)
