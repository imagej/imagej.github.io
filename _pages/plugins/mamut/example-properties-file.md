---
mediawiki: Example_mamut.properties_file
title: Example mamut.properties file
categories: [Tutorials]
---

The key-bindings used in the [MaMuT](/plugins/mamut) viewer can be customized through a text file, that allow you to remap any command to any key. To so, create a text file named `mamut.properties` in the `Fiji.app` folder (where the `plugins` and `jars` folders are). This file must follow this syntax example:

    A=add spot
    ENTER=add spot
    D=delete spot
    E=increase spot radius
    Q=decrease spot radius
    shift\ E=increase spot radius a lot
    shift\ Q=decrease spot radius a lot
    control\ E=increase spot radius a bit
    control\ Q=decrease spot radius a bit
    ...

It follows the syntax `key=command`, one per line. Modifier keys such as {% include key key='Control' %} and {% include key key='Shift' %} are specified by prepending the key with their name, separated by a space escaped with a backslash `\`. Spaces in commands do not need to be escaped. The dash \# character at the beginning of a line is used to insert comments.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

&lt;source lang="properties&gt;

1.  The key bindings for MaMuT viewer windows.
2.  Available actions are the following (space in between words must be included):
3.  
4.  add spot
5.  delete spot
6.  increase spot radius
7.  increase spot radius a lot
8.  increase spot radius a bit
9.  decrease spot radius
10. decrease spot radius a lot
11. decrease spot radius a bit
12.
13. semi-auto tracking
14. toggle linking mode
15.
16. show help
17. toggle brightness dialog
18. toggle interpolation
19. toggle fused mode
20. toggle grouping
21.
22. toggle source visibility 0
23. toggle source visibility 1
24. toggle source visibility ... up to 9
25.
26. align XY plane
27. align ZY plane
28. align XZ plane
29.
30. next timepoint
31. previous timepoint
32. step time forward
33. step time backward
34.
35. No space around '='!
36. An action can have several key bindings.
37. When using shift, control, etc... use a a backslash-space after the modifier
38. (as in 'control\\ Q').

A=add spot ENTER=add spot D=delete spot E=increase spot radius Q=decrease spot radius shift\\ E=increase spot radius a lot shift\\ Q=decrease spot radius a lot control\\ E=increase spot radius a bit control\\ Q=decrease spot radius a bit shift\\ A=semi-auto tracking shift\\ L=toggle linking mode L=toggle link F1=help

S=brightness settings F6=visibility and grouping I=toggle interpolation F=toggle fused mode G=toggle grouping T=toggle manual transformation

F8=record max projection movie F10=record movie

shift\\ 1=toggle source visibility 0 shift\\ 2=toggle source visibility 1 shift\\ 3=toggle source visibility 2 shift\\ 4=toggle source visibility 3 shift\\ 5=toggle source visibility 4 shift\\ 6=toggle source visibility 5 shift\\ 7=toggle source visibility 6 shift\\ 8=toggle source visibility 7 shift\\ 9=toggle source visibility 8 shift\\ 0=toggle source visibility 9

shift\\ Z=align XY plane shift\\ X=align ZY plane shift\\ Y=align XZ plane shift\\ C=align XZ plane

CLOSE\_BRACKET=step time forward M=next timepoint OPEN\_BRACKET=step time backward N=previous timepoint

shift\\ CLOSE\_BRACKET=step time forward shift\\ M=next timepoint shift\\ OPEN\_BRACKET=step time backward shift\\ N=previous timepoint

shift\\ B=set bookmark B=go to bookmark O=go to bookmark rotation

</source>
