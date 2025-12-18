// Research Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Research area filter
    const areaFilters = document.querySelectorAll('.area-filter');
    areaFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const area = this.dataset.area;
            filterByResearchArea(area);

            areaFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Publication search
    const publicationSearch = document.getElementById('publication-search');
    if (publicationSearch) {
        publicationSearch.addEventListener('input', debounce(function() {
            const query = this.value.toLowerCase();
            searchPublications(query);
        }, 300));
    }

    // Publication year filter
    const yearFilter = document.getElementById('year-filter');
    if (yearFilter) {
        yearFilter.addEventListener('change', function() {
            const year = this.value;
            filterByYear(year);
        });
    }

    // Research center modal
    const centerButtons = document.querySelectorAll('.view-center-btn');
    centerButtons.forEach(button => {
        button.addEventListener('click', function() {
            const centerId = this.dataset.centerId;
            openCenterModal(centerId);
        });
    });

    // Conference registration
    const registerButtons = document.querySelectorAll('.register-conference-btn');
    registerButtons.forEach(button => {
        button.addEventListener('click', function() {
            const conferenceId = this.dataset.conferenceId;
            registerForConference(conferenceId);
        });
    });

    // Innovation project details
    const projectButtons = document.querySelectorAll('.view-project-btn');
    projectButtons.forEach(button => {
        button.addEventListener('click', function() {
            const projectId = this.dataset.projectId;
            openProjectDetails(projectId);
        });
    });

    // Publication download
    const downloadButtons = document.querySelectorAll('.download-publication-btn');
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const publicationId = this.dataset.publicationId;
            downloadPublication(publicationId);
        });
    });

    // Citation format selector
    const citationFormatButtons = document.querySelectorAll('.citation-format-btn');
    citationFormatButtons.forEach(button => {
        button.addEventListener('click', function() {
            const format = this.dataset.format;
            const publicationId = this.dataset.publicationId;
            showCitation(publicationId, format);
        });
    });

    // Research collaboration form
    const collaborationForm = document.getElementById('collaboration-form');
    if (collaborationForm) {
        collaborationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitCollaborationRequest();
        });
    }

    // Impact metrics animation
    animateImpactMetrics();

    // Animate cards
    animateResearchCards();

    // Sort publications
    const sortSelect = document.getElementById('publication-sort');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const sortBy = this.value;
            sortPublications(sortBy);
        });
    }
});

function filterByResearchArea(area) {
    const items = document.querySelectorAll('[data-research-area]');
    items.forEach(item => {
        if (area === 'all' || item.dataset.researchArea === area) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

function searchPublications(query) {
    const publications = document.querySelectorAll('.publication-card');
    publications.forEach(pub => {
        const title = pub.querySelector('.publication-title').textContent.toLowerCase();
        const authors = pub.querySelector('.publication-authors').textContent.toLowerCase();

        if (title.includes(query) || authors.includes(query)) {
            pub.style.display = 'block';
        } else {
            pub.style.display = 'none';
        }
    });
}

function filterByYear(year) {
    const publications = document.querySelectorAll('.publication-card');
    publications.forEach(pub => {
        if (year === 'all' || pub.dataset.year === year) {
            pub.style.display = 'block';
        } else {
            pub.style.display = 'none';
        }
    });
}

function openCenterModal(centerId) {
    console.log('Opening research center details:', centerId);
    // Implementation for center modal
}

function registerForConference(conferenceId) {
    console.log('Registering for conference:', conferenceId);
    if (confirm('Would you like to register for this conference?')) {
        alert('Registration successful! Check your email for confirmation.');
    }
}

function openProjectDetails(projectId) {
    console.log('Opening project details:', projectId);
    // Implementation for project details modal
}

function downloadPublication(publicationId) {
    console.log('Downloading publication:', publicationId);
    alert('Download will start shortly...');
}

function showCitation(publicationId, format) {
    console.log('Showing citation:', publicationId, 'in format:', format);
    // Implementation for citation display
}

function submitCollaborationRequest() {
    const form = document.getElementById('collaboration-form');
    if (!form) return;

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    console.log('Submitting collaboration request:', data);
    alert('Thank you for your interest in collaboration! We will contact you soon.');
    form.reset();
}

function sortPublications(sortBy) {
    const container = document.querySelector('.publications-showcase');
    if (!container) return;

    const publications = Array.from(document.querySelectorAll('.publication-card'));

    publications.sort((a, b) => {
        if (sortBy === 'date') {
            return parseInt(b.dataset.year) - parseInt(a.dataset.year);
        } else if (sortBy === 'citations') {
            return parseInt(b.dataset.citations || 0) - parseInt(a.dataset.citations || 0);
        } else if (sortBy === 'title') {
            const titleA = a.querySelector('.publication-title').textContent;
            const titleB = b.querySelector('.publication-title').textContent;
            return titleA.localeCompare(titleB);
        }
        return 0;
    });

    publications.forEach(pub => container.appendChild(pub));
}

function animateImpactMetrics() {
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };

    const metricsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const numberElement = entry.target.querySelector('.impact-number');
                if (numberElement) {
                    animateNumber(numberElement);
                }
                metricsObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.impact-metric').forEach(metric => {
        metricsObserver.observe(metric);
    });
}

function animateNumber(element) {
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

function animateResearchCards() {
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

    document.querySelectorAll('.research-center-card, .publication-card, .project-card').forEach((card, index) => {
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
window.ResearchModule = {
    filterByResearchArea,
    searchPublications,
    sortPublications
};
