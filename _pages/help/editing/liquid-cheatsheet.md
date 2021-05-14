---
title: Editing the Wiki - Liquid Cheatsheet
section: Help:Editing the Wiki
---

## Truthy or Falsy?

<table style="width: auto">
<tbody>
<tr><th>Expression</th><th>truthiness</th></tr>
<tr><td><code>"have a cow"</code></td><td>{% if "have a cow" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>""</code></td><td>{% if "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil</code></td><td>{% if nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or ""</code></td><td>{% if nil or "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or "" or "hello" or "goodbye"</code></td><td>{% if nil or "" or "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" or "hello" or "goodbye"</code></td><td>{% if "" or "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"hello" or "goodbye"</code></td><td>{% if "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or ""</code></td><td>{% if nil or "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" or nil</code></td><td>{% if "" or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or false</code></td><td>{% if true or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or true</code></td><td>{% if false or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or true</code></td><td>{% if true or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or false</code></td><td>{% if false or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or nil</code></td><td>{% if true or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or true</code></td><td>{% if nil or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or nil</code></td><td>{% if false or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or false</code></td><td>{% if nil or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or nil or true</code></td><td>{% if false or nil or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or false or true</code></td><td>{% if nil or false or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and ""</code></td><td>{% if nil and "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" and nil</code></td><td>{% if "" and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and false</code></td><td>{% if true and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and true</code></td><td>{% if false and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and true</code></td><td>{% if true and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and false</code></td><td>{% if false and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and nil</code></td><td>{% if true and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and true</code></td><td>{% if nil and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and nil</code></td><td>{% if false and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and false</code></td><td>{% if nil and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and nil and true</code></td><td>{% if false and nil and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and false and true</code></td><td>{% if nil and false and true %} true {% else %} false {% endif %}</td></tr>
</tbody>
</table>
