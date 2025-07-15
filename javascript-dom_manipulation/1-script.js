// Selects the div with the id "red_header"
const redHeader = document.getElementById('red_header');

// Select the <header> to modify
const header = document.querySelector('header');

// Add the click event
redHeader.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
