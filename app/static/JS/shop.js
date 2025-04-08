class ProductStore {
    constructor() {
        this.products = [];
        this.currentProductIndex = 0;
        this.currentImageIndex = 0;

        this.initializeElements();
        this.fetchProducts();
    }

    initializeElements() {
        this.productImages = document.getElementById('product-images');
        this.sliderDots = document.getElementById('slider-dots');
        this.productTitle = document.getElementById('product-title');
        this.productDescription = document.getElementById('product-description');
        this.productPrice = document.getElementById('product-price');
        this.originalPrice = document.getElementById('original-price');
        this.buyButton = document.getElementById('buy-button');
        this.prevButton = document.querySelector('.navigation-arrow.prev');
        this.nextButton = document.querySelector('.navigation-arrow.next');

        this.prevButton.addEventListener('click', () => this.changeProduct(-1));
        this.nextButton.addEventListener('click', () => this.changeProduct(1));
        this.buyButton.addEventListener('click', () => this.handleBuyClick());
    }

    async fetchProducts() {
        try {

            const response = await fetch('/api/shop/swags');
            if (!response.ok) {
                throw new Error('Error fetching products');
            }
            this.products = await response.json();


            this.renderProduct(0);


            this.setupAutoSlide();
        } catch (error) {
            console.error('Error:', error);
            this.showErrorState();
        }
    }

    renderProduct(productIndex) {
        if (this.products.length === 0) return;

        const product = this.products[productIndex];


        this.productImages.innerHTML = '';
        this.sliderDots.innerHTML = '';


        product.images.forEach((src, index) => {
            const img = document.createElement('img');
            console.log(src)
            img.src = src;
            img.alt = `${product.name} - Image ${index + 1}`;
            img.classList.add(index === 0 ? 'active' : 'hidden');
            this.productImages.appendChild(img);


            const dot = document.createElement('span');
            dot.classList.add('slider-dot');
            if (index === 0) dot.classList.add('active');
            dot.dataset.index = index;
            dot.addEventListener('click', () => this.changeImage(index));
            this.sliderDots.appendChild(dot);
        });


        this.productTitle.textContent = product.name;
        this.productDescription.textContent = product.description;
        this.productPrice.textContent = `${product.price} CFA`;
        this.originalPrice.textContent = `${product.originalPrice} CFA`;
    }

    changeProduct(direction) {
        this.currentProductIndex = (this.currentProductIndex + direction + this.products.length) % this.products.length;
        this.currentImageIndex = 0;
        this.renderProduct(this.currentProductIndex);
    }

    changeImage(index) {
        const images = this.productImages.querySelectorAll('img');
        const dots = this.sliderDots.querySelectorAll('.slider-dot');

        images.forEach(img => {
            img.classList.remove('active');
            img.classList.add('hidden');
        });
        dots.forEach(dot => dot.classList.remove('active'));

        images[index].classList.remove('hidden');
        images[index].classList.add('active');
        dots[index].classList.add('active');
        this.currentImageIndex = index;
    }

    setupAutoSlide() {
        setInterval(() => {
            if (this.products.length > 0) {
                const product = this.products[this.currentProductIndex];
                this.currentImageIndex = (this.currentImageIndex + 1) % product.images.length;
                this.changeImage(this.currentImageIndex);
            }
        }, 5000);
    }

    handleBuyClick() {
        const product = this.products[this.currentProductIndex];

        alert(`Thank you for choosing Python Togo: ${product.name}`);
    }

    showErrorState() {

        this.productTitle.textContent = 'Error Loading Products';
        this.productDescription.textContent = 'Impossible to load products. Please try again later.';
        this.productPrice.textContent = '';
        this.originalPrice.textContent = '';
        this.buyButton.disabled = true;
    }
}


document.addEventListener('DOMContentLoaded', () => {
    new ProductStore();
});