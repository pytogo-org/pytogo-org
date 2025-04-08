
const passwordToggles = document.querySelectorAll('.password-toggle');
passwordToggles.forEach(toggle => {
    toggle.addEventListener('click', function () {
        const passwordField = this.previousElementSibling;
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);

        const icon = this.querySelector('i');
        icon.classList.toggle('fa-eye');
        icon.classList.toggle('fa-eye-slash');
    });
});

const roleCards = document.querySelectorAll('.role-card');
roleCards.forEach(card => {
    card.addEventListener('click', function () {
        roleCards.forEach(c => c.classList.remove('selected'));
        this.classList.add('selected');
    });
});

const form = document.getElementById('registration-form');
form.addEventListener('submit', function (e) {
    e.preventDefault();

    let isValid = true;

    const firstName = document.getElementById('first-name');
    if (!firstName.value.trim()) {
        firstName.parentElement.classList.add('invalid');
        isValid = false;
    } else {
        firstName.parentElement.classList.remove('invalid');
    }

    const lastName = document.getElementById('last-name');
    if (!lastName.value.trim()) {
        lastName.parentElement.classList.add('invalid');
        isValid = false;
    } else {
        lastName.parentElement.classList.remove('invalid');
    }

    const email = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        email.parentElement.classList.add('invalid');
        isValid = false;
    } else {
        email.parentElement.classList.remove('invalid');
    }

    const password = document.getElementById('password');
    if (password.value.length < 8) {
        password.parentElement.parentElement.classList.add('invalid');
        isValid = false;
    } else {
        password.parentElement.parentElement.classList.remove('invalid');
    }

    const confirmPassword = document.getElementById('confirm-password');
    if (confirmPassword.value !== password.value) {
        confirmPassword.parentElement.parentElement.classList.add('invalid');
        isValid = false;
    } else {
        confirmPassword.parentElement.parentElement.classList.remove('invalid');
    }

    const selectedRole = document.querySelector('.role-card.selected');
    if (!selectedRole) {
        alert('Please select an account type');
        isValid = false;
    }

    const terms = document.getElementById('terms');
    if (!terms.checked) {
        alert('Please agree to the Terms of Service and Privacy Policy');
        isValid = false;
    }

    if (isValid) {
        document.querySelector('.signup-form').style.display = 'none';
        document.querySelector('.success-message').style.display = 'block';

    }
});
