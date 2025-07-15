fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.getElementById('list_movies');
    for (let i = 0; i < data.results.length; i++) {
      const li = document.createElement('li');
      li.textContent = data.results[i].title; // Retrieves the title of the film
      listMovies.appendChild(li); // Adds the element to the <ul>
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
