---
mediawiki: Command_Line_Tips_and_Tricks
title: Command Line Diagnostics
categories: [tutorials]
---

This page lists hints on how to use the command line for developer diagnostics in the different environments supported by Fiji.

| Action                         | Linux                                   | macOS                     | Windows                                                                                            |
|--------------------------------|-----------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------|
| List dependencies of libraries | `ldd `<library-file>                    | `otool -L `<library-file> | `objdump -p `<library-file>` | grep "DLL Name:"`                                                   |
| Trace system calls             | `strace -Ffo syscall.log ./fiji `<args> | `dtruss ./fiji `<args>    | Use [Sysinternal's Process Monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx) |
