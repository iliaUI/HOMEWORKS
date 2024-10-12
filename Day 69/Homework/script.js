function createCountryCard() {
    const country = document.getElementById('countryInput').value;
    const capital = document.getElementById('capitalInput').value;
    const result = `Country: ${country}, Capital: ${capital}`;
    document.getElementById('output').textContent = result;
}