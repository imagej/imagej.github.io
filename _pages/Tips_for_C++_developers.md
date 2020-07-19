{{DevelopMenu | tutorials}}
{{TOC}}
= Introduction =

Many developers are more familiar with C++ than Java when starting to develop code for Fiji. There are a few common pitfalls when coding in Java, being used to C++, and this page tries to help you avoid them.

= General differences =

== Compile time ==

In C++, all the optimization takes place at compile time. Especially with C++ templates, that can take a long time and it is even possible to have inifinite loops. As C++ targets assembler code, it makes no sense to try to post-optimize the code after that.

In Java, the compiler only produces bytecode that will be interpreted and/or Just-In-Time compiled by the Java Runtime. When some piece of bytecode is run multiple times, the Just-In-Time compiler will actually try to optimize harder, so compile time with Java is not really only limited to compiling the .java files into .class files.

== Templates vs Generics ==

Java's generics are implemented using erasure, which means that generics help catching bugs due to compile-time checks, but the compiled classes will actually have forgotten about the generic parameters. In particular, you cannot use the generic parameter to instantiate classes, i.e. this does not work:

 public<T> T create() { return new T(); } // does _not_ work

The upside of this limitation is that you will never get as cryptic multi-page long error messages as with C++.

A downside is that the Java compiler just cannot optimize generics as much as C++ can do with templates, also due to the fact that Java does not recompile the base classes of the generics -- in contrast to what C++ does with templates. However, due to the [[#Compile_time|compile time]] being fuzzy, Java can optimize a lot in the Just-In-Time compiler, especially when you use the ''final'' keyword wisely; a method marked as final cannot be overridden in subclasses, and is therefore a prime candidate for Just-In-Time optimization.

== Java has no pointers ==

In C++, you often find constructs like this:

 const char *string = "Hello, World!";
 some_func(string + 7);

This is not possible in Java. Instead, you have to use String's substring() method.

In the same spirit, it is not possible to realloc() memory. If you need a larger buffer, you have to allocate it, possibly copying existing data into it using the method ''System.arraycopy()''.

== There is no need for ''this->'' ==

In Java, member variables and methods can be accessed without the prefix ''this.'', so it is considered better to skip that unnecessary prefix. But it also means that your code has to make clear what variables are local in another manner.

= Pitfalls =

== Java only knows ''by-reference'' ==

Whenever you pass an object to a method, Java does so by reference. That makes it harder to write inefficient code copying large amounts of memory back and forth, but it is something to watch out for when you are used to C++: when passing an object to a method which modifies the members, the caller will see the changes.

== You <u>cannot</u> compare Strings using <nowiki>==</nowiki> ==

There is no operator overloading in Java, so the operator ''<nowiki>==</nowiki>'' refers to equality of the reference, rather than equality of the referenced object. You must use the ''equals()'' method for that.

== Objects are not instantiated by default ==

When declaring a variable like this:

 ImagePlus image;

Java does not initialize the variable automatically. Remember, objects are passed by reference, so ''image'' is just an uninitialized reference to an ''ImagePlus'' at this stage.

== Java knows of no destructors ==

While it is convenient that Java does automatic garbage collection, it is easy to forget that every reference to an object will prevent it from being released. Even worse, sometimes the garbage collection does not kick in in time, so you have to call ''System.gc();'' explicitely, possibly multiple times.

== Java is inherently multithreaded ==

When coming from C++, one often tries to avoid multi-threading, as it is painful to use threads in C++ in a portable manner.

In Java, threads are really easy. And portable. But that does not mean that coding multi-threaded programs is easy. Humans are just too used to a linear time-course to think of all the possible side-effects of multi-threaded code, or of the need to make code blocks ''synchronized'' (i.e. ensure that certain code blocks are not executed simultaneously in multiple threads).

However, the most notorious bugs are the ones in multi-threaded code, as they are really, really difficult to debug. It is not uncommon that a multi-threading bug goes away when debug messages are introduced into the code.

Of course, the advantage of multi-threaded programs is that multi-core systems will benefit immediately from that code.

== Not taking advantage of Java's syntax ==

Many C++ programmers think of Java as a C++ dialect, forgetting that there are convenient syntax constructs. For example, you will often find code such as

 for (int i = 0; i < array.length; i++) {
         String string = array[i];
         // do something
 }

or even worse:

 Iterator<String> iter = list.iterator();
 while (iter.hasNext()) {
        String string = iter.next();
        // do something
 }

rather than using the Java syntax (available since Java 1.5):

 for (String string : array)
         // do something

== Not taking advantage of Java's standard libraries ==

Coming from C++, developers often tend to implement everything themselves, even if the algorithm was already implemented. For example, ''java.util.Collections'' and ''java.util.Arrays'' contain methods to sort, shuffle, filter or binary search collections and arrays respectively.

Likewise, Java comes with useful classes implementing neat things such as priority queues (since Java 1.5).


== 'final' does not mean 'const' ==

In C++, when an array is declared <i>const</i>, none of its entries can be edited in any way. But in java, when a variable that points to an array is declared <i>final</i> only that variable cannot be assigned. Any entries of the array (or collection, or whatever container) are editable, and the entry slots themselves may be reassigned.

= Conventions =

== Class and function names ==

In C++, the common style is to use underscores for both class and function names, e.g. ''gaussian_blur'' (except if you are developing on Windows, where the class names are frequently prefixed by a capital ''C'' and CamelCased).

In Java, the convention is to use CamelCase instead of underscores, and to start class names with a capital letter, but fields and method names lowercase, e.g. ''ImagePlus'' and ''newImage()''.
