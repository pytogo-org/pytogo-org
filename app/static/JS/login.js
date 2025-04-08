document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    let isValid = true;

    document.getElementById('username-error').classList.remove('show');
    document.getElementById('password-error').classList.remove('show');
    document.getElementById('login-error').classList.remove('show');

    if (!username) {
        document.getElementById('username-error').classList.add('show');
        isValid = false;
    }

    if (!password) {
        document.getElementById('password-error').classList.add('show');
        isValid = false;
    }

    if (isValid) {
    
        document.getElementById('login-error').classList.add('show');
        document.querySelector('.login-container').classList.add('shake');

       
        setTimeout(() => {
            document.querySelector('.login-container').classList.remove('shake');
        }, 500);
    }
});