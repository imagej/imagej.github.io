---
title: Figures
---

{% include notice icon="warning" content="This page is still a work in progress. Please ignore for the moment!" %}

{% include figure/begin columns=2 title='Centered text at the top of the figure' caption='Centered text at the bottom of the figure' %}
  {% include figure/panel caption="Panel A: Top left"     %} {% include img src='icons/nih-image' %}
  {% include figure/panel caption="Panel B: Top right"    %} {% include img src='icons/imagej' %}
  {% include figure/panel caption="Panel C: Bottom left"  %} {% include img src='icons/imagej2' %}
  {% include figure/panel caption="Panel D: Bottom right with a really long caption, just to see what happens" %} {% include img src='icons/fiji' %}
{% include figure/end %}
