---
title: Videos 
section: Help:Editing the Wiki
description: This page demonstrates how to embed videos on a page.
nav-links: true
---

The `video` include allows you to embed video onto a page.

## YouTube

{% highlight liquid %}{% raw %}
{% include video platform="youtube" id="GVHaSQ_O6IE" aspect="1:1" %}
{% endraw %}{% endhighlight %}

{% include video platform="youtube" id="GVHaSQ_O6IE" aspect="1:1" %}

Above, we set the aspect ratio to 1:1 because the video is square; this
parameter is optional though, with the default being 4:3 at 400 x 300.

### YouTube playlists

The `video` include automatically detects when you pass a YouTube playlist ID
(they always start with `PL`), and embeds the playlist accordingly.

{% highlight liquid %}{% raw %}
{% include video platform="youtube" id="PLh7mLbGrvbzkQXGYPuyOpMiFT7pEUsYsf" %}
{% endraw %}{% endhighlight %}

{% include video platform="youtube" id="PLh7mLbGrvbzkQXGYPuyOpMiFT7pEUsYsf" %}

## Vimeo

{% highlight liquid %}{% raw %}
{% include video platform="vimeo" id="140929687" aspect="16:9" width=500 %}
{% endraw %}{% endhighlight %}

{% include video platform="vimeo" id="140929687" aspect="16:9" width=500 %}

We use the `width` parameter to make the above video from Vimeo a bit wider than the default of 400.

## SWITCHtube

{% highlight liquid %}{% raw %}
{% include video platform="switchtube" id="98578061" aspect="16:9" height=281 %}
{% endraw %}{% endhighlight %}

{% include video platform="switchtube" id="98578061" aspect="16:9" height=281 %}

We override this SWITCHtube video's height to be a specific value.
This is useful if you need to align a series of videos in a row.

## Direct links

{% highlight liquid %}{% raw %}
{% include video src="https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4" %}
{% endraw %}{% endhighlight %}

{% include video src="https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4" %}
