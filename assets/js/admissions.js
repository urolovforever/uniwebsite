// Admissions Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // FAQ Accordion
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

    // Application form validation
    const applicationForm = document.querySelector('.application-form');
    if (applicationForm) {
        applicationForm.addEventListener('submit', function(e) {
            e.preventDefault();

            let isValid = true;
            const requiredFields = this.querySelectorAll('[required]');

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#dc2626';
                } else {
                    field.style.borderColor = '#10b981';
                }
            });

            if (isValid) {
                alert('Application submitted successfully!');
                this.reset();
            } else {
                alert('Please fill in all required fields.');
            }
        });
    }

    // Deadline countdown
    const deadlineElements = document.querySelectorAll('[data-deadline]');
    deadlineElements.forEach(element => {
        const deadline = new Date(element.dataset.deadline);
        updateDeadlineCountdown(element, deadline);
        setInterval(() => updateDeadlineCountdown(element, deadline), 1000);
    });

    // Scholarship calculator
    const tuitionInput = document.getElementById('tuition-amount');
    const scholarshipSelect = document.getElementById('scholarship-type');
    const calculatedAmount = document.getElementById('calculated-amount');

    if (tuitionInput && scholarshipSelect && calculatedAmount) {
        function calculateScholarship() {
            const tuition = parseFloat(tuitionInput.value) || 0;
            const scholarshipPercent = parseFloat(scholarshipSelect.value) || 0;
            const finalAmount = tuition * (1 - scholarshipPercent / 100);
            calculatedAmount.textContent = `$${finalAmount.toLocaleString()}`;
        }

        tuitionInput.addEventListener('input', calculateScholarship);
        scholarshipSelect.addEventListener('change', calculateScholarship);
    }

    // Step cards animation
    const stepCards = document.querySelectorAll('.step-card');
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '0px'
    };

    const stepObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    stepCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        stepObserver.observe(card);
    });

    // Document upload preview
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                const label = this.nextElementSibling;
                if (label) {
                    label.textContent = `Selected: ${fileName}`;
                    label.style.color = '#10b981';
                }
            }
        });
    });
});

function updateDeadlineCountdown(element, deadline) {
    const now = new Date();
    const diff = deadline - now;

    if (diff <= 0) {
        element.textContent = 'Deadline passed';
        return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

    element.textContent = `${days} days, ${hours} hours, ${minutes} minutes`;
}

// Export functions
window.AdmissionsModule = {
    updateDeadlineCountdown
};
