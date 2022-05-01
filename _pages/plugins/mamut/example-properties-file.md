---
title: Example mamut.properties file
---

The key-bindings used in the [MaMuT](/plugins/mamut) viewer can be customized through a text file, that allow you to remap any command to any key. To so, create a text file named `mamut.properties` in the `Fiji.app` folder (where the `plugins` and `jars` folders are). This file must follow this syntax example:

```
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
```

It follows the syntax `key=command`, one per line. Modifier keys such as {% include key key='Control' %} and {% include key key='Shift' %} are specified by prepending the key with their name, separated by a space escaped with a backslash `\`. Spaces in commands do not need to be escaped. The dash # character at the beginning of a line is used to insert comments.


____________________________________

```ini
# The key bindings for MaMuT viewer windows.
# Available actions are the following (space in between words must be included):
#   
#   add spot
#   delete spot
#   increase spot radius
#   increase spot radius a lot
#   increase spot radius a bit
#   decrease spot radius
#   decrease spot radius a lot
#   decrease spot radius a bit
#
#   semi-auto tracking
#   toggle linking mode
#
#   show help
#   toggle brightness dialog
#   toggle interpolation
#   toggle fused mode
#   toggle grouping
#
#   toggle source visibility 0
#   toggle source visibility 1
#   toggle source visibility ... up to 9
#
#   align XY plane
#   align ZY plane
#   align XZ plane
#
#   next timepoint
#   previous timepoint
#   step time forward
#   step time backward
#
# No space around '='!
# An action can have several key bindings.
# When using shift, control, etc... use a a backslash-space after the modifier
# (as in 'control\ Q').

A=add spot 
ENTER=add spot 
D=delete spot 
E=increase spot radius 
Q=decrease spot radius 
shift\ E=increase spot radius a lot 
shift\ Q=decrease spot radius a lot 
control\ E=increase spot radius a bit 
control\ Q=decrease spot radius a bit 
shift\ A=semi-auto tracking 
shift\ 
L=toggle linking mode L=toggle link 
F1=help

S=brightness settings 
F6=visibility and grouping 
I=toggle interpolation 
F=toggle fused mode 
G=toggle grouping 
T=toggle manual transformation

F8=record max projection movie 
F10=record movie

shift\ 1=toggle source visibility 0 
shift\ 2=toggle source visibility 1 
shift\ 3=toggle source visibility 2 
shift\ 4=toggle source visibility 3 
shift\ 5=toggle source visibility 4 
shift\ 6=toggle source visibility 5 
shift\ 7=toggle source visibility 6 
shift\ 8=toggle source visibility 7 
shift\ 9=toggle source visibility 8 
shift\ 0=toggle source visibility 9

shift\ Z=align XY plane 
shift\ X=align ZY plane 
shift\ Y=align XZ plane 
shift\ C=align XZ plane

CLOSE_BRACKET=step time forward 
M=next timepoint 
OPEN_BRACKET=step time backward 
N=previous timepoint

shift\ CLOSE_BRACKET=step time forward 
shift\ M=next timepoint 
shift\ OPEN_BRACKET=step time backward 
shift\ N=previous timepoint

shift\ B=set bookmark 
B=go to bookmark 
O=go to bookmark rotation
```
