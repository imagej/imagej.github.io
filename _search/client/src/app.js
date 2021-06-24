/* global algoliasearch instantsearch */

import TypesenseInstantSearchAdapter from "typesense-instantsearch-adapter";

const typesenseInstantsearchAdapter = new TypesenseInstantSearchAdapter({
  server: {
    apiKey: "hz046FoyrmnivD6aCNxGOQA5OZ8dNI70", // Be sure to use the search-only-api-key
    nodes: [
      {
        host: "search.imagej.net",
        port: "8108",
        protocol: "https"
      }
    ]
  },
  // The following parameters are directly passed to Typesense's search API endpoint.
  //  So you can pass any parameters supported by the search endpoint below.
  //  queryBy is required.
  additionalSearchParameters: {
    queryBy: "title,description,content",
    numTypos: 1
  }
});
const searchClient = typesenseInstantsearchAdapter.searchClient;

const search = instantsearch({
  searchClient,
  indexName: "imagej-wiki"
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#search-box',
  }),
  instantsearch.widgets.hits({
    container: '#search-hits',
    templates: {
      item: `
        <a href="{{#helpers.highlight}}{ "attribute": "id" }{{/helpers.highlight}}">
          <div class="search-result">
            <img class="hit-icon" src="{{#helpers.highlight}}{ "attribute": "icon" }{{/helpers.highlight}}"></img>
            <div class="hit-title">
              {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
            </div>
            <div class="hit-description">
              {{#helpers.highlight}}{ "attribute": "description" }{{/helpers.highlight}}
            </div>
          </div>
        </a>
      `,
    },
    /* See: https://www.algolia.com/doc/guides/building-search-ui/widgets/customize-an-existing-widget/js/#modify-the-list-of-items-in-widgets */
    transformItems(items) {
      var query = document.getElementById('search-box').querySelector('.ais-SearchBox-input').value;
      /* Credit: https://www.tutorialspoint.com/levenshtein-distance-in-javascript */
      function levenshteinDistance(str1, str2) {
        const track = Array(str2.length + 1).fill(null).map(() =>
          Array(str1.length + 1).fill(null));
        for (let i = 0; i <= str1.length; i += 1) track[0][i] = i;
        for (let j = 0; j <= str2.length; j += 1) track[j][0] = j;
        for (let j = 1; j <= str2.length; j += 1) {
          for (let i = 1; i <= str1.length; i += 1) {
            const indicator = str1[i - 1] === str2[j - 1] ? 0 : 1;
            track[j][i] = Math.min(
              track[j][i - 1] + 1, // deletion
              track[j - 1][i] + 1, // insertion
              track[j - 1][i - 1] + indicator, // substitution
            );
          }
        }
        return track[str2.length][str1.length];
      }
      return items.sort((a,b) => levenshteinDistance(a.title, query) - levenshteinDistance(b.title, query));
    }
  }),
  instantsearch.widgets.pagination({
    container: '#pagination',
  }),
]);

search.start();
