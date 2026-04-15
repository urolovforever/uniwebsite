// About Section - Campus Gallery & Lightbox

var campusImages = [];
var currentImageIndex = 0;

// Build image list from thumbnail elements
document.addEventListener('DOMContentLoaded', function() {
    var thumbs = document.querySelectorAll('.campus-thumb');
    thumbs.forEach(function(thumb) {
        var img = thumb.querySelector('img');
        if (img) {
            campusImages.push({
                src: thumb.getAttribute('onclick') ? thumb.getAttribute('onclick').match(/'([^']+)'/)[1] : img.src,
                caption: img.alt || ''
            });
        }
    });

    var lightboxModal = document.getElementById('lightboxModal');
    if (lightboxModal) {
        document.addEventListener('keydown', function(e) {
            if (!lightboxModal.classList.contains('active')) return;
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowRight') nextImage();
            if (e.key === 'ArrowLeft') prevImage();
        });

        lightboxModal.addEventListener('click', function(e) {
            if (e.target === this) closeLightbox();
        });
    }

    // Also init for why-work gallery (hiring page)
    var whyWorkThumbs = document.querySelectorAll('.why-work-thumb');
    if (whyWorkThumbs.length) {
        initWhyWorkGallery();
    }
});

function changeCampusImage(src, thumb) {
    var img = document.getElementById('mainCampusImg');
    if (img) {
        img.style.opacity = '0';
        setTimeout(function() {
            img.src = src;
            img.style.opacity = '1';
        }, 200);
    }
    document.querySelectorAll('.campus-thumb').forEach(function(t) { t.classList.remove('active'); });
    thumb.classList.add('active');
    // Find index
    for (var i = 0; i < campusImages.length; i++) {
        if (campusImages[i].src === src) {
            currentImageIndex = i;
            break;
        }
    }
}

function openFullscreen() {
    var modal = document.getElementById('lightboxModal');
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    updateLightbox();
}

function closeLightbox() {
    var modal = document.getElementById('lightboxModal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

function updateLightbox() {
    if (!campusImages.length) return;
    var mainImg = document.getElementById('lightboxImg');
    var caption = document.getElementById('lightboxCaption');
    var prevImg = document.getElementById('lightboxPrev');
    var nextImg = document.getElementById('lightboxNext');

    if (mainImg) mainImg.src = campusImages[currentImageIndex].src;
    if (caption) caption.textContent = campusImages[currentImageIndex].caption;

    var prevIndex = (currentImageIndex - 1 + campusImages.length) % campusImages.length;
    var nextIndex = (currentImageIndex + 1) % campusImages.length;

    if (prevImg) prevImg.src = campusImages[prevIndex].src;
    if (nextImg) nextImg.src = campusImages[nextIndex].src;
}

function nextImage() {
    if (!campusImages.length) return;
    currentImageIndex = (currentImageIndex + 1) % campusImages.length;
    updateLightbox();
}

function prevImage() {
    if (!campusImages.length) return;
    currentImageIndex = (currentImageIndex - 1 + campusImages.length) % campusImages.length;
    updateLightbox();
}

// === Why Work Here Gallery (hiring page) ===
function initWhyWorkGallery() {
    // Auto-handled by hiring page inline JS
}
