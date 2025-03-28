---
mediawiki: List_all_threads
title: List all threads
categories: [Scripting,Unmaintained]
---

## Purpose

An example [Jython](/scripting/jython) script to illustrate how to query a ThreadGroup recursively to gather all children Thread instances.

The output is something like the following:

```
Threads:
1: Reference Handler
2: Finalizer
3: Signal Dispatcher
4: Java2D Disposer
5: TimerQueue
6: AWT-XAWT
7: AWT-Shutdown
8: AWT-EventQueue-0
9: SocketListener
10: DestroyJavaVM
11: pool-3-thread-1
12: 3D-V-IMP-updater
13: pool-4-thread-1
14: list all threads
15: J3D-RenderingAttributesStructureUpdateThread
16: J3D-TimerThread
17: J3D-NotificationThread
18: J3D-MasterControl-1
19: J3D-Renderer-1
20: J3D-BehaviorStructureUpdateThread-1
21: J3D-GeometryStructureUpdateThread-1
22: J3D-SoundStructureUpdateThread-1
23: J3D-RenderingEnvironmentStructureUpdateThread-1
24: J3D-TransformStructureUpdateThread-1
25: J3D-BehaviorScheduler-1
26: J3D-RenderStructureUpdateThread-1
27: J3D-SoundSchedulerUpdateThread-1
28: J3D-InputDeviceScheduler-1
```

## Code

```python
from jarray import zeros
from java.lang import *

def findRootThreadGroup():
    tg = Thread.currentThread().getThreadGroup()
    root_tg = tg.getParent()
    root_tg = tg
    parent = root_tg.getParent()
    while None != parent:
        root_tg = parent
        parent = parent.getParent()
    return root_tg

def listGroup(list, group):
    threads = zeros(group.activeCount(), Thread)
    group.enumerate(threads, 0)
    groups = zeros(group.activeGroupCount(), ThreadGroup)
    group.enumerate(groups, 0)
    for t in threads:
        if None is not t: list.append(t.getName())
    for g in groups:
        if None is not g: listGroup(list, g)

def listThreadNames():
    list = []
    listGroup(list, findRootThreadGroup())
    return list

IJ.log("Threads:")
i = 1
for thread in listThreadNames():
    IJ.log(str(i) + ": " + thread)
    i += 1
```
## See also

[Jython Scripting](/scripting/jython)

  
