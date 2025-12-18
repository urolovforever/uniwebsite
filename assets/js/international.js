// International Students Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Country filter and search
    const countryFilter = document.getElementById('country-filter');
    if (countryFilter) {
        countryFilter.addEventListener('change', function() {
            const selectedCountry = this.value;
            filterByCountry(selectedCountry);
        });
    }

    // Visa requirements checker
    const visaChecker = document.getElementById('visa-checker');
    if (visaChecker) {
        visaChecker.addEventListener('submit', function(e) {
            e.preventDefault();
            const country = document.getElementById('student-country').value;
            showVisaRequirements(country);
        });
    }

    // Accommodation comparison
    const accommodationCards = document.querySelectorAll('.accommodation-card');
    const compareAccommodation = [];

    accommodationCards.forEach(card => {
        const compareBtn = card.querySelector('.compare-btn');
        if (compareBtn) {
            compareBtn.addEventListener('click', function() {
                const accommodationId = card.dataset.accommodationId;
                toggleAccommodationComparison(accommodationId);
            });
        }
    });

    // Partner university search
    const partnerSearch = document.getElementById('partner-search');
    if (partnerSearch) {
        partnerSearch.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const partnerCards = document.querySelectorAll('.partner-card');

            partnerCards.forEach(card => {
                const name = card.querySelector('.partner-name').textContent.toLowerCase();
                const location = card.querySelector('.partner-location').textContent.toLowerCase();

                if (name.includes(searchTerm) || location.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // Exchange program calculator
    const exchangeCalculator = document.getElementById('exchange-calculator');
    if (exchangeCalculator) {
        exchangeCalculator.addEventListener('submit', function(e) {
            e.preventDefault();
            calculateExchangeCosts();
        });
    }

    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px'
    };

    const elementsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.country-card, .partner-card, .testimonial-card').forEach(el => {
        elementsObserver.observe(el);
    });

    // Testimonials carousel
    initTestimonialsCarousel();

    // Language support toggle
    const languageButtons = document.querySelectorAll('.language-support-btn');
    languageButtons.forEach(button => {
        button.addEventListener('click', function() {
            const language = this.dataset.language;
            showLanguageSupport(language);
        });
    });
});

function filterByCountry(country) {
    const cards = document.querySelectorAll('[data-country]');
    cards.forEach(card => {
        if (country === 'all' || card.dataset.country === country) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function showVisaRequirements(country) {
    const requirementsDiv = document.getElementById('visa-requirements-result');
    if (!requirementsDiv) return;

    // Simulated visa requirements data
    const requirements = {
        default: [
            'Valid passport (at least 6 months validity)',
            'Acceptance letter from TIU',
            'Proof of financial support',
            'Medical certificate',
            'Police clearance certificate',
            'Passport-sized photos (3x4 cm)',
            'Completed visa application form'
        ]
    };

    const countryReqs = requirements[country] || requirements.default;

    requirementsDiv.innerHTML = `
        <h3>Visa Requirements for ${country || 'International Students'}</h3>
        <ul class="requirements-list">
            ${countryReqs.map(req => `<li><i class="fas fa-check"></i> ${req}</li>`).join('')}
        </ul>
    `;
    requirementsDiv.style.display = 'block';
}

function toggleAccommodationComparison(accommodationId) {
    console.log('Toggle accommodation comparison:', accommodationId);
    // Implementation for accommodation comparison
}

function calculateExchangeCosts() {
    const duration = parseInt(document.getElementById('exchange-duration').value) || 0;
    const accommodation = document.getElementById('exchange-accommodation').value;

    const baseCosts = {
        dormitory: 200,
        apartment: 400,
        homestay: 350
    };

    const monthlyCost = baseCosts[accommodation] || 300;
    const totalCost = duration * monthlyCost;

    const resultDiv = document.getElementById('cost-result');
    if (resultDiv) {
        resultDiv.innerHTML = `
            <h3>Estimated Cost</h3>
            <p><strong>Duration:</strong> ${duration} months</p>
            <p><strong>Monthly Cost:</strong> $${monthlyCost}</p>
            <p><strong>Total Cost:</strong> $${totalCost.toLocaleString()}</p>
        `;
        resultDiv.style.display = 'block';
    }
}

function initTestimonialsCarousel() {
    const testimonials = document.querySelectorAll('.testimonial-card');
    let currentIndex = 0;

    if (testimonials.length === 0) return;

    setInterval(() => {
        testimonials[currentIndex].style.opacity = '0';
        currentIndex = (currentIndex + 1) % testimonials.length;
        testimonials[currentIndex].style.opacity = '1';
    }, 5000);
}

function showLanguageSupport(language) {
    console.log('Showing language support for:', language);
    // Implementation for showing language support resources
}

// Export functions
window.InternationalModule = {
    filterByCountry,
    showVisaRequirements,
    calculateExchangeCosts
};
