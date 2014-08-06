{{Infobox
| software               = ImageJ
| name                   = Dithering
| author                 = Gabriel Landini
| maintainer             = Gabriel Landini (G.Landini at bham. ac. uk)
| filename               = Dithering_.txt
| source                 = See below
| latest version         = v1.0 (17 May 2009)
| status                 = active 
}}

== Purpose ==
This macro takes an 8 bit greyscale or a 24 bit RGB image and performs dithering using one of the methods supported. 
Dithering is a type of half tone thresholding where greyscale (or RGB channel) intensity is converted into a local density of binary pixels. This is ideal for rendering images in devices with a binary output such as printers (greyscale) or with a small number of colours (colour dithering). 

In the case of 24 bit RGB images the macro lets you either apply dithering to the greyscale version of the image or to each of the RGB channels (colour dithering).

== Installation ==
Copy the source code below and save it into a file called "Dithering_.txt" somewhere in the /Plugins folder. Restarting Fiji or ImageJ will show a new command called "Dithering".

== Available methods ==
The following methods have been implemented (there are several more): Floyd-Steinberg, Atkinson, Jarvis-Judice-Ninke, Stucki, Bayer_2x2, Bayer_4x4, Bayer_8x8, Clustered_4x4 and Random.<br>
Scaling dithered images by certain factors introduce numerous artifacts, so it is essential to apply dithering after image resizing.<br>
Dithering results are best rendered when the image is displayed or printed using small pixels.

The following images have been magnified by a factor of 2 to show the individual pixels. 

[[Image:DitheringMontage.png]]

== Macro code ==
<source lang="java">

// Dithering
// G. Landini at bham. ac. uk
// 17/ May 2009

Dialog.create("Dithering");
items=newArray("Floyd-Steinberg", "Atkinson", "Jarvis-Judice-Ninke","Stucki",
        "Bayer_2x2", "Bayer_4x4", "Bayer_8x8", "Clustered_4x4", "Random");
doColour = false;

Dialog.addChoice("Method", items);
if (bitDepth==24) Dialog.addCheckbox("Colour dithering", false);
Dialog.show() ;
method=Dialog.getChoice();
if (bitDepth==24)
   doColour=Dialog.getCheckbox();

setBatchMode(true);
w=getWidth();
h=getHeight();
run("Duplicate...", "title="+method);
if (bitDepth == 24 && doColour) {
   run("RGB Stack");
   for (i=1; i<4; i++){
     showProgress(i/4);
     setSlice(i);
     dither(method);
   } 
   run("RGB Color");
}
else{
  if (bitDepth>8 && !doColour) run("8-bit");
  dither(method);
}
setBatchMode(false);

function dither(method) {
 if (method=="Floyd-Steinberg"){
  w1=7/16;
  w2=3/16;
  w3=5/16;
  w4=1/16;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      oldpixel = getPixel(x,y);
      if (oldpixel<128) newpixel=0; else newpixel=255;
      setPixel(x,y, newpixel);
      quant_error = oldpixel - newpixel;
      setPixel(x+1,y, getPixel(x+1,y) + w1 * quant_error);
      setPixel(x-1,y+1, getPixel(x-1,y+1) + w2 * quant_error);
      setPixel(x,y+1, getPixel(x,y+1) + w3 * quant_error);
      setPixel(x+1,y+1, getPixel(x+1,y+1) + w4 * quant_error);
    }
  }
 }
 else if (method=="Atkinson"){
  w1=1/8;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      oldpixel = getPixel(x,y);
      if (oldpixel<128) newpixel = 0; else newpixel=255;
      setPixel(x,y, newpixel);
      quant_error = oldpixel - newpixel;
      setPixel(x+1,y, getPixel(x+1,y) + w1 * quant_error);
      setPixel(x+2,y, getPixel(x+2,y) + w1 * quant_error);
      setPixel(x-1,y+1, getPixel(x-1,y+1) + w1 * quant_error);
      setPixel(x,y+1, getPixel(x,y+1) + w1 * quant_error);
      setPixel(x+1,y+1, getPixel(x+1,y+1) + w1 * quant_error);
      setPixel(x,y+2, getPixel(x,y+2) + w1 * quant_error);
    }
  }
 }
 else if (method=="Jarvis-Judice-Ninke"){
  w7=7/48;
  w5=5/48;
  w3=3/48;
  w1=1/48;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      oldpixel = getPixel(x,y);
      if (oldpixel<128) newpixel = 0; else newpixel=255;
      setPixel(x,y, newpixel);
      quant_error = oldpixel - newpixel;
      setPixel(x+1,y, getPixel(x+1,y) + w7 * quant_error);
      setPixel(x+2,y, getPixel(x+2,y) + w5 * quant_error);
      setPixel(x-2,y+1, getPixel(x-2,y+1) + w3 * quant_error);
      setPixel(x-1,y+1, getPixel(x-1,y+1) + w5 * quant_error);
      setPixel(x,y+1, getPixel(x,y+1) + w7 * quant_error);
      setPixel(x+1,y+1, getPixel(x+1,y+1) + w5 * quant_error);
      setPixel(x+2,y+1, getPixel(x+2,y+1) + w3 * quant_error);
      setPixel(x-2,y+2, getPixel(x-2,y+2) + w1 * quant_error);
      setPixel(x-1,y+2, getPixel(x-1,y+2) + w3 * quant_error);
      setPixel(x,y+2, getPixel(x,y+2) + w5 * quant_error);
      setPixel(x+1,y+2, getPixel(x+1,y+2) + w3 * quant_error);
      setPixel(x+2,y+2, getPixel(x+2,y+2) + w1 * quant_error);
    }
  }
 }
 else if (method=="Stucki"){
  w8= 8/42;
  w7=7/42;
  w5=5/42;
  w4= 4/42;
  w2=2/42;
  w1=1/42;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      oldpixel = getPixel(x,y);
      if (oldpixel<128) newpixel = 0; else newpixel=255;
      setPixel(x,y, newpixel);
      quant_error = oldpixel - newpixel;
      setPixel(x+1,y, getPixel(x+1,y) + w7 * quant_error);
      setPixel(x+2,y, getPixel(x+2,y) + w5 * quant_error);
      setPixel(x-2,y+1, getPixel(x-2,y+1) + w2 * quant_error);
      setPixel(x-1,y+1, getPixel(x-1,y+1) + w4 * quant_error);
      setPixel(x,y+1, getPixel(x,y+1) + w8 * quant_error);
      setPixel(x+1,y+1, getPixel(x+1,y+1) + w4 * quant_error);
      setPixel(x+2,y+1, getPixel(x+2,y+1) + w2 * quant_error);
      setPixel(x-2,y+2, getPixel(x-2,y+2) + w1 * quant_error);
      setPixel(x-1,y+2, getPixel(x-1,y+2) + w2 * quant_error);
      setPixel(x,y+2, getPixel(x,y+2) + w4 * quant_error);
      setPixel(x+1,y+2, getPixel(x+1,y+2) + w2 * quant_error);
      setPixel(x+2,y+2, getPixel(x+2,y+2) + w1 * quant_error);
    }
  }
 }
 else if (method=="Bayer_2x2"){
  d= newArray(2,3,4,1);
  for (i=0; i<d.length; i++)
    d[i]=d[i] * 64 - 1;

  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      if (getPixel(x,y)>=d[(y%2*2+x%2)])
          newpixel = 255; 
      else 
          newpixel=0;
      setPixel(x,y, newpixel);
    }
  }
 }
 else if (method=="Bayer_4x4"){
  d= newArray(0.1250, 1.0000, 0.1875, 0.8125, 0.6250, 0.3750, 0.6875,
     0.4375,0.2500, 0.8750, 0.0625, 0.9375, 0.7500, 0.5000, 0.5625, 0.3125);
  for (i=0; i<d.length; i++)
    d[i]*=255;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      if (getPixel(x,y)>=d[(y%4*4+x%4)])
          newpixel = 255; 
      else 
          newpixel = 0;
      setPixel(x,y, newpixel);
    }
  }
 }
 else if (method=="Bayer_8x8"){
  d= newArray(1, 33,  9, 41, 3,  35, 11, 43, 49, 17, 57, 25, 51, 19, 59, 27, 13, 45, 5, 
    37, 15, 47, 7, 39, 61, 29, 53, 21, 63, 31, 55, 23, 4, 36, 12, 44, 2, 34, 10, 42, 52,
    20, 60, 28, 50, 18, 58, 26, 16, 48, 8, 40, 14, 46, 6, 38, 64, 32, 56, 24, 62, 30,
    54, 22);

  for (i=0; i<d.length; i++)
    d[i]=d[i] * 4 - 1;

  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      if (getPixel(x,y)>=d[(y%8*8+x%8)])
          newpixel = 255; 
      else 
          newpixel = 0;
      setPixel(x,y, newpixel);

    }
  }
 }
 else if (method=="Clustered_4x4"){
  d= newArray(0.7500, 0.3750, 0.6250, 0.2500, 0.0625, 1.0000, 0.8750, 0.4375,
    0.5000, 0.8125, 0.9375, 0.1250, 0.1875, 0.5625, 0.3125, 0.6875);
  for (i=0; i<d.length; i++)
    d[i]*=255;

  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      if (getPixel(x,y)>=d[(y%4*4+x%4)])
          newpixel = 255; 
      else 
          newpixel = 0;
      setPixel(x,y, newpixel);
    }
  }
 }
else if (method=="Random"){
  w1=1/8;
  for (y=0; y<h; y++){
    for (x=0; x<w; x++){
      if(getPixel(x,y)> random*255)
        setPixel(x,y, 255);
      else   
        setPixel(x,y, 0);
    }
  }
 }
}
</source>

[[Category:Plugins]]
[[Category:Segmentation]]
