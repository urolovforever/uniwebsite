// ================================================
// TIU Website - Main JavaScript
// Tashkent International University
// ================================================

document.addEventListener('DOMContentLoaded', function() {

    // ================================================
    // Mobile Menu Toggle
    // ================================================
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            this.classList.toggle('active');
        });
    }

    // ================================================
    // Mobile Dropdown Toggle
    // ================================================
    const dropdownParents = document.querySelectorAll('.nav-menu > li > a');

    dropdownParents.forEach(function(link) {
        link.addEventListener('click', function(e) {
            // Only prevent default on mobile
            if (window.innerWidth <= 968) {
                const parentLi = this.parentElement;
                const hasDropdown = parentLi.querySelector('.dropdown');

                if (hasDropdown) {
                    e.preventDefault();
                    parentLi.classList.toggle('active');
                }
            }
        });
    });

    // Sub-dropdown toggle for mobile
    const subDropdownParents = document.querySelectorAll('.dropdown > li > a');

    subDropdownParents.forEach(function(link) {
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 968) {
                const parentLi = this.parentElement;
                const hasSubDropdown = parentLi.querySelector('.sub-dropdown');

                if (hasSubDropdown) {
                    e.preventDefault();
                    parentLi.classList.toggle('active');
                }
            }
        });
    });

    // ================================================
    // Language Switcher
    // ================================================
    const langButtons = document.querySelectorAll('.lang-btn');

    langButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            langButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Here you would implement actual language switching logic
            const lang = this.getAttribute('data-lang');
            console.log('Language switched to:', lang);
        });
    });

    // ================================================
    // Smooth Scroll for Anchor Links
    // ================================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // ================================================
    // Sticky Header on Scroll
    // ================================================
    const header = document.querySelector('.main-header');
    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // ================================================
    // Close mobile menu when clicking outside
    // ================================================
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 968) {
            if (!e.target.closest('.main-nav') && !e.target.closest('.mobile-toggle')) {
                mainNav.classList.remove('active');
                mobileToggle.classList.remove('active');
            }
        }
    });

    // ================================================
    // Form Validation (for contact forms, application forms, etc.)
    // ================================================
    const forms = document.querySelectorAll('.tiu-form');

    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Basic validation
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');

            inputs.forEach(function(input) {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });

            if (isValid) {
                console.log('Form is valid, submitting...');
                // Here you would implement actual form submission
                alert('Form submitted successfully! (This is a demo)');
            } else {
                alert('Please fill in all required fields.');
            }
        });
    });

    // ================================================
    // Active Navigation Highlight
    // ================================================
    function highlightActiveNav() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-menu a');

        navLinks.forEach(function(link) {
            const linkPath = new URL(link.href).pathname;
            if (linkPath === currentPath) {
                link.classList.add('active');
            }
        });
    }

    highlightActiveNav();

    // ================================================
    // Image Lazy Loading (for better performance)
    // ================================================
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img.lazy').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // ================================================
    // Back to Top Button
    // ================================================
    const backToTop = document.querySelector('.back-to-top');

    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

});

// ================================================
// Utility Functions
// ================================================

// Toggle dropdown programmatically
function toggleDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    if (dropdown) {
        dropdown.classList.toggle('active');
    }
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(function() {
        notification.remove();
    }, 3000);
}
