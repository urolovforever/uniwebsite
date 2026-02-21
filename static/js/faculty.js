// Faculty Section Specific JavaScript

var ITEMS_PER_PAGE = 6;
var currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    // Faculty search
    var searchInput = document.getElementById('faculty-search');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(function() {
            currentPage = 1;
            applyFilters();
        }, 300));
    }

    // Department dropdown filter
    var deptSelect = document.getElementById('dept-filter');
    if (deptSelect) {
        deptSelect.addEventListener('change', function() {
            currentPage = 1;
            applyFilters();
        });
    }

    // Role dropdown filter
    var roleSelect = document.getElementById('role-filter');
    if (roleSelect) {
        roleSelect.addEventListener('change', function() {
            currentPage = 1;
            applyFilters();
        });
    }

    // Reset buttons
    var resetBtn = document.getElementById('reset-filters');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetAllFilters);
    }

    var resetLink = document.getElementById('reset-filters-link');
    if (resetLink) {
        resetLink.addEventListener('click', resetAllFilters);
    }

    // Initial render with pagination
    if (document.getElementById('faculty-list')) {
        applyFilters();
    }

    // Legacy department filter buttons
    var deptFilters = document.querySelectorAll('.dept-filter');
    deptFilters.forEach(function(filter) {
        filter.addEventListener('click', function() {
            var dept = this.dataset.department;
            filterByDepartment(dept);
            deptFilters.forEach(function(f) { f.classList.remove('active'); });
            this.classList.add('active');
        });
    });

    // Faculty profile modal
    var profileButtons = document.querySelectorAll('.view-profile-btn');
    profileButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var facultyId = this.dataset.facultyId;
            openFacultyProfile(facultyId);
        });
    });

    // Research interests filter
    var researchFilters = document.querySelectorAll('.research-filter');
    researchFilters.forEach(function(filter) {
        filter.addEventListener('click', function() {
            var topic = this.dataset.topic;
            filterByResearchTopic(topic);
        });
    });

    // Sort faculty
    var sortSelect = document.getElementById('faculty-sort');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            sortFaculty(this.value);
        });
    }

    // Animate cards (uses shared animateCards from main.js)
    if (typeof animateCards === 'function') {
        animateCards('.faculty-card, .faculty-member-card, .department-card, .faculty-profile-item');
    }
});

// Accordion toggle for directory page
function toggleLeaderBio(btn) {
    var content = btn.parentElement.querySelector('.leader-accordion-content');
    btn.classList.toggle('active');
    content.classList.toggle('show');
}

function getFilteredItems() {
    var searchInput = document.getElementById('faculty-search');
    var deptSelect = document.getElementById('dept-filter');
    var roleSelect = document.getElementById('role-filter');

    var query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    var dept = deptSelect ? deptSelect.value : 'all';
    var role = roleSelect ? roleSelect.value : 'all';

    var allItems = document.querySelectorAll('#faculty-list .faculty-profile-item');
    var filtered = [];

    allItems.forEach(function(item) {
        var name = item.dataset.name || '';
        var title = item.dataset.title || '';
        var itemDept = item.dataset.department || '';
        var itemRole = item.dataset.role || '';

        var matchesSearch = !query || name.includes(query) || title.includes(query) || itemDept.toLowerCase().includes(query);
        var matchesDept = dept === 'all' || itemDept === dept;
        var matchesRole = role === 'all' || itemRole === role;

        if (matchesSearch && matchesDept && matchesRole) {
            filtered.push(item);
        }
    });

    return filtered;
}

function applyFilters() {
    var allItems = document.querySelectorAll('#faculty-list .faculty-profile-item');
    var filtered = getFilteredItems();
    var noResults = document.getElementById('no-results');
    var resultsCount = document.getElementById('results-count');
    var totalFiltered = filtered.length;

    // Hide all items first
    allItems.forEach(function(item) {
        item.style.display = 'none';
    });

    // Calculate pagination
    var totalPages = Math.ceil(totalFiltered / ITEMS_PER_PAGE);
    if (currentPage > totalPages) currentPage = totalPages;
    if (currentPage < 1) currentPage = 1;

    var startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    var endIndex = startIndex + ITEMS_PER_PAGE;

    // Show only current page items
    for (var i = startIndex; i < endIndex && i < totalFiltered; i++) {
        filtered[i].style.display = '';
    }

    // No results state
    if (noResults) {
        noResults.style.display = totalFiltered === 0 && allItems.length > 0 ? 'flex' : 'none';
    }

    // Results count
    if (resultsCount) {
        var showingStart = totalFiltered > 0 ? startIndex + 1 : 0;
        var showingEnd = Math.min(endIndex, totalFiltered);
        resultsCount.textContent = 'Showing ' + showingStart + '–' + showingEnd + ' of ' + totalFiltered + ' member' + (totalFiltered !== 1 ? 's' : '');
    }

    // Render pagination
    renderPagination(totalPages);
}

function renderPagination(totalPages) {
    var container = document.getElementById('pagination');
    if (!container) return;

    if (totalPages <= 1) {
        container.innerHTML = '';
        return;
    }

    var html = '';

    // Previous button
    html += '<button class="pagination-btn' + (currentPage === 1 ? ' disabled' : '') + '" data-page="prev"' + (currentPage === 1 ? ' disabled' : '') + '><i class="fas fa-chevron-left"></i> Previous</button>';

    // Page numbers
    html += '<div class="pagination-numbers">';
    for (var i = 1; i <= totalPages; i++) {
        html += '<button class="pagination-num' + (i === currentPage ? ' active' : '') + '" data-page="' + i + '">' + i + '</button>';
    }
    html += '</div>';

    // Next button
    html += '<button class="pagination-btn' + (currentPage === totalPages ? ' disabled' : '') + '" data-page="next"' + (currentPage === totalPages ? ' disabled' : '') + '>Next <i class="fas fa-chevron-right"></i></button>';

    container.innerHTML = html;

    // Bind click events
    container.querySelectorAll('[data-page]').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var page = this.dataset.page;
            if (page === 'prev' && currentPage > 1) {
                currentPage--;
            } else if (page === 'next' && currentPage < totalPages) {
                currentPage++;
            } else if (page !== 'prev' && page !== 'next') {
                currentPage = parseInt(page);
            }
            applyFilters();
            // Scroll to top of list
            var section = document.querySelector('.faculty-search-section');
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

function resetAllFilters() {
    var searchInput = document.getElementById('faculty-search');
    var deptSelect = document.getElementById('dept-filter');
    var roleSelect = document.getElementById('role-filter');

    if (searchInput) searchInput.value = '';
    if (deptSelect) deptSelect.value = 'all';
    if (roleSelect) roleSelect.value = 'all';

    currentPage = 1;
    applyFilters();
}

function filterFaculty(query) {
    var cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(function(card) {
        var name = card.querySelector('.faculty-name').textContent.toLowerCase();
        var dept = card.querySelector('.faculty-department').textContent.toLowerCase();
        var specializations = card.querySelector('.faculty-specialization');
        var specText = specializations ? specializations.textContent.toLowerCase() : '';

        if (name.includes(query) || dept.includes(query) || specText.includes(query)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterByDepartment(dept) {
    var cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(function(card) {
        if (dept === 'all' || card.dataset.department === dept) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterByResearchTopic(topic) {
    var cards = document.querySelectorAll('.faculty-member-card');
    cards.forEach(function(card) {
        var research = card.dataset.research || '';
        if (topic === 'all' || research.includes(topic)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function sortFaculty(sortBy) {
    var container = document.querySelector('.faculty-directory');
    if (!container) return;

    var cards = Array.from(document.querySelectorAll('.faculty-member-card'));

    cards.sort(function(a, b) {
        if (sortBy === 'name') {
            var nameA = a.querySelector('.faculty-name').textContent;
            var nameB = b.querySelector('.faculty-name').textContent;
            return nameA.localeCompare(nameB);
        } else if (sortBy === 'department') {
            var deptA = a.dataset.department || '';
            var deptB = b.dataset.department || '';
            return deptA.localeCompare(deptB);
        }
        return 0;
    });

    cards.forEach(function(card) { container.appendChild(card); });
}

// Export functions
window.FacultyModule = {
    filterFaculty: filterFaculty,
    filterByDepartment: filterByDepartment,
    sortFaculty: sortFaculty,
    applyFilters: applyFilters,
    resetAllFilters: resetAllFilters
};
