#!/usr/bin/env python3
"""
TIU Website Page Generator
Generates all required pages for the TIU website with proper structure
"""

import os

# Define the page structure
pages = {
    'about': [
        ('overview.html', 'Overview', 'Learn about TIU\'s history, achievements, and academic excellence.'),
        ('mission-vision.html', 'Mission & Vision', 'Our commitment to excellence in education, research, and innovation.'),
        ('leadership.html', 'Leadership & Administration', 'Meet our leadership team and administrative staff.'),
        ('why-tiu.html', 'Why TIU', 'Discover what makes TIU the right choice for your education.'),
        ('sustainability.html', 'Sustainability & Impact', 'Our commitment to sustainability and positive social impact.'),
        ('campus-map.html', 'Campus Map', 'Navigate our modern campus and facilities.'),
    ],
    'admissions': [
        ('index.html', 'Admissions', 'Welcome to TIU Admissions - Start your journey here.'),
        ('how-to-apply.html', 'How to Apply', 'Step-by-step guide to applying to TIU.'),
        ('apply-bachelor.html', 'Apply - Bachelor Programs', 'Application process for undergraduate programs.'),
        ('apply-master.html', 'Apply - Master Programs', 'Application process for graduate programs.'),
        ('apply-international.html', 'Apply - International Students', 'Application guide for international students.'),
        ('requirements.html', 'Admission Requirements', 'Academic and language requirements for admission.'),
        ('tuition-fees.html', 'Tuition & Fees', 'Detailed information about tuition costs and fees.'),
        ('scholarships.html', 'Scholarships & Financial Aid', 'Available scholarships and financial assistance.'),
        ('faqs.html', 'FAQs', 'Frequently asked questions about admissions.'),
        ('apply-now.html', 'Apply Now', 'Submit your application to TIU.'),
    ],
    'programs': [
        ('index.html', 'Academic Programs', 'Explore our comprehensive range of academic programs.'),
        ('by-level.html', 'Programs by Level', 'Browse programs by academic level.'),
        ('bachelor.html', 'Bachelor Programs', 'Undergraduate degree programs.'),
        ('master.html', 'Master Programs', 'Graduate degree programs.'),
        ('certificates.html', 'Certificates & Short Programs', 'Professional certificates and short courses.'),
        ('by-faculty.html', 'Programs by Faculty', 'Browse programs by faculty or school.'),
        ('business-economics.html', 'Business & Economics', 'Business and economics programs.'),
        ('it-engineering.html', 'IT & Engineering', 'Information technology and engineering programs.'),
        ('law.html', 'Law Programs', 'Legal studies programs.'),
        ('humanities.html', 'Humanities & Social Sciences', 'Humanities and social sciences programs.'),
        ('international-programs.html', 'International Programs', 'International partnerships and programs.'),
        ('joint-degrees.html', 'Joint Degrees', 'Dual and joint degree programs.'),
        ('exchange-programs.html', 'Exchange Programs', 'Student exchange opportunities.'),
    ],
    'international': [
        ('index.html', 'International Students', 'Welcome international students to TIU.'),
        ('why-study-tiu.html', 'Why Study at TIU', 'Benefits for international students at TIU.'),
        ('admission-process.html', 'Admission Process', 'How international students can apply.'),
        ('visa-immigration.html', 'Visa & Immigration', 'Visa requirements and immigration support.'),
        ('accommodation.html', 'Accommodation', 'Housing options for international students.'),
        ('partner-universities.html', 'Partner Universities', 'Our global network of partner institutions.'),
        ('exchange-opportunities.html', 'Exchange Opportunities', 'Study abroad and exchange programs.'),
    ],
    'current-students': [
        ('index.html', 'Current Students', 'Resources and services for TIU students.'),
        ('academic-life.html', 'Academic Life', 'Academic resources and support.'),
        ('calendar.html', 'Academic Calendar', 'Important dates and academic calendar.'),
        ('lms.html', 'LMS / Moodle', 'Access the learning management system.'),
        ('exams-results.html', 'Exams & Results', 'Exam schedules and results.'),
        ('timetable.html', 'Timetable', 'Class schedules and timetables.'),
        ('campus-services.html', 'Campus Services', 'Available campus services and facilities.'),
        ('housing.html', 'Housing', 'On-campus and off-campus housing options.'),
        ('library.html', 'Library', 'University library and e-resources.'),
        ('it-services.html', 'IT Services', 'Technology support and services.'),
        ('cafeteria.html', 'Cafeteria', 'Dining options on campus.'),
        ('student-life.html', 'Student Life', 'Student activities and campus life.'),
        ('student-union.html', 'Student Union', 'Student government and representation.'),
        ('clubs.html', 'Clubs & Organizations', 'Student clubs and organizations.'),
        ('sports.html', 'Sports & Recreation', 'Sports facilities and activities.'),
    ],
    'research': [
        ('index.html', 'Research at TIU', 'Research initiatives and opportunities.'),
        ('centers.html', 'Research Centers', 'Our research centers and labs.'),
        ('publications.html', 'Publications & Journals', 'Academic publications and journals.'),
        ('conferences.html', 'Conferences & Events', 'Academic conferences and events.'),
        ('innovation.html', 'Innovation & Projects', 'Innovation projects and initiatives.'),
    ],
    'faculty': [
        ('index.html', 'Faculty', 'Information for faculty and staff.'),
        ('directory.html', 'Faculty Directory', 'Browse our faculty members.'),
        ('departments.html', 'Departments', 'Academic departments and divisions.'),
        ('profiles.html', 'Academic Staff Profiles', 'Faculty member profiles.'),
    ],
    'careers': [
        ('index.html', 'Careers & Alumni', 'Career services and alumni network.'),
        ('career-center.html', 'Career Center', 'Career development and support.'),
        ('internships.html', 'Internships & Employment', 'Internship and job opportunities.'),
        ('employer-partnerships.html', 'Employer Partnerships', 'Corporate partnerships and recruitment.'),
        ('alumni-network.html', 'Alumni Network', 'Connect with TIU alumni.'),
    ],
    'news': [
        ('index.html', 'News & Media', 'Latest news and media from TIU.'),
        ('news.html', 'News', 'University news and announcements.'),
        ('events.html', 'Events', 'Upcoming events and activities.'),
        ('press-releases.html', 'Press Releases', 'Official press releases.'),
        ('gallery.html', 'Photo & Video Gallery', 'Multimedia gallery.'),
    ],
    'contact': [
        ('index.html', 'Contact Us', 'Get in touch with TIU.'),
        ('contact-info.html', 'Contact Information', 'Contact details and locations.'),
        ('rector-reception.html', 'Rector\'s Virtual Reception', 'Connect with university leadership.'),
        ('support.html', 'Ask a Question / Support', 'Submit questions or get support.'),
    ],
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - TIU</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{css_path}assets/css/tiu-main.css">
</head>
<body>
    <!-- Utility Bar -->
    <div class="utility-bar">
        <div class="container">
            <div class="utility-links">
                <a href="{root_path}current-students/lms.html"><i class="fas fa-graduation-cap"></i> Student Portal</a>
                <a href="{root_path}current-students/library.html"><i class="fas fa-book"></i> E-Library</a>
                <a href="{root_path}current-students/timetable.html"><i class="fas fa-calendar"></i> Timetable</a>
                <a href="#"><i class="fas fa-envelope"></i> University Email</a>
            </div>
            <div class="language-switcher">
                <span>Language:</span>
                <a href="#" class="lang-btn active" data-lang="en">EN</a>
                <a href="#" class="lang-btn" data-lang="ru">RU</a>
                <a href="#" class="lang-btn" data-lang="uz">UZ</a>
            </div>
        </div>
    </div>

    <!-- Main Header -->
    <header class="main-header">
        <div class="nav-container">
            <div class="logo-section">
                <a href="{root_path}index-tiu.html">
                    <div class="logo-text">
                        <h1>TIU</h1>
                        <p>Tashkent International University</p>
                    </div>
                </a>
            </div>

            <div class="mobile-toggle">
                <span></span>
                <span></span>
                <span></span>
            </div>

            <nav class="main-nav">
                <ul class="nav-menu">
                    <li><a href="{root_path}about/index.html">About TIU <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}admissions/index.html">Admissions <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}programs/index.html">Programs <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}international/index.html">International <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}current-students/index.html">Current Students <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}research/index.html">Research <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}faculty/index.html">Faculty <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}careers/index.html">Careers & Alumni <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}news/index.html">News & Media <i class="fas fa-chevron-down"></i></a></li>
                    <li><a href="{root_path}contact/index.html">Contact <i class="fas fa-chevron-down"></i></a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Page Header -->
    <div class="page-header">
        <h1>{title}</h1>
        <div class="breadcrumb">
            <a href="{root_path}index-tiu.html">Home</a>
            <span>/</span>
            <a href="{section_index}">{section_name}</a>
            <span>/</span>
            <span>{title}</span>
        </div>
    </div>

    <!-- Main Content -->
    <section class="content-section">
        <div class="container">
            <div class="section-title">
                <h2>{title}</h2>
                <p>{description}</p>
            </div>

            <div class="info-box">
                <h3><i class="fas fa-info-circle"></i> Content Guidelines</h3>
                <p>This page should include:</p>
                <ul style="margin-left: 2rem; margin-top: 1rem;">
                    <li style="margin-bottom: 0.5rem;">• Detailed information about {title_lower}</li>
                    <li style="margin-bottom: 0.5rem;">• Relevant images and visual content</li>
                    <li style="margin-bottom: 0.5rem;">• Links to related pages and resources</li>
                    <li style="margin-bottom: 0.5rem;">• Contact information if applicable</li>
                    <li style="margin-bottom: 0.5rem;">• Call-to-action buttons for key actions</li>
                </ul>
            </div>

            <div style="margin-top: 3rem;">
                <h3>About {title}</h3>
                <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                    {description} At Tashkent International University, we are committed to providing comprehensive
                    information and support to help you make informed decisions about your education and career.
                </p>

                <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                    <strong>Placeholder Content:</strong> This section should be filled with specific information about
                    {title_lower}. Include relevant details, statistics, requirements, processes, or other pertinent
                    information that would be valuable to your target audience.
                </p>

                {specific_content}
            </div>

            <div class="info-box highlight text-center" style="margin-top: 3rem;">
                <h3>Need More Information?</h3>
                <p>Contact our team for personalized assistance</p>
                <div style="margin-top: 1.5rem;">
                    <a href="{root_path}contact/support.html" class="cta-gold">Contact Us</a>
                    <a href="{root_path}admissions/apply-now.html" class="cta-secondary" style="margin-left: 1rem; color: white; border-color: white;">Apply Now</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>About TIU</h3>
                <p>Leading institution committed to excellence in teaching, research, and community service.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="{root_path}about/index.html">About</a></li>
                    <li><a href="{root_path}admissions/index.html">Admissions</a></li>
                    <li><a href="{root_path}programs/index.html">Programs</a></li>
                    <li><a href="{root_path}contact/index.html">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Contact</h3>
                <ul>
                    <li><i class="fas fa-phone"></i> +998 71 XXX XX XX</li>
                    <li><i class="fas fa-envelope"></i> info@tiu.uz</li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 Tashkent International University. All rights reserved.</p>
        </div>
    </footer>

    <script src="{js_path}assets/js/tiu-main.js"></script>
</body>
</html>
"""

def get_specific_content(section, filename, title):
    """Generate specific content based on page type"""

    # Add specific content for different page types
    if 'apply' in filename or filename == 'apply-now.html':
        return """
                <div class="card" style="margin-top: 2rem;">
                    <div class="card-content">
                        <h4>Application Form</h4>
                        <form class="tiu-form" style="margin-top: 1.5rem;">
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Full Name *</label>
                                <input type="text" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Email Address *</label>
                                <input type="email" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Phone Number *</label>
                                <input type="tel" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Program of Interest *</label>
                                <select required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                                    <option value="">Select a program</option>
                                    <option value="business">Business & Economics</option>
                                    <option value="it">IT & Engineering</option>
                                    <option value="law">Law</option>
                                    <option value="humanities">Humanities & Social Sciences</option>
                                </select>
                            </div>
                            <button type="submit" class="cta-primary" style="border: none; cursor: pointer;">Submit Application</button>
                        </form>
                    </div>
                </div>
        """
    elif filename == 'faqs.html':
        return """
                <div style="margin-top: 2rem;">
                    <div class="card" style="margin-bottom: 1rem;">
                        <div class="card-content">
                            <h4>What are the admission requirements?</h4>
                            <p>Admission requirements vary by program. Generally, you need a high school diploma for bachelor's programs and a bachelor's degree for master's programs, plus language proficiency.</p>
                        </div>
                    </div>
                    <div class="card" style="margin-bottom: 1rem;">
                        <div class="card-content">
                            <h4>When is the application deadline?</h4>
                            <p>Application deadlines are typically in June for the Fall semester and December for the Spring semester. Check specific program pages for exact dates.</p>
                        </div>
                    </div>
                    <div class="card" style="margin-bottom: 1rem;">
                        <div class="card-content">
                            <h4>Are scholarships available?</h4>
                            <p>Yes, TIU offers merit-based and need-based scholarships. Visit our Scholarships page for more information and application procedures.</p>
                        </div>
                    </div>
                </div>
        """
    elif 'contact' in filename or filename == 'support.html':
        return """
                <div class="card" style="margin-top: 2rem;">
                    <div class="card-content">
                        <h4>Contact Form</h4>
                        <form class="tiu-form" style="margin-top: 1.5rem;">
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Your Name *</label>
                                <input type="text" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Email *</label>
                                <input type="email" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Subject *</label>
                                <input type="text" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;">
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Message *</label>
                                <textarea required rows="5" style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 4px;"></textarea>
                            </div>
                            <button type="submit" class="cta-primary" style="border: none; cursor: pointer;">Send Message</button>
                        </form>
                    </div>
                </div>
        """
    else:
        return """
                <div class="card-grid" style="margin-top: 2rem;">
                    <div class="card">
                        <div class="card-content">
                            <h4>Key Information</h4>
                            <p>Add key information, statistics, or highlights relevant to this page.</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-content">
                            <h4>Resources</h4>
                            <p>Link to downloadable resources, brochures, or related documents.</p>
                        </div>
                    </div>
                </div>
        """

def generate_pages():
    """Generate all pages"""
    section_names = {
        'about': 'About TIU',
        'admissions': 'Admissions',
        'programs': 'Programs',
        'international': 'International Students',
        'current-students': 'Current Students',
        'research': 'Research',
        'faculty': 'Faculty',
        'careers': 'Careers & Alumni',
        'news': 'News & Media',
        'contact': 'Contact',
    }

    for section, page_list in pages.items():
        # Create section directory if it doesn't exist
        os.makedirs(section, exist_ok=True)

        for filename, title, description in page_list:
            # Skip if already exists (like about/index.html we already created)
            if section == 'about' and filename == 'index.html':
                continue

            filepath = os.path.join(section, filename)

            # Determine paths
            root_path = '../'
            css_path = '../'
            js_path = '../'
            section_index = 'index.html'
            section_name = section_names.get(section, section.title())

            # Get specific content
            specific_content = get_specific_content(section, filename, title)

            # Generate HTML
            html = html_template.format(
                title=title,
                description=description,
                title_lower=title.lower(),
                root_path=root_path,
                css_path=css_path,
                js_path=js_path,
                section_index=section_index,
                section_name=section_name,
                specific_content=specific_content
            )

            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"Created: {filepath}")

    print("\n✓ All pages generated successfully!")

if __name__ == '__main__':
    generate_pages()
