---
title: Tables
section: Contribute:Editing the Wiki
nav-links: true
---

This page explains how to insert a table into your page.

## Usage

There is no dedicated include to create a table.
You can, however, easily create one using Markdown:

{% capture simple-table %}
| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |
{% endcapture %}
{% include editing/example code=simple-table %}

## Aligning Tables

By default, tables are stretched to 100% width:

| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |

If you want the table to be its natural width instead, put `{:.left}` beneath the table:

**Code**

```
| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |
{:.left}
```

**Result**

| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |
{:.left}

Or for a centered table, use `{:.center}`:

**Code**

```
| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |
{:.center}
```

**Result**

| Blue | Red | Green | Yellow | Purple |
|------|-----|-------|--------|--------|
| 5    | 4   | 3     | 2      | 1      |
| 1    | 2   | 3     | 4      | 5      |
{:.center}

## Aligning Columns

You can place `:` symbols in the table header to specify column alignment:

{% capture aligned-columns %}
|       Day | Abbreviation | Description     |
|----------:|:------------:|:----------------|
|    Monday |     Mon      | Dynamo anagram  |
|   Tuesday |     Tue      | Day of victory! |
| Wednesday |     Wed      | The best Addams |
|  Thursday |     Thu      | Friday's Friday |
|    Friday |     Fri      | TGIF            |
{% endcapture %}
{% include editing/example code=aligned-columns %}

## Adding Images

You can include images within tables:

{% capture table-with-images %}
| ![Plugins](/media/editing/plugins.png) | The bread and butter of ImageJ. |
| ![Extend](/media/editing/extend.png)   | You know you want to.           |
{% endcapture %}
{% include editing/example code=table-with-images %}

## Custom Styling

You can add custom styling to a table by attaching a
[CSS class](https://www.w3schools.com/Css/):

{% capture custom-styling %}
| Superhero     | Superpower           |
| ------------- | -------------------- |
| Cyclops       | optic blasts         |
| The Flash     | super speed          |
| Squirrel Girl | talks with squirrels |
{:.box}
{% endcapture %}
{% include editing/example code=custom-styling %}

If there is not already a class with the styling you want,
you can declare it inline:

{% capture custom-styling-inline %}
<style>
.power-levels-table {
  background-image: repeating-linear-gradient(60deg,
    plum, hotpink 30px, turquoise 30px, aquamarine 60px);
  font-family: "Comic Sans MS", "Comic Sans", cursive;
  font-weight: bold;
}
</style>

| Superhero      | Power Level |
| -------------- | -----------|
| Captain Marvel | ridiculous |
| Superman       | ludicrous  |
| Silver Surfer  | absurd     |
{:.power-levels-table}
{% endcapture %}
{% include editing/example code=custom-styling-inline %}

## Spreadsheets

You can embed an external spreadsheet.

### Google Sheets

{% highlight liquid %}{% raw %}
{% include spreadsheet platform="google" id="1xl0owZ1kAJDLrA2XtNjlvKwhO5ZsS5_CMmw-dU64sFk" %}
{% endraw %}{% endhighlight %}

{% include notice class="fas fa-hard-hat" content="This include is under construction! Coming soon." %}
