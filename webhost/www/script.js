//find all divs with attribute data-color over cutoff value
var alls = document.querySelectorAll('.filter-all');
var white = document.querySelectorAll('[data-filter-white]');
var black = document.querySelectorAll('[data-filter-black]');
var gray = document.querySelectorAll('[data-filter-gray]');
var red = document.querySelectorAll('[data-filter-red]');
var orange = document.querySelectorAll('[data-filter-orange]');
var brown = document.querySelectorAll('[data-filter-brown]');
var yellow = document.querySelectorAll('[data-filter-yellow]');
var green = document.querySelectorAll('[data-filter-green]');
var turquoise = document.querySelectorAll('[data-filter-turquoise]');
var blue = document.querySelectorAll('[data-filter-blue]');
var lilac = document.querySelectorAll('[data-filter-lilac]');
var pink = document.querySelectorAll('[data-filter-pink]');

filterSelection('all') // Execute the function and show all columns
function filterSelection(c) {
  if (c == 'all') {
    filterSelection('none');
    for (var i = 0; i < alls.length; ++i) {
      alls[i].style.display = 'inline-block';
    }
    return;
  }
  if (c == 'none') {
    for (var i = 0; i < alls.length; ++i) {
      alls[i].style.display = 'none';
    }
    return;
  }
  else {
    filterSelection('none');
    for (var i = 0; i < eval(c).length; i++) {
      eval(c)[i].style.display = 'inline-block';
    }
  }
}


// show all function
  // hide all function
  // loop through all items and set style.display="inline-block"

// hide all function
  // loop through all items and set style.display=""
  // loop through all color filters and set style.display=""

// show color function
  // hide all function
  // loop through for that color and set style.display="inline-block"
