// ================================================
// TIU Website - Main JavaScript (Minimal & Clean)
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

});
