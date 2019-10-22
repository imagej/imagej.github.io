(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== The relation between Content and Universe ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


The following figure shows a simplified class diagram which shows the class hierarchy and relationship of the most important classes for users ofthe API:
[[Image:3DViewer-class-diagram.png|thumb|center|800px|Simplified class diagram showing the core classes of the 3D Viewer.]]



=== The class hierarchy of the universe classes ===

There exist three classes which together provide the functionality of the
universe:
* <code><b>DefaultUniverse</b></code> initializes the scene graph. It provides methods for retrieving the window in which the universe is shown, and the root <code>BranchGroup</code> of the Java3D scene graph, under which all objects are placed.
* <code><b>DefaultAnimatableUniverse</b></code> extends <code>DefaultUniverse</code>. It provides functionality for animation and recording.
* <code><b>Image3DUniverse</b></code> in turn extends <code>DefaultAnimatableUniverse</code>. It provides methods for adding, deleting and selecting Contents.


=== The relationship between <code>Content</code> and <code>Image3DUniverse</code> ===
<code>Image3DUniverse</code> can hold several <code>Content</code>s. This are stored in a hash map, identified by their name. This requires that the name of a <code>Content</code> is unique.

The <code>Content</code> itself holds its attributes like color, transparency etc, but also a local transformation and a reference to the <code>ContentNode</code>.

=== The relationship between <code>Content</code> and <code>ContentNode</code> ===
<code>ContentNode</code> is the actual class which represents a 3D object. It is an abstract class, which is among others subclassed by <code>VoltexGroup</code> (representing a volume rendering) and <code>MeshGroup</code> (representing an isosurface). A <code>Content</code> has exactly one reference to a <code>ContentNode</code> at a time.

When functionality is required which is common to all <code>ContentNode</code>s, is is often sufficient to work with <code>Content</code> itself. For special functionality of a certain type of <code>Content</code>, however, it is most probably required to work with the <code>ContentNode</code>.

As an example think of volume editing. Functionality about that makes only sense in the context of volume renderings, and therefore, the corresponding methods are located in <code>VoltexGroup</code>.


=== The message flow between Content and ContentNode ===
When e.g. <code>Content.setColor()</code> is called, it first checks if the specified color is different from the existing color. If it is, it sets the current color (which is a field of <code>Content</code>) and calls the <code>colorUpdated()</code> method which is defined in the <code>ContentNode</code> interface.
