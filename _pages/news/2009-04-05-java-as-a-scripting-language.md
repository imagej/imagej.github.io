---
title: 2009-04-05 - Java as a scripting language
categories: [News]
---

## Is Java a scripting language?

In the next Fiji release, Java will behave as if it were a scripting language: just drop your .java file into plugins/ and call {% include bc path='Plugins | Scripting | Refresh Javas'%}. You will not only see the plugin appearing in your Plugins folder, when you click on it, it will be compiled and run (thanks to OpenJDK's javac, which we bundle in Fiji).

The best thing about it: you can change the source in the .java file, and Fiji picks up on that when you call that plugin again, recompiling it as needed -- without the need to restart Fiji or call {% include bc path='Help | Update Menus'%}.

So indeed, Java becomes a scripting language!


