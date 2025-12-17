// ================================================
// TIU Website - Enhanced Homepage JavaScript
// Additional functionality for video hero and scroll effects
// ================================================

document.addEventListener('DOMContentLoaded', function() {

    // ================================================
    // Transparent to Solid Navigation on Scroll
    // ================================================
    const mainHeader = document.getElementById('mainHeader');
    const utilityBar = document.querySelector('.utility-bar');

    function handleNavigationScroll() {
        const scrollPosition = window.pageYOffset;

        if (scrollPosition > 100) {
            // Scrolled down - make navigation solid
            mainHeader.classList.remove('transparent');
            mainHeader.classList.add('scrolled');

            // Hide utility bar when scrolled (optional)
            if (utilityBar) {
                utilityBar.style.display = 'none';
            }
        } else {
            // At top - make navigation transparent
            mainHeader.classList.add('transparent');
            mainHeader.classList.remove('scrolled');

            // Show utility bar at top
            if (utilityBar) {
                utilityBar.style.display = 'block';
            }
        }
    }

    // Run on scroll
    window.addEventListener('scroll', handleNavigationScroll);

    // Run once on page load to set initial state
    handleNavigationScroll();

    // ================================================
    // Scroll Reveal Animations
    // ================================================
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: stop observing after reveal
                // observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(function(element) {
        revealOnScroll.observe(element);
    });

    // ================================================
    // Stats Counter Animation
    // ================================================
    const statNumbers = document.querySelectorAll('.stat-number');
    let countersAnimated = false;

    function animateCounter(element) {
        const target = parseInt(element.textContent.replace(/\D/g, ''));
        const suffix = element.textContent.replace(/[0-9]/g, '');
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60 FPS
        let current = 0;

        const timer = setInterval(function() {
            current += increment;
            if (current >= target) {
                element.textContent = target.toLocaleString() + suffix;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current).toLocaleString() + suffix;
            }
        }, 16);
    }

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        const statsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !countersAnimated) {
                    countersAnimated = true;
                    statNumbers.forEach(function(stat) {
                        animateCounter(stat);
                    });
                }
            });
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }

    // ================================================
    // Video Hero - Ensure Video Plays
    // ================================================
    const heroVideo = document.querySelector('.video-hero video');
    if (heroVideo) {
        // Ensure video plays on mobile devices
        heroVideo.play().catch(function(error) {
            console.log('Video autoplay prevented:', error);
        });

        // Fallback: show poster image if video fails
        heroVideo.addEventListener('error', function() {
            console.log('Video failed to load');
            const videoHero = document.querySelector('.video-hero');
            videoHero.style.background = 'linear-gradient(135deg, rgba(0, 64, 128, 0.9) 0%, rgba(0, 86, 163, 0.8) 100%), url("img/back.jpg") center/cover';
        });
    }

    // ================================================
    // Smooth Scroll for Scroll Indicator
    // ================================================
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.addEventListener('click', function() {
            const introSection = document.querySelector('.intro-section');
            if (introSection) {
                introSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    }

    // ================================================
    // Newsletter Form Submission
    // ================================================
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value;

            if (email) {
                // Here you would implement actual newsletter subscription
                alert('Thank you for subscribing! You will receive updates at ' + email);
                emailInput.value = '';
            }
        });
    }

    // ================================================
    // Enhanced Card Hover Effects
    // ================================================
    const cards = document.querySelectorAll('.card, .program-card, .news-card');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // ================================================
    // Icon Card Interactions
    // ================================================
    const iconCards = document.querySelectorAll('.icon-card');
    iconCards.forEach(function(card, index) {
        // Stagger animation delay
        card.style.animationDelay = (index * 0.1) + 's';

        card.addEventListener('mouseenter', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1.1) rotate(5deg)';
            }
        });

        card.addEventListener('mouseleave', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });

    // ================================================
    // Parallax Effect - DISABLED for professional look
    // ================================================
    // const videoHeroContent = document.querySelector('.video-hero-content');
    // if (videoHeroContent) {
    //     window.addEventListener('scroll', function() {
    //         const scrolled = window.pageYOffset;
    //         const parallaxSpeed = 0.5;

    //         if (scrolled < window.innerHeight) {
    //             videoHeroContent.style.transform = 'translateY(' + (scrolled * parallaxSpeed) + 'px)';
    //             videoHeroContent.style.opacity = 1 - (scrolled / 600);
    //         }
    //     });
    // }

    // ================================================
    // Dynamic Active State for Navigation
    // ================================================
    function updateActiveNavigation() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

        window.addEventListener('scroll', function() {
            let current = '';

            sections.forEach(function(section) {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;

                if (pageYOffset >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(function(link) {
                link.classList.remove('active');
                if (link.getAttribute('href').slice(1) === current) {
                    link.classList.add('active');
                }
            });
        });
    }

    // ================================================
    // Load More News (if applicable)
    // ================================================
    const loadMoreBtn = document.querySelector('.load-more-news');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            // Here you would implement loading more news items
            console.log('Loading more news...');
        });
    }

    // ================================================
    // Mobile Navigation Enhancement
    // ================================================
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileToggle && mainNav) {
        // Close mobile menu when clicking on a link
        const mobileNavLinks = mainNav.querySelectorAll('a');
        mobileNavLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                // Only close if it's not a dropdown parent
                if (!this.nextElementSibling || this.nextElementSibling.classList.contains('dropdown')) {
                    return;
                }

                if (window.innerWidth <= 968) {
                    mainNav.classList.remove('active');
                    mobileToggle.classList.remove('active');
                }
            });
        });
    }

    // ================================================
    // Lazy Loading for Images
    // ================================================
    if ('loading' in HTMLImageElement.prototype) {
        // Browser supports native lazy loading
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(function(img) {
            img.src = img.dataset.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const images = document.querySelectorAll('img[data-src]');

        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // ================================================
    // Accessibility: Keyboard Navigation
    // ================================================
    const focusableElements = document.querySelectorAll('a, button, input, textarea, select');
    focusableElements.forEach(function(element) {
        element.addEventListener('focus', function() {
            this.style.outline = '2px solid var(--primary-blue)';
            this.style.outlineOffset = '2px';
        });

        element.addEventListener('blur', function() {
            this.style.outline = '';
        });
    });

    // ================================================
    // Performance: Reduce Motion for Users Who Prefer It
    // ================================================
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (prefersReducedMotion.matches) {
        // Disable animations for users who prefer reduced motion
        document.body.style.setProperty('--transition', 'none');

        // Remove reveal animations
        revealElements.forEach(function(element) {
            element.classList.add('active');
        });
    }

    // ================================================
    // Console Welcome Message
    // ================================================
    console.log('%cWelcome to TIU!', 'color: #004080; font-size: 24px; font-weight: bold;');
    console.log('%cTashkent International University', 'color: #666; font-size: 14px;');
    console.log('%cBuilding Tomorrow\'s Leaders', 'color: #d4af37; font-size: 12px;');

});

// ================================================
// Utility Functions
// ================================================

// Smooth scroll to element
function scrollToElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Show loading spinner
function showLoading() {
    const loader = document.createElement('div');
    loader.className = 'loading-spinner';
    loader.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    document.body.appendChild(loader);
}

// Hide loading spinner
function hideLoading() {
    const loader = document.querySelector('.loading-spinner');
    if (loader) {
        loader.remove();
    }
}

// Format number with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Debounce function for performance
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

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
