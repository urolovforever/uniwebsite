// About Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Animate stats on scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    };

    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all stat numbers
    document.querySelectorAll('.stat-number').forEach(stat => {
        statsObserver.observe(stat);
    });

    // Animate timeline items
    const timelineObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateX(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.timeline-item').forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-30px)';
        item.style.transition = 'all 0.6s ease';
        timelineObserver.observe(item);
    });

    // Leadership card hover effects
    document.querySelectorAll('.leader-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Campus map interactive features
    const buildingItems = document.querySelectorAll('.building-item');
    buildingItems.forEach(item => {
        item.addEventListener('click', function() {
            buildingItems.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
});

function animateStats(element) {
    const targetText = element.textContent;
    const targetNumber = parseInt(targetText.replace(/[^0-9]/g, ''));
    const suffix = targetText.replace(/[0-9]/g, '');
    const duration = 2000;
    const steps = 60;
    const stepValue = targetNumber / steps;
    let currentNumber = 0;
    let currentStep = 0;

    const timer = setInterval(() => {
        currentStep++;
        currentNumber = Math.min(Math.floor(stepValue * currentStep), targetNumber);
        element.textContent = currentNumber.toLocaleString() + suffix;

        if (currentStep >= steps) {
            clearInterval(timer);
            element.textContent = targetText;
        }
    }, duration / steps);
}

// Export functions for use in other scripts
window.AboutModule = {
    animateStats
};
