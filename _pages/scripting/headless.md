---
title: Scripting Headless
section: Extend:Scripting
project: /software/imagej2
---

[ImageJ2 scripts](/scripting) are designed to operate independently of user interface—including [headless](/learn/headless), with **no** user interface. This is made easy with the use of [script parameters](/scripting/parameters).

To start ImageJ2 headless mode, run (with the launcher appropriate for your system substituted):

```ssh
./ImageJ-linux64 --ij2 --headless
```

By default, when ImageJ2 runs headlessly it acts like a one-off program: it will only perform the requested operations, then quit. To run a script headlessly, use:

```ssh
./ImageJ-linux64 --ij2 --headless --run path/to/script [key1=value1,key2=value2,...]
```

{% include notice icon="warning" content='In many cases, it is necessary to enclose the entire list of key/value pairs in single quotes, to avoid shell expansion. See the following examples.' %}


## Basic run

Let's say we have the following Python script saved in a file, `hello.py`:

```ssh
#@String name
print('Hello ' + name)
```

we could run this script with the command on [Linux](/platforms/linux):

```ssh
./ImageJ-linux64 --ij2 --headless --console --run hello.py 'name="Mr Kraken"'
```

Note that the `name` parameter must be enclosed in double quotes, since it is a string literal.

The optional `--console` argument allows to have `print`, `IJ.log` and error statements returned to the console window.

On [Windows](/platforms/windows) systems, single/double quotes might be inverted though, such that strings are enclosed in single quotes while the list of argument as well as the path to the py script are in double quotes.

```ssh
ImageJ-win64.exe --ij2 --headless --console --run "PathTo/hello.py" "name='Mr Kraken'"
```

On [macOS](/platforms/macos) systems, the command can run in with the same quoting as on Linux:

```ssh
./ImageJ-macosx --ij2 --headless --console --run hello.py 'name="Mr Kracken"'
```

## Multiple parameters

If your script has more than one parameter:

```ssh
#@String name1
#@String name2
print('Hello ' + name1 + " and " + name2)
```

then these are filled by using a comma-separated list of parameter pairs—e.g.:

```ssh
./ImageJ-linux64 --ij2 --headless --console --run hello.py 'name1="Mr",name2="Mrs Kraken"'
```

Similarly for Windows (again respect single/double quotes) or macOS,

```ssh
ImageJ-win64.exe --ij2 --headless --console --run "PathTo/hello.py" "name1='Mr', name2='Kraken'"
./ImageJ-macosx --ij2 --headless --console --run hello.py 'name1="Mr",name2="Mrs Kraken"'
```

## Controlling the Updater

To prevent unnecessary server connections to update sites in headless mode you can set the `imagej.updater.disableAutocheck` java parameter `true`:

```ssh
./ImageJ-linux64 -Dimagej.updater.disableAutocheck=true -- --ij2 --headless --console --run hello.py 'name="Mr Kraken"'
```

Often headless mode is used to run many scripts in parallel that could result in huge numbers of server connections. Setting this parameter will prevent this issue. This parameter does not persist between launches and must be included every time server connections to update sites should be prevented.

If desired, the updater can be controlled in headless mode using the following commands to add an update site and update ImageJ.

```ssh
./ImageJ-linux64 --update add-update-site BAR https://sites.imagej.net/Tiago/
./ImageJ-linux64 --ij2 --headless --update update
```

You can also add multiple update sites in a single command line:

```ssh
./ImageJ-win64.exe --update add-update-sites "BAR" "https://sites.imagej.net/Tiago/" "IJPB-plugins" "https://sites.imagej.net/IJPB-plugins/"
```

Go to the updater section to get the [complete list of available commands](/plugins/updater).
