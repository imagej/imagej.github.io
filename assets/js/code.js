/* Credit: https://stackoverflow.com/a/987376/1207769 */
function selectText(element) {
	if (document.body.createTextRange) { //ms
		var range = document.body.createTextRange();
		range.moveToElementText(element);
		range.select();
	} else if (window.getSelection) { //all others
		var selection = window.getSelection();
		var range = document.createRange();
		range.selectNodeContents(element);
		selection.removeAllRanges();
		selection.addRange(range);
	}
}

// When double clicking in a code block, select the whole block.
document.querySelectorAll("code").forEach(function(code) {
	code.ondblclick = function(e) { selectText(this); }
});
