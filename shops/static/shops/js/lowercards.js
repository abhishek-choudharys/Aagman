		jQuery(document).ready(function($) {

  // OWL CAROUSEL - https://owlcarousel2.github.io/OwlCarousel2/
  $('.owl-carousel').owlCarousel(
    {
      items: 4,
      margin: 0,
      loop: true,
      nav: true,
      navText: ['<<','>>'],
      dots: false,
      dotsEach: true,
      autoplay: false,
      autoplaySpeed: 1500,
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      smartSpeed: 1500,
    }
  );
  $('#owl-1 .owl-carousel').owlCarousel(
    {
      items: 4,
      margin: 20,
      loop: true,
     smartSpeed: 1500,
      stagePadding: 64,
      nav: true,
        navText: ['Back','Next'],
      navText: ['',''],
      // navText: ["<img src='myprevimage.png'>","<img src='mynextimage.png'>"],
      dots: false,
      nav: true,
      dotsEach: true,
      lazyLoad: false,
      autoplay: false,
      autoplaySpeed: 1500,
      navSpeed: 500,
      autoplayTimeout: 2000,
      autoplayHoverPause: true,
    }
  );

  $('#owl-2 .owl-carousel').owlCarousel(
    {
      items: 4,
      margin: 20,
      stagePadding: 32,
      loop: true,

      autoplay: true,
      autoplaySpeed: 500,
      navSpeed: 500,
      dots: false,
      dotsEach: true,
      nav: true,
      // navTexhttps://codepen.io/krishnay/pen/GyKVNyt: ['Back','Next'],
      navText: ['',''],
      autoplayTimeout: 2000,
      autoplayHoverPause: false,
      animateOut: 'slideOutDown',
      animateIn: 'flipInX',
    }
  );

});