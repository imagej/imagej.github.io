---
mediawiki: Time_Stamper
title: Time Stamper
categories: [Image annotation]
artifact: sc.fiji:Time_Stamper
---

This plugin adds time stamps to a stack. The times are drawn in the current foreground color. Use the color picker ({% include bc path='Image | Color | Color Picker'%} or double-click on the color picker button <img src="/media/plugins/color-picker.png" width="16"/> ) to set the foreground color. A dialog box allows the user to specify the starting time, time between frames, location, font size, decimal places and unit of time. Create a rectangular selection and the X and Y locations in the dialog box will be based on that selection. Set time between frames to zero to display nothing but the text in the Suffix field.

## Usage

Start the plugin on a stack or hyperstack using {% include bc path='Image | Stacks | Time Stamper'%}.

![](/media/plugins/time-stamper-parameters.png)

Options:

-   **Starting Time**
-   **Interval**

<!-- -->

-   **X Location**
-   **Y Location**
-   **Font Size**

  
The latter three values are determined from a rectangular ROI if a ROI is active upon start of the plugin.

-   **00:00 format**
-   **Decimal places**
-   **Suffix**
-   **Anti-aliased text**

![](/media/plugins/time-stamper-result.png)

 
