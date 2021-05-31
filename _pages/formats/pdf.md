---
mediawiki: Extract_Images_From_PDF...
title: Extract Images From PDF...
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
artifact: sc.fiji:IO_
---


Select {% include bc path='File|Import|Extract Images From PDF...'%}

A dialog pops up to pick a file. Choose a .pdf file, and all its images will be opened as ImageJ images, in their original resolution.

### From URL

If the PDF file is on the web, use a macro or script to call the plugin with the URL as argument:

      IJ.runPlugIn("io.Extract_Images_From_PDF", "http://www.example.org/slides.pdf")

For example, open the Jython Interpreter from Plugins / Scripting / Jython Interpreter (See [Scripting Help](/scripting)), and paste the above with a desired .pdf URL argument.

 
