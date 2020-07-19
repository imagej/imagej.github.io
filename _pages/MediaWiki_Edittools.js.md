// copied from [[mw:User:Alex Smotrov/edittools.js]], modified for use on the English Wikipedia.
// enableForAllFields() feature from [[commons:MediaWiki:Edittools.js]]
// combined and modified by [[User:Ilmari Karonen]]
// after making changes to this page and testing them, update the number after "edittools-version-" in [[MediaWiki:Edittools]] to purge the cache for everyone
// <source lang="javascript">

if (typeof (EditTools_set_focus) == 'undefined')
   var EditTools_set_focus = true;

if (typeof (EditTools_set_focus_initially) == 'undefined')
   var EditTools_set_focus_initially = EditTools_set_focus;

var EditTools =
{
  charinsert : {
     'Insert': ' – — … ‘ “ ’ ” ° ″ ′ ≈ ≠ ≤ ≥ ± − × ÷ ← → · §  Sign_your_posts_on_talk_pages: ~~\~~  Cite_your_sources: <ref>+</ref>',
     'Wiki markup': '{\{+}}  {\{\{+}}}  |  [+]  [\[+]]  [\[Category:+]]  #REDIRECT.[\[+]]  &nbsp;  <s>+</s>  <sup>+</sup>  <sub>+</sub>  <code>+</code>  <blockquote>+</blockquote>  <ref>+</ref>  {\{Reflist}}  <references/>  <includeonly>+</includeonly>  <noinclude>+</noinclude>  {\{DEFAULTSORT:+}}  <nowiki>+</nowiki>  <!--.+_-->  <span.class="plainlinks">+</span>',
     'Symbols': '~ | ¡¿†‡↔↑↓•¶  # ½⅓⅔¼¾⅛⅜⅝⅞∞  ‘“’” «+»  ¤₳฿₵¢₡₢$₫₯€₠₣ƒ₴₭₤ℳ₥₦№₧₰£៛₨₪৳₮₩¥  ♠♣♥♦  m² m³', 
     'Latin': 'ÁáĆćÉéÍíĹĺŃńÓóŔŕŚśÚúÝýŹź  ÀàÈèÌìÒòÙù  ÂâĈĉÊêĜĝĤĥÎîĴĵÔôŜŝÛûŴŵŶŷ  ÄäËëÏïÖöÜüŸÿ  ß  ÃãẼẽĨĩÑñÕõŨũỸỹ  ÇçĢģĶķĻļŅņŖŗŞşŢţ  Đ đ  Ů ů  ǍǎČčĎďĚěǏǐĽľŇňǑǒŘřŠšŤťǓǔŽž  ĀāĒēĪīŌōŪūȲȳǢǣ  ǖǘǚǜ  ĂăĔĕĞğĬĭŎŏŬŭ  ĊċĖėĠġİıŻż  ĄąĘęĮįǪǫŲų  ḌḍḤḥḶḷḸḹṂṃṆṇṚṛṜṝṢṣṬṭ  Ł ł  ŐőŰű  Ŀ ŀ  Ħ ħ  ÐðÞþ  Œ œ  ÆæØøÅå  Ə ə   {\{Unicode|+}}',
     'Greek': 'ΆάΈέΉήΊίΌόΎύΏώ  ΑαΒβΓγΔδ  ΕεΖζΗηΘθ  ΙιΚκΛλΜμ  ΝνΞξΟοΠπ  ΡρΣσςΤτΥυ  ΦφΧχΨψΩω   {\{Polytonic|+}}',
     'Cyrillic': 'АаБбВвГг  ҐґЃѓДдЂђ  ЕеЁёЄєЖж  ЗзЅѕИиІі  ЇїЙйЈјКк  ЌќЛлЉљМм  НнЊњОоПп  РрСсТтЋћ  УуЎўФфХх  ЦцЧчЏџШш  ЩщЪъЫыЬь  ЭэЮюЯя ӘәӨөҒғҖҗ ҚқҜҝҢңҮү ҰұҲҳҸҹҺһ  ҔҕӢӣӮӯҘҙ  ҠҡҤҥҪҫӐӑ  ӒӓӔӕӖӗӰӱ  ӲӳӸӹӀ  ҞҟҦҧҨҩҬҭ  ҴҵҶҷҼҽҾҿ  ӁӂӃӄӇӈӋӌ  ӚӛӜӝӞӟӠӡ  ӤӥӦӧӪӫӴӵ',
     'Hebrew': 'אבגדהוזחטיךכלםמןנסעףפץצקרשת  ׳ ״  װױײ',
     'Arabic': 'ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي',
     'IPA': 'p b t d t̪ d̪ ʈɖcɟkɡqɢʡʔ  ɸβfvθðszʃʒɕʑʂʐçʝxɣχʁħʕʜʢhɦ  m ɱnn̪ɳɲŋɴ  β̞ ʋɹɻjɰ  ʙrʀɾɽ ɢ̆ ʡ̯  ll̪ɫɬɮɺɭʎ ʎ̯ ʟ ʟ̆  ʍwɥɧ  ɓɗʄɠʛ  ʘǀǃǂǁ  i y ɨʉɯu  ɪʏʊ  e øɘɵɤo  ə ɚ  ɛœɜɝɞʌɔ  æ ɐ  a ɶɑɒ  ʰʷʲˠˤⁿˡ  ˈˌːˑ ̪   {\{IPA|+}}'
  },

  charinsertDivider : "\240",

  extraCSS : '\
    #editpage-specialchars {\
      margin-top: 15px;\
      border-width: 1px;\
      border-style: solid;\
      border-color: #aaaaaa;\
      padding: 2px;\
    }\
    #editpage-specialchars a {\
    }\
    #editpage-specialchars a:hover {\
    }\
  ',

  appendExtraCSS : function ()
  {
     appendCSS(EditTools.extraCSS);
  },


  cookieName : 'edittoolscharsubset',

  createEditTools : function (placeholder)
  {
     var box = document.createElement("div");
     box.id = "editpage-specialchars";
     box.title = 'Click on the character or tag to insert it into edit window';
     
     //append user-defined sets
     if (window.charinsertCustom)
	for (id in charinsertCustom)
	   if (EditTools.charinsert[id]) EditTools.charinsert[id] += ' ' + charinsertCustom[id];
	   else EditTools.charinsert[id] = charinsertCustom[id];

     //create drop-down select
     var prevSubset = 0, curSubset = 0;
     var sel = document.createElement('select'), id;
     for (id in EditTools.charinsert)
	sel.options[sel.options.length] = new Option(id, id);
     sel.selectedIndex = 0;
     sel.style.cssFloat = sel.style.styleFloat = 'left';
     sel.style.marginRight = '5px';
     sel.title = 'Choose character subset';
     sel.onchange = sel.onkeyup = selectSubset;
     box.appendChild(sel);

     //create "recall" switch
     if (window.editToolsRecall) {
	var recall = document.createElement('span');
	recall.appendChild(document.createTextNode('↕')); // ↔
	recall.onclick = function () {
	   sel.selectedIndex = prevSubset;
	   selectSubset();
	}
	with (recall.style) { cssFloat = styleFloat = 'left'; marginRight = '5px'; cursor = 'pointer'; }
	box.appendChild(recall);
     }

     // load latest selection from cookies
     try {
        var cookieRe = new RegExp ("(?:^|;)\\s*" + EditTools.cookieName + "=(\\d+)\\s*(?:;|$)");
        var m = cookieRe.exec(document.cookie);
        if (m && m.length > 1 && parseInt(m[1]) < sel.options.length)
           sel.selectedIndex = parseInt(m[1]);
     } catch (err) { /* ignore */ }

     placeholder.parentNode.replaceChild(box, placeholder);
     selectSubset();
     return;

     function selectSubset ()
     {
	//remember previous (for "recall" button)
	prevSubset = curSubset;
	curSubset = sel.selectedIndex;
        //save into cookies for persistence
        try {
           var expires = new Date ();
           expires.setTime( expires.getTime() + 30 * 24 * 60 * 60 * 1000 );  // + 30 days
           document.cookie = EditTools.cookieName + "=" + curSubset + ";path=/;expires=" + expires.toUTCString();
        } catch (err) { /* ignore */ }
	//hide other subsets
	var pp = box.getElementsByTagName('p') ;
	for (var i=0; i<pp.length; i++)
	   pp[i].style.display = 'none';
	//show/create current subset
	var id = sel.options[curSubset].value;
	var p = document.getElementById(id);
	if (!p){
	   p = document.createElement('p');
	   p.id = id;
	   if (id == 'Arabic' || id == 'Hebrew'){ p.style.fontSize = '120%'; p.dir = 'rtl'; }
	   EditTools.createTokens(p, EditTools.charinsert[id]);
	   box.appendChild(p);
	}
	p.style.display = 'inline';
     } 
  },
  createTokens : function (paragraph, str)
  {
     var tokens = str.split(' '), token, i, n;
     for (i = 0; i < tokens.length; i++) {
	token = tokens[i];
	n = token.indexOf('+');
	if (token == '' || token == '_')
	   addText(EditTools.charinsertDivider + ' ');
	else if (token == '\n')
	   paragraph.appendChild(document.createElement('br'));
	else if (token == '___')
	   paragraph.appendChild(document.createElement('hr'));
	else if (token.charAt(token.length-1) == ':')  // : at the end means just text
	   addBold(token);
	else if (n == 0) // +<tag>  ->   <tag>+</tag>
	   addLink(token.substring(1), '</' + token.substring(2), token.substring(1));
	else if (n > 0) // <tag>+</tag>
	   addLink(token.substring(0,n), token.substring(n+1));
	else if (token.length > 2 && token.charCodeAt(0) > 127) //a string of insertable characters
	   for (var j=0; j < token.length; j++) addLink(token.charAt(j), '');
	else
	   addLink(token, '');
     }
     return;

     function addLink (tagOpen, tagClose, name)
     {
	var a = document.createElement('a');
	tagOpen = tagOpen.replace(/\./g,' ');
	tagClose = tagClose ? tagClose.replace(/_/g,' ') : '';
	name = name || tagOpen + tagClose;
	name = name.replace(/\\n/g,'');
	a.appendChild(document.createTextNode(name));
	a.href = "javascript:insertTags('" + tagOpen + "','" + tagClose + "','')";
	paragraph.appendChild(a);
	addText(' ');
     }
     function addBold (text)
     {
	var b = document.createElement('b');
	b.appendChild(document.createTextNode(text.replace(/_/g,' ')));
	paragraph.appendChild(b);
	addText(' ');
     }     
     function addText (txt)
     {
	paragraph.appendChild(document.createTextNode(txt));
     }
  },
 
 
  enableForAllFields : function ()
  {
     if (typeof (insertTags) != 'function' || window.WikEdInsertTags) return;
     // insertTags from the site-wide /skins-1.5/common/edit.js just inserts in the first
     // textarea in the document. Evidently, that's not good if we have multiple textareas.
     // My first idea was to simply add a hidden textarea as the first one, and redefine
     // insertTags such that it copied first the last active textareas contents over to that hidden
     // field, set the cursor or selection there, let the standard insertTags do its thing, and
     // then copy the hidden field's text, cursor position and selection back to the currently
     // active field. Unfortunately, that is just as complex as simply copying the whole code
     // from wikibits to here and let it work on the right text field in the first place.
     var texts = document.getElementsByTagName ('textarea');    
     for (var i = 0; i < texts.length; i++) {
	addHandler (texts[i], 'focus', EditTools.registerTextField);
     }
     // While we're at it, also enable it for input fields
     texts = document.getElementsByTagName ('input');
     for (var i = 0; i < texts.length; i++) {
	if (texts[i].type == 'text') addHandler (texts[i], 'focus', EditTools.registerTextField);
     }
     insertTags = EditTools.insertTags; // Redefine the global insertTags
  },
 
  last_active_textfield : null,
 
  registerTextField : function (evt)
  {
     var e = evt || window.event;
     var node = e.target || e.srcElement;
     if (!node) return;
     EditTools.last_active_textfield = node.id;
     return true;
  },
 
  getTextArea : function ()
  {
     var txtarea = null;
     if (EditTools.last_active_textfield && EditTools.last_active_textfield != "")
	txtarea = document.getElementById (EditTools.last_active_textfield);
     if (!txtarea) {
	// Fallback option: old behaviour
	if (document.editform) {
	   txtarea = document.editform.wpTextbox1;
	} else {
	   // Some alternate form? Take the first one we can find
	   txtarea = document.getElementsByTagName ('textarea');
	   if (txtarea.length > 0) txtarea = txtarea[0]; else txtarea = null;
	}
     }
     return txtarea;
  },
 
  insertTags : function (tagOpen, tagClose, sampleText)
  {
     var txtarea = EditTools.getTextArea ();
     if (!txtarea) return;
     var selText, isSample = false;

     function checkSelectedText ()
     {
	if (!selText) {
	   selText = sampleText; isSample = true;
	} else if (selText.charAt (selText.length - 1) == ' ') { // Exclude ending space char
	   selText = selText.substring (0, selText.length - 1);
	   tagClose += ' ';
	} 
     }
 
     if (document.selection && document.selection.createRange) { // IE/Opera
	// Save window scroll position
	var winScroll = 0;
	if (document.documentElement && document.documentElement.scrollTop)
	   winScroll = document.documentElement.scrollTop;
	else if (document.body)
	   winScroll = document.body.scrollTop;
	// Get current selection  
	txtarea.focus();
	var range = document.selection.createRange();
	selText = range.text;
	// Insert tags
	checkSelectedText ();
	range.text = tagOpen + selText + tagClose;
	// Mark sample text as selected
	if (isSample && range.moveStart) {
	   if (window.opera) tagClose = tagClose.replace (/\n/g, "");
	   range.moveStart( 'character', - tagClose.length - selText.length); 
	   range.moveEnd ('character', - tagClose.length); 
	}
	range.select ();   
	// Restore window scroll position
	if (document.documentElement && document.documentElement.scrollTop)
	   document.documentElement.scrollTop = winScroll;
	else if (document.body)
	   document.body.scrollTop = winScroll;
     } else if (txtarea.selectionStart || txtarea.selectionStart == '0') { // Mozilla
	// Save textarea scroll position
	var textScroll = txtarea.scrollTop;
	// Get current selection
	txtarea.focus();
	var startPos = txtarea.selectionStart;
	var endPos   = txtarea.selectionEnd;
	selText = txtarea.value.substring (startPos, endPos);
	// Insert tags
	checkSelectedText ();
	txtarea.value = txtarea.value.substring (0, startPos)
	+ tagOpen + selText + tagClose
	+ txtarea.value.substring (endPos);
	// Set new selection
	if (isSample) {
	   txtarea.selectionStart = startPos + tagOpen.length;
	   txtarea.selectionEnd = startPos + tagOpen.length + selText.length;
	} else {
	   txtarea.selectionStart = startPos + tagOpen.length + selText.length + tagClose.length;
	   txtarea.selectionEnd = txtarea.selectionStart;
	}
	// Restore textarea scroll position
	txtarea.scrollTop = textScroll;
     }
  }, // end insertTags
 
  setup : function ()
  {
     var placeholder = document.getElementById("editpage-specialchars");
     if (!placeholder) return;  // has this already been run once?
     EditTools.appendExtraCSS ();
     EditTools.createEditTools (placeholder);
     EditTools.enableForAllFields ();
  }

}; // end EditTools
   
// Do not use addOnloadHook; it runs *before* the onload event fires. At that time, onclick or
// onfocus handlers may not yet be set up properly.
hookEvent ('load', EditTools.setup);

// </source>
