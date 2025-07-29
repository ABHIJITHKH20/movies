window.onload = function () {
    const movies = JSON.parse(localStorage.getItem('movies')) || [];
    const movieCardsContainer = document.getElementById('movie-cards');
  
    if (movies.length === 0) {
      movieCardsContainer.innerHTML = '<p>No movies available.</p>';
      return;
    }
  
    movies.forEach((movie) => {
      const movieCard = document.createElement('div');
      movieCard.classList.add('movie-card');
  
      movieCard.innerHTML = `
        <img src="${movie.image}" alt="${movie.title}">
        <div class="info">
          <h3>${movie.title}</h3>
          <p>${movie.description}</p>
          <p class="showtime">Showtime: ${movie.showtime}</p>
        </div>
      `;
  
      movieCardsContainer.appendChild(movieCard);
    });
  };
  function toggleFlip(button) {
    const cardInner = button.closest('.card-inner');
    cardInner.classList.toggle('flipped');
  }
<script src="{% static 'main.js' %}"></script>
  
  