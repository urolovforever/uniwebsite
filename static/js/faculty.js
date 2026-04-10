// Faculty Directory JavaScript

var ITEMS_PER_PAGE = 6;
var currentPage = 1;

document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('faculty-search');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(function() {
            currentPage = 1;
            applyFilters();
        }, 300));
    }

    var deptSelect = document.getElementById('dept-filter');
    if (deptSelect) {
        deptSelect.addEventListener('change', function() {
            currentPage = 1;
            applyFilters();
        });
    }

    var roleSelect = document.getElementById('role-filter');
    if (roleSelect) {
        roleSelect.addEventListener('change', function() {
            currentPage = 1;
            applyFilters();
        });
    }

    var resetBtn = document.getElementById('reset-filters');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetAllFilters);
    }

    var resetLink = document.getElementById('reset-filters-link');
    if (resetLink) {
        resetLink.addEventListener('click', resetAllFilters);
    }

    if (document.getElementById('faculty-list')) {
        applyFilters();
    }
});

// Accordion toggle for leader-style profiles
function toggleLeaderBio(btn) {
    var content = btn.parentElement.querySelector('.leader-accordion-content');
    var icon = btn.querySelector('i');
    btn.classList.toggle('active');
    content.classList.toggle('show');
    if (content.classList.contains('show')) {
        content.style.maxHeight = content.scrollHeight + 'px';
        if (icon) icon.style.transform = 'rotate(180deg)';
    } else {
        content.style.maxHeight = '0';
        if (icon) icon.style.transform = 'rotate(0)';
    }
}

function getFilteredItems() {
    var searchInput = document.getElementById('faculty-search');
    var deptSelect = document.getElementById('dept-filter');
    var roleSelect = document.getElementById('role-filter');

    var query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    var dept = deptSelect ? deptSelect.value : 'all';
    var role = roleSelect ? roleSelect.value : 'all';

    var allItems = document.querySelectorAll('#faculty-list .faculty-item');
    var filtered = [];

    allItems.forEach(function(item) {
        var name = item.dataset.name || '';
        var title = item.dataset.title || '';
        var itemDept = item.dataset.department || '';
        var itemJobtitle = item.dataset.jobtitle || '';

        var matchesSearch = !query || name.includes(query) || title.includes(query) || itemDept.toLowerCase().includes(query);
        var matchesDept = dept === 'all' || itemDept === dept;
        var matchesRole = role === 'all' || itemJobtitle === role;

        if (matchesSearch && matchesDept && matchesRole) {
            filtered.push(item);
        }
    });

    return filtered;
}

function applyFilters() {
    var allItems = document.querySelectorAll('#faculty-list .faculty-item');
    var filtered = getFilteredItems();
    var noResults = document.getElementById('no-results');
    var resultsCount = document.getElementById('results-count');
    var totalFiltered = filtered.length;

    allItems.forEach(function(item) {
        item.style.display = 'none';
    });

    var totalPages = Math.ceil(totalFiltered / ITEMS_PER_PAGE);
    if (currentPage > totalPages) currentPage = totalPages;
    if (currentPage < 1) currentPage = 1;

    var startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    var endIndex = startIndex + ITEMS_PER_PAGE;

    for (var i = startIndex; i < endIndex && i < totalFiltered; i++) {
        filtered[i].style.display = '';
    }

    if (noResults) {
        noResults.style.display = totalFiltered === 0 && allItems.length > 0 ? 'flex' : 'none';
    }

    if (resultsCount) {
        if (totalFiltered > 0) {
            var showingStart = startIndex + 1;
            var showingEnd = Math.min(endIndex, totalFiltered);
            resultsCount.textContent = showingStart + '–' + showingEnd + ' / ' + totalFiltered;
        } else {
            resultsCount.textContent = '';
        }
    }

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
    html += '<button class="pagination-btn' + (currentPage === 1 ? ' disabled' : '') + '" data-page="prev"' + (currentPage === 1 ? ' disabled' : '') + '><i class="fas fa-chevron-left"></i></button>';

    html += '<div class="pagination-numbers">';
    for (var i = 1; i <= totalPages; i++) {
        html += '<button class="pagination-num' + (i === currentPage ? ' active' : '') + '" data-page="' + i + '">' + i + '</button>';
    }
    html += '</div>';

    html += '<button class="pagination-btn' + (currentPage === totalPages ? ' disabled' : '') + '" data-page="next"' + (currentPage === totalPages ? ' disabled' : '') + '><i class="fas fa-chevron-right"></i></button>';

    container.innerHTML = html;

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
            var section = document.querySelector('.fdir-filters-bar');
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
