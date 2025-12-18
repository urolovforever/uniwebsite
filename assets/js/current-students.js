// Current Students Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Academic calendar filter
    const calendarFilter = document.getElementById('calendar-filter');
    if (calendarFilter) {
        calendarFilter.addEventListener('change', function() {
            const filterValue = this.value;
            filterCalendarEvents(filterValue);
        });
    }

    // Timetable view switcher
    const viewButtons = document.querySelectorAll('.view-btn');
    viewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const view = this.dataset.view;
            switchTimetableView(view);
        });
    });

    // Library search
    const librarySearch = document.getElementById('library-search');
    if (librarySearch) {
        librarySearch.addEventListener('input', debounce(function() {
            const query = this.value;
            searchLibraryResources(query);
        }, 300));
    }

    // Club filter
    const clubFilters = document.querySelectorAll('.club-filter');
    clubFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const category = this.dataset.category;
            filterClubs(category);

            clubFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Sports facility booking
    const bookingButtons = document.querySelectorAll('.book-facility-btn');
    bookingButtons.forEach(button => {
        button.addEventListener('click', function() {
            const facilityId = this.dataset.facilityId;
            openBookingModal(facilityId);
        });
    });

    // Housing application
    const applyButtons = document.querySelectorAll('.apply-housing-btn');
    applyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const housingType = this.dataset.housingType;
            submitHousingApplication(housingType);
        });
    });

    // LMS quick access
    const lmsLinks = document.querySelectorAll('.lms-link');
    lmsLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const course = this.dataset.course;
            openLMSCourse(course);
        });
    });

    // Exam schedule countdown
    updateExamCountdowns();
    setInterval(updateExamCountdowns, 60000); // Update every minute

    // Grade calculator
    const gradeInputs = document.querySelectorAll('.grade-input');
    gradeInputs.forEach(input => {
        input.addEventListener('input', calculateGPA);
    });

    // Cafeteria menu
    loadCafeteriaMenu();

    // IT Services ticket system
    const ticketForm = document.getElementById('it-ticket-form');
    if (ticketForm) {
        ticketForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitITTicket();
        });
    }

    // Student union events
    loadStudentUnionEvents();

    // Animate cards on scroll
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

    document.querySelectorAll('.quick-link-card, .club-card, .facility-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.5s ease';
        cardObserver.observe(card);
    });
});

function filterCalendarEvents(filter) {
    const events = document.querySelectorAll('.calendar-event');
    events.forEach(event => {
        if (filter === 'all' || event.dataset.category === filter) {
            event.style.display = 'flex';
        } else {
            event.style.display = 'none';
        }
    });
}

function switchTimetableView(view) {
    const timetable = document.getElementById('timetable');
    if (!timetable) return;

    timetable.dataset.view = view;
    // Implementation for different timetable views (day, week, month)
    console.log('Switching to', view, 'view');
}

function searchLibraryResources(query) {
    console.log('Searching library for:', query);
    // Implementation for library search
}

function filterClubs(category) {
    const clubs = document.querySelectorAll('.club-card');
    clubs.forEach(club => {
        if (category === 'all' || club.dataset.category === category) {
            club.style.display = 'block';
        } else {
            club.style.display = 'none';
        }
    });
}

function openBookingModal(facilityId) {
    console.log('Opening booking modal for facility:', facilityId);
    // Implementation for facility booking modal
}

function submitHousingApplication(housingType) {
    console.log('Submitting housing application for:', housingType);
    alert('Housing application submitted successfully!');
}

function openLMSCourse(course) {
    console.log('Opening LMS course:', course);
    // Redirect to LMS or open in new tab
    window.open(`/lms/course/${course}`, '_blank');
}

function updateExamCountdowns() {
    const countdownElements = document.querySelectorAll('[data-exam-date]');
    countdownElements.forEach(element => {
        const examDate = new Date(element.dataset.examDate);
        const now = new Date();
        const diff = examDate - now;

        if (diff > 0) {
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            element.textContent = `${days} days, ${hours} hours`;
        } else {
            element.textContent = 'Exam in progress or completed';
        }
    });
}

function calculateGPA() {
    const gradeInputs = document.querySelectorAll('.grade-input');
    let totalPoints = 0;
    let totalCredits = 0;

    gradeInputs.forEach(input => {
        const grade = parseFloat(input.value) || 0;
        const credits = parseFloat(input.dataset.credits) || 0;
        totalPoints += grade * credits;
        totalCredits += credits;
    });

    const gpa = totalCredits > 0 ? (totalPoints / totalCredits).toFixed(2) : 0;
    const gpaDisplay = document.getElementById('gpa-display');
    if (gpaDisplay) {
        gpaDisplay.textContent = gpa;
    }
}

function loadCafeteriaMenu() {
    // Implementation for loading cafeteria menu
    console.log('Loading cafeteria menu');
}

function submitITTicket() {
    const form = document.getElementById('it-ticket-form');
    if (!form) return;

    const formData = new FormData(form);
    console.log('Submitting IT ticket:', Object.fromEntries(formData));
    alert('IT support ticket submitted successfully!');
    form.reset();
}

function loadStudentUnionEvents() {
    // Implementation for loading student union events
    console.log('Loading student union events');
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
window.CurrentStudentsModule = {
    filterCalendarEvents,
    switchTimetableView,
    searchLibraryResources,
    filterClubs,
    calculateGPA
};
