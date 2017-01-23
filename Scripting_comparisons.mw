__FORCETOC__ {{Learn | scripting}}
<big>'''Example: a command launcher'''</big>

A short plugin is used as example: a little dialog window that lets you type in a command for ImageJ to execute. A command is a menu item, which executes a plugin.

As the name of the command is typed, the color of the text changes from red to black if the command exists.

The plugin consists of four parts:

#Obtaining the list of all commands, from <code>ij.Menus</code> class.
#Setting up a dialog with a text box.
#Adding a text listener to the text box, that changes the color of the font in completing the typing of a word that matches a command.
#Executing the command when clicking the 'ok' button or pushing the return key.


The command launcher as written in java is by far the longest in lines of code, and worse, the most verbose.

While in Clojure one is able to declare types if desired, it's not required; the low computational requirements of the plugin do not invite to make it verbose unnecessarily. But java demands type declarations just so that the plugin can be compiled and thus a binary .class file generated.

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using ''let'' statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not ''required'' as in java, neither as natural and straightforward as in Clojure.

As an advantage, each jython script executes within its own namespace and instance of the interpreter, whereas clojure scripts run all within a unique static interpreter and thus share the namespace.

The javascript version (at least, the naive code pasted below) is very much java-like. Each script runs on its separate thread and namespace, like jython scripts.

To remark here that [http://clojure.org Clojure] is '''not''' a scripting language: Clojure compiles directly the JVM byte code, and thus runs at native speed.


==In Java==
See also the [[Introduction into Developing Plugins]] documentation page.

<source lang="java">
import ij.IJ;
import ij.plugin.PlugIn;
import ij.gui.GenericDialog;
import java.util.Hashtable;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Iterator;
import java.awt.TextField;
import java.awt.event.TextListener;
import java.awt.event.TextEvent;
import java.awt.Color;

public class Command_Launcher implements PlugIn {

    public void run(String arg) {
        // obtain a list of all commands, sorted
        Hashtable commands = ij.Menus.getCommands();
        final ArrayList keys = new ArrayList();
        keys.addAll(commands.keySet());
        Collections.sort(keys);

        // gui
        GenericDialog gd = new GenericDialog("Launcher");
        gd.addStringField("Command: ", "");
        final TextField prompt = (TextField)gd.getStringFields().get(0);
        prompt.setForeground(Color.red);

        prompt.addTextListener(new TextListener() {
            public void textValueChanged(TextEvent e) {
                String text = prompt.getText();
                // if a command matches, redo color to black
                for (Iterator it = keys.iterator(); it.hasNext(); ) {
                    String command = (String)it.next();
                    if (command.equals(text)) {
                        prompt.setForeground(Color.black);
                        return;
                    }
                }
                // no command found, set to red:
                prompt.setForeground(Color.red);
            }
        });

        gd.showDialog();
        if (gd.wasCanceled()) return;

        String command = gd.getNextString();

        // execute!
        IJ.doCommand(command);
    }
}
</source>

Note that above the loop is only set as an example. It's easier to simply query the list of ''keys'' for the specific ''text'' key we are looking for:

<source lang="java">
...
                // if a command matches, redo color to black  
                if (keys.contains(text)) {
                    prompt.setForeground(Color.black);
                    return;
                }
...
</source>

==In Jython==

See also the [[Jython Scripting]] documentation page.

<source lang="python">
from java.awt import Color
from java.awt.event import TextListener
import ij

commands = ij.Menus.getCommands().keySet().toArray()
gd = ij.gui.GenericDialog('Command Launcher')
gd.addStringField('Command: ', '');
prompt = gd.getStringFields().get(0)
prompt.setForeground(Color.red)

class TypeListener(TextListener):
    def textValueChanged(self, tvc):
        if prompt.getText() in commands:
            prompt.setForeground(Color.black)
            return  
        prompt.setForeground(Color.red)

prompt.addTextListener(TypeListener())
gd.showDialog()
if not gd.wasCanceled():
    ij.IJ.doCommand(gd.getNextString())
</source>

Above, note that instead of looping the list of commands, we just query it with an "if element in list" construct. To actually loop, do the following:

<source lang="python">
text = prompt.getText()
for c in commands:
    if c == text:
        prompt.setForeground(Color.black)
        return
prompt.setForeground(Color.red)
</source>

==In Clojure==

See also the [[Clojure Scripting]] documentation page.

<source lang="lisp">
(import '(java.awt Color)
        '(java.awt.event TextListener)
        '(ij.gui GenericDialog)
        '(ij IJ)
        '(ij Menus))

(let [commands (keys (. Menus getCommands))
      gd (GenericDialog. "Command Launcher")]
  (.addStringField gd "Command: " "")
  (let [prompt (. (. gd getStringFields) get 0)]
    (doto prompt
      (.setForeground (. Color red))
      (.addTextListener (proxy [TextListener] []
        (textValueChanged [tvc]
          (let [text (.getText prompt)]
            (.setForeground prompt
              (if (some #{text} commands)
                (. Color black)
                (. Color red)))))))))
  (.showDialog gd)
  (when-not (.wasCanceled gd)
    (IJ/doCommand (.getNextString gd))))
</source>

A second version, lispier, rewritten from the above by Clojure's author [http://clojure.sourceforge.net Rich Hickey]. Note the use of the ''some'' funtion to check whether any given key in a list (''text'' is the only key here) is contained in a set of keys (''commands''):

<source lang="lisp">
(import '(java.awt Color)
        '(java.awt.event TextListener))
 
(let [commands (keys (.getCommands ij.Menus))
      gd (ij.gui.GenericDialog. "Command Launcher")]
  (.addStringField gd "Command: " "")
  (let [prompt (.. gd getStringFields (get 0))]
    (doto prompt
      (setForeground (. Color red))
      (addTextListener (proxy [TextListener] []
        (textValueChanged [tvc]
          (let [text (.getText prompt)]
            (.setForeground prompt
              (if (some #{text} commands)
                (. Color black)
                (. Color red)))))))))
  (.showDialog gd)
  (when-not (.wasCanceled gd)
    (.doCommand ij.IJ (.getNextString gd))))
</source>

==In Javascript==

See also the [[Javascript Scripting]] documentation page.

<source lang="javascript">
// All ImageJ and java.lang.* classes have been automatically imported
// using importPackage(Package.ij) etc. directives.

importClass(Packages.java.awt.event.TextListener);
importClass(Packages.java.awt.Color)

var commands = Menus.getCommands();
var keys = commands.keySet();

var gd = new GenericDialog("Command Launcher");
gd.addStringField("Command: ", "");
var prom = gd.getStringFields().get(0);
prom.setForeground(Color.red);
prom.addTextListener(new TextListener( {
    textValueChanged: function(evt) {
        if (keys.contains(prom.getText()))
            prom.setForeground(Color.black);
        else
            prom.setForeground(Color.red);
    }
}));

gd.showDialog();
if (!gd.wasCanceled())
    IJ.doCommand(gd.getNextString());
</source>

==In JRuby==

For some tutorial material on using JRuby to script ImageJ, please see [[JRuby Scripting]].

<source lang="ruby">
include_class 'java.awt.Color'
include_class 'java.awt.event.TextListener'

class TypeListener

  # This is the (slightly surprising) JRuby way of implementing
  # a Java interface:
  include TextListener

  def initialize(commands,prompt)
    @commands = commands
    @prompt = prompt
  end

  def textValueChanged(tvc)
    text = @prompt.getText
    if @commands.include? text
      @prompt.setForeground Color.black
    else
      @prompt.setForeground Color.red
    end
  end

end

commands = ij.Menus.getCommands.keySet.toArray

gd = ij.gui.GenericDialog.new 'CommandLauncher'
gd.addStringField 'Command: ', ''

prompt = gd.getStringFields[0]
prompt.setForeground Color.red

prompt.addTextListener TypeListener.new( commands, prompt )

gd.showDialog
unless gd.wasCanceled
  ij.IJ.doCommand gd.getNextString
end
</source>

==In BeanShell==

See also the [[Beanshell Scripting]] documentation page.

For some tutorial material on using BeanShell, see [http://www.beanshell.org/manual/quickstart.html#Java_Statements_and_Expressions BeanShell's Quickstart].

If this looks awfully like the Java example to you, you are absolutely correct: BeanShell has the same syntax as Java, although it is not strongly typed (you do not need to declare variables if you do not want to), and it is interpreted.

<source lang="java">
import ij.IJ;
import ij.Menus;

import ij.plugin.PlugIn;

import ij.gui.GenericDialog;

import java.util.Hashtable;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Iterator;

import java.awt.TextField;
import java.awt.event.TextListener;
import java.awt.event.TextEvent;
import java.awt.Color;
 
keys = new ArrayList();
keys.addAll(Menus.getCommands().keySet());
Collections.sort(keys);
 
// gui
GenericDialog gd = new GenericDialog("Launcher");
gd.addStringField("Command: ", "");
final TextField prompt = (TextField)gd.getStringFields().get(0);
prompt.setForeground(Color.red);

prompt.addTextListener(new TextListener() {
	public void textValueChanged(TextEvent e) {
		String text = prompt.getText();
		// if a command matches, redo color to black
		for (Iterator it = keys.iterator(); it.hasNext(); ) {
			String command = (String)it.next();
			if (command.equals(text)) {
				prompt.setForeground(Color.black);
				return;
			}
		}
		// no command found, set to red:
		prompt.setForeground(Color.red);
	}
});

gd.showDialog();
if (gd.wasCanceled()) return;

String command = gd.getNextString();

// execute!
IJ.doCommand(command);
</source>


[[Category:Scripting]]
