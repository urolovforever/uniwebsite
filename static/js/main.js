// ================================================
// TIU Website - Main JavaScript (Professional & Interactive)
// ================================================

document.addEventListener('DOMContentLoaded', function() {

    // ================================================
    // Mobile Navigation — Dropdown below navbar
    // ================================================
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');
    const navContainer = document.querySelector('.nav-container');

    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', function () {
            // Set top position to match navbar height + any header offset (utility bar)
            if (navContainer) {
                const header = navContainer.closest('.main-header');
                const headerTop = header ? header.getBoundingClientRect().top : 0;
                const navBottom = headerTop + navContainer.offsetHeight;
                const top = Math.max(0, navBottom);
                mainNav.style.top = top + 'px';
                mainNav.style.height = 'calc(100dvh - ' + top + 'px)';
            }
            mainNav.classList.toggle('active');
            mobileToggle.classList.toggle('active');
            document.body.style.overflow = mainNav.classList.contains('active') ? 'hidden' : '';
        });
    }

    // ================================================
    // Transparent to Solid Navigation on Scroll
    // ================================================
    const mainHeader = document.getElementById('mainHeader');
    const utilityBar = document.querySelector('.utility-bar');

    if (mainHeader) {
        // Check if this is a scrolled header (subpage) or transparent header (home page)
        const isSubpage = mainHeader.classList.contains('scrolled');

        // Add padding to body for subpages to account for fixed header
        // Skip if page has .page-hero (hero handles its own padding)
        const hasPageHero = document.querySelector('.page-hero');
        if (isSubpage && !hasPageHero) {
            document.body.style.paddingTop = '85px';
        }

        function handleScroll() {
            // Only handle scroll for home page (transparent header)
            if (!isSubpage) {
                const scrollPosition = window.pageYOffset;

                // Masofani 150 yoki 200 qilsangiz, header darhol almashib qolmaydi
                if (scrollPosition > 150) {
                    mainHeader.classList.remove('transparent');
                    mainHeader.classList.add('scrolled');
                    if (utilityBar) {
                        utilityBar.style.transform = 'translateY(-100%)'; // Hidden o'rniga transform ishlating
                        utilityBar.style.transition = '0.4s';
                    }
                } else {
                    mainHeader.classList.add('transparent');
                    mainHeader.classList.remove('scrolled');
                    if (utilityBar) {
                        utilityBar.style.transform = 'translateY(0)';
                    }
                }
            }
            // Subpages with scrolled class don't need scroll handling - they stay fixed
        }

        window.addEventListener('scroll', handleScroll);
        handleScroll();
    }

    // ================================================
    // Mega Menu — Desktop: position below header; Mobile: toggle submenus
    // ================================================
    const navItems = document.querySelectorAll('.nav-menu > li');

    // Desktop: set mega-menu top to header bottom on hover
    navItems.forEach(item => {
        const megaMenu = item.querySelector('.mega-menu');
        if (megaMenu) {
            item.addEventListener('mouseenter', function () {
                if (window.innerWidth > 1024) {
                    const header = document.getElementById('mainHeader');
                    if (header) {
                        megaMenu.style.top = header.getBoundingClientRect().bottom + 'px';
                    }
                }
            });
        }
    });

    // Mobile: toggle submenus on click
    navItems.forEach(item => {
        const link = item.querySelector(':scope > a');
        if (link) {
            link.addEventListener('click', function (e) {
                if (window.innerWidth <= 1024) {
                    const megaMenu = item.querySelector('.mega-menu');
                    if (megaMenu) {
                        e.preventDefault();
                        navItems.forEach(other => {
                            if (other !== item) other.classList.remove('active');
                        });
                        item.classList.toggle('active');
                    }
                }
            });
        }
    });

    // Don't close menu on link click — let it stay visible until new page loads

    // Reset state when returning via back/forward (bfcache)
    window.addEventListener('pageshow', function (e) {
        if (e.persisted && mainNav) {
            mainNav.style.transition = '';
            mainNav.classList.remove('active');
            if (mobileToggle) mobileToggle.classList.remove('active');
            document.body.style.overflow = '';
        }
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
            const parallaxSpeed = 0.3;
            const heroHeight = heroSection.offsetHeight;

            // Only apply parallax while hero is visible
            if (scrolled < heroHeight) {
                heroSection.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
                heroSection.style.opacity = 1 - (scrolled / heroHeight) * 0.3;
            } else {
                // Reset transform when scrolled past hero
                heroSection.style.transform = 'translateY(0)';
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

});

function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150; // Element qachon ko'rinishni boshlashi

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    }
  }
}

window.addEventListener("scroll", reveal);

// Sahifa yuklanganda ham bir marta tekshirib olish uchun:
reveal();

// ================================================
// Shared Utilities (used by section-specific JS)
// ================================================

/**
 * Debounce function — delays execution until after wait ms of inactivity.
 * Previously duplicated across careers.js, current-students.js, faculty.js, news.js, research.js.
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Animate cards on scroll — applies fade-in + translateY via IntersectionObserver.
 * Previously duplicated across 6 JS files.
 * Usage: animateCards('.my-card-selector');
 */
function animateCards(selector, options = {}) {
    const threshold = options.threshold || 0.1;
    const translateY = options.translateY || '30px';
    const cards = document.querySelectorAll(selector);

    if (!cards.length) return;

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = `translateY(${translateY})`;
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
                cardObserver.unobserve(entry.target);
            }
        });
    }, { threshold });

    cards.forEach(card => cardObserver.observe(card));
}