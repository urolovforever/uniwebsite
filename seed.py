"""
Seed script — run with: python3 manage.py shell < seed.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiu_project.settings.dev')
django.setup()

from datetime import date, timedelta
from django.utils import timezone
from apps.core.models import SiteSettings, Partner, ContactMessage, Scholarship
from apps.news.models import Category, NewsArticle, Event, PublicationCategory, AuthorType, Publication
from apps.programs.models import Department, Program
from apps.people.models import Leader, Person
from apps.jobs.models import JobDepartment, JobType, JobRole, JobPosition

now = timezone.now()

# === Site Settings ===
ss, _ = SiteSettings.objects.get_or_create(pk=1, defaults={
    'site_name': 'Tashkent International University',
    'site_name_uz': 'Toshkent Xalqaro Universiteti',
    'site_name_ru': 'Ташкентский Международный Университет',
    'address': '7 Little Ring Road, Tashkent, Uzbekistan',
    'address_uz': "Kichik Halqa yo'li 7, Toshkent, O'zbekiston",
    'address_ru': 'Малая кольцевая дорога 7, Ташкент, Узбекистан',
    'phone': '+998 71 200 00 00',
    'email': 'info@tiu.uz',
    'facebook_url': 'https://facebook.com/tiu.uz',
    'instagram_url': 'https://instagram.com/tiu.uz',
    'telegram_url': 'https://t.me/tiu_uz',
    'linkedin_url': 'https://linkedin.com/school/tiu-uz',
    'youtube_url': 'https://youtube.com/@tiu_uz',
})
print("✓ Site Settings")

# === Departments (Kafedralar) ===
depts_data = [
    {'name': 'Jurisprudence', 'name_uz': 'Yurisprudensiya', 'name_ru': 'Юриспруденция', 'slug': 'jurisprudence', 'faculty': 'jurisprudence', 'excerpt': 'Department of Law and Legal Studies', 'excerpt_uz': 'Huquq va huquqshunoslik kafedrasi', 'order': 1},
    {'name': 'Business and Economics', 'name_uz': 'Biznes va iqtisodiyot', 'name_ru': 'Бизнес и экономика', 'slug': 'business-economics', 'faculty': 'business', 'excerpt': 'Department of Business, Finance, and Economics', 'excerpt_uz': 'Biznes, moliya va iqtisodiyot kafedrasi', 'order': 2},
    {'name': 'Information Technology', 'name_uz': 'Axborot texnologiyalari', 'name_ru': 'Информационные технологии', 'slug': 'information-technology', 'faculty': 'business', 'excerpt': 'Department of IT and Computer Science', 'excerpt_uz': 'IT va kompyuter fanlari kafedrasi', 'order': 3},
    {'name': 'Education and Pedagogy', 'name_uz': "Ta'lim va pedagogika", 'name_ru': 'Образование и педагогика', 'slug': 'education-pedagogy', 'faculty': 'business', 'excerpt': 'Department of Education and Teaching', 'excerpt_uz': "Ta'lim va o'qitish kafedrasi", 'order': 4},
    {'name': 'Foreign Languages and Literature', 'name_uz': 'Chet tillari va adabiyot', 'name_ru': 'Иностранные языки и литература', 'slug': 'foreign-languages', 'faculty': 'business', 'excerpt': 'Department of Languages, Translation, and Literature', 'excerpt_uz': 'Tillar, tarjima va adabiyot kafedrasi', 'order': 5},
]
depts = {}
for d in depts_data:
    dept, _ = Department.objects.get_or_create(slug=d['slug'], defaults=d)
    depts[d['slug']] = dept
print("✓ Departments")

# === Programs ===
programs_data = [
    {'title': 'Business Administration', 'title_uz': 'Biznes boshqaruvi', 'slug': 'business-administration', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '22,000,000 UZS'},
    {'title': 'Economics', 'title_uz': 'Iqtisodiyot', 'slug': 'economics-bachelor', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '22,000,000 UZS'},
    {'title': 'Information Technology', 'title_uz': 'Axborot texnologiyalari', 'slug': 'it-bachelor', 'department': depts['information-technology'], 'faculty': 'business', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '24,000,000 UZS'},
    {'title': 'Pedagogy', 'title_uz': 'Pedagogika', 'slug': 'pedagogy-bachelor', 'department': depts['education-pedagogy'], 'faculty': 'business', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '20,000,000 UZS'},
    {'title': 'English Language and Literature', 'title_uz': 'Ingliz tili va adabiyoti', 'slug': 'english-bachelor', 'department': depts['foreign-languages'], 'faculty': 'business', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '20,000,000 UZS'},
    {'title': 'Law', 'title_uz': 'Huquqshunoslik', 'slug': 'law-bachelor', 'department': depts['jurisprudence'], 'faculty': 'jurisprudence', 'level': 'bachelor', 'duration': '4 years', 'tuition_fee': '22,000,000 UZS'},
    {'title': 'Public Finance and International Finance', 'title_uz': 'Davlat moliyasi va xalqaro moliya', 'slug': 'public-finance-master', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'master', 'duration': '2 years', 'tuition_fee': '26,000,000 UZS'},
    {'title': 'Economics', 'title_uz': 'Iqtisodiyot', 'slug': 'economics-master', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'master', 'duration': '2 years', 'tuition_fee': '26,000,000 UZS'},
    {'title': 'Public Finance and International Finance', 'title_uz': 'Davlat moliyasi va xalqaro moliya', 'slug': 'public-finance-phd', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'phd', 'duration': '3 years', 'tuition_fee': '30,000,000 UZS'},
    {'title': 'Economics', 'title_uz': 'Iqtisodiyot', 'slug': 'economics-phd', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'phd', 'duration': '3 years', 'tuition_fee': '30,000,000 UZS'},
    {'title': 'Management', 'title_uz': 'Menejment', 'slug': 'management-phd', 'department': depts['business-economics'], 'faculty': 'business', 'level': 'phd', 'duration': '3 years', 'tuition_fee': '30,000,000 UZS'},
]
for p in programs_data:
    Program.objects.get_or_create(slug=p['slug'], defaults=p)
print("✓ Programs")

# === Leaders ===
leaders_data = [
    {'first_name': 'Abdulla', 'last_name': 'Karimov', 'job_title': 'Rector', 'job_title_uz': 'Rektor', 'job_title_ru': 'Ректор', 'excerpt': 'Provides overall strategic leadership for TIU.', 'excerpt_uz': 'TIU uchun umumiy strategik rahbarlikni amalga oshiradi.', 'order': 1},
    {'first_name': 'Nilufar', 'last_name': 'Rashidova', 'job_title': 'Vice Rector for Academic Affairs', 'job_title_uz': "O'quv ishlari bo'yicha prorektor", 'job_title_ru': 'Проректор по учебной работе', 'excerpt': 'Oversees curriculum development and academic quality.', 'excerpt_uz': "O'quv dasturlarini ishlab chiqish va akademik sifatni nazorat qiladi.", 'order': 2},
    {'first_name': 'Jamshid', 'last_name': 'Umarov', 'job_title': 'Vice Rector for International Affairs', 'job_title_uz': 'Xalqaro aloqalar bo\'yicha prorektor', 'job_title_ru': 'Проректор по международным связям', 'excerpt': 'Manages global partnerships and exchange programs.', 'excerpt_uz': 'Global hamkorliklar va almashuv dasturlarini boshqaradi.', 'order': 3},
]
for l in leaders_data:
    Leader.objects.get_or_create(first_name=l['first_name'], last_name=l['last_name'], defaults=l)
print("✓ Leaders")

# === People (Faculty & Staff) ===
people_data = [
    {'first_name': 'Sardor', 'last_name': 'Alimov', 'slug': 'sardor-alimov', 'job_title': 'Associate Professor', 'job_title_uz': 'Dotsent', 'department': depts['business-economics'], 'email': 's.alimov@tiu.uz', 'order': 1},
    {'first_name': 'Maria', 'last_name': 'Kim', 'slug': 'maria-kim', 'job_title': 'Senior Lecturer', 'job_title_uz': 'Katta o\'qituvchi', 'department': depts['information-technology'], 'email': 'm.kim@tiu.uz', 'order': 2},
    {'first_name': 'Olga', 'last_name': 'Petrova', 'slug': 'olga-petrova', 'job_title': 'Professor', 'job_title_uz': 'Professor', 'department': depts['jurisprudence'], 'email': 'o.petrova@tiu.uz', 'order': 3},
    {'first_name': 'Bobur', 'last_name': 'Nazarov', 'slug': 'bobur-nazarov', 'job_title': 'Lecturer', 'job_title_uz': "O'qituvchi", 'department': depts['foreign-languages'], 'email': 'b.nazarov@tiu.uz', 'order': 4},
    {'first_name': 'Dilnoza', 'last_name': 'Yusupova', 'slug': 'dilnoza-yusupova', 'job_title': 'Assistant Professor', 'job_title_uz': 'Assistent professor', 'department': depts['education-pedagogy'], 'email': 'd.yusupova@tiu.uz', 'order': 5},
    {'first_name': 'James', 'last_name': 'Wilson', 'slug': 'james-wilson', 'job_title': 'Visiting Professor', 'job_title_uz': 'Tashrif buyuruvchi professor', 'department': depts['business-economics'], 'email': 'j.wilson@tiu.uz', 'order': 6},
]
for p in people_data:
    Person.objects.get_or_create(slug=p['slug'], defaults=p)
print("✓ People")

# === News Categories ===
cats_data = [
    {'name': 'University', 'name_uz': 'Universitet', 'name_ru': 'Университет', 'slug': 'university'},
    {'name': 'Academics', 'name_uz': 'Akademik', 'name_ru': 'Академия', 'slug': 'academics'},
    {'name': 'International', 'name_uz': 'Xalqaro', 'name_ru': 'Международный', 'slug': 'international'},
    {'name': 'Student Life', 'name_uz': 'Talaba hayoti', 'name_ru': 'Студенческая жизнь', 'slug': 'student-life'},
]
cats = {}
for c in cats_data:
    cat, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
    cats[c['slug']] = cat
print("✓ Categories")

# === News Articles ===
news_data = [
    {'title': 'TIU Signs Partnership Agreement with Korean University', 'title_uz': 'TIU Koreya universiteti bilan hamkorlik shartnomasini imzoladi', 'slug': 'tiu-korean-partnership', 'excerpt': 'A new dual degree pathway has been established with a leading South Korean university.', 'excerpt_uz': 'Janubiy Koreyaning yetakchi universiteti bilan yangi qo\'shma diplom yo\'li o\'rnatildi.', 'faculty': 'business', 'published_date': now - timedelta(days=2)},
    {'title': 'New IT Lab Opens on Campus', 'title_uz': 'Kampusda yangi IT laboratoriya ochildi', 'slug': 'new-it-lab', 'excerpt': 'State-of-the-art computer laboratory with 50 workstations now available for students.', 'excerpt_uz': '50 ta ish stantsiyali zamonaviy kompyuter laboratoriyasi talabalarga taqdim etildi.', 'published_date': now - timedelta(days=5)},
    {'title': 'TIU Students Win Regional Case Competition', 'title_uz': 'TIU talabalari mintaqaviy keys musobaqasida g\'olib bo\'ldi', 'slug': 'case-competition-win', 'excerpt': 'Business students secured first place at the Central Asian case competition.', 'excerpt_uz': 'Biznes talabalari Markaziy Osiyo keys musobaqasida birinchi o\'rinni egalladi.', 'faculty': 'business', 'published_date': now - timedelta(days=8)},
    {'title': 'International Faculty Exchange Program Launches', 'title_uz': 'Xalqaro professor-o\'qituvchilar almashuv dasturi boshlandi', 'slug': 'faculty-exchange-launch', 'excerpt': 'TIU welcomes visiting professors from partner universities in Europe and Asia.', 'excerpt_uz': 'TIU Yevropa va Osiyodagi hamkor universitetlardan tashrif buyuruvchi professorlarni qabul qildi.', 'published_date': now - timedelta(days=12)},
    {'title': 'Law Faculty Hosts Moot Court Competition', 'title_uz': 'Huquq fakulteti sun\'iy sud musobaqasini o\'tkazdi', 'slug': 'moot-court', 'excerpt': 'Students argued cases before a panel of practicing judges and legal professionals.', 'excerpt_uz': 'Talabalar amaliyotchi sudyalar va huquqshunoslar hay\'ati oldida ishlarni himoya qildi.', 'faculty': 'jurisprudence', 'published_date': now - timedelta(days=15)},
    {'title': 'TIU Celebrates First Academic Year Completion', 'title_uz': 'TIU birinchi o\'quv yili yakunlanishini nishonladi', 'slug': 'first-year-celebration', 'excerpt': 'The university community gathered to celebrate milestones achieved in the inaugural year.', 'excerpt_uz': 'Universitet jamoasi birinchi yilda erishilgan yutuqlarni nishonlash uchun yig\'ildi.', 'published_date': now - timedelta(days=20)},
    {'title': 'Scholarship Program Expanded for 2025', 'title_uz': '2025-yil uchun stipendiya dasturi kengaytirildi', 'slug': 'scholarship-expanded', 'excerpt': 'More merit-based and need-based scholarships available for incoming students.', 'excerpt_uz': 'Yangi talabalar uchun ko\'proq iqtidor va ehtiyojga asoslangan stipendiyalar mavjud.', 'published_date': now - timedelta(days=25)},
]
for n in news_data:
    article, created = NewsArticle.objects.get_or_create(slug=n['slug'], defaults=n)
    if created:
        article.categories.add(cats.get('university', cats['academics']))
print("✓ News")

# === Events ===
events_data = [
    {'title': 'Open Day — Spring 2026', 'title_uz': 'Ochiq eshiklar kuni — 2026 bahor', 'slug': 'open-day-spring-2026', 'excerpt': 'Visit our campus and meet faculty.', 'excerpt_uz': 'Kampusimizga tashrif buyuring va professor-o\'qituvchilar bilan tanishing.', 'event_date': date.today() + timedelta(days=10), 'event_time': '10:00', 'location': 'TIU Main Campus'},
    {'title': 'Career Fair 2026', 'title_uz': 'Karyera yarmarkasi 2026', 'slug': 'career-fair-2026', 'excerpt': 'Meet employers and explore internship opportunities.', 'excerpt_uz': 'Ish beruvchilar bilan tanishing va amaliyot imkoniyatlarini o\'rganing.', 'event_date': date.today() + timedelta(days=20), 'event_time': '09:00', 'location': 'TIU Conference Hall'},
    {'title': 'Guest Lecture: AI in Education', 'title_uz': 'Mehmon ma\'ruza: Ta\'limda sun\'iy intellekt', 'slug': 'ai-education-lecture', 'excerpt': 'Leading expert discusses the future of AI in higher education.', 'excerpt_uz': 'Yetakchi ekspert oliy ta\'limda sun\'iy intellekt kelajagini muhokama qiladi.', 'event_date': date.today() + timedelta(days=30), 'event_time': '14:00', 'location': 'Auditorium A', 'faculty': 'business'},
    {'title': 'Student Sports Tournament', 'title_uz': 'Talabalar sport musobaqasi', 'slug': 'sports-tournament', 'excerpt': 'Annual inter-faculty sports competition.', 'excerpt_uz': 'Yillik fakultetlararo sport musobaqasi.', 'event_date': date.today() + timedelta(days=40), 'event_time': '11:00', 'location': 'TIU Sports Complex'},
    {'title': 'International Law Seminar', 'title_uz': 'Xalqaro huquq seminari', 'slug': 'law-seminar', 'excerpt': 'Seminar on international legal frameworks and human rights.', 'excerpt_uz': 'Xalqaro huquqiy asoslar va inson huquqlari bo\'yicha seminar.', 'event_date': date.today() + timedelta(days=50), 'event_time': '15:00', 'location': 'Law Faculty Hall', 'faculty': 'jurisprudence'},
    {'title': 'Nawruz Cultural Festival', 'title_uz': 'Navro\'z madaniy festivali', 'slug': 'nawruz-festival', 'excerpt': 'Celebrate Nawruz with music, food, and cultural performances.', 'excerpt_uz': 'Navro\'zni musiqa, taom va madaniy ko\'rsatuvlar bilan nishonlang.', 'event_date': date.today() + timedelta(days=60), 'event_time': '16:00', 'location': 'Campus Garden'},
    {'title': 'Research Methodology Workshop', 'title_uz': 'Tadqiqot metodologiyasi seminari', 'slug': 'research-workshop', 'excerpt': 'Hands-on workshop for graduate students on research methods.', 'excerpt_uz': 'Magistratura talabalari uchun tadqiqot usullari bo\'yicha amaliy seminar.', 'event_date': date.today() + timedelta(days=70), 'event_time': '10:00', 'location': 'Library Seminar Room'},
]
for e in events_data:
    Event.objects.get_or_create(slug=e['slug'], defaults=e)
print("✓ Events")

# === Publication Categories ===
pub_cats_data = [
    {'name': 'Journal Article', 'name_uz': 'Jurnal maqolasi', 'name_ru': 'Журнальная статья', 'slug': 'journal-article'},
    {'name': 'Conference Paper', 'name_uz': 'Konferensiya maqolasi', 'name_ru': 'Доклад конференции', 'slug': 'conference-paper'},
    {'name': 'Book Chapter', 'name_uz': 'Kitob bobi', 'name_ru': 'Глава книги', 'slug': 'book-chapter'},
]
pub_cats = {}
for pc in pub_cats_data:
    pcat, _ = PublicationCategory.objects.get_or_create(slug=pc['slug'], defaults=pc)
    pub_cats[pc['slug']] = pcat
print("✓ Publication Categories")

# === Author Types ===
at_data = [
    {'name': 'Faculty', 'name_uz': 'Professor-o\'qituvchi', 'name_ru': 'Преподаватель', 'slug': 'faculty'},
    {'name': 'Student', 'name_uz': 'Talaba', 'name_ru': 'Студент', 'slug': 'student'},
    {'name': 'Joint', 'name_uz': 'Hamkorlikda', 'name_ru': 'Совместная', 'slug': 'joint'},
]
author_types = {}
for at in at_data:
    atype, _ = AuthorType.objects.get_or_create(slug=at['slug'], defaults=at)
    author_types[at['slug']] = atype
print("✓ Author Types")

# === Publications ===
pubs_data = [
    {'title': 'Digital Transformation in Central Asian Banking', 'title_uz': 'Markaziy Osiyo banklarida raqamli transformatsiya', 'slug': 'digital-banking-ca', 'author': 'S. Alimov, J. Wilson', 'author_type': author_types['joint'], 'excerpt': 'Analysis of digital banking adoption across Central Asian economies.', 'published_date': now - timedelta(days=30)},
    {'title': 'Constitutional Development in Post-Soviet States', 'title_uz': 'Sovet davlatlaridan keyingi konstitutsiyaviy rivojlanish', 'slug': 'constitutional-dev', 'author': 'O. Petrova', 'author_type': author_types['faculty'], 'excerpt': 'Comparative study of constitutional frameworks in Central Asia.', 'published_date': now - timedelta(days=60)},
    {'title': 'Machine Learning Applications in Education', 'title_uz': 'Ta\'limda mashinali o\'rganish qo\'llanilishi', 'slug': 'ml-education', 'author': 'M. Kim, B. Nazarov', 'author_type': author_types['faculty'], 'excerpt': 'Exploring AI-driven personalized learning in university settings.', 'published_date': now - timedelta(days=90)},
]
for pub in pubs_data:
    p, created = Publication.objects.get_or_create(slug=pub['slug'], defaults=pub)
    if created:
        p.categories.add(pub_cats['journal-article'])
print("✓ Publications")

# === Partners ===
for i in range(1, 7):
    Partner.objects.get_or_create(name=f'Partner University {i}', defaults={'order': i, 'is_active': True})
print("✓ Partners")

# === Jobs ===
jd1, _ = JobDepartment.objects.get_or_create(slug='academic', defaults={'name': 'Academic', 'name_uz': 'Akademik', 'name_ru': 'Академический'})
jd2, _ = JobDepartment.objects.get_or_create(slug='administrative', defaults={'name': 'Administrative', 'name_uz': 'Ma\'muriy', 'name_ru': 'Административный'})
jt1, _ = JobType.objects.get_or_create(slug='full-time', defaults={'name': 'Full-time', 'name_uz': 'To\'liq stavka', 'name_ru': 'Полная занятость'})
jt2, _ = JobType.objects.get_or_create(slug='part-time', defaults={'name': 'Part-time', 'name_uz': 'Yarim stavka', 'name_ru': 'Частичная занятость'})
jr1, _ = JobRole.objects.get_or_create(slug='professor', defaults={'name': 'Professor', 'name_uz': 'Professor', 'name_ru': 'Профессор'})
jr2, _ = JobRole.objects.get_or_create(slug='lecturer', defaults={'name': 'Lecturer', 'name_uz': 'O\'qituvchi', 'name_ru': 'Преподаватель'})

jobs_data = [
    {'title': 'Senior Lecturer in Business Administration', 'title_uz': 'Biznes boshqaruvi bo\'yicha katta o\'qituvchi', 'slug': 'lecturer-business', 'department': jd1, 'job_type': jt1, 'role': jr2, 'salary': 'Discussed at interview', 'salary_uz': 'Intervyuda kelishiladi', 'deadline': date.today() + timedelta(days=30), 'description': '<p>We are looking for an experienced lecturer in Business Administration.</p>'},
    {'title': 'IT Support Specialist', 'title_uz': 'IT qo\'llab-quvvatlash mutaxassisi', 'slug': 'it-support', 'department': jd2, 'job_type': jt1, 'role': jr2, 'salary': '8,000,000 - 12,000,000 UZS', 'salary_uz': '8,000,000 - 12,000,000 so\'m', 'deadline': date.today() + timedelta(days=45)},
    {'title': 'Visiting Professor of International Law', 'title_uz': 'Xalqaro huquq bo\'yicha tashrif buyuruvchi professor', 'slug': 'visiting-prof-law', 'department': jd1, 'job_type': jt2, 'role': jr1, 'salary': 'Competitive', 'salary_uz': 'Raqobatbardosh', 'deadline': date.today() + timedelta(days=60)},
]
for j in jobs_data:
    JobPosition.objects.get_or_create(slug=j['slug'], defaults=j)
print("✓ Jobs")

# === Scholarships ===
Scholarship.objects.get_or_create(slug='merit-scholarship', defaults={
    'title': 'TIU Merit Scholarship', 'title_uz': 'TIU iqtidor stipendiyasi', 'slug': 'merit-scholarship',
    'excerpt': 'For outstanding academic achievers.', 'excerpt_uz': 'Yuqori akademik natijalarga erishganlar uchun.',
    'level': 'bachelor', 'award_type': 'merit', 'applicant_type': 'new',
    'award_tag_text': 'Up to 50% tuition', 'order': 1,
})
Scholarship.objects.get_or_create(slug='need-scholarship', defaults={
    'title': 'TIU Need-Based Grant', 'title_uz': 'TIU ehtiyojga asoslangan granti', 'slug': 'need-scholarship',
    'excerpt': 'Financial support for students in need.', 'excerpt_uz': 'Muhtoj talabalarga moliyaviy yordam.',
    'level': 'bachelor master', 'award_type': 'need', 'applicant_type': 'all',
    'award_tag_text': 'Up to 30% tuition', 'order': 2,
})
print("✓ Scholarships")

print("\n=== Seed complete! ===")
