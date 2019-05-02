//find all divs with attribute data-color over cutoff value
var color_cutoff = 0;
var alls = document.getElementsByClassName('filter-all');
var white = [];
var black = [];
var black = [];
var gray = [];
var red = [];
var orange = [];
var brown = [];
var yellow = [];
var green = [];
var turquoise = [];
var blue = [];
var lilac = [];
var pink = [];

function parse_colors() {
    white = $(alls).filter(function() { return parseInt($(this).attr("data-filter-white")) > color_cutoff; });
    black = $(alls).filter(function() { return parseInt($(this).attr("data-filter-black")) > color_cutoff; });
    gray = $(alls).filter(function() { return parseInt($(this).attr("data-filter-gray")) > color_cutoff; });
    red = $(alls).filter(function() { return parseInt($(this).attr("data-filter-red")) > color_cutoff; });
    orange = $(alls).filter(function() { return parseInt($(this).attr("data-filter-orange")) > color_cutoff; });
    brown = $(alls).filter(function() { return parseInt($(this).attr("data-filter-brown")) > color_cutoff; });
    yellow = $(alls).filter(function() { return parseInt($(this).attr("data-filter-yellow")) > color_cutoff; });
    green = $(alls).filter(function() { return parseInt($(this).attr("data-filter-green")) > color_cutoff; });
    turquoise = $(alls).filter(function() { return parseInt($(this).attr("data-filter-turquoise")) > color_cutoff; });
    blue = $(alls).filter(function() { return parseInt($(this).attr("data-filter-blue")) > color_cutoff; });
    lilac = $(alls).filter(function() { return parseInt($(this).attr("data-filter-lilac")) > color_cutoff; });
    pink = $(alls).filter(function() { return parseInt($(this).attr("data-filter-pink")) > color_cutoff; });
    }

// execute the function and show all pictures
filterSelection('all');

// adjust display based on color button selection
function filterSelection(c) {
  if (c == 'all') {
    parse_colors(); //needs to be run after the script loads images to the page
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
