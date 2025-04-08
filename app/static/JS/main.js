// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.getElementById('navLinks');
console.log('clicked');

mobileMenuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');

});

// Close menu when clicking on a link
const links = document.querySelectorAll('.nav-links a');
links.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        console.log('clicked');
    });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav') && !e.target.closest('.mobile-menu-btn')) {
        navLinks.classList.remove('active');
    }
});
