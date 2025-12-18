// Contact Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitContactForm();
        });
    }

    // Rector reception form
    const rectorForm = document.getElementById('rector-form');
    if (rectorForm) {
        rectorForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitRectorForm();
        });
    }

    // FAQ accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const answer = this.nextElementSibling;
            const isActive = answer.classList.contains('active');

            // Close all answers
            document.querySelectorAll('.faq-answer').forEach(a => {
                a.classList.remove('active');
            });

            // Toggle current answer
            if (!isActive) {
                answer.classList.add('active');
            }
        });
    });

    // Department contact quick links
    const departmentLinks = document.querySelectorAll('.department-link');
    departmentLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const department = this.dataset.department;
            scrollToDepartment(department);
        });
    });

    // Live chat toggle
    const liveChatBtn = document.getElementById('live-chat-btn');
    if (liveChatBtn) {
        liveChatBtn.addEventListener('click', toggleLiveChat);
    }

    // Initialize map
    initializeMap();

    // Form validation
    setupFormValidation();

    // Office hours status
    updateOfficeStatus();
    setInterval(updateOfficeStatus, 60000); // Update every minute

    // Quick contact options
    const quickContactBtns = document.querySelectorAll('.quick-contact-btn');
    quickContactBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const contactType = this.dataset.type;
            handleQuickContact(contactType);
        });
    });
});

function submitContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    console.log('Submitting contact form:', data);

    // Show success message
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.innerHTML = `
        <i class="fas fa-check-circle"></i>
        <p>Thank you for contacting us! We will get back to you within 24 hours.</p>
    `;
    successDiv.style.cssText = 'background: #10b981; color: white; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;';

    form.insertAdjacentElement('afterend', successDiv);
    form.reset();

    setTimeout(() => {
        successDiv.remove();
    }, 5000);
}

function submitRectorForm() {
    const form = document.getElementById('rector-form');
    if (!form) return;

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    console.log('Submitting rector reception form:', data);

    alert('Your message has been sent to the Rector\'s office. You will receive a response within 3 business days.');
    form.reset();
}

function scrollToDepartment(department) {
    const element = document.getElementById(`dept-${department}`);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        element.classList.add('highlight');
        setTimeout(() => element.classList.remove('highlight'), 2000);
    }
}

function toggleLiveChat() {
    console.log('Toggling live chat');
    // Implementation for live chat widget
    alert('Live chat will be available soon!');
}

function initializeMap() {
    const mapContainer = document.getElementById('map-container');
    if (!mapContainer) return;

    // Placeholder for Google Maps or other map service integration
    mapContainer.innerHTML = `
        <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #e5e7eb;">
            <i class="fas fa-map-marked-alt" style="font-size: 4rem; color: var(--primary-blue); margin-bottom: 1rem;"></i>
            <p style="color: #666; font-size: 1.1rem;">Interactive map will be loaded here</p>
            <p style="color: #666; font-size: 0.9rem; margin-top: 0.5rem;">Tashkent, Uzbekistan</p>
        </div>
    `;
}

function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (!this.value.trim()) {
                    this.style.borderColor = '#dc2626';
                } else {
                    this.style.borderColor = '#10b981';
                }
            });

            input.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.style.borderColor = '#e5e7eb';
                }
            });
        });
    });
}

function updateOfficeStatus() {
    const statusElement = document.getElementById('office-status');
    if (!statusElement) return;

    const now = new Date();
    const hour = now.getHours();
    const day = now.getDay();

    // Office hours: Monday-Friday 9:00-18:00
    const isOpen = day >= 1 && day <= 5 && hour >= 9 && hour < 18;

    statusElement.innerHTML = isOpen
        ? '<span style="color: #10b981;"><i class="fas fa-circle"></i> Office Open</span>'
        : '<span style="color: #dc2626;"><i class="fas fa-circle"></i> Office Closed</span>';
}

function handleQuickContact(type) {
    switch (type) {
        case 'phone':
            window.location.href = 'tel:+998711234567';
            break;
        case 'email':
            window.location.href = 'mailto:info@tiu.uz';
            break;
        case 'whatsapp':
            window.open('https://wa.me/998901234567', '_blank');
            break;
        case 'telegram':
            window.open('https://t.me/tiu_official', '_blank');
            break;
        default:
            console.log('Unknown contact type:', type);
    }
}

// Export functions
window.ContactModule = {
    submitContactForm,
    submitRectorForm,
    scrollToDepartment
};
