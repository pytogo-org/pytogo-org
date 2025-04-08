
document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector('.slider');
    const sledesClass = document.getElementsByClassName('.slide');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.slider-nav.prev');
    const nextBtn = document.querySelector('.slider-nav.next');

    let currentIndex = 0;
    const totalSlides = slides.length;

    // Set up the slider
    function updateSlider() {
        slider.style.transform = `translateX(-${currentIndex * 100}%)`;
        sledesClass[currentIndex - 1].style.display = 'none';
        sledesClass[currentIndex + 1].style.display = 'none';

    }

    // Navigation
    prevBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === 0) ? totalSlides - 1 : currentIndex - 1;
        updateSlider();
    });

    nextBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === totalSlides - 1) ? 0 : currentIndex + 1;
        updateSlider();
    });

    // Auto-slide every 5 seconds
    setInterval(function () {
        currentIndex = (currentIndex === totalSlides - 1) ? 0 : currentIndex + 1;
        updateSlider();
    }, 5000);
    // set display none for the next and the prev slide
    
});