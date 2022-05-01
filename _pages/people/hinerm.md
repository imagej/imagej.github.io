---
title: Mark Hiner
name: Mark Hiner
honorific: Champion of ImageJ
gravatar: 02dba515add5d5c4991f6b93520d502c
affiliation:
- Eliceiri Lab / LOCI | /orgs/loci
- University of Wisconsin-Madison | https://wisc.edu/
forum: hinerm
github: hinerm
stackoverflow: 1027800/hinerm
openhub: hinerm
linkedin: pub/mark-hiner/63/984/8b2
orcid: 0000-0001-9404-7579
---

Mark was a member of the core [ImageJ2](/software/imagej2) development team at [LOCI](/orgs/loci) from 2011-2016, earning the title of Champion of ImageJ for his tireless enthusiasm and dedication to the community. He is co-founder of the [SCIFIO](/libs/scifio) project, a robust and extensible library for reading and writing scientific image file formats, and accessible foundation for image format processing. He also developed the [ImageJ-MATLAB](/scripting/matlab) project for [ImageJ2](/software/imagej2)/[MATLAB](/scripting/matlab) interoperability. Mark rejoined the ImageJ2 team in 2020.

## My work at LOCI

After working at [LOCI](/orgs/loci) for two years as a Research Assistant, Mark completed a M.S. degree in computer science and decided to stay on as a Research Intern. Until 2016 he worked as the lead developer on [SCIFIO](/libs/scifio). His primary areas of interest within CS are artificial intelligence, robotics and programming languages.

You can follow his latest work [on GitHub](https://github.com/hinerm).

Earlier work at LOCI includes:

-   Implemented write functionality in BFITK plugins
-   Modified {% include github org='uw-loci' repo='jar2lib' label='Jar2Lib' %} to automatically collect its output C++ libraries into a single location, and compress that directory for easy automation.
-   Added a generic utility library to the Jar2Lib project, which includes methods for consistent JVM invocation.
-   Modified {% include github org='uw-loci' repo='cppwrap-maven-plugin' label='cpp-wrap' %} to account for the changes in Jar2Lib's structure
-   Created a Java Native Interface ([JNI](http://java.sun.com/developer/onlineTraining/Programming/JDCBook/jni.html)) implementation of [BFITK](http://www.loci.wisc.edu/bio-formats/itk).
-   Established benchmarking process to compare three BFITK implementations
-   Reworked the build system for the BFITK plugins - removing [Ant](http://ant.apache.org/) dependency in favor of [CMake](http://www.cmake.org/) post-build commands
-   Modified Jar2Lib to accept user-defined files to append to the automatically generated `CMakeLists.txt` build files, allowing for custom options to be defined.
-   Used user-defined appending of make files to remove Ant dependency for building BF-CPP (stand-alone C++ library of Bio-Formats) by creating a Jar2Lib script
-   Cross-platform testing of BFITK with [FARSIGHT](http://www.farsight-toolkit.org/) toolkit.
-   Creation of comprehensive developer and user [guides](http://www.farsight-toolkit.org/wiki/FARSIGHT_Tutorials/Building_Software/Bio-Formats) for using Bio-Formats with the FARSIGHT toolkit.
-   Contributed to the FARSIGHT toolkit functionality (general usability improvements, such as hotkeys, window focus and a pixel probe).
