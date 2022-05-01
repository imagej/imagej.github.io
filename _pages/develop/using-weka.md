---
mediawiki: Using_Weka
title: Using Weka
---

## A very small how to get started with Weka using a KDTree

[Weka](http://sourceforge.net/projects/weka/) seems to be a very nice framework that implements a lot of stuff for machine learning. It is completely Java based and Open Source. Here I just want to share my experiences getting started with Weka.

### Why do I want to use Weka

In my case, I simply want to find nearest neighbors in two clouds of 3D points.

### Setting up Weka

As of commit {% include github org=fiji repo=fiji commit=df44aab197dcff1c0de228b0ac08b7ef8966b75e %} (December 16th, 2009), Fiji's *master* branch comes with Weka.

### Using the Weka datastructures

Weka is seems to work with arbitrary datastructures and -types. They are defined using the weka.core.Attribute object that can even hold weka.core.FastVector objects. Each weka.core.Instance is one dataelement that contains n Attributes and their respective values. Groups of same type of Instance objects are grouped using weka.core.Instances.

Below is a Java method howto store a list of 3D points as a Weka datastructure.

```java
/**
* Creates a Weka Datastructure out of a List of 3D Points
* @param points - List of 3D Points
* @param name - Instance name
* @return Instances containing all 3D points
*/
public Instances insertIntoWeka(final List <Point3d> points, final String name)
{
    // Create numeric attributes "x" and "y" and "z"
    Attribute x = new Attribute("x");
    Attribute y = new Attribute("y");
    Attribute z = new Attribute("z");

        // Create vector of the above attributes
    FastVector attributes = new FastVector(3);
    attributes.addElement(x);
    attributes.addElement(y);
    attributes.addElement(z);

    // Create the empty datasets "wekaPoints" with above attributes
    Instances wekaPoints = new Instances(name, attributes, 0);

    for (Iterator<Point3d> i = points.iterator(); i.hasNext();)
    {
        // Create empty instance with three attribute values
        Instance inst = new Instance(3);

        // get the point3d
        Point3d p = i.next();

        // Set instance's values for the attributes "x", "y", and "z"
        inst.setValue(x, p.x);
        inst.setValue(y, p.y);
        inst.setValue(z, p.z);

        // Set instance's dataset to be the dataset "wekaPoints"
        inst.setDataset(wekaPoints);

        // Add the Instance to Instances
        wekaPoints.add(inst);
    }

    return wekaPoints;
}
```

### Setting up the KDTree

Setting up the {% include wikipedia title='Kd-tree' text='KDTree'%} is rather simple. The tricky part is the Euclidean Distance measure. It is very nice that Weka automatically figures out how to compute the Euclidean Distance as we use only simple numeric attributes. However, by default it nomalizes the data independently for each dimension which might cause problems as in my case. If you want to prevent him from doing so you have to assign a new EuclideanDistance object that does not normalize.

```java
//
// Create the weka datastructure for 3D Points
//

Instances wekaPoints1 = insertIntoWeka(points1, "wekaPoints1");

//
// Set up the KDTree
//

KDTree tree = new KDTree();

try
{
    tree.setInstances(wekaPoints1);

    EuclideanDistance df = new EuclideanDistance(wekaPoints1);
    df.setDontNormalize(true);

    tree.setDistanceFunction(df);
}
catch (Exception e) { e.printStackTrace();}
```

### Searching the KDTree

Once solved the normalization issue, searching the KDTree for the N-Nearest Neighbors is simple again. You create another Instance of the same type and ask the KDTree for its nearest neigbors.

First we create an Instance that can be used to search the KDTree. Later on it is very simple to just update its values rather than creating a new one for each query.

```java
/**
* Create an Instance of the same type as the Instances object you are searching in.
* @param p - a 3D point
* @param dataset - the dataset you are searching in, which was used to build the KDTree
* @return an Instance that the nearest neighbor can be found for
*/
public Instance createInstance(final Point3d p, final Instances dataset)
{
    // Create numeric attributes "x" and "y" and "z"
    Attribute x = dataset.attribute(0);
    Attribute y = dataset.attribute(1);
    Attribute z = dataset.attribute(2);

    // Create vector of the above attributes
    FastVector attributes = new FastVector(3);
    attributes.addElement(x);
    attributes.addElement(y);
    attributes.addElement(z);

    // Create empty instance with three attribute values
    Instance inst = new Instance(3);

    // Set instance's values for the attributes "x", "y", and "z"
    inst.setValue(x, p.x);
    inst.setValue(y, p.y);
    inst.setValue(z, p.z);

    // Set instance's dataset to be the dataset "points1"
    inst.setDataset(dataset);

    return inst;
}
```

Now we can easily search the KDTree.

```java
// let's search for the nearest and second nearest neighbor
Instance nn1, nn2;
final Instance p = createInstance(new Point3d(0,0,0), wekaPoints);

try
{
    Instances neighbors = tree.kNearestNeighbours(p, 2);
    nn1 = neighbors.instance(0);
    nn2 = neighbors.instance(1);
}
catch (Exception e) { nn1 = nn2 = null; }

System.out.println(nn1 + " is the nearest neigbor for " + p);
System.out.println(nn2 + " is the second nearest neigbor for " + p);

// Now we can also easily compute the distances as the KDTree does it

DistanceFunction df = tree.getDistanceFunction();
System.out.println("The distance between" + nn1 + " and " + p + " is " + df.distance(nn1, p));
System.out.println("The distance between" + nn2 + " and " + p + " is " + df.distance(nn2, p));
```

### See also

-   How to [use Weka in your Java code](https://waikato.github.io/weka-wiki/use_weka_in_your_java_code/)
