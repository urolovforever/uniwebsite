"""
Seed script for Programs — run with: python manage.py shell < seed_programs.py

Creates:
- StudyType records (kunduzgi, sirtqi, masofaviy)
- Departments (if missing)
- Program records matching the TIU tuition table (50 entries)

Faculty assignment:
- Yurisprudensiya → jurisprudence faculty
- Everything else → business faculty
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiu_project.settings.dev')
django.setup()

from apps.programs.models import Department, Program, StudyType


STUDY_TYPES = [
    {'slug': 'kunduzgi', 'name': 'Full-time', 'name_uz': 'Kunduzgi', 'name_ru': 'Очное'},
    {'slug': 'sirtqi', 'name': 'Part-time', 'name_uz': 'Sirtqi', 'name_ru': 'Заочное'},
    {'slug': 'masofaviy', 'name': 'Distance', 'name_uz': 'Masofaviy', 'name_ru': 'Дистанционное'},
]
study_types = {}
for st in STUDY_TYPES:
    obj, _ = StudyType.objects.update_or_create(slug=st['slug'], defaults=st)
    study_types[st['slug']] = obj
print(f"✓ Study Types ({len(study_types)})")


DEPARTMENTS = [
    {'slug': 'jurisprudence', 'name': 'Jurisprudence', 'name_uz': 'Yurisprudensiya',
     'name_ru': 'Юриспруденция', 'faculty': 'jurisprudence',
     'excerpt': 'Department of Law and Legal Studies',
     'excerpt_uz': 'Huquq va huquqshunoslik kafedrasi', 'order': 1},
    {'slug': 'business-economics', 'name': 'Business and Economics',
     'name_uz': 'Biznes va iqtisodiyot', 'name_ru': 'Бизнес и экономика',
     'faculty': 'business', 'excerpt': 'Department of Business, Finance, and Economics',
     'excerpt_uz': 'Biznes, moliya va iqtisodiyot kafedrasi', 'order': 2},
    {'slug': 'information-technology', 'name': 'Information Technology',
     'name_uz': 'Axborot texnologiyalari', 'name_ru': 'Информационные технологии',
     'faculty': 'business', 'excerpt': 'Department of IT and Computer Science',
     'excerpt_uz': 'IT va kompyuter fanlari kafedrasi', 'order': 3},
    {'slug': 'education-pedagogy', 'name': 'Education and Pedagogy',
     'name_uz': "Ta'lim va pedagogika", 'name_ru': 'Образование и педагогика',
     'faculty': 'business', 'excerpt': 'Department of Education and Teaching',
     'excerpt_uz': "Ta'lim va o'qitish kafedrasi", 'order': 4},
    {'slug': 'foreign-languages', 'name': 'Foreign Languages and Literature',
     'name_uz': 'Chet tillari va adabiyot', 'name_ru': 'Иностранные языки и литература',
     'faculty': 'business', 'excerpt': 'Department of Languages, Translation, and Literature',
     'excerpt_uz': 'Tillar, tarjima va adabiyot kafedrasi', 'order': 5},
]
depts = {}
for d in DEPARTMENTS:
    obj, _ = Department.objects.update_or_create(slug=d['slug'], defaults=d)
    depts[d['slug']] = obj
print(f"✓ Departments ({len(depts)})")


BASES = {
    'preschool': {
        'title': 'Pre-school Education', 'title_uz': "Maktabgacha ta'lim",
        'title_ru': 'Дошкольное образование', 'dept': 'education-pedagogy',
        'desc_uz': "Bolalar bog'chalari va maktabgacha ta'lim muassasalarida faoliyat olib boradigan malakali pedagog-murabbiylar tayyorlash. Bolalar rivojlanishi, o'yin pedagogikasi va ijodiy faoliyatni tashkil etish kompetensiyalari shakllantiriladi.",
        'desc_en': "Prepares qualified educators for kindergartens and preschool institutions. Builds competencies in child development, play-based pedagogy, and creative activity design.",
    },
    'primary': {
        'title': 'Primary Education', 'title_uz': "Boshlang'ich ta'lim",
        'title_ru': 'Начальное образование', 'dept': 'education-pedagogy',
        'desc_uz': "Boshlang'ich sinf o'qituvchilarini zamonaviy o'qitish metodikalari, bolalar psixologiyasi va amaliy pedagogika asosida tayyorlash dasturi.",
        'desc_en': "Training primary school teachers in modern teaching methodologies, child psychology, and practical pedagogy.",
    },
    'psychology': {
        'title': 'Psychology', 'title_uz': 'Psixologiya', 'title_ru': 'Психология',
        'dept': 'education-pedagogy',
        'desc_uz': "Insoniy xulq-atvor, shaxsiyat va aqliy jarayonlarni tadqiq qiluvchi amaliy va nazariy psixologiya dasturi. Maslahatchilik, tashkiliy va klinik psixologiya yo'nalishlari.",
        'desc_en': "Applied and theoretical psychology exploring human behavior, personality, and cognition. Tracks in counselling, organizational, and clinical psychology.",
    },
    'english-philology': {
        'title': 'Foreign Languages and Literature: English',
        'title_uz': "Xorijiy til va adabiyoti: ingliz tili",
        'title_ru': 'Иностранные языки и литература: английский',
        'dept': 'foreign-languages',
        'desc_uz': "Ingliz tili va adabiyoti, tarjimashunoslik va til pedagogikasiga chuqur yondashuv. CEFR C1+ darajasigacha til malakasini rivojlantirish.",
        'desc_en': "In-depth study of English language and literature, translation, and language pedagogy. Develops language proficiency to CEFR C1+ level.",
    },
    'korean-philology': {
        'title': 'Philology and Language Teaching: Korean',
        'title_uz': "Filologiya va tillarni o'qitish: koreys tili",
        'title_ru': 'Филология и преподавание языков: корейский',
        'dept': 'foreign-languages',
        'desc_uz': "Koreys tili, adabiyoti va madaniyati bo'yicha mutaxassislar tayyorlash. TOPIK imtihoniga tayyorgarlik va Koreya-O'zbekiston aloqalari yo'nalishida amaliyot.",
        'desc_en': "Training specialists in Korean language, literature, and culture. TOPIK exam preparation and practice in Korea-Uzbekistan relations.",
    },
    'economics': {
        'title': 'Economics', 'title_uz': 'Iqtisodiyot', 'title_ru': 'Экономика',
        'dept': 'business-economics',
        'desc_uz': "Mikro- va makroiqtisodiyot, ekonometrika va iqtisodiy siyosat asosida iqtisodchi-tahlilchilar tayyorlash. Zamonaviy raqamli tahlil vositalari bilan ishlash.",
        'desc_en': "Training economist-analysts grounded in micro/macroeconomics, econometrics, and economic policy. Hands-on work with modern digital analysis tools.",
    },
    'finance': {
        'title': 'Finance and Financial Technologies',
        'title_uz': 'Moliya va moliyaviy texnologiyalar',
        'title_ru': 'Финансы и финансовые технологии',
        'dept': 'business-economics',
        'desc_uz': "Moliya bozorlari, korporativ moliya va FinTech yo'nalishlari bo'yicha keng qamrovli ta'lim. Blokcheyn, raqamli to'lovlar va moliyaviy modellashtirish.",
        'desc_en': "Comprehensive education in financial markets, corporate finance, and FinTech. Covers blockchain, digital payments, and financial modeling.",
    },
    'management': {
        'title': 'Management', 'title_uz': 'Menejment', 'title_ru': 'Менеджмент',
        'dept': 'business-economics',
        'desc_uz': "Zamonaviy boshqaruv, strategiya va tashkilot rahbarligi ko'nikmalarini shakllantirish. Biznes-keys yondashuvi va amaliy loyihalar.",
        'desc_en': "Building modern management, strategy, and organizational leadership skills. Case-based approach with applied projects.",
    },
    'marketing': {
        'title': 'Marketing (by sectors and industries)',
        'title_uz': "Marketing (tarmoqlar va sohalar bo'yicha)",
        'title_ru': 'Маркетинг (по отраслям)',
        'dept': 'business-economics',
        'desc_uz': "Raqamli marketing, brend menejmenti va sohalar bo'yicha marketing strategiyalari. SMM, SEO va marketing analitikasi.",
        'desc_en': "Digital marketing, brand management, and industry-specific strategies. SMM, SEO, and marketing analytics.",
    },
    'accounting': {
        'title': 'Accounting', 'title_uz': 'Buxgalteriya hisobi',
        'title_ru': 'Бухгалтерский учёт', 'dept': 'business-economics',
        'desc_uz': "Moliyaviy hisobot, audit va xalqaro buxgalteriya standartlari (IFRS) bo'yicha professional tayyorlov. ACCA qo'shimcha sertifikatlariga tayyorgarlik.",
        'desc_en': "Professional training in financial reporting, auditing, and IFRS standards. Preparation for ACCA certifications.",
    },
    'banking': {
        'title': 'Banking', 'title_uz': 'Bank ishi', 'title_ru': 'Банковское дело',
        'dept': 'business-economics',
        'desc_uz': "Bank tizimi, kredit siyosati va moliyaviy xizmatlar bo'yicha mutaxassislar tayyorlash. Markaziy bank regulyatsiyasi va risk menejmenti.",
        'desc_en': "Training specialists in banking systems, credit policy, and financial services. Central bank regulation and risk management.",
    },
    'world-economy': {
        'title': 'World Economy and International Economic Relations',
        'title_uz': 'Jahon iqtisodiyoti va XIM',
        'title_ru': 'Мировая экономика и МЭО',
        'dept': 'business-economics',
        'desc_uz': "Xalqaro savdo, iqtisodiy integratsiya va global iqtisodiy munosabatlarni o'rganish. WTO, mintaqaviy birlashmalar va valyuta siyosati.",
        'desc_en': "Studying international trade, economic integration, and global economic relations. WTO, regional unions, and currency policy.",
    },
    'info-systems': {
        'title': 'Information Systems and Technologies',
        'title_uz': 'Axborot tizimlari va texnologiyalari',
        'title_ru': 'Информационные системы и технологии',
        'dept': 'information-technology',
        'desc_uz': "Korporativ axborot tizimlari, ma'lumotlar bazasi boshqaruvi va biznes-analitika yo'nalishi. ERP, CRM va bulut texnologiyalari.",
        'desc_en': "Enterprise information systems, database management, and business analytics. ERP, CRM, and cloud technologies.",
    },
    'cybersecurity': {
        'title': 'Cybersecurity Engineering',
        'title_uz': 'Kiberxavfsizlik injiniringi',
        'title_ru': 'Инженерия кибербезопасности',
        'dept': 'information-technology',
        'desc_uz': "Axborot xavfsizligi, kriptografiya va tarmoq himoyasi mutaxassislarini tayyorlash. Penetration testing, SOC operatsiyalari va incident response.",
        'desc_en': "Training specialists in information security, cryptography, and network defense. Penetration testing, SOC operations, and incident response.",
    },
    'computer-eng': {
        'title': 'Computer Engineering', 'title_uz': 'Kompyuter injiniringi',
        'title_ru': 'Компьютерная инженерия', 'dept': 'information-technology',
        'desc_uz': "Kompyuter tizimlari, mikroprotsessorlar va apparat-dasturiy integratsiya injinerlarini tayyorlash. Embedded systems va IoT yo'nalishi.",
        'desc_en': "Training engineers in computer systems, microprocessors, and hardware-software integration. Embedded systems and IoT track.",
    },
    'software-eng': {
        'title': 'Software Engineering', 'title_uz': 'Dasturiy injiniring',
        'title_ru': 'Программная инженерия', 'dept': 'information-technology',
        'desc_uz': "Zamonaviy dasturlash tillari, dasturiy ta'minot arxitekturasi va DevOps amaliyotlari. Agile metodologiyalari va loyiha boshqaruvi.",
        'desc_en': "Modern programming languages, software architecture, and DevOps practices. Agile methodologies and project management.",
    },
    'law': {
        'title': 'Jurisprudence', 'title_uz': 'Yurisprudensiya',
        'title_ru': 'Юриспруденция', 'dept': 'jurisprudence',
        'desc_uz': "O'zbekiston va xalqaro huquq, sud jarayonlari va korporativ huquq bo'yicha yuristlar tayyorlash. Konstitutsiyaviy, fuqarolik, jinoyat va xalqaro huquq yo'nalishlari.",
        'desc_en': "Training lawyers in Uzbek and international law, litigation, and corporate law. Tracks in constitutional, civil, criminal, and international law.",
    },
    'public-finance': {
        'title': 'Public Finance and International Finance',
        'title_uz': 'Davlat moliyasi va xalqaro moliya',
        'title_ru': 'Государственные финансы и международные финансы',
        'dept': 'business-economics',
        'desc_uz': "Davlat byudjeti, soliq tizimi va xalqaro moliyaviy munosabatlar bo'yicha magistrlik dasturi. Fiskal siyosat va xalqaro moliyaviy institutlar.",
        'desc_en': "Master's program in public budget, taxation, and international financial relations. Fiscal policy and international financial institutions.",
    },
}


# (base_key, study_type_slug, level, language, fee_in_millions)
ROWS = [
    # === KUNDUZGI (daytime, bachelor) ===
    ('preschool',        'kunduzgi', 'bachelor', 'Uzbek',   16),
    ('primary',          'kunduzgi', 'bachelor', 'Uzbek',   16),
    ('psychology',       'kunduzgi', 'bachelor', 'Uzbek',   16),
    ('psychology',       'kunduzgi', 'bachelor', 'Russian', 16),
    ('english-philology','kunduzgi', 'bachelor', 'Uzbek',   19),
    ('english-philology','kunduzgi', 'bachelor', 'Russian', 19),
    ('korean-philology', 'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('economics',        'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('economics',        'kunduzgi', 'bachelor', 'Russian', 19),
    ('economics',        'kunduzgi', 'bachelor', 'English', 25),
    ('finance',          'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('management',       'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('accounting',       'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('banking',          'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('world-economy',    'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('world-economy',    'kunduzgi', 'bachelor', 'Russian', 19),
    ('marketing',        'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('info-systems',     'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('cybersecurity',    'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('cybersecurity',    'kunduzgi', 'bachelor', 'Russian', 19),
    ('cybersecurity',    'kunduzgi', 'bachelor', 'English', 25),
    ('computer-eng',     'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('software-eng',     'kunduzgi', 'bachelor', 'Uzbek',   19),
    ('law',              'kunduzgi', 'bachelor', 'Uzbek',   25),

    # === MAGISTRATURA (master, full-time) ===
    ('economics',        'kunduzgi', 'master',   'Uzbek',   25),
    ('public-finance',   'kunduzgi', 'master',   'Uzbek',   25),

    # === MASOFAVIY (distance, bachelor) ===
    ('preschool',        'masofaviy', 'bachelor', 'Uzbek', 15),
    ('primary',          'masofaviy', 'bachelor', 'Uzbek', 15),
    ('psychology',       'masofaviy', 'bachelor', 'Uzbek', 15),
    ('economics',        'masofaviy', 'bachelor', 'Uzbek', 16),
    ('finance',          'masofaviy', 'bachelor', 'Uzbek', 16),
    ('management',       'masofaviy', 'bachelor', 'Uzbek', 16),
    ('marketing',        'masofaviy', 'bachelor', 'Uzbek', 16),
    ('accounting',       'masofaviy', 'bachelor', 'Uzbek', 16),
    ('banking',          'masofaviy', 'bachelor', 'Uzbek', 16),
    ('world-economy',    'masofaviy', 'bachelor', 'Uzbek', 16),
    ('info-systems',     'masofaviy', 'bachelor', 'Uzbek', 16),
    ('cybersecurity',    'masofaviy', 'bachelor', 'Uzbek', 16),
    ('computer-eng',     'masofaviy', 'bachelor', 'Uzbek', 16),
    ('software-eng',     'masofaviy', 'bachelor', 'Uzbek', 16),
    ('law',              'masofaviy', 'bachelor', 'Uzbek', 20),

    # === SIRTQI (part-time, bachelor) ===
    ('psychology',       'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('economics',        'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('finance',          'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('management',       'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('accounting',       'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('banking',          'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('cybersecurity',    'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('computer-eng',     'sirtqi', 'bachelor', 'Uzbek', 14.5),
    ('law',              'sirtqi', 'bachelor', 'Uzbek', 18),
]


LEVEL_DURATION = {'bachelor': '4 years', 'master': '2 years', 'phd': '3 years'}
LANG_SUFFIX = {'Uzbek': '', 'Russian': '-ru', 'English': '-en'}


def format_fee(millions):
    if millions == int(millions):
        return f"{int(millions):,} 000 000 so'm".replace(',', ' ')
    # 14.5 → "14 500 000 so'm"
    whole = int(millions)
    frac = int(round((millions - whole) * 1000))
    return f"{whole} {frac:03d} 000 so'm"


created, updated = 0, 0
for order, (key, st_slug, level, lang, fee) in enumerate(ROWS, 1):
    base = BASES[key]
    dept = depts[base['dept']]
    faculty = 'jurisprudence' if key == 'law' else 'business'

    level_suffix = '-master' if level == 'master' else ''
    lang_suffix = LANG_SUFFIX[lang]
    slug = f"{key}-{st_slug}{level_suffix}{lang_suffix}"

    title = base['title']
    title_uz = base['title_uz']
    title_ru = base['title_ru']
    if lang == 'Russian':
        title_uz = f"{base['title_uz']} (rus tilida)"
    elif lang == 'English':
        title_uz = f"{base['title_uz']} (ingliz tilida)"

    defaults = {
        'title': title,
        'title_uz': title_uz,
        'title_ru': title_ru,
        'department': dept,
        'faculty': faculty,
        'level': level,
        'study_type': study_types[st_slug],
        'language': lang,
        'tuition_fee': format_fee(fee),
        'duration': LEVEL_DURATION[level],
        'description': base['desc_en'],
        'description_uz': base['desc_uz'],
        'description_ru': '',
        'is_published': True,
        'order': order,
    }
    _, was_created = Program.objects.update_or_create(slug=slug, defaults=defaults)
    if was_created:
        created += 1
    else:
        updated += 1

print(f"✓ Programs: {created} created, {updated} updated ({len(ROWS)} total)")


# === Cleanup legacy data from original seed.py ===
LEGACY_PROGRAM_SLUGS = [
    'business-administration', 'economics-bachelor', 'it-bachelor',
    'pedagogy-bachelor', 'english-bachelor', 'law-bachelor',
    'public-finance-master', 'economics-master',
    'public-finance-phd', 'economics-phd', 'management-phd',
]
del_count = Program.objects.filter(slug__in=LEGACY_PROGRAM_SLUGS).delete()[0]
print(f"✓ Legacy programs deleted: {del_count}")

LEGACY_STUDY_TYPE_SLUGS = ['full-time', 'part-time', 'evening']
del_st = StudyType.objects.filter(slug__in=LEGACY_STUDY_TYPE_SLUGS, programs__isnull=True).distinct().delete()[0]
print(f"✓ Legacy study types deleted: {del_st}")
