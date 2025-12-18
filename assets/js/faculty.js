// Faculty Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Faculty search and filter
    const searchInput = document.getElementById('faculty-search');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(function() {
            const query = this.value.toLowerCase();
            filterFaculty(query);
        }, 300));
    }

    // Department filter
    const deptFilters = document.querySelectorAll('.dept-filter');
    deptFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const dept = this.dataset.department;
            filterByDepartment(dept);

            deptFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Faculty profile modal
    const profileButtons = document.querySelectorAll('.view-profile-btn');
    profileButtons.forEach(button => {
        button.addEventListener('click', function() {
            const facultyId = this.dataset.facultyId;
            openFacultyProfile(facultyId);
        });
    });

    // Research interests filter
    const researchFilters = document.querySelectorAll('.research-filter');
    researchFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const topic = this.dataset.topic;
            filterByResearchTopic(topic);
        });
    });

    // Sort faculty
    const sortSelect = document.getElementById('faculty-sort');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const sortBy = this.value;
            sortFaculty(sortBy);
        });
    }

    // Animate cards
    animateFacultyCards();
});

function filterFaculty(query) {
    const cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(card => {
        const name = card.querySelector('.faculty-name').textContent.toLowerCase();
        const dept = card.querySelector('.faculty-department').textContent.toLowerCase();
        const specializations = card.querySelector('.faculty-specialization')?.textContent.toLowerCase() || '';

        if (name.includes(query) || dept.includes(query) || specializations.includes(query)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterByDepartment(dept) {
    const cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(card => {
        if (dept === 'all' || card.dataset.department === dept) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterByResearchTopic(topic) {
    const cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(card => {
        const research = card.dataset.research || '';
        if (topic === 'all' || research.includes(topic)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function sortFaculty(sortBy) {
    const container = document.querySelector('.faculty-directory');
    if (!container) return;

    const cards = Array.from(document.querySelectorAll('.faculty-member-card'));

    cards.sort((a, b) => {
        if (sortBy === 'name') {
            const nameA = a.querySelector('.faculty-name').textContent;
            const nameB = b.querySelector('.faculty-name').textContent;
            return nameA.localeCompare(nameB);
        } else if (sortBy === 'department') {
            const deptA = a.dataset.department || '';
            const deptB = b.dataset.department || '';
            return deptA.localeCompare(deptB);
        }
        return 0;
    });

    cards.forEach(card => container.appendChild(card));
}

function openFacultyProfile(facultyId) {
    console.log('Opening faculty profile:', facultyId);
    // Implementation for opening faculty profile modal or page
}

function animateFacultyCards() {
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

    document.querySelectorAll('.faculty-member-card, .department-card').forEach((card, index) => {
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
window.FacultyModule = {
    filterFaculty,
    filterByDepartment,
    sortFaculty
};
