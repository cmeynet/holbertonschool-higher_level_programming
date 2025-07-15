// Sends a GET request
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Converts the request to a JSON object
  .then(data => {
    const characterDiv = document.getElementById('character');
    characterDiv.textContent = data.name; // Insert the character's name into this HTML element
  })
  .catch(error => {
    console.error('Error:', error); // Display the error in the console for debugging
  });
