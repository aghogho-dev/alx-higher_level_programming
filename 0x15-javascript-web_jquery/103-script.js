$(document).ready(function() {
	function tranlateHello() {
		const languageCode = $('language_code').val();
		$.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function(x) {
			$('#hello').text(x.hello);
		});
	}
	$('#btn_translate').click(translateHello);
	$('#language_code').keypress(function(y) {
		if (y.which = 13) {
			translateHello();
		}
	});
});
