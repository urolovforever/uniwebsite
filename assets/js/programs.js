// Programs Section Specific JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Program filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const programCards = document.querySelectorAll('.program-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.dataset.filter;

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter programs
            programCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 10);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Program search
    const searchInput = document.getElementById('program-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();

            programCards.forEach(card => {
                const title = card.querySelector('.program-title').textContent.toLowerCase();
                const description = card.querySelector('.program-description').textContent.toLowerCase();

                if (title.includes(searchTerm) || description.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // Curriculum accordion
    const curriculumSections = document.querySelectorAll('.curriculum-year');
    curriculumSections.forEach(section => {
        const header = section.querySelector('.year-header');
        if (header) {
            header.addEventListener('click', function() {
                const content = section.querySelector('.year-content');
                const isActive = content.classList.contains('active');

                // Close all sections
                document.querySelectorAll('.year-content').forEach(c => {
                    c.classList.remove('active');
                });

                // Toggle current section
                if (!isActive) {
                    content.classList.add('active');
                }
            });
        }
    });

    // Program comparison tool
    const compareCheckboxes = document.querySelectorAll('.compare-checkbox');
    const selectedPrograms = [];

    compareCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const programId = this.dataset.programId;

            if (this.checked) {
                if (selectedPrograms.length < 3) {
                    selectedPrograms.push(programId);
                } else {
                    this.checked = false;
                    alert('You can compare up to 3 programs at a time');
                }
            } else {
                const index = selectedPrograms.indexOf(programId);
                if (index > -1) {
                    selectedPrograms.splice(index, 1);
                }
            }

            updateComparisonPanel(selectedPrograms);
        });
    });

    // Animate program cards on scroll
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

    programCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease';
        cardObserver.observe(card);
    });

    // Program details modal
    const detailButtons = document.querySelectorAll('.view-details-btn');
    detailButtons.forEach(button => {
        button.addEventListener('click', function() {
            const programId = this.dataset.programId;
            openProgramModal(programId);
        });
    });
});

function updateComparisonPanel(programs) {
    const panel = document.getElementById('comparison-panel');
    if (!panel) return;

    if (programs.length === 0) {
        panel.style.display = 'none';
    } else {
        panel.style.display = 'block';
        panel.innerHTML = `
            <div class="comparison-header">
                <h3>Comparing ${programs.length} programs</h3>
                <button onclick="viewComparison()">View Comparison</button>
            </div>
        `;
    }
}

function openProgramModal(programId) {
    // Implementation for opening program details modal
    console.log('Opening program details for:', programId);
}

function viewComparison() {
    // Implementation for viewing program comparison
    console.log('Viewing program comparison');
}

// Export functions
window.ProgramsModule = {
    updateComparisonPanel,
    openProgramModal,
    viewComparison
};
