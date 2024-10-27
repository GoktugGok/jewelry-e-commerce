document.addEventListener('DOMContentLoaded', function () {
  var accordionContainer = document.getElementById('accordionPanelsStayOpenExampleDetails');
  var accordionItems = accordionContainer.querySelectorAll('.accordion-item');

  accordionItems.forEach(function (item, index) {
    var collapse = item.querySelector('.accordion-collapse');
    var symbol = item.querySelector('.symbol');
    

    if (collapse.classList.contains('show')) {
        symbol.textContent = '-'
    } else {
       symbol.textContent = '+'
    }

  });

});
document.addEventListener('DOMContentLoaded', function () {
  // Tüm accordion butonlarını seçiyoruz
  var accordionButtons = document.querySelectorAll('.accordion-button');

  // Her buton için event listener ekliyoruz
  accordionButtons.forEach(function (accordionButton) {
    
    accordionButton.addEventListener('click', function (event) {
      // Sembolü buluyoruz
      var symbol = accordionButton.querySelector('.symbol');

      // Aria-expanded özelliğini kontrol ediyoruz
      var isExpanded = accordionButton.getAttribute('aria-expanded') === 'true';

      // Eğer içerik açık ise, sembolü '-' yap
      if (isExpanded) {
        symbol.textContent = '-';
        console.log('Accordion açık: "-" sembolü gösteriliyor.');
      } else {
        // İçerik kapalıysa sembolü '+' yap
        symbol.textContent = '+';
        console.log('Accordion kapalı: "+" sembolü gösteriliyor.');
      }
    });
  });
});





// Thumbnail Slider
var thumbsSwiper = new Swiper('.thumbs-slider', {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true
});

// Main Slider
var mainSwiper = new Swiper('.main-slider', {
  spaceBetween: 10,
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
  },
  thumbs: {
      swiper: thumbsSwiper
  }
});


let carouselElement = document.getElementById('carouselExampleMobile');
let thumbnails = document.querySelectorAll('.thumbnail-container .img-thumbnail')

thumbnails.forEach((thumbnail,index) =>{
    thumbnail.addEventListener('click',function() {
        thumbnails.forEach(t => t.classList.remove('selected'));

        this.classList.add('selected');
    })
})

carouselElement.addEventListener('slid.bs.carousel', function(event) {
  let activeIndex = event.to;
  thumbnails.forEach(t => t.classList.remove('selected'));

  thumbnails[activeIndex].classList.add('selected');
})

thumbnails[0].classList.add('selected');
