---
mediawiki: Java_Tricks_and_Quirks
title: Java Tricks and Quirks
categories: [development]
---

## SoftReference and OutOfMemoryError

We have recently learned an interesting fact about Java's [SoftReference](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) and the potential occurence of an [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html). The result first: An [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html) may be thrown in a situation where [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) can be released after which enough memory would be available. The reason is that normal garbage collection happens in an independent thread and does not halt other threads when they allocate memory. Only an explicit [System.gc()](http://docs.oracle.com/javase/6/docs/api/java/lang/System.html#gc%28%29) waits until the memory is freed . The consequence is that whenever you allocate memory then you should do that with the following clause:

    final MyObject o;
    try {
      o = new MyObject();
    }
    catch (OutOfMemoryError e) {
      System.gc();
      o = new MyObject();
    }  

We found this by implementing a simple cache using a [HashMap](http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html) of [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) to an object that on finalize removes the corresponding key in the [HashMap](http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html). That cache is used to store image tiles for an [ImgLib2](/libs/imglib2) backend that uses a [CATMAID](http://fly.mpi-cbg.de/~saalfeld/catmaid/) stack ({% include github repo='imglib' tag='9f38afca3f0a4aa7b3ddc77160430a710a20501a' path='imglib2/tests/src/test/java/catmaid/CATMAIDRandomAccessibleInterval.java' label='GitHub' %}). It turned out that the painter thread in an interactive viewer was fetching new tiles quicker than the garbage collector would finalize [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) and stopped with an [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html). We could solve that with the the above construct.
