$(window).scroll(function () {
	if ($(this).scrollTop() > 0) {
		$(".navbar").addClass("active");
	} else {
		$(".navbar").removeClass("active");
	};
});