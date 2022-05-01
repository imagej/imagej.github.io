---
mediawiki: Javassist
title: Javassist
---

[Javassist](http://www.javassist.org) is a Java library to generate, modify and inspect bytecode (i.e. the machine language of Java).

# Quick example

Let's assume that you want to know which call paths lead to a given method (e.g. `foo()`) in a given class (e.g. `org.soft.micro.Narf`).

```java
// get the class pool
ClassPool pool = ClassPool.getDefault();
// access the class without loading it just yet
CtClass clazz = pool.get("org.soft.micro.Narf");
// get the method; you can find the signature (2nd parameter) like this:
// fiji --javap -s org.soft.micro.Narf | grep -A1 foo
CtMethod method = clazz.getMethod("foo", "()V");
// now let's output a whole lot of stuff whenever this method is entered
method.insertBefore("new Exception(\"Here I am!\").printStackTrace();");
```

Of course, you are not limited to outputting a stack trace. You could also generate Strings of those traces and put them into a Map, possibly counting the occurrences.

Other useful actions include inspecting the parameters passed to the method which you can access by the special names `$1`, `$2`, ...

Further reading: Javassist's [online tutorial](http://www.csg.is.titech.ac.jp/~chiba/javassist/tutorial/tutorial.html).

# Code editing

While Javassist allows to edit bytecode directly, its most powerful feature is that it allows you to modify methods using snippets of Java code. There are two slightly different methods to do so: the [CodeConverter](http://www.csg.ci.i.u-tokyo.ac.jp/~chiba/javassist/html/index.html) and the [ExprEditor](http://www.csg.ci.i.u-tokyo.ac.jp/~chiba/javassist/html/javassist/expr/ExprEditor.html) (it depends which one to use, *CodeConverter* is easier to use but *ExprEditor* is more powerful.

## Wrapping existing code blocks

A common reason for Javassist'ing code is to handle previously unhandled exceptions, or to make certain parts of the code conditional. As an example, we demonstrate here how, say, a hypothetical *OpenAccess*' `toString()` method could be protected against a `NullPointerException`:

```java
// get the class pool
ClassPool pool = ClassPool.getDefault();
// access the class without loading it just yet
CtClass clazz = pool.get("OpenAccess");
CtMethod method = clazz.getMethod("toString", "()Ljava/lang/String;");
// now let's handle NullPointerExceptions
method.setBody("try {"
  + "  $_ = $proceed($$);"
  + "} catch (java.lang.NullPointerException e) {"
  + "  return \"(null)\";"
  + "}");
```

Note that the special `$_ = $proceed($$)` is a Javassist-specific syntax referring to the original code. See [the Javassist tutorial](http://www.csg.ci.i.u-tokyo.ac.jp/~chiba/javassist/tutorial/tutorial2.html#before) for details.

# Debugging

Javassist has very useful tools for disassembly and introspection. For example, you could inspect the contents of a class using some code like this:

```java
// get the class pool
ClassPool pool = ClassPool.getDefault();
// access the class without loading it just yet
CtClass clazz = pool.get("org.soft.micro.Narf");
// output the contents
ClassFilePrinter.print(clazz.getClassFile());
```

Or you could disassemble a method like this:

```java
// get the class pool
ClassPool pool = ClassPool.getDefault();
// access the class without loading it just yet
CtClass clazz = pool.get("org.soft.micro.Narf");
// get the method
CtMethod method = clazz.getMethod("foo", "()V");
// disassemble the method
InstructionPrinter.print(method, System.err);
```

If you absolutely do not want the output to go to `System.err`, you could substitute it by `new PrintStream(new IJLogOutputStream())` (the class `IJLogOutputStream` is defined in [Fiji Updater](/plugins/updater)'s `fiji.updater.util` class for you to reuse).

# VerifyError

For security reasons, HotSpot does not allow any malformed bytecode to execute. To verify that the bytecode is reasonably sane, the code is *verified* before being executed.

Unfortunately, the error messages of said verifier are not exactly stellar.

If you want to avoid being misled by the error message (the method mentioned in the `VerifyError` is most likely to be <u>not</u> the offending one), and moreover want to know where in the bytecode the error happened, probably the easiest way to go forward is to use [BCEL](http://commons.apache.org/bcel/) (you can get it directly from the [Maven repository](https://maven.scijava.org/index.html#nexus-search;gav%7E%7Ebcel%7E%7E%7E)), Apache's *Byte Code Engineering Library*. For that, you have to write out `.class` files first:

```java
CtClass clazz = ...;
...;

File directory = ...;
File file = new File(directory, clazz.getName().replace('.', '/') + ".class");
file.getParentFile().makeDirectories();
DataOutputStream out = new DataOutputStream(new FileOutputStream(file));
clazz.getClassFile().write(out);
out.close();
```

Then you can use the verifier:

```java
fiji --classpath=/path/to/bcel.jar:directory/ \
            --main-class=org.apache.bcel.verifier.Verifier \
            my.class.Name

```
(Side note: Apache calls the verifier *JustIce*, but the name is not reflected in the program name, only in its output.)

More on this issue can be found [here](http://elliotth.blogspot.com/2008/03/generating-jvm-bytecode.html).

Side note: the ASM component (which is included in JRuby, which in turn is included in Fiji) also has a verifier. You can start it with some command-line invocation similar to this:

```shell
fiji --classpath /path/to/classes \
            --main-class jruby.objectweb.asm.util.CheckClassAdapter \
            my.class.Name
```
If you are using Fiji's {% include github org='fiji' repo='fiji-compat' branch='master' source='fiji/JavassistHelper.java' label='JavassistHelper class' %}, you can use the *verify()* method which does nothing else than to hand off to the ASM component's verifier. Example:
```java
import fiji.JavassistHelper;
import javassist.ClassPool;

...

  ClassPool.getDefault().addClassPath("/path/to/my.jar");
  JavassistHelper helper = new JavassistHelper();
  // hack away
  helper.verify(hacker.get("the.class.in.question"), System.err);
...
```
