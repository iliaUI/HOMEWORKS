document.getElementById('checkDayBtn').addEventListener('click', function() {
    const dayInput = document.getElementById('dayInput').value;
    const result = document.getElementById('result');
    let dayName;

    switch (parseInt(dayInput)) {
        case 1:
            dayName = 'Monday';
            break;
        case 2:
            dayName = 'Tuesday';
            break;
        case 3:
            dayName = 'Wednesday';
            break;
        case 4:
            dayName = 'Thursday';
            break;
        case 5:
            dayName = 'Friday';
            break;
        case 6:
            dayName = 'Saturday';
            break;
        case 7:
            dayName = 'Sunday';
            break;
        default:
            dayName = 'Please enter a valid number.';
    }

    result.textContent = dayName;
});
