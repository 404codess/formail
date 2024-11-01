
document.getElementById('contactForm').addEventListener('submit', function (event) {
    let valid = true;

    // Validate Name (assuming name is the username equivalent)
    const name = document.getElementById('id_name').value;
    const usernameError = document.getElementById('usernameError');
    if (name.length < 4) {
        usernameError.style.display = 'block';
        valid = false;
    } else {
        usernameError.style.display = 'none';
    }

    // Validate Message (assuming message is the password equivalent)
    const message = document.getElementById('id_message').value;
    const passwordError = document.getElementById('passwordError');
    if (message.length < 6) {
        passwordError.style.display = 'block';
        valid = false;
    } else {
        passwordError.style.display = 'none';
    }

    // Prevent form submission if validation fails
    if (!valid) {
        event.preventDefault();
    }
});
