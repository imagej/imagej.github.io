This page explains a fairly simple way of generating code coverage statistics when testing Fiji using [http://emma.sourceforge.net/ EMMA], a Java code coverage tool which is [http://www.gnu.org/philosophy/free-sw.html free software].

To install EMMA, on Debian or Ubuntu you just do:
 apt-get install libemma-java
... which installs the relevant jar file to <tt>/usr/share/java/emma.jar</tt>

The example I'm using here is to instrument VIB_.jar, since that's where the plugin I'm working on is compiled into.

First, I remove any old coverage data:
 $ cd ~/fiji/
 $ rm -rf coverage coverage.ec coverage.em
Then, make sure Fiji is built and up-to-date:
 $ make
(Quit the instance of Fiji that starts up.)

Now edit VIB_.jar to add code coverage instrumentation:
 $ java -cp /usr/share/java/emma.jar emma instr -m overwrite -cp plugins/VIB_.jar
 EMMA: processing instrumentation path ...
 EMMA: instrumentation path processed in 10913 ms
 EMMA: [726 class(es) instrumented, 72 resource(s) copied]
 EMMA: metadata merged into [/home/mark/fiji/coverage.em] {in 2218 ms}
That should create a file called <tt>coverage.em</tt>.  Start up Fiji as normal, except adding <tt>emma.jar</tt> to the class path, and run your tests:
 $ ./fiji --class-path /usr/share/java/emma.jar
When you exit Fiji after running your tests, this will have created a coverage.ec file as well:
 EMMA: runtime coverage data merged into [/home/mark/fiji/coverage.ec] {in 52 ms}
Now generate an HTML report of the coverage data with:
 $ java -cp /usr/share/java/emma.jar emma report -r html -sp VIB -in coverage.em -in coverage.ec
 EMMA: processing input files ...
 EMMA: 2 file(s) read and merged in 583 ms
 EMMA: writing [html] report to [/home/mark/fiji/coverage/index.html] ...
(The <tt>-sp VIB</tt> parameter says to use the VIB subdirectory as a source path - without this you won't be able to see the source code highlighted according to coverage.)  That command generates the report in a subdirectory called <tt>coverage</tt>, so view the report with, for example:
 $ firefox coverage/index.html
You should see a summary like the following:
[[Image:Coverage-summary.png]]

... and can click through to line-by-line coverage of a source file, like the example below. (The green lines were executed, while the red ones were not.  Yellow lines were partially executed, e.g. if only one branch of the ternary operator (?:) was run, as explained in the [http://emma.sourceforge.net/faq.html#faq-N101CF EMMA FAQ].

[[Image:Coverage-file.png]]
