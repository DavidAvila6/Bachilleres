const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    updateSlider();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    updateSlider();
}

function updateSlider() {
    const slider = document.getElementById('image-slider');
    slider.style.transform = `translateX(-${currentSlide * 50}%)`;
}

// Iniciar el cambio automático de diapositivas
setInterval(nextSlide, 5000); // Cambiar la imagen cada 5 segundos
