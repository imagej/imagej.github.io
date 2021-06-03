const Cite = require('citation-js')

function doiToHTML(element) {
  let doi = element.getAttribute('data-citation-id');
  let style = element.getAttribute('data-citation-style');
  if (doi == null || style == null) return null;
  let citation = new Cite(doi);
  return citation.format('bibliography', {
    format: 'html',
    template: style,
    lang: 'en-US'
  }).replace(/(https:\/\/doi\.org\/([^<]*))/, '<a href="$1">doi:$2</a>');
}

document.querySelectorAll(".citation").forEach(function(element) {
  var html = doiToHTML(element);
  if (html != null) element.innerHTML = html;
});
