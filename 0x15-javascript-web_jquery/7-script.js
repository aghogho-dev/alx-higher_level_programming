$.ajax({url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	success: function(x) {
		$('div#character').text(x.name);
	}
});
