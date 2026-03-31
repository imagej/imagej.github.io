/* Credit:
 * - https://stackoverflow.com/a/987376/1207769
 * - https://www.w3schools.com/howto/howto_js_copy_clipboard.asp
 */
function selectAndCopy(element) {
  if (document.body.createTextRange) { //ms
    var range = document.body.createTextRange();
    range.moveToElementText(element);
    range.select();
  }
  else if (window.getSelection) { //all others
    var selection = window.getSelection();
    var range = document.createRange();
    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
  }
  document.execCommand("copy");
}

// Load emgithub embeds with the correct style for the current light/dark theme.
// The _includes/code template emits a <div class="emgithub-embed" data-src-base="...">
// placeholder (URL without &style=). We inject the <script> tag at runtime so the
// style can match the active theme, and re-inject when the user toggles the theme.
(function () {
  function emgithubStyle() {
    return document.documentElement.getAttribute('data-theme') === 'dark'
      ? 'github-dark' : 'github';
  }

  function loadEmbed(div) {
    div.innerHTML = '';
    var script = document.createElement('script');
    script.src = div.dataset.srcBase + '&style=' + emgithubStyle();
    div.appendChild(script);
  }

  function loadAllEmbeds() {
    document.querySelectorAll('.emgithub-embed').forEach(loadEmbed);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadAllEmbeds);
  } else {
    loadAllEmbeds();
  }

  // Re-render when the user toggles light/dark (theme.js sets data-theme on <html>).
  new MutationObserver(function (mutations) {
    for (var i = 0; i < mutations.length; i++) {
      if (mutations[i].attributeName === 'data-theme') { loadAllEmbeds(); return; }
    }
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
})();

// Splice in a "Copy" button next to each code block.
document.querySelectorAll("pre").forEach(function(pre) {
  if (pre.childElementCount != 1) return;
  var code = pre.children[0];
  if (code.nodeName != "CODE") return;

  var copy = document.createElement("A");
  copy.innerHTML = "Copy";
  copy.style.backgroundColor = '#f7f7f7';
  copy.style.border = '1px solid black';
  copy.style.borderRadius = '3px';
  copy.style.color = '#586069';
  copy.style.cursor = 'pointer';
  copy.style.display = 'none';
  copy.style.font = 'bold 1em monospace';
  copy.style.padding = '0.4rem';
  copy.style.position = 'absolute';
  copy.style.right = '5px';
  copy.style.textDecoration = 'none';
  copy.style.top = '5px';
  copy.onclick = function(e) { selectAndCopy(code); }

  pre.onmouseover = function(e) { copy.style.display = 'inline'; }
  pre.onmouseout = function(e) { copy.style.display = 'none'; }
  pre.style.position = 'relative';
  pre.insertBefore(copy, code);
});
