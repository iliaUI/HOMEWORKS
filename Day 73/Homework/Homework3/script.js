document.getElementById('checkPriceBtn').addEventListener('click', function() {
    const productInput = document.getElementById('productInput').value.toLowerCase();
    const result = document.getElementById('result');
    let price;

    switch (productInput) {
        case 'computer':
            price = '$1000';
            break;
        case 'television':
            price = '$500';
            break;
        case 'smartphone':
            price = '$300';
            break;
        default:
            price = 'Please enter a valid product.';
    }

    result.textContent = `The price is: ${price}`;
});
