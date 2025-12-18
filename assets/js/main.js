// ================================================
// TIU Website - Main JavaScript (Professional & Interactive)
// ================================================

document.addEventListener('DOMContentLoaded', function() {

    // ================================================
    // Mobile Navigation Toggle
    // ================================================
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
        });
    }

    // ================================================
    // Transparent to Solid Navigation on Scroll
    // ================================================
    const mainHeader = document.getElementById('mainHeader');
    const utilityBar = document.querySelector('.utility-bar');

    if (mainHeader) {
        function handleScroll() {
            const scrollPosition = window.pageYOffset;

            if (scrollPosition > 100) {
                mainHeader.classList.remove('transparent');
                mainHeader.classList.add('scrolled');
                if (utilityBar) {
                    utilityBar.style.opacity = '0';
                    utilityBar.style.visibility = 'hidden';
                }
            } else {
                mainHeader.classList.add('transparent');
                mainHeader.classList.remove('scrolled');
                if (utilityBar) {
                    utilityBar.style.opacity = '1';
                    utilityBar.style.visibility = 'visible';
                }
            }
        }

        window.addEventListener('scroll', handleScroll);
        handleScroll();
    }

    // ================================================
    // Dropdown Navigation for Mobile
    // ================================================
    const navItems = document.querySelectorAll('.nav-menu > li');

    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (window.innerWidth <= 968) {
                const dropdown = this.querySelector('.dropdown');
                if (dropdown) {
                    e.stopPropagation();
                    this.classList.toggle('active');
                }
            }
        });
    });

    const dropdownItems = document.querySelectorAll('.dropdown > li');

    dropdownItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (window.innerWidth <= 968) {
                const subDropdown = this.querySelector('.sub-dropdown');
                if (subDropdown) {
                    e.stopPropagation();
                    this.classList.toggle('active');
                }
            }
        });
    });

    // ================================================
    // Scroll Animations - Intersection Observer
    // ================================================
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                // Unobserve after animation to improve performance
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all sections and cards
    const animatedElements = document.querySelectorAll('.section-spacing, .card, .stat-item, .hero-quick-access, .news-card, .icon-card');
    animatedElements.forEach(el => {
        el.classList.add('fade-in-element');
        observer.observe(el);
    });

    // ================================================
    // Counter Animation for Stats
    // ================================================
    function animateCounter(element, target, duration = 2000) {
        const start = 0;
        const increment = target / (duration / 16); // 60fps
        let current = start;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current).toLocaleString();
            }
        }, 16);
    }

    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNumber = entry.target.querySelector('.stat-number');
                const text = statNumber.textContent;
                const number = parseInt(text.replace(/[^0-9]/g, ''));
                const suffix = text.replace(/[0-9,]/g, '');

                if (number && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');
                    statNumber.textContent = '0';

                    let current = 0;
                    const increment = number / 60;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= number) {
                            statNumber.textContent = number.toLocaleString() + suffix;
                            clearInterval(timer);
                        } else {
                            statNumber.textContent = Math.floor(current).toLocaleString() + suffix;
                        }
                    }, 30);
                }
            }
        });
    }, { threshold: 0.5 });

    const statItems = document.querySelectorAll('.stat-item');
    statItems.forEach(item => statsObserver.observe(item));

    // ================================================
    // Smooth Scroll for Anchor Links
    // ================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 100;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ================================================
    // Parallax Effect on Hero (Subtle)
    // ================================================
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallaxSpeed = 0.5;
            if (scrolled < window.innerHeight) {
                heroSection.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
            }
        });
    }

    // ================================================
    // Global Partners Carousel
    // ================================================
    const carouselPrev = document.querySelector('.carousel-prev');
    const carouselNext = document.querySelector('.carousel-next');
    const carousel = document.querySelector('.partners-carousel');

    if (carousel && carouselPrev && carouselNext) {
        let currentIndex = 0;
        const slides = carousel.querySelectorAll('.partner-slide');
        const slideWidth = slides[0]?.offsetWidth || 200;
        const gap = 64; // 4rem gap

        carouselNext.addEventListener('click', function() {
            if (currentIndex < slides.length - 3) {
                currentIndex++;
                carousel.style.transform = `translateX(-${currentIndex * (slideWidth + gap)}px)`;
            }
        });

        carouselPrev.addEventListener('click', function() {
            if (currentIndex > 0) {
                currentIndex--;
                carousel.style.transform = `translateX(-${currentIndex * (slideWidth + gap)}px)`;
            }
        });

        // Auto-play carousel
        let autoplayInterval = setInterval(() => {
            if (currentIndex < slides.length - 3) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            carousel.style.transform = `translateX(-${currentIndex * (slideWidth + gap)}px)`;
        }, 4000);

        // Pause on hover
        carousel.parentElement.addEventListener('mouseenter', () => {
            clearInterval(autoplayInterval);
        });

        carousel.parentElement.addEventListener('mouseleave', () => {
            autoplayInterval = setInterval(() => {
                if (currentIndex < slides.length - 3) {
                    currentIndex++;
                } else {
                    currentIndex = 0;
                }
                carousel.style.transform = `translateX(-${currentIndex * (slideWidth + gap)}px)`;
            }, 4000);
        });
    }

    // ================================================
    // Active Link Highlighting on Scroll
    // ================================================
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // ================================================
    // Lazy Loading Images
    // ================================================
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // ================================================
    // Language Selector Dropdown
    // ================================================
    const langSelectorBtn = document.getElementById('langSelectorBtn');
    const langDropdown = document.getElementById('langDropdown');
    const langSelector = document.querySelector('.language-selector-dropdown');
    const langOptions = document.querySelectorAll('.lang-option');
    const currentLangSpan = document.querySelector('.current-lang');

    if (langSelectorBtn && langDropdown) {
        // Toggle dropdown
        langSelectorBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            langSelector.classList.toggle('active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!langSelector.contains(e.target)) {
                langSelector.classList.remove('active');
            }
        });

        // Handle language selection
        langOptions.forEach(option => {
            option.addEventListener('click', function(e) {
                e.preventDefault();

                // Remove active class from all options
                langOptions.forEach(opt => opt.classList.remove('active'));

                // Add active class to selected option
                this.classList.add('active');

                // Update button text
                const selectedLang = this.getAttribute('data-lang').toUpperCase();
                currentLangSpan.textContent = selectedLang;

                // Close dropdown
                langSelector.classList.remove('active');

                // Here you can add logic to actually change the language
                console.log('Language changed to:', selectedLang);
            });
        });
    }

});
