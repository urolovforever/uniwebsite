// News & Media Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // News filter
    const newsFilters = document.querySelectorAll('.news-filter');
    newsFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const category = this.dataset.category;
            filterNews(category);

            newsFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // News search
    const newsSearch = document.getElementById('news-search');
    if (newsSearch) {
        newsSearch.addEventListener('input', debounce(function() {
            const query = this.value.toLowerCase();
            searchNews(query);
        }, 300));
    }

    // Load more news
    const loadMoreBtn = document.getElementById('load-more-news');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', loadMoreNews);
    }

    // Gallery lightbox
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const imageId = this.dataset.imageId;
            openLightbox(imageId);
        });
    });

    // Video player
    const videoThumbnails = document.querySelectorAll('.video-thumbnail');
    videoThumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const videoId = this.dataset.videoId;
            playVideo(videoId);
        });
    });

    // Event registration
    const registerButtons = document.querySelectorAll('.register-event-btn');
    registerButtons.forEach(button => {
        button.addEventListener('click', function() {
            const eventId = this.dataset.eventId;
            registerForEvent(eventId);
        });
    });

    // Social media sharing
    const shareButtons = document.querySelectorAll('.share-btn');
    shareButtons.forEach(button => {
        button.addEventListener('click', function() {
            const platform = this.dataset.platform;
            const url = this.dataset.url;
            shareOnSocialMedia(platform, url);
        });
    });

    // Newsletter subscription
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            subscribeToNewsletter();
        });
    }

    // Calendar view toggle
    const calendarToggle = document.getElementById('calendar-toggle');
    if (calendarToggle) {
        calendarToggle.addEventListener('click', toggleCalendarView);
    }

    // Animate cards (uses shared animateCards from main.js)
    animateCards('.news-card, .event-item');

    // Initialize date filters
    initializeDateFilters();
});

function filterNews(category) {
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function searchNews(query) {
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach(card => {
        const title = card.querySelector('.news-title').textContent.toLowerCase();
        const excerpt = card.querySelector('.news-excerpt').textContent.toLowerCase();

        if (title.includes(query) || excerpt.includes(query)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}


function shareOnSocialMedia(platform, url) {
    const shareUrls = {
        facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`,
        twitter: `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`,
        linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`,
        telegram: `https://t.me/share/url?url=${encodeURIComponent(url)}`
    };

    if (shareUrls[platform]) {
        window.open(shareUrls[platform], '_blank', 'width=600,height=400');
    }
}

function subscribeToNewsletter() {
    const emailInput = document.getElementById('newsletter-email');
    const email = emailInput ? emailInput.value.trim() : '';
    if (!email) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value
        || document.cookie.match(/csrftoken=([^;]+)/)?.[1] || '';

    fetch('/news/api/newsletter-subscribe/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ email }),
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            emailInput.value = '';
            showNotification(data.message, 'success');
        } else {
            showNotification(data.message, 'error');
        }
    })
    .catch(() => showNotification('Something went wrong. Please try again.', 'error'));
}

function registerForEvent(eventId) {
    const name = prompt('Enter your full name:');
    if (!name) return;
    const email = prompt('Enter your email:');
    if (!email) return;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value
        || document.cookie.match(/csrftoken=([^;]+)/)?.[1] || '';

    fetch('/news/api/event-register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ event_id: eventId, name, email }),
    })
    .then(res => res.json())
    .then(data => {
        showNotification(data.message, data.success ? 'success' : 'error');
    })
    .catch(() => showNotification('Something went wrong. Please try again.', 'error'));
}

function showNotification(message, type) {
    const existing = document.querySelector('.js-notification');
    if (existing) existing.remove();

    const div = document.createElement('div');
    div.className = 'js-notification';
    div.textContent = message;
    Object.assign(div.style, {
        position: 'fixed', top: '20px', right: '20px', zIndex: '9999',
        padding: '14px 24px', borderRadius: '8px', color: '#fff', fontSize: '14px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)', transition: 'opacity 0.3s',
        background: type === 'success' ? '#16a34a' : '#dc2626',
    });
    document.body.appendChild(div);
    setTimeout(() => { div.style.opacity = '0'; setTimeout(() => div.remove(), 300); }, 4000);
}

function toggleCalendarView() {
    const calendarView = document.getElementById('calendar-view');
    const listView = document.getElementById('list-view');

    if (calendarView && listView) {
        calendarView.classList.toggle('hidden');
        listView.classList.toggle('hidden');
    }
}


function initializeDateFilters() {
    const dateFilters = document.querySelectorAll('.date-filter');
    dateFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const dateRange = this.dataset.range;
            filterByDate(dateRange);
        });
    });
}

// Export functions
window.NewsModule = {
    filterNews,
    searchNews,
    shareOnSocialMedia
};
