{{ComponentStats:sc.fiji:Reconstruct_Reader}}The Reconstruct Reader plugin is a utility to transform [http://synapses.clm.utexas.edu/tools/reconstruct/reconstruct.stm Reconstruct] projects directly into [[TrakEM2]] projects.

== Usage ==
Reconstruct projects consist of a folder containing a series file, a set of section files, and a set of image files. A series file will have a ''.ser'' extension, while a section file will have a numeric extension, like Project.1, Project.2, ... , Project.100, and so forth.

To translate a Reconstruct project into a TrakEM2 project, you may either open it through Fiji's {{bc | File | Open...}} dialog, or through the {{bc | File | Import | Reconstruct Project...}} dialog. Either one will prompt you to open a series file.

The log output will show That the Reconstruct Translator has been created, and that translation has begun. Translation often takes only a handful of seconds, but generating mipmaps will often take quite some time.

== Function ==
The Reconstruct Reader plugin functions by translating a Reconstruct project folder directly into a single TrakEM2 project ''.xml'' file, then opening that file in TrakEM2.

No changes are ever saved to the Reconstruct project. The new ''.xml'' file associated with the project should be opened for any successive TrakEM2 sessions.

== Known Bugs and Issues ==
* After translation, the user is informed that TrakEM2 has detected a crash. This is because the translation process does not currently generate certain non-critical files that TrakEM2 expects to exist. This does not indicate an actual problem.

== Contact ==
The author of this plugin is {{Person|Lindsey}}

----

[[Category:Plugins]]
[[Category:TrakEM2]]
