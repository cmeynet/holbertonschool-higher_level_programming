const redHeader = document.getElementById('red_header');

const header = document.querySelector('header');

// When the "redHeader" element is clicked, add the "red" class to the <header>
redHeader.addEventListener('click', function () {
  header.classList.add('red');
});
