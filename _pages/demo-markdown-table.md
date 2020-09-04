---
title: Demo Markdown Table
layout: page
categories: demo
description: This page explains how to insert a markdown table into your page, as well as add images to said table.
---
## Usage

We do not have a dedicated include to create a table. You can, however, easily create a table in markdown:

```
| Item 1 | Item 2 | Item 3 |
| :---: | :---: | :---: |
| A | B | C |
| 1 | 2 | 3 |
```
## Example
```
| Blue | Red | Green | Yellow | Purple |
| :---: | :---: | :---: | :---: |:---: |
| 5 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 5 |
```
produces:
| Blue | Red | Green | Yellow | Purple |
| :---: | :---: | :---: | :---: |:---: |
| 5 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 5 |

## Adding Images

A table with images, use the .image.table to make it align with text:
```
| :---: | :---: |
|![Image1]({{"/path/to/image1.png" | relative_url}}){: .image.table} | Text associated with Image1.
| ![Image2]({{"/path/to/image2.png" | relative_url}}){: .image.table} | Text associated with Image2 |
```
**Note:** the method above assumes that your images are stored within the repository, thus uses the `relative_url` tag.

### Example
```
| :---: | :---: |
|![Plugins]({{"/images/icons/plugins_icon.png" | relative_url}}){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways.
| ![Extend]({{"/images/icons/extend_icon.png" | relative_url}}){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |
```
produces:

| :---: | :---: |
|![Plugins]({{"/images/icons/plugins_icon.png" | relative_url}}){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways.
| ![Extend]({{"/images/icons/extend_icon.png" | relative_url}}){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |
