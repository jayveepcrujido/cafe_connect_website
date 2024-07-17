/* JavaScript */
document.addEventListener('DOMContentLoaded', () => {
    const cartBtn = document.getElementById('cart-btn');
    const cartSection = document.getElementById('cart');
    const categoryOverviewBtn = document.getElementById('category-overview-btn');
    const searchBtn = document.getElementById('search-btn');
    const loginBtn = document.getElementById('login-btn');
    const searchInput = document.getElementById('search-input');
    const pageBtn = document.getElementById('page-btn');
    const pageSection = document.getElementById('menu');


    cartBtn.addEventListener('click', () => {
        cartSection.scrollIntoView({ behavior: 'smooth' });
    });

    pageBtn.addEventListener('click', () => {
        pageSection.scrollIntoView({ behavior: 'smooth'});
    });

    categoryOverviewBtn.addEventListener('click', () => {
        document.getElementById('category-overview').scrollIntoView({ behavior: 'smooth' });
    });

    searchBtn.addEventListener('click', () => {
        document.getElementById('search-results').scrollIntoView({ behavior: 'smooth' });
    });

    loginBtn.addEventListener('click', () => {
        document.getElementById('account').scrollIntoView({ behavior: 'smooth' });
    });

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.toLowerCase();
        const products = document.querySelectorAll('.product');
        const searchOutput = document.getElementById('search-output');
        searchOutput.innerHTML = '';

        let resultsFound = false;
        products.forEach(product => {
            const productName = product.dataset.name.toLowerCase();
            if (productName.includes(query)) {
                const productClone = product.cloneNode(true);
                searchOutput.appendChild(productClone);
                resultsFound = true;
            }
        });

        if (!resultsFound) {
            searchOutput.innerHTML = '<p>No products found.</p>';
        }
    });
});

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const main = document.getElementById('main');

signUpButton.addEventListener('click', ()=>{
    main.classList.add("right-panel-active");
});
signInButton.addEventListener('click', ()=>{
    main.classList.remove("right-panel-active");
});

 function showAlert() {
            alert("This is an alert message!");
        };


