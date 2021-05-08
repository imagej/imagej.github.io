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
  }),
  instantsearch.widgets.pagination({
    container: '#pagination',
  }),
]);

search.start();
