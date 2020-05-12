(function() {
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) { // Are there any results?
      var appendString = '';

      for (var i = 0; i < results.length; i++) {  // Iterate over the results
        var item = store[results[i].ref];
        appendString += '<a href="' + item.url + '"><h2>' + item.title + '</h2></a>';
        appendString += '<p>' + item.description.substring(0, 150) + '...</p>';
      }

      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<h2>No results found</h2>';
    }
  }

  function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');

      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  var searchTerm = getQueryVariable('query');

  if (searchTerm) {
    // Initalize lunr with the fields it will be searching on. I've given title
    // a boost of 10 to indicate matches on this field are more important.
      
    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('category');
      this.field('description');
      for (var key in window.store) {
        this.add({
          'id': key,
          'title': window.store[key].title,
          'author': window.store[key].author,
          'category': window.store[key].category,
          'description': window.store[key].description
        });
      }
    });
  }

  var results = idx.search(searchTerm); // Get lunr to perform a search
  displaySearchResults(results, window.store); // We'll write this in the next section
  

})();