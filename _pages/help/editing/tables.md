---
title: Tables
section: Help:Editing the Wiki
nav-links: true
---

This page explains how to insert a table into your page.

## Usage

There is no dedicated include to create a table. You can, however, easily
create a table in Markdown:

```
| Item 1 | Item 2 | Item 3 |
| :---: | :---: | :---: |
| A | B | C |
| 1 | 2 | 3 |
```
## Example
<p>
| Blue | Red | Green | Yellow | Purple |<br/>
| :---: | :---: | :---: | :---: |:---: |<br/>
| 5 | 4 | 3 | 2 | 1 |<br/>
| 1 | 2 | 3 | 4 | 5 |
</p>

produces:

| Blue | Red | Green | Yellow | Purple |
| :---: | :---: | :---: | :---: |:---: |
| 5 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 5 |



## Adding Images

A table with images, use the .image.table to make it align with text:
```
| :---: | :---: |
|![Image1](/path/to/image1.png){: .image.table} | Text associated with Image1.
| ![Image2](/path/to/image2.png){: .image.table} | Text associated with Image2 |
```

### Example
```
| :---: | :---: |
|![Plugins](/media/help/plugins.png){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways.
| ![Extend](/media/help/extend.png){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |
```
produces:

| :---: | :---: |
|![Plugins](/media/help/plugins.png){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways.
| ![Extend](/media/help/extend.png){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |
