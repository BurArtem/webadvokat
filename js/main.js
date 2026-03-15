// скрол меню
$(window).scroll(function () {
	if ($(this).scrollTop() > 50) {
		$('.fixed_menu').addClass('fixed');
		$('.premium-sticky-menu').addClass('scrolled');
	} else {
		$('.fixed_menu').removeClass('fixed');
		$('.premium-sticky-menu').removeClass('scrolled');
	}
});
// слайдер на главной
$('.why_are_we_carousel').slick({
	dots: true,
	slidesToShow: 3,
	slidesToScroll: 1,
	autoplay: true,
	autoplaySpeed: 5000,
	prevArrow: "<img src='img/arrow-left.png' class='prev' alt=''>",
	nextArrow: "<img src='img/arrow-right.png' class='next' alt=''>",
	responsive: [{
		breakpoint: 768,
		settings: {
			slidesToShow: 2,
		}
	},
	{
		breakpoint: 480,
		settings: {
			slidesToShow: 1,
		}
	}
	]
});
// Слайдер с отзывами
$('.reviews_carousel').slick({
	dots: true,
	// autoplay: true,
	// autoplaySpeed: 3000,
	responsive: [{
		breakpoint: 991,
		settings: {
			dots: true,
			arrows: false,
		}
	}]
});
// Слайдер о бюро
$('.about_carousel').slick({
	dots: true,
	arrows: true,
	slidesToShow: 3,
	slidesToScroll: 1,
	autoplay: true,
	autoplaySpeed: 5000,
	responsive: [{
		breakpoint: 768,
		settings: {
			slidesToShow: 2,
		}
	},
	{
		breakpoint: 480,
		settings: {
			slidesToShow: 1,
		}
	}
	]
});

$(document).ready(function () {
	$('.popup-gallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
		},
		image: {
			tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
			titleSrc: function (item) {
				return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
			}
		}
	});
});

// Карта
function initMap() {
	// The location of Uluru
	var uluru = {
		lat: -25.344,
		lng: 131.036
	};
	// The map, centered at Uluru
	var map = new google.maps.Map(
		document.getElementById('map'), {
		zoom: 4,
		center: uluru
	});
	// The marker, positioned at Uluru
	var marker = new google.maps.Marker({
		position: uluru,
		map: map
	});
}

