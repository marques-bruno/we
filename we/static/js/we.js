$(function () {

	$('#auto-fade').fadeTo(10000,1).fadeOut(5000);

	$(document).scroll(function () {
	var $nav = $(".navbar-fixed-top");
	$nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
	});
});

$(document).scroll(function () {
	var $nav = $(".navbar-fixed-top");
	$nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
});

$('#auto-fade').fadeTo(1000,1).fadeOut(2000);