function searchInput() {
  return document.getElementById("search-box").querySelector("input");
}
function searchClear() {
  return document.getElementById("search-box").querySelectorAll("button")[1];
}
function searchResults() {
  return document.getElementById("search-results");
}
function searchHitItems() {
  return document.getElementsByClassName("search-result");
}
function searchPageLinks() {
  return document.getElementsByClassName("ais-Pagination-link");
}

function refreshSearchResultsVisibility() {
  var displayMode = searchInput().value == '' ? 'none' : 'block';
  searchResults().style.display = displayMode;
}

function focusSearchBar() {
  searchInput().focus();
  refreshSearchResultsVisibility();
}

function isSearchActive() {
  return searchResults().style.display == 'block' ||
         document.activeElement == searchInput();
}

function clearSearch() {
  searchInput().value = '';
  refreshSearchResultsVisibility();
}

var itemsPerPage = 10;
var selectedHit = -1;

function visitSelected() {
  var hit = Math.max(0, selectedHit);
  var i = Math.min(hit % itemsPerPage, searchHitItems().length - 1);
  window.location = searchHitItems()[i].parentElement.href;
}

function selectHit(step) {
  var pageCount = searchPageLinks().length - 4; // do not count << < > >> buttons

  // deselect previously selected hit, if any
  var oldHitPage = 0, oldHitIndex = -1;
  if (selectedHit >= 0) {
    // moved from one selected hit to another
    // (not off the search box onto the list)
    oldHitPage = Math.floor(selectedHit / itemsPerPage);
    oldHitIndex = selectedHit % itemsPerPage;
    if (oldHitIndex < searchHitItems().length) {
      searchHitItems()[oldHitIndex].style.background = null;
    }
  }

  // move the selected hit
  selectedHit += step;
  if (selectedHit < -1) selectedHit = -1;
  else if (selectedHit < 0) {
    // moved off the list, back to the search box
    focusSearchBar();
  }
  else {
    var hitPage = Math.floor(selectedHit / itemsPerPage);
    if (hitPage >= pageCount) hitPage = pageCount - 1;
    if (hitPage != oldHitPage) {
      console.log('CHANGING PAGES: ' + oldHitPage + ' -> ' + hitPage);
      searchPageLinks()[hitPage + 2].click();
    }

    var hitIndex = selectedHit % itemsPerPage;
    var maxIndex = searchHitItems().length - 1;
    if (hitIndex > maxIndex) hitIndex = maxIndex;
    searchHitItems()[hitIndex].style.background = '#7dd';
    searchHitItems()[hitIndex].focus();
  }
}

searchInput().oninput = refreshSearchResultsVisibility;
searchInput().onkeydown = function(e) {
  if (e.keyCode == 27) clearSearch(); // escape
  else if (e.keyCode == 13) visitSelected(); // enter
};

searchClear().onkeydown = function(e) {
  if (e.keyCode == 32) clearSearch(); // space bar
};
searchClear().onclick = function(e) { clearSearch(); }

document.addEventListener("keydown", function(e) {
  if (isSearchActive()) {
    if (e.keyCode == 40) selectHit(1); // down arrow
    else if (e.keyCode == 38) selectHit(-1); // up arrow
    else return;
  }
  else {
    if (e.keyCode == 76) focusSearchBar(); // L
    else return;
  }
  e.preventDefault();
}, false);
