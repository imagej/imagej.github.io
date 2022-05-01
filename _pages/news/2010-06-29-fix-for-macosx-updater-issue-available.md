---
title: 2010-06-29 - Fix for MacOSX Updater issue available
---

**Critical:** If you update Fiji on MacOSX, and instead of a Fiji window nothing is opened when you try to restart Fiji, you need to follow [these instructions](/learn/troubleshooting).  
Earlier, these instructions were quite involved, but we have a small Java application now which discovers where you installed Fiji (it first looks in the Dock, then on the Desktop, then in Applications, and falls back to asking the user when it did not find Fiji) and fixes the executable permissions.


