// To access the first element of the collection
const ul = document.getElementsByClassName('my_list')[0];

const addItem = document.getElementById('add_item');
addItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
