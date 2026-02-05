// About Section - Campus Gallery & Lightbox

const campusImages = [
    { src: '../assets/img/back1.jpg', caption: 'Main entrance to the TIU campus with modern architecture.' },
    { src: '../assets/img/back2.jpg', caption: 'Beautiful view of the university buildings and surroundings.' },
    { src: '../assets/img/b1.jpg', caption: 'State-of-the-art facilities for students and faculty.' },
    { src: '../assets/img/b2.jpg', caption: 'Green spaces and recreational areas on campus.' },
    { src: '../assets/img/b3.jpg', caption: 'Modern learning environments designed for success.' },
    { src: '../assets/img/c2.jpg', caption: 'Student life and community at TIU.' }
];
let currentImageIndex = 0;

function changeCampusImage(src, thumb) {
    document.getElementById('mainCampusImg').src = src;
    document.querySelectorAll('.campus-thumb').forEach(t => t.classList.remove('active'));
    thumb.classList.add('active');
    currentImageIndex = campusImages.findIndex(img => img.src === src);
}

function openFullscreen() {
    const modal = document.getElementById('lightboxModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    updateLightbox();
}

function closeLightbox() {
    const modal = document.getElementById('lightboxModal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

function updateLightbox() {
    const mainImg = document.getElementById('lightboxImg');
    const caption = document.getElementById('lightboxCaption');
    const prevImg = document.getElementById('lightboxPrev');
    const nextImg = document.getElementById('lightboxNext');

    mainImg.src = campusImages[currentImageIndex].src;
    caption.textContent = campusImages[currentImageIndex].caption;

    const prevIndex = (currentImageIndex - 1 + campusImages.length) % campusImages.length;
    const nextIndex = (currentImageIndex + 1) % campusImages.length;

    prevImg.src = campusImages[prevIndex].src;
    nextImg.src = campusImages[nextIndex].src;
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % campusImages.length;
    updateLightbox();
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + campusImages.length) % campusImages.length;
    updateLightbox();
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    const lightboxModal = document.getElementById('lightboxModal');

    if (lightboxModal) {
        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowRight') nextImage();
            if (e.key === 'ArrowLeft') prevImage();
        });

        // Close on background click
        lightboxModal.addEventListener('click', function(e) {
            if (e.target === this) closeLightbox();
        });
    }
});
