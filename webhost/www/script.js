//find all divs with attribute data-color over cutoff value
var color_cutoff = 0;
//var alls = document.querySelectorAll('.filter-all');
var alls = document.getElementsByClassName('filter-all');
var white = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-white")) > color_cutoff; });
var black = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-black")) > color_cutoff; });
var gray = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-gray")) > color_cutoff; });
var red = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-red")) > color_cutoff; });
var orange = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-orange")) > color_cutoff; });
var brown = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-brown")) > color_cutoff; });
var yellow = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-yellow")) > color_cutoff; });
var green = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-green")) > color_cutoff; });
var turquoise = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-turquoise")) > color_cutoff; });
var blue = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-blue")) > color_cutoff; });
var lilac = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-lilac")) > color_cutoff; });
var pink = $('.filter-all').filter(function() { return parseInt($(this).attr("data-filter-pink")) > color_cutoff; });

console.log(alls); //debug
console.log($(alls).filter(function() { return $(this).attr("data-filter-gray"); })); //debug


// execute the function and show all pictures
filterSelection('all')

// adjust display based on color button selection
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
