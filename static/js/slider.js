let slideIndex = 0;
let intervalId = null;

document.addEventListener("DOMContentLoaded", initializeSlider);
document.addEventListener("htmx:afterSwap", function(event) {
    if (event.detail.target.id === "content") {
        initializeSlider();
    }
});

function initializeSlider() {
    const slides = document.querySelectorAll(".slides img");

    if (intervalId) {
        clearInterval(intervalId);
    }

    if (slides.length > 0) {
        slides.forEach(slide => slide.classList.remove("displaySlide"));
        slides[slideIndex].classList.add("displaySlide");

        intervalId = setInterval(nextSlide, 5000);
    }
}

function showSlide(index) {
    const slides = document.querySelectorAll(".slides img");
    if (slides.length === 0) return; 

    slideIndex = (index + slides.length) % slides.length; 
    slides.forEach(slide => slide.classList.remove("displaySlide"));
    slides[slideIndex].classList.add("displaySlide");
}

function prevSlide() {
    clearInterval(intervalId);
    showSlide(slideIndex - 1);
}

function nextSlide() {
    clearInterval(intervalId); 
    showSlide(slideIndex + 1);
}
