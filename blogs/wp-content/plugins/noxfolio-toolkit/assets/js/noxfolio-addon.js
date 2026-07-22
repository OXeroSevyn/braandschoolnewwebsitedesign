; (function ($) {
  "use strict";

  var WidgetDefaultHandler = function ($scope) {

    // ## Video Popup
    // if ($scope.find('.video-play').length) {
    //   $('.video-play').magnificPopup({
    //     type: 'video',
    //   });
    // }


  //  Portfolio filter js
  $('.grid').imagesLoaded(function () {

    var $grid = $('.grid').isotope({
      itemSelector: '.grid-item',
      percentPosition: true,
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: '',
      }
    });


    // filter items on button click
    $('.masonary-menu').on('click', 'button', function () {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({ filter: filterValue });
    });

    //for menu active class
    $('.masonary-menu button').on('click', function (event) {
      $(this).siblings('.active').removeClass('active');
      $(this).addClass('active');
      event.preventDefault();
    });

  });

    // 30. Nice Select Js
    if ($("select").length > 0) {
      $("select").niceSelect();
    }


    // 31. magnificPopup img view Js 
    $('.popup-image').magnificPopup({
      // delegate: 'a',
      type: 'image',
      gallery: {
        enabled: true
      }
    });


    // 32. magnificPopup video view Js
    $(".popup-video").magnificPopup({
      type: "iframe",
    });


    // 33. Rating Js
    if ($(".fill-ratings span").length > 0) {
      var star_rating_width = $(".fill-ratings span").width();
      $(".star-ratings").width(star_rating_width);
    }




    // 35. Skillbar Js
    $(document).ready(function () {
      progress_bar();
    });
    function progress_bar() {
      var speed = 30;
      var items = $(".progress_bar").find(".progress-item");
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var item = $(entry.target).find(".progress");
            var itemValue = item.data("progress");
            var i = 0;
            var value = $(entry.target);
            var count = setInterval(function () {
              if (i <= itemValue) {
                var iStr = i.toString();
                item.css({
                  width: iStr + "%",
                });
                value.find(".item_value").html(iStr + "%");
              } else {
                clearInterval(count);
              }
              i++;
            }, speed);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      items.each(function () {
        observer.observe(this);
      });
    }


    // 36. Wow Js
    //new WOW().init();


    // 37. Counter Js
    new PureCounter();
    new PureCounter({
      filesizing: true,
      selector: ".filesizecount",
      pulse: 2,
    });

  };

  //elementor front start
  $(window).on("elementor/frontend/init", function () {
    elementorFrontend.hooks.addAction(
      "frontend/element_ready/widget",
      WidgetDefaultHandler
    );
  });

   // 2. Common Js
   $("[data-background").each(function () {
    $(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
  });

    // 19. Hover-animation Js
    function hoverWidget_animation() {
      let active_bg = $(".wt-hover__widget .active-bg");
      let element = $(".wt-hover__widget .current");
      $(".wt-hover__widget .wt-widget__item").on("mouseenter", function () {
        let e = $(this);
        activeHover(active_bg, e);
      });
      $(".wt-hover__widget").on("mouseleave", function () {
        element = $(".wt-hover__widget .current");
        activeHover(active_bg, element);
        element.closest(".wt-widget__item").siblings().removeClass("mleave");
      });
      activeHover(active_bg, element);
    }
    hoverWidget_animation();
  
    function activeHover(active_bg, e) {
      if (!e.length) {
        return false;
      }
      let topOff = e.offset().top;
      let height = e.outerHeight();
      let menuTop = $(".wt-hover__widget").offset().top;
      e.closest(".wt-widget__item").removeClass("mleave");
      e.closest(".wt-widget__item").siblings().addClass("mleave");
      active_bg.css({
        top: topOff - menuTop + "px",
        height: height + "px"
      });
    }
    $(".wt-hover__widget .wt-widget__item").on("click", function () {
      $(".wt-hover__widget .wt-widget__item").removeClass("current");
      $(this).addClass("current");
    });
  
  
    // 20. hover reveal for image Js
    const hoverItem = document.querySelectorAll(".wt-hover__reveal-item");
  
    function moveImage(e, hoverItem, index) {
      const item = hoverItem.getBoundingClientRect();
      const x = e.clientX - item.x;
      const y = e.clientY - item.y;
      if (hoverItem.children[index]) {
        hoverItem.children[index].style.transform = `translate(${x}px, ${y}px)`;
      }
    }
    hoverItem.forEach((item, i) => {
      item.addEventListener("mousemove", (e) => {
        setInterval(moveImage(e, item, 1), 50);
      });
    });

      // 21. button hover animation Js
  $('.wt-hover-btn').on('mouseenter', function (e) {
    var x = e.pageX - $(this).offset().left;
    var y = e.pageY - $(this).offset().top;

    $(this).find('.wt-btn-circle-dot').css({
      top: y,
      left: x
    });
  });

  $('.wt-hover-btn').on('mouseout', function (e) {
    var x = e.pageX - $(this).offset().left;
    var y = e.pageY - $(this).offset().top;

    $(this).find('.wt-btn-circle-dot').css({
      top: y,
      left: x
    });
  });

    // 31. magnificPopup img view Js 
    $('.popup-image').magnificPopup({
      // delegate: 'a',
      type: 'image',
      gallery: {
        enabled: true
      }
    });


    // 32. magnificPopup video view Js
    $(".popup-video").magnificPopup({
      type: "iframe",
    });

})(jQuery);