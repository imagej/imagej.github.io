==SoftReference and OutOfMemoryError==

We have recently learned an interesting fact about Java's [http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html SoftReference] and the potential occurence of an [http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html OutOfMemoryError].  The result first: An [http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html OutOfMemoryError] may be thrown in a situation where [http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html SoftReferences] can be released after which enough memory would be available.  The reason is that normal garbage collection happens in an independent thread and does not halt other threads when they allocate memory.  Only an explicit [http://docs.oracle.com/javase/6/docs/api/java/lang/System.html#gc%28%29 System.gc()] waits until the memory is freed .  The consequence is that whenever you allocate memory then you should do that with the following clause:

<source lang="java">
final MyObject o;
try {
  o = new MyObject();
}
catch (OutOfMemoryError e) {
  System.gc();
  o = new MyObject();
}  
</source>

We found this by implementing a simple cache using a [http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html HashMap] of [http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html SoftReferences] to an object that on finalize removes the corresponding key in the [http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html HashMap].  That cache is used to store image tiles for an [[ImgLib2]] backend that uses a [http://fly.mpi-cbg.de/~saalfeld/catmaid/ CATMAID] stack ({{GitHub|repo=imglib|tag=9f38afca3f0a4aa7b3ddc77160430a710a20501a|path=imglib2/tests/src/test/java/catmaid/CATMAIDRandomAccessibleInterval.java|label=GitHub}}).  It turned out that the painter thread in an interactive viewer was fetching new tiles quicker than the garbage collector would finalize [http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html SoftReferences] and stopped with an [http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html OutOfMemoryError].  We could solve that with the the above construct.
