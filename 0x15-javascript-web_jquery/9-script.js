$('document').ready(function() {
	$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(x) {
		$('div#hello').text(x.hello);
	});
});
