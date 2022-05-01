---
title: 2012-12-11 - Hiding generics in SCIFIO
---

### Generics in SCIFIO

The use of generic types makes a lot of sense in SCIFIO: you have an interface-driven design, intended to be flexible and extensible, yet each {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/Format.java' label='Format' %} implementation is tightly linked with concrete implementations of the other SCIFIO components. Using generics ensures type safety of operations within these components, so that each interacts only with objects they know how to handle (e.g. it wouldn't make sense to provide an APNG {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/Reader.java' label='Reader' %} with an OME-TIFF {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/Metadata.java' label='Metadata' %} object).

### Two scenarios

There are essentially two use cases in SCIFIO.

-   General algorithms. In this case, the developer is writing general image IO algorithms that will operate on a variety of image formats. In this case, there are no known concrete instances.
-   Specific algorithms. The developer is coding against a specific, known image format(s). The concrete type can be instantiated.

In the second case, there are no generics to worry about. In the first case, if generics were present in all levels of the SCIFIO interfaces, you would either have to use raw types or wildcards in any declarations, and may need to cast in many method calls. The generics are working against you, because you literally can't know what types to code against.

### Hiding generics

To shield developers from generic wildcards, raw types, and casting, we split the component interfaces in SCIFIO. Each component has a base interface (e.g. {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/Reader.java' label='Reader' %}) and a typed subclass ({% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/TypedReader.java' label='TypedReader' %}). Base interfaces reference the base interfaces of other components, and typed interfaces referenced other typed interfaces (and propagate generic parameters up to the concrete implementations, where they disappear again).

So if you want to use SCIFIO components in a general way, you can use the base interfaces and won't have to fight with generics to find the proper syntax. If you know what formats you're going to be using, you have the benefit of methods accepting and returning those known types. In either case, generics are providing compile-time safety.

### The problem with type narrowing

The base/typed interface split is nice because return types can naturally be narrowed as you descend the class hierarchy and learn more about what types are present. However, method parameters cannot be narrowed this way: the general base interface implies methods will work with any implementation of their parameters (e.g. {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/Writer.java\#L92' label='Writer\#setMetadata' %}). When you get to the `TypedWriter`, which has access to a generic Metadata parameter `M`, you can't just declare `setMetadata(M)` if `M extends Metadata`. That method would have the same type erasure as in the base interface.

To avoid creating differently named method signatures, we followed the base/typed pattern for any SCIFIO class that appeared as a generic parameter, and created: {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/TypedMetadata.java' label='TypedMetadata' %}and {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/DataPlane.java' label='DataPlane' %}. Although these typed classes extend base classes that are used with parallel signatures, they provide a different point for erasure and allow the happy inclusion of parameterized methods, like {% include github org='hinerm' repo='bioformats' tag='blog-generics' path='components/scifio-devel/src/ome/scifio/DataPlane.java' label='TypedWriter\#setMetadata' %}.

This does mean that when you are programming with concrete implementations, you may see some extra (less specific) method signatures in the API that will throw `IllegalArgumentExceptions` if given incorrect parameters. But we think it's worth it to avoid code like this:

{% include img align="center" src="/media/news/terrifying-generics.jpg" caption="**The Evolution of SCIFIO**: Generics can be terrifying." width="700px" %}
 
