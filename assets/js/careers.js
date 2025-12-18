// Careers & Alumni Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Job search and filter
    const jobSearch = document.getElementById('job-search');
    if (jobSearch) {
        jobSearch.addEventListener('input', debounce(function() {
            const query = this.value.toLowerCase();
            filterJobs(query);
        }, 300));
    }

    // Job type filter
    const jobTypeFilters = document.querySelectorAll('.job-type-filter');
    jobTypeFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const type = this.dataset.type;
            filterByJobType(type);

            jobTypeFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Apply for job
    const applyButtons = document.querySelectorAll('.apply-job-btn');
    applyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const jobId = this.dataset.jobId;
            applyForJob(jobId);
        });
    });

    // Internship application
    const internshipButtons = document.querySelectorAll('.apply-internship-btn');
    internshipButtons.forEach(button => {
        button.addEventListener('click', function() {
            const internshipId = this.dataset.internshipId;
            applyForInternship(internshipId);
        });
    });

    // Alumni directory search
    const alumniSearch = document.getElementById('alumni-search');
    if (alumniSearch) {
        alumniSearch.addEventListener('input', debounce(function() {
            const query = this.value.toLowerCase();
            filterAlumni(query);
        }, 300));
    }

    // Career counseling booking
    const counselingBtn = document.getElementById('book-counseling-btn');
    if (counselingBtn) {
        counselingBtn.addEventListener('click', openCounselingBooking);
    }

    // Resume builder
    const resumeBuilderBtn = document.getElementById('resume-builder-btn');
    if (resumeBuilderBtn) {
        resumeBuilderBtn.addEventListener('click', openResumeBuilder);
    }

    // Networking events
    loadNetworkingEvents();

    // Salary insights calculator
    const salaryCalculator = document.getElementById('salary-calculator');
    if (salaryCalculator) {
        salaryCalculator.addEventListener('submit', function(e) {
            e.preventDefault();
            calculateSalaryInsights();
        });
    }

    // Animate cards
    animateCareerCards();

    // Job alerts subscription
    const alertsForm = document.getElementById('job-alerts-form');
    if (alertsForm) {
        alertsForm.addEventListener('submit', function(e) {
            e.preventDefault();
            subscribeToJobAlerts();
        });
    }
});

function filterJobs(query) {
    const listings = document.querySelectorAll('.job-listing');
    listings.forEach(listing => {
        const title = listing.querySelector('.job-title').textContent.toLowerCase();
        const company = listing.querySelector('.company-name').textContent.toLowerCase();

        if (title.includes(query) || company.includes(query)) {
            listing.style.display = 'block';
        } else {
            listing.style.display = 'none';
        }
    });
}

function filterByJobType(type) {
    const listings = document.querySelectorAll('.job-listing');
    listings.forEach(listing => {
        if (type === 'all' || listing.dataset.type === type) {
            listing.style.display = 'block';
        } else {
            listing.style.display = 'none';
        }
    });
}

function applyForJob(jobId) {
    console.log('Applying for job:', jobId);
    // Implementation for job application
    if (confirm('Do you want to apply for this position?')) {
        alert('Application submitted successfully! We will contact you soon.');
    }
}

function applyForInternship(internshipId) {
    console.log('Applying for internship:', internshipId);
    if (confirm('Do you want to apply for this internship?')) {
        alert('Internship application submitted successfully!');
    }
}

function filterAlumni(query) {
    const cards = document.querySelectorAll('.alumni-card');
    cards.forEach(card => {
        const name = card.querySelector('.alumni-name').textContent.toLowerCase();
        const position = card.querySelector('.alumni-position').textContent.toLowerCase();
        const company = card.querySelector('.alumni-company').textContent.toLowerCase();

        if (name.includes(query) || position.includes(query) || company.includes(query)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function openCounselingBooking() {
    console.log('Opening career counseling booking');
    // Implementation for counseling booking modal
}

function openResumeBuilder() {
    console.log('Opening resume builder');
    window.open('/career-center/resume-builder', '_blank');
}

function loadNetworkingEvents() {
    console.log('Loading networking events');
    // Implementation for loading networking events
}

function calculateSalaryInsights() {
    const field = document.getElementById('salary-field').value;
    const experience = parseInt(document.getElementById('salary-experience').value) || 0;

    // Simulated salary data
    const baseSalaries = {
        'it': 50000,
        'business': 45000,
        'engineering': 55000,
        'law': 60000
    };

    const baseSalary = baseSalaries[field] || 45000;
    const experienceBonus = experience * 3000;
    const estimatedSalary = baseSalary + experienceBonus;

    const resultDiv = document.getElementById('salary-result');
    if (resultDiv) {
        resultDiv.innerHTML = `
            <h3>Estimated Salary Range</h3>
            <p><strong>Field:</strong> ${field.toUpperCase()}</p>
            <p><strong>Experience:</strong> ${experience} years</p>
            <p><strong>Estimated Annual Salary:</strong> $${estimatedSalary.toLocaleString()} - $${(estimatedSalary * 1.2).toLocaleString()}</p>
        `;
        resultDiv.style.display = 'block';
    }
}

function subscribeToJobAlerts() {
    const email = document.getElementById('alert-email').value;
    console.log('Subscribing to job alerts:', email);
    alert('Successfully subscribed to job alerts!');
}

function animateCareerCards() {
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px'
    };

    const cardObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.service-card, .internship-card, .alumni-card').forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.5s ease ${index * 0.05}s`;
        cardObserver.observe(card);
    });
}

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

// Export functions
window.CareersModule = {
    filterJobs,
    filterByJobType,
    filterAlumni,
    calculateSalaryInsights
};
