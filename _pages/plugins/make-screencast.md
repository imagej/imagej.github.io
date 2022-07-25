---
mediawiki: Make_Screencast
name: "Make\_Screencast.bsh"
title: Make Screencast
categories: [Scripting]
dev-status: "stable"
team-founder: '@dscho'
team-maintainer: '@dscho'
---


{% capture source%}
{% include github repo='fiji' branch='master' path='plugins/Scripts/File/Make_Screencast.bsh' %}
{% endcapture %}
{% include info-box filename='Make\_Screencast.bsh' source=source %}

**Make Screencast** is a [Beanshell](/scripting/beanshell) script to record a screencast in {% include wikipedia title='Ogg' text='Ogg'%} or {% include wikipedia title='QuickTime File Format' text='Quicktime'%} video formats.

Access it via {% include bc path='File | Make Screencast'%}.

Stop recording the screencast via {% include bc path='File | Stop Screencast'%}.

**Note**: This script requires the open source video player [VLC](http://www.videolan.org/vlc/index.html) to be installed. When started, it tries to autodetect VLC on your system, and asks to install it if it fails to detect it.

# Tips for a good screencast

-   A screencast's primary purpose is to cast the screen. So: make sure that something moves on the screen every once in a while, rather than presenting a boring static screen while rambling on.
-   Take your time. There is no need to click so fast that nobody can follow.
-   Use the mouse. If you use keyboard shortcuts, be sure to tell the user, preferably by pointing to a menu item whose label mentions the shortcut. Remember: you want to teach others, not to show off how clever you are.
-   Make an outline As with any good presentation, you want to tell a story. Take the audience from where they are right now, motivate them (e.g. by showing a nice image to process), explain the steps, show the end result. Maybe end on a funny note.
-   What makes a good screencast excellent is a good verbal explanation. It is okay to explain slowly, with lots of breaks, but it needs to give the whole presentation a shape and a direction.

The crucial -- and most difficult part -- is without doubt the verbal explanation. To that end, it is most helpful to imagine a real person to direct your explanation to. It cannot hurt to practice what you want to say without recording it right away.
