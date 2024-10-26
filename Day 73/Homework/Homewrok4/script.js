document.getElementById('checkGenderBtn').addEventListener('click', function() {
    const genderInput = document.getElementById('genderInput').value.toUpperCase();
    const result = document.getElementById('result');
    let message;

    if (genderInput === 'M') {
        message = 'Your gender: Male';
    } else if (genderInput === 'F') {
        message = 'Your gender: Female';
    } else {
        message = 'Please enter a valid gender (M or F).';
    }

    result.textContent = message;
});
