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

    // Animate cards
    animateNewsCards();

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

function loadMoreNews() {
    console.log('Loading more news...');
    // Implementation for loading more news
}

function openLightbox(imageId) {
    console.log('Opening lightbox for image:', imageId);
    // Implementation for image lightbox
}

function playVideo(videoId) {
    console.log('Playing video:', videoId);
    // Implementation for video player
}

function registerForEvent(eventId) {
    console.log('Registering for event:', eventId);
    if (confirm('Would you like to register for this event?')) {
        alert('Successfully registered for the event!');
    }
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
    const email = document.getElementById('newsletter-email').value;
    console.log('Subscribing to newsletter:', email);
    alert('Successfully subscribed to our newsletter!');
}

function toggleCalendarView() {
    const calendarView = document.getElementById('calendar-view');
    const listView = document.getElementById('list-view');

    if (calendarView && listView) {
        calendarView.classList.toggle('hidden');
        listView.classList.toggle('hidden');
    }
}

function animateNewsCards() {
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

    document.querySelectorAll('.news-card, .event-item').forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.5s ease ${index * 0.05}s`;
        cardObserver.observe(card);
    });
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

function filterByDate(range) {
    console.log('Filtering by date range:', range);
    // Implementation for date filtering
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
window.NewsModule = {
    filterNews,
    searchNews,
    shareOnSocialMedia
};
