{{DevelopMenu | tutorials}}{{TOC}}{{Outdated}}

= Introduction =

Sometimes, you may want to use 3rd party libraries that are not available as Java components, but only as native libraries.

There are two options available to make use of native libraries: [http://jna.java.net/ JNA] and JNI (see below for detailed descriptions).

== Disadvantages of using native libraries ==

Even if JNA and JNI provide some convenience for using native libraries, there are substantial downsides of using native libraries:

* Using native libraries flies in the face of the platform independence of Java
: Even if ImageJ only supports 32-bit/64-bit Windows, MacOSX and Linux (and PowerPC with MacOSX for the time being), it is a major hassle to maintain them. It also means that you incur the problems with C/C++ where a library compiling successfully on one platform does not at all imply that it compiles on any other platform. There are even examples of C code compiling fine for 32-bit but not for 64-bit CPUs on the very same Operating system.

* No "Compile once, run everywhere"
: It is one of Java's greatest strengths that you do not need to compile for every platform you plan (or anyone else plans) to run on. Native libraries take away that advantage.

* By using native libraries, it is much easier to produce fatal errors that tear down the complete Java virtual machine. Consequently, debugging can be really hard when using native libraries.

For further arguments to use Java instead of native libraries, see also our [[Why Java|rationale for using Java]].

== JNA vs JNI ==

The benefits of JNA over JNI are:

* scriptable
* you do not need a C compiler
* a native library can be dropped in for an additional platform without any recompilation

The benefits of JNI over JNA are:

* official part of Java
* way faster
* JNI is "type-safer" (i.e. Java and native code access data via the same type definitions)

= JNA =

The [http://jna.java.net/ JNA project] (''Java Native Access'') tries to provide an easy, pure-Java way to access native libraries using their native interface.

== Functions ==

To this end, the developer has to define an interface describing in Java terms what functions the library provides. Example:

<source lang="java">
import com.sun.jna.Library;

public interface C extends Library {
        public int symlink(String oldpath, String newpath);
}
</source>

Note:
* Even if the package name is ''com.sun.jna'', JNA is not an official part of Java. As a consequence, JNA supports less platforms than official Java itself.
* You do not need to declare all the functions offered by the native library. In this example, only ''symlink'' was declared.
* The Java type ''String'' is mapped to ''const char *'' in the C layer. The same happens for other primitive Java types.
* Since the parameters need to be mapped prior to calling the native function, and mapped back after it returns, and all this mapping is done using reflection, JNA is relatively slow compared to JNI (except when the amount of time spent copying data is outweighed by the processing time spent within the native library).
* There is no guarantee by the compiler that the interface is correct. In fact, you can declare the functions incorrectly very easily, which results in hard crashes of the Java virtual machine.
* Note: to define this interface in [[Beanshell Scripting|Beanshell]], you need to use the syntax <code>interface C implements Library</code> instead of employing the keyword <code>extends</code>.

Use the library in this way:

<source lang="java">
import com.sun.jna.Native;

C c = (C)Native.loadLibrary("c", C.class);
int result = c.symlink(source, target);
</source>

=== Specifying library search paths ===

If you want to use a library that is not installed in one of the locations your platform looks for libraries by default, you may need to tell JNA where to find the library:

<source lang="java">
NativeLibrary.addSearchPath("opencv", "C:\\opencv");
OpenCV openCV = (OpenCV)NativeLibrary.loadLibrary("opencv", OpenCV.class);
</source>

Note: some libraries depend on other libraries. If the dependencies are not in the default library path, it might be not possible to load them from within Java without restarting the virtual machine, depending on the platform. On Linux, e.g. you would need to set the environment variable ''LD_LIBRARY_PATH'' accordingly (setting them in the Java process does not help, as the dynamic loader was already initialized and does not respect a change in that variable after initialization).

=== Constants/enums ===

If the C header defines constants using the ''#define'' statement, the constant is nowhere to be found in the compiled native library. Likewise, the C compiler optimizes out the names of enums. Therefore, both constants and enums need to be defined in the interface.

For example, this C header:

<source lang="cpp">
#ifndef MY_HEADER_H
#define MY_HEADER_H

#define OFF 0
#define ON 0xff

enum counter_t {
        ZERO,
        ONE,
        TWO,
        THREE
};

extern counter_t get_counter(void);
#endif
</source>

would need to be handled with a JNA-based interface like this one:

<source lang="java">
public interface MyLibrary extends Library {
        public final int OFF = 0;
        public final int ON = 0xff;
        public final int ZERO = 0;
        public final int ONE = 1;
        public final int TWO = 2;
        public final int THREE = 3;

        public int get_counter();
}
</source>

=== Structures ===

Some functions do not take simple data types as parameters, but so-called ''structs''. These have to be defined as inner static classes of the interface, and they need to extend the class ''com.sun.jna.Structure'':

<source lang="java">
import com.sun.jna.Library;
import com.sun.jna.Structure;

public interface C extends Library {
        public static class timeval implements Structure {
                long tv_sec, tv_usec;
        }
        public static class timezeone implements Structure {
                int tz_minuteswest, tz_dsttime;
        }
        public int gettimeofday(timeval timeval, timezone timezone);
}
</source>

Some fields of the structures might be fixed-size arrays (e.g. ''unsigned char path[1024]''). These fields should be declared with default initializers in Java (e.g. ''byte[] path = new byte[1024];'').

==== Accessing structures via pointers ====

A function you call may return a pointer to a structure. To initialize the fields of a Java version of such a structure, you can use the ''useMemory(Pointer)'' and ''read()'' methods:

<source lang="java">
...
        public static class MyStruct {
                public MyStruct(Pointer p) {
                        // cannot use super(p) because of fixed-size array fields
                        super();
                        useMemory(p); // set pointer
                        read(); // initialize fields
                }

                public MyStruct() {
                        super();
                        // handle fixed-size array fields correctly
                        ensureAllocated();
                }
        }
...
</source>

Note: when the superclass' constructor is called, the fixed-size array fields are not yet initialized. Therefore, the superclass' constructor has no way to handle them correctly: their size is not known. That is the reason why you have to call ''ensureAllocated()'' and why you cannot use the superclass' ''super(Pointer)'' constructor. Technically, when your struct does not contain fixed-size array fields, you can, but getting used to always avoid the ''super(Pointer)'' constructor will help you stay out of trouble.

=== Passing structures by value ===

When passing instances of a Structure to a function, memory is allocated and written to automatically, and a pointer is passed.

If you want to pass a Structure by value instead, you have to subclass it and implement the ''Structure.ByValue'' interface. This interface is purely a tag, and does not require any additional functions to be defined.

Example:

<source lang="java">
public class Timespec extends Structure {
	long tv_sec;
	long tv_usec;
}

public class Stat extends Structure {
	long /* dev_t */      st_dev;     /* ID of device containing file */
	long /* ino_t */      st_ino;     /* inode number */
	long /* nlink_t */    st_nlink;   /* number of hard links */
	int /* mode_t */      st_mode;    /* protection */
	int /* uid_t */       st_uid;     /* user ID of owner */
	int /* gid_t */       st_gid;     /* group ID of owner */
	int __pad0;
	long /* dev_t */      st_rdev;    /* device ID (if special file) */
	long /* off_t */      st_size;    /* total size, in bytes */
	long /* blksize_t */  st_blksize; /* blocksize for file system I/O */
	int /* blkcnt_t */    st_blocks;  /* number of 512B blocks allocated */
	Timespec /* time_t */ st_atime;   /* time of last access */
	Timespec /* time_t */ st_mtime;   /* time of last modification */
	Timespec /* time_t */ st_ctime;   /* time of last status change */
}

public class StatByValue extends Stat implements Structure.ByValue {
	public StatByValue(Stat stat) {
		super();
		ensureAllocated();
		byte[] buffer = new byte[size()];
		stat.getPointer().read(0, buffer, 0, buffer.length);
		getPointer().write(0, buffer, 0, buffer.length);
		read();
	}
}
</source>

== Scripting JNA ==

In [[Beanshell Scripting|Beanshell]], it is not possible to extend interfaces, so it is not possible to imitate the plain Java way to use JNA. Other scripting languages have similar problems as far as JNA is concerned.

But you can use the ''getFunction(String)'' method of ''NativeLibrary'' to get a function object, whose methods ''invokeInt(Object[])'', ''invokePointer(Object[])'' and friends will allow you to call the function.

If the result is not a basic type, you can use ''Pointer'''s methods to access the data. Beanshell example:

<source lang="java">
import com.sun.jna.NativeLibrary;

// get the C runtime library
c = NativeLibrary.getInstance("c");

// retrieve the getenv() function and call it
getenv = c.getFunction("getenv");
print(getenv.invokePointer(new Object[] { "HELLO" }).getString(0));

// retrieve and use the setenv() function
setenv = c.getFunction("setenv");
print(setenv.invokeInt(new Object[] { "HELLO", "world", new Integer(1) }));

// show that it did something
print(getenv.invokePointer(new Object[] { "HELLO" }).getString(0));

// note that System.getenv() remains oblivious
print(System.getenv("HELLO"));
</source>

There can be substantial complications: some function names do not actually refer to functions in the native library, but are redirected to another function by the preprocessor. Example: at least on Linux, ''lstat()'' actually calls ''__lxstat()'' with additional parameters.

Also, the classes defined in your scripting language of choice might not be applicable for use with JNA. Beanshell, for one, adds two fields that JNA cannot (and should not) handle. As a workaround, you can use ''Pointer'''s ''get'' family of methods.

Example:

<source lang="java">
import com.sun.jna.Memory;
import com.sun.jna.NativeLibrary;

import java.util.Date;

c = NativeLibrary.getInstance("c");
lstat = c.getFunction("__lxstat");
errno = c.getFunction("errno");

path = System.getProperty("imagej.dir");
print(path);
stat = new Memory(144);
result = lstat.invokeInt(new Object[] { new Integer(0), path, stat });

print("result: " + result);
if (result < 0) {
	strerror = c.getFunction("strerror");
	err = errno.getInt(0);
	error = strerror.invokePointer(new Object[] { new Integer(err) }).getString(0);
	print("errno: " + error + " (" + err + ")");
}
print("blocks: " + stat.getInt(64));
print("atime: " + new Date(stat.getLong(72) * 1000));
print("mtime: " + new Date(stat.getLong(88) * 1000));
print("ctime: " + new Date(stat.getLong(104) * 1000));
</source>

= JNI =

The abbreviation ''JNI'' stands for ''Java Native Interface''. It is the original and best supported way to access native libraries from within Java. As such, it is robust but also a bit cumbersome to use.

== First steps ==

Before implementing any native (C or C++) code, you need to declare a native function. Example:

<source lang="java">
public class Hello_World_JNI {
        public native void helloWorld();
}
</source>

This tells the JVM that the method ''helloWorld()'' is implemented in a native library (which has to be loaded separately).

The next step is to generate a C header with the declaration of the C function implementing that method:

<source lang="bash">
javac Hello_World_JNI.java
javah -classpath . Hello_World_JNI
</source>

Note that the executable ''javah'' works on ''.class'' files only, hence we have to compile the ''.java'' source file first. The output is a ''.h'' file.

After this, the code doing the actual work needs to be implemented in a separate ''.c'' file. This should include the header file generated by ''javah'' and be compiled to a shared library: ''.dll'' on Windows, ''.dylib'' on MacOSX (Apple's Java also used the extension ''.jnilib''), and ''.so'' everywhere else.

Before the native method can be called, the JVM needs to load the native library. There are basically two different methods to do that, ''System.loadLibrary()'' and ''System.load()''. The former looks for the library in the system-wide library search path while the latter expects an absolute path to the dynamic link library file. For the purposes of ImageJ, the latter is usually preferred because we want to avoid requiring administrator privileges of our users.

== Support in ImageJ ==

Native libraries located in:

   '''<ImageJ-directory>/lib/<platform>/'''

will automatically be added to the '''<code>java.library.path</code>''', exposing them in Java land - where they still need to be loaded. One option for loading is to create a <code>Service</code> that loads the native library in its <code>initialize()</code> method. For example, see the [https://github.com/imagej/imagej-itk/blob/imagej-itk-0.1.0/src/main/java/net/imagej/itk/DefaultImageJItkService.java#L84-L91 ITK compatibility layer].

The Fiji build system also supports native targets by compiling source files whose names end in ''.c'' using gcc. If C sources are found, javah will be called and a native library will be compiled using GCC and the resulting shared library will be put into the ''<fiji-directory>/lib/<platform>/'' directory.

Finally, the ''fiji.JNI'' class in ''fiji-lib.jar'' provides convenience methods to load native libraries. Example:

<source lang="java">
static {
        JNI.loadLibrary("hello-world");
}
</source>

See also the [[#JNI Example|JNI Example]] below.

== Using the Java Native Interface from C ==

There are a couple of things one needs to keep in mind when accessing Java classes, instances and methods from C.

The most important is: Java has its own memory management. In contrast to C, it moves things around when needed. In C, once you have obtained an address to some data, it is the programmer's duty to make sure that the memory range is valid until no variables hold any references (addresses) to that range any longer. To access data stored in the Java Virtual Machine's memory range (the ''heap''), one has to ''pin'' those data to a certain memory location and tell the JVM when it is free to move the data again.

Such pinning issues are the nastiest things when working with JNI since it is all too easy to come up with sloppy code that just works by chance during the testing phase.

Every call from Java to a native function passes as first parameter a reference to the JNI environment. This is an opaque pointer to internal state variables that are required for literally every interaction with Java. Example:

<source lang="cpp">
JNIEXPORT void JNICALL Java_Hello_1World_helloWorld
    (JNIEnv *env, jclass object, jstring message);
</source>

Typically, you will work a lot with primitive types that are available under the names ''jbyte, jshort, jint, jlong,'' etc. These are usually identical with the native C types ''char, short, int, long'' (but not always; the devil is in the cross-platform details, as always).

One notable exception is ''jchar'' which is _not_ identical to ''char''. The authors of Unix decided in their infinite wisdom that you will only ever need 7 bits, or at most 8 bits, to encode text. The authors of Java knew that this is wrong and therefore ''jchar'' refers to 16-bit Unicode characters. In C, you will typically work with UTF-8 (for convenience and to save memory), so make sure you use the ''*UTF*'' functions of the JNI API (e.g. ''NewStringUTF()'' instead of ''NewString()'').

=== Calling the JNI API ===

There are many functions in the JNI API, and almost all of them are stored as function pointers in the JNIEnv instance. Since many of them need to access the environment to interact with state variables hidden from the user, most calls look like this, passing the environment as first parameter back to the function:

<source lang="cpp">
(*env)->NameOfTheFunction(env, ...);
</source>

=== Calling methods and accessing fields ===

If you need to call a Java method from C, you first need a reference to the class. Note: the class name must be passed in UTF-8 and in the ''slashed'' format rather than the dotted one. Example:

<source lang="cpp">
jclass image_plus_class = (*env)->FindClass(env, "ij/ImagePlus");
</source>

Primitive types do not have corresponding ''jclass'' instances, there are individual accessors for every primitive type where applicable.

Should you need to access arrays, prefix the class name with an opening square bracket, e.g. "[ij/process/ImageProcessor";

Arrays of primitive types are special: the "class names" are upper-case letters such as "B" for ''byte'', "I" for ''int'' and (funnily enough) "Z" for ''boolean''. The corresponding array's class name is then "[B", "[I" and "[Z".

The easiest way to determine the class name is to instantiate the class in Java and call ''instance.getClass().getName()'' on the instance.

To call a method you need to obtain the method id first:

<source lang="cpp">
jmethodID get_title_method = (*env)->GetMethodID(env,
    image_plus_class, "getTitle", "Ljava/lang/String;()");
</source>

The fourth parameter is the ''signature'' specifying the input parameters' and the return value's types. The easiest way to find out what the exact signature is, is to call ''javap'' on the class, passing the ''-s'' option to show the signatures in addition to the human-digestable information.

Once you have the method id, you can call the method, passing an instance of the corresponding class:

<source lang="cpp">
(*env)->CallVoidMethod(env, instance, image, get_title_method);
</source>

The ''Call<return-type>Method()'' family of functions take a variable number of arguments. Be very careful to pass the correct number and types of parameters!

=== Some tips ===

* Never assume that the reference to a method, or even the JNIEnv parameter are constant between calls to native functions. A very likely source for segmentation faults/access violations that take the complete JVM down.

* Always make sure that you release the memory accessed via JNI as soon as possible. This avoids not only memory leaks but also performance issues due to preventing the JVM's memory management to do its thing.

* For performance, you should minimize the use of ''FindClass()'' and ''GetMethodID()'': while Java 7 promises better performance for these functions, still a lot of people work with Java 5 or Java 6 where such calls are slow.

* Pay attention to the compiler's warnings. They are not there just for fun.

== JNI Example ==

There is an example in Fiji's source code: {{GitHub|org=imagej|repo=minimal-ij1-plugin|tag=native|path=src/main/c/JNI_Example.c}}.

To compile it, simply run

<source lang="bash">
sh Build.sh plugins/JNI_Example.jar
</source>

That will result in the two files ''plugins/JNI_Example.jar'' and ''lib/<platform>/JNI_Example.<extension>'' and a new menu item {{bc | Plugins | JNI | JNI Example}}.

It does not do terribly useful things as its primary purpose is to show how things are done in a straight-forward manner.

== Caveats ==

The most important issue is that you should know which platforms (combination of Operating System and architecture, i.e. ''i386 Windows'' and ''x86_64 Windows'' are different) you need to support and make sure that the native libraries are present. Otherwise your users will see a lot of unhelpful ''UnsatisfiedLinkError'' exceptions.

Usually, you should not need to worry about these issues, as Fiji hides them conveniently from you (this is one of Fiji's mission, to hide unnecessarily and annoyingly tedious details).

* The C source needs to be compiled with the ''_JNI_IMPLEMENATION_'' symbol defined. This is due to Windows which requires ''.dll'' files to mark explicitly which symbols are to be offered by the library and which ones need to be imported from another library.

* On Windows, symbols are auto-versioned by default. This interfers with constant names required by JNI. Therefore, you need to compile C sources with the GCC linker option ''-kill-at''. If you ask GCC to link for you, you need to pass that option as ''-Wl,-kill-at''.

* The java property ''java.library.path'' needs to be set to the path where the ''.so'', ''.dylib/.jnilib'' or ''.dll'' files can be found (for Linux/BSD/Haiku/etc, MacOSX and Windows, respectively).

* Additionally to the ''java.library.path'' property, the environment variable ''LD_LIBRARY_PATH'', ''DYLD_LIBRARY_PATH'' or ''PATH'' should be adjusted accordingly on Linux/BSD/Haiku/etc, MacOSX and Windows, respectively.

* If you need to load not only one library, but that library needs to load yet another library, you should set the search path so that the dynamic linker looks in the same directory as the original library, to avoid having to adjust the system-wide search path (which requires administrator privileges). The GCC linker option is called ''-R$ORIGIN/'' (note that you must prevent the command-line from expanding the ''$'' character).

== Further reading ==

For full information on JNI, see [http://java.sun.com/docs/books/jni/html/jniTOC.html Sun's/Oracle's programmer guide on JNI].

[[Category:Development]]
