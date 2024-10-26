document.getElementById('checkSeasonBtn').addEventListener('click', function() {
    const monthInput = document.getElementById('monthInput').value.toLowerCase();
    const result = document.getElementById('result');
    let season;

    switch (monthInput) {
        case 'march':
        case 'april':
        case 'may':
            season = 'Spring';
            break;
        case 'june':
        case 'july':
        case 'august':
            season = 'Summer';
            break;
        case 'september':
        case 'october':
        case 'november':
            season = 'Autumn';
            break;
        case 'december':
        case 'january':
        case 'february':
            season = 'Winter';
            break;
        default:
            season = 'Please enter a valid month.';
    }

    result.textContent = season;
});
