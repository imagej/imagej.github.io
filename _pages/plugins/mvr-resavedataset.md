---
mediawiki: MVR-ResaveDataset
title: MVR-ResaveDataset
categories: [Uncategorized]
---

Resaving a dataset is a simple two step process:

-   select existing dataset
-   define resaving parameters

![](/media/plugins/mvr-resave1.png)

![](/media/plugins/mvr-resave2.png)

Some log output shows the resaving process.

```
starting export...
proccessing timepoint 1 / 1
proccessing setup 1 / 7
Thu Aug 21 13:36:24 CEST 2014: Opening '/Users/janosch/no_backup/HisYFP/././spim_TL18_Angle000.lsm' [1388x1040x81 ch=0 tp=0 type=uint8 image=ArrayImg<UnsignedShortType>]
.
.
.
(Thu Aug 21 13:38:15 CEST 2014): Saved xml '/Users/janosch/no_backup/HisYFP/dataset-hdf5.xml'.
```

## View with BigDataViewer

Finally you can use [BigDataViewer](/plugins/bdv) to view your data set.

![](/media/plugins/mvr-resave3.png)
