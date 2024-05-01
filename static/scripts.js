
let currentIndex = 0;

function nextSlide() {
  const slides = document.querySelectorAll('.slide');
  currentIndex = (currentIndex + 1) % slides.length; 
  displaySlide(currentIndex);
}

function prevSlide() {
  const slides = document.querySelectorAll('.slide');
  currentIndex = (currentIndex - 1 + slides.length) % slides.length; 
  displaySlide(currentIndex);
}

function displaySlide(index) {
  const slides = document.querySelector('.slides');
  const offset = -1 * index * slides.offsetWidth;
  slides.style.transform = `translateX(${offset}px)`;
}
/////////