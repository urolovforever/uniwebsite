// ================================================
// COOL MODERN EFFECTS FOR TIU WEBSITE
// ================================================

document.addEventListener('DOMContentLoaded', function() {

    // ================================================
    // Page Loader
    // ================================================
    window.addEventListener('load', function() {
        const loader = document.querySelector('.page-loader');
        if (loader) {
            setTimeout(() => {
                loader.classList.add('hidden');
                setTimeout(() => {
                    loader.style.display = 'none';
                }, 500);
            }, 1000);
        }
    });

    // ================================================
    // Scroll Progress Bar
    // ================================================
    function createScrollProgress() {
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', function() {
            const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = (window.pageYOffset / windowHeight) * 100;
            progressBar.style.width = scrolled + '%';
        });
    }
    createScrollProgress();

    // ================================================
    // Particle Effect for Hero Section - DISABLED FOR PROFESSIONAL LOOK
    // ================================================
    // function createParticles() {
    //     const hero = document.querySelector('.video-hero');
    //     if (!hero) return;

    //     const particlesContainer = document.createElement('div');
    //     particlesContainer.className = 'particles';
    //     hero.appendChild(particlesContainer);

    //     for (let i = 0; i < 50; i++) {
    //         const particle = document.createElement('div');
    //         particle.className = 'particle';
    //         particle.style.left = Math.random() * 100 + '%';
    //         particle.style.animationDelay = Math.random() * 15 + 's';
    //         particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
    //         particlesContainer.appendChild(particle);
    //     }
    // }
    // createParticles();

    // ================================================
    // Animated Background Gradients - DISABLED FOR PROFESSIONAL LOOK
    // ================================================
    // function createAnimatedBackground() {
    //     const hero = document.querySelector('.video-hero');
    //     if (!hero) return;

    //     const bgDiv = document.createElement('div');
    //     bgDiv.className = 'hero-animated-bg';

    //     for (let i = 0; i < 3; i++) {
    //         const circle = document.createElement('div');
    //         circle.className = 'gradient-circle';
    //         bgDiv.appendChild(circle);
    //     }

    //     hero.insertBefore(bgDiv, hero.firstChild);
    // }
    // createAnimatedBackground();

    // ================================================
    // Enhanced Navigation Interactions
    // ================================================
    const navLinks = document.querySelectorAll('.nav-menu > li > a');

    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });

        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // ================================================
    // Language Switcher Enhanced Interaction
    // ================================================
    const langButtons = document.querySelectorAll('.lang-btn');

    langButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove active from all
            langButtons.forEach(b => b.classList.remove('active'));

            // Add active to clicked
            this.classList.add('active');

            // Get selected language
            const selectedLang = this.getAttribute('data-lang');

            // Create notification
            showNotification(`Language changed to ${selectedLang.toUpperCase()}`, 'success');

            // Here you would implement actual language switching
            console.log('Language switched to:', selectedLang);
        });

        // Add ripple effect
        btn.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');

            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // ================================================
    // Enhanced Card Interactions - SIMPLIFIED FOR PROFESSIONAL LOOK
    // ================================================
    const cards = document.querySelectorAll('.card, .news-card, .icon-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            // Simple hover effect - just lift the card
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });

    // ================================================
    // Notification System
    // ================================================
    window.showNotification = function(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i>
                <span>${message}</span>
            </div>
        `;

        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: ${type === 'success' ? '#10b981' : '#004080'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            z-index: 99999;
            animation: slideInRight 0.5s ease;
            font-weight: 500;
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.5s ease';
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    };

    // Add notification animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            animation: rippleEffect 0.6s ease-out;
            pointer-events: none;
        }
        @keyframes rippleEffect {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
        .notification-content {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .notification-content i {
            font-size: 1.25rem;
        }
    `;
    document.head.appendChild(style);

    // ================================================
    // Smooth Parallax Effect
    // ================================================
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;

        parallaxElements.forEach(element => {
            const speed = element.getAttribute('data-parallax') || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });

    // ================================================
    // Typing Effect for Hero Text
    // ================================================
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.textContent = '';

        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }

        type();
    }

    // ================================================
    // Enhanced Scroll Reveal with Stagger
    // ================================================
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('active');
                }, index * 100);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(element => {
        revealObserver.observe(element);
    });

    // ================================================
    // Stats Counter with Easing
    // ================================================
    function animateCounter(element, start, end, duration) {
        const range = end - start;
        const increment = range / (duration / 16);
        let current = start;

        const timer = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
                current = end;
                clearInterval(timer);
            }

            const suffix = element.textContent.replace(/[0-9,]/g, '');
            element.textContent = Math.floor(current).toLocaleString() + suffix;
        }, 16);
    }

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const statNumbers = entry.target.querySelectorAll('.stat-number');
                    statNumbers.forEach(stat => {
                        const text = stat.textContent;
                        const number = parseInt(text.replace(/\D/g, ''));
                        animateCounter(stat, 0, number, 2000);
                    });
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }

    // ================================================
    // CTA Button Magnetic Effect
    // ================================================
    const ctaButtons = document.querySelectorAll('.cta-primary, .cta-gold, .cta-secondary');

    ctaButtons.forEach(button => {
        button.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            this.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });

    // ================================================
    // Custom Cursor (Optional)
    // ================================================
    if (window.innerWidth > 1024) {
        const cursor = document.createElement('div');
        cursor.className = 'cursor-trail';
        document.body.appendChild(cursor);

        let mouseX = 0, mouseY = 0;
        let cursorX = 0, cursorY = 0;

        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });

        function animateCursor() {
            cursorX += (mouseX - cursorX) * 0.1;
            cursorY += (mouseY - cursorY) * 0.1;

            cursor.style.left = cursorX + 'px';
            cursor.style.top = cursorY + 'px';

            requestAnimationFrame(animateCursor);
        }
        animateCursor();

        // Expand cursor on hover over interactive elements
        const interactiveElements = document.querySelectorAll('a, button, .card');
        interactiveElements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                cursor.style.transform = 'scale(2)';
            });
            element.addEventListener('mouseleave', () => {
                cursor.style.transform = 'scale(1)';
            });
        });
    }

    // ================================================
    // Image Lazy Loading with Blur Effect
    // ================================================
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.filter = 'blur(10px)';
                img.src = img.dataset.src;

                img.addEventListener('load', () => {
                    img.style.transition = 'filter 0.5s';
                    img.style.filter = 'blur(0)';
                });

                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // ================================================
    // Smooth Anchor Scrolling
    // ================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offset = 80; // Account for fixed header
                    const targetPosition = target.offsetTop - offset;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ================================================
    // Console Easter Egg
    // ================================================
    console.log('%c🎓 Tashkent International University', 'color: #004080; font-size: 24px; font-weight: bold;');
    console.log('%cWelcome to TIU Website!', 'color: #d4af37; font-size: 16px;');
    console.log('%cBuilt with ❤️ for excellence in education', 'color: #666; font-size: 12px;');

    // ================================================
    // Performance Monitoring
    // ================================================
    if (window.performance && window.performance.timing) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const perfData = window.performance.timing;
                const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log(`%cPage loaded in ${pageLoadTime}ms`, 'color: #10b981; font-weight: bold;');
            }, 0);
        });
    }

});

// ================================================
// Utility Functions
// ================================================

// Debounce function
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

// Throttle function
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

// Check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
