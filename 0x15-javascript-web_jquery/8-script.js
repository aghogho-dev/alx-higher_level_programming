$.ajax({url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: function(x) {
		$.each(x.results, function(index, movie) {
			$('<li>').text(movie.title).appendTo('#list_movies');
		});
	}
});
