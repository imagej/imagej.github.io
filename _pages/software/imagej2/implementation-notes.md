---
mediawiki:
- ImageJ2/Documentation/Edit/Options/Compatibility
- ImageJ2/Documentation/Edit/Options/Misc
- ImageJ2/Documentation/Image/Overlay/OverlayManager
- ImageJ2/Documentation/PointSetDemo
- ImageJ2/Documentation/Process/Math/Equation
title: ImageJ2 implementation notes
---

This page documents technical details of certain parts of ImageJ2.

## {% include bc path='Process | Math | Equation' %}

This section documents that language that can be used to specify equations via the {% include bc path='Process | Math | Equation'%} command.

The {% include bc path='Process | Math | Equation'%} dialog supports a powerful language for defining equations that can be used to fill images with data.

An equation is defined by a list of index variable declarations and a formula definition. If the formula does not refer to any index variables they can be omitted from the definition. (Index variables are discussed a bit later)

For example here is the most basic definition:

```
12
```

When you query this equation it returns the value 12. Note that there are no index variable definitions.

Here is an example of an equation with index variable definitions:

```
[ u , v ] , u + v
```

When you query this equation for a loaded image it substitutes each x index for u and each y index for v and returns u + v (resulting in a ramp).

Note that index names do not have to be those defined in ImageJ 1.x (i.e. x, y, c, z, or t). They can be any name you designate. The key concept is that the order of index definition is important. If your input image is defined such that it has axes `[X,Y,FREQUENCY]` you want your equation to match (i.e. `[u,v,freq] , freq * 1.3` )

If you have a multidimensional set of data it is important to specify all axes as index variables. For instance for a 5d `[X,Y,Z,C,T]` data set we might want an equation that sets the pixel value to 2 times the time index. If you specified it like this

```
[ t ] , t * 2
```

the input image would substitute x values for the t variable and you would not get what you want. A correct specification would be:

```
[x,y,z,c,t] , t * 2
```

However one can underspecify a set of axes without issue if they are not used. Given an input image whose axes are `[X,Y,Z,C,T]` one can legally specify a function like this:

```
[x,y,z], x + z
```

Notice that we don't care about the Y axis but we specify it to keep the positional indexes populated correctly. And we are ignoring the C and T axes.

One can also use the current image's data values as input to an equation. For instance here is an example that does so:

```
img+23
```

When you query this equation for a loaded image it substitutes each pixel value for the `img` function and adds 23 to it (resulting in a brightening).

Equations are specified in pieces. The equation language supports:

- add / subtract / multiply / divide / mod (`+` `-` `*` `/` `%`)
- raising to a power ( `^` )
- negation ( `-` )
- variable index references ( `x in [x,y]` , `3 * x` )
- an image reference ( `img` )
- calls to built in functions (such as `sin(v)` - more listed below)
- constants ( such as `E` and `PI`  in `E * 7` or `PI / 4` )
- parentheses

Here are some simple examples:

-   `7`
-   `7 - PI + E`
-   `[x], (3*x) - 9`
-   `[x,y], 200/(y + 30)`
-   `[x,y] , x^2 + y^2`
-   `img`
-   `[x,y] , sin(y)`

There are numerous built in functions that can appear in an equation. For reference they are enumerated here:

| **Function** | **Example**                | **Description**                                                                                                             |
|--------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **abs**      | `[x,y] , abs(y)`           | Returns the absolute value of its input.                                                                                    |
| **acos**     | `[x,y] , acos(y)`          | Returns the angle in radians whose cosine equals the given input.                                                           |
| **acosh**    | `[x,y] , acosh(y)`         | Returns the angle in radians whose hyperbolic cosine equals the given input.                                                |
| **acot**     | `[x,y] , acot(y)`          | Returns the angle in radians whose cotangent equals the given input.                                                        |
| **acoth**    | `[x,y] , acoth(y)`         | Returns the angle in radians whose hyperbolic cotangent equals the given input.                                             |
| **acsc**     | `[x,y] , acsc(y)`          | Returns the angle in radians whose cosecant equals the given input.                                                         |
| **acsch**    | `[x,y] , acsch(y)`         | Returns the angle in radians whose hyperbolic cosecant equals the given input.                                              |
| **angle**    | `[x,y,z,c,t] , angle(z,t)` | Returns the angle in radians of a given pixel along two specified axes.                                                     |
| **asec**     | `[x,y] , asec(y)`          | Returns the angle in radians whose secant equals the given input.                                                           |
| **asech**    | `[x,y] , asech(y)`         | Returns the angle in radians whose hyperbolic secant equals the given input.                                                |
| **asin**     | `[x,y] , asin(y)`          | Returns the angle in radians whose sine equals the given input.                                                             |
| **asinh**    | `[x,y] , asinh(y)`         | Returns the angle in radians whose hyperbolic sine equals the given input.                                                  |
| **atan**     | `[x,y] , atan(y)`          | Returns the angle in radians whose tangent equals the given input.                                                          |
| **atanh**    | `[x,y] , atanh(y)`         | Returns the angle in radians whose hyperbolic tangent equals the given input.                                               |
| **cbrt**     | `[x,y] , cbrt(y)`          | Returns the cube root of the given input.                                                                                   |
| **ceil**     | `[x,y] , ceil(y)`          | Returns the result of pushing a non integral input value to the next higher integral value.                                 |
| **cos**      | `[x,y] , cos(y)`           | Returns the cosine of an input value.                                                                                       |
| **cosh**     | `[x,y] , cosh(y)`          | Returns the hyperbolic cosine of an input value.                                                                            |
| **cot**      | `[x,y] , cot(y)`           | Returns the cotangent of an input value.                                                                                    |
| **coth**     | `[x,y] , coth(y)`          | Returns the hyperbolic cotangent of an input value.                                                                         |
| **csc**      | `[x,y] , csc(y)`           | Returns the cosecant of an input value.                                                                                     |
| **csch**     | `[x,y] , csch(y)`          | Returns the hyperbolic cosecant of an input value.                                                                          |
| **dctr**     | `[x,y] , dctr`             | Returns the distance from the center of the image for each input pixel.                                                     |
| **dim**      | `[x,y,z], dim(z)`          | Returns the dimension of a specified axis of an input image. I.e. for a 200x500 image `dim(y)` would be 500.                |
| **exp**      | `[x,y] , exp(y)`           | Returns the result of raising the constant E to the power equal to the given input.                                         |
| **expm1**    | `[x,y] , expm1(y)`         | Returns the result of raising the constant E to the power equal to the given input and subtracting one.                     |
| **floor**    | `[x,y] , floor(y)`         | Returns the result of truncating an input value to an integral value.                                                       |
| **gauss**    | `[x,y] , gauss(y)`         | Returns a gaussian random variable of mean 0 and whose standard deviation matches the input value.                          |
| **img**      | `[x,y] , img`              | Returns pixel values from the currently active image.                                                                       |
| **log**      | `[x,y] , log(y)`           | Returns the natural log of the given input.                                                                                 |
| **log1p**    | `[x,y] , log1p(y)`         | Returns the natural log of the sum of the given input and one.                                                              |
| **log10**    | `[x,y] , log10(y)`         | Returns the 10-based log of the given input.                                                                                |
| **log2**     | `[x,y] , log2(y)`          | Returns the 2-based log of the given input.                                                                                 |
| **max**      | `[x,y] , max(x,y)`         | Returns the maximum of the two input values.                                                                                |
| **min**      | `[x,y] , min(x,y)`         | Returns the minimum of the two input values.                                                                                |
| **rand**     | `[x,y] , rand(y)`          | Returns a random number uniformly distributed on the range of 0 up to but not including the input value.                    |
| **rint**     | `[x,y] , rint(y)`          | Returns the result of rounding a given input value to the nearest integer value (redundant).                                |
| **round**    | `[x,y] , round(y)`         | Returns the result of rounding a given input value to the nearest integer value (redundant).                                |
| **sec**      | `[x,y] , sec(y)`           | Returns the secant of an input value.                                                                                       |
| **sech**     | `[x,y] , sech(y)`          | Returns the hyperbolic secant of an input value.                                                                            |
| **signum**   | `[x,y] , signum(y)`        | Returns -1, 0, or 1 depending upon whether a given input value is negative, zero, or positive.                              |
| **sin**      | `[x,y] , sin(y)`           | Returns the sine of an input value.                                                                                         |
| **sinc**     | `[x,y] , sinc(y)`          | Returns sin(x) / x for a given input value x.                                                                               |
| **sincpi**   | `[x,y] , sincpi(y)`        | Returns sin(PI*x) / (PI*x) for a given input value x.                                                                       |
| **sinh**     | `[x,y] , sinh(y)`          | Returns the hyperbolic sine of an input value.                                                                              |
| **sqr**      | `[x,y] , sqr(y)`           | Returns the square of an input value.                                                                                       |
| **sqrt**     | `[x,y] , sqrt(y)`          | Returns the square root of an input value.                                                                                  |
| **step**     | `[x,y] , step(y)`          | Returns 0 if an input value is less than 0. Otherwise returns 1.                                                            |
| **tan**      | `[x,y] , tan(y)`           | Returns the tangent of an input value.                                                                                      |
| **tanh**     | `[x,y] , tanh(y)`          | Returns the hyperbolic tangent of an input value.                                                                           |
| **tmax**     | `[x,y], tmax`              | Returns the maximum possible value of a pixel for a given input image. E.g. uint8=255, int8=127.                            |
| **tmin**     | `[x,y], tmin`              | Returns the minimum possible value of a pixel for a given input image. E.g. uint8=0, int8=-128.                             |
| **ulp**      | `[x,y], ulp(y)`            | Returns the positive distance between the input floating-point value and the floating point value next larger in magnitude. |

We can compare this language to the ImageJ 1.x {% include bc path='Process | Math | Macro'%} language. In ImageJ 1.x the default macro for the command is defined as `v = v + 50*sin(d/10)`. Note that this exact string is not legal syntax in the new equation language. But it can now be specified as `img+50*sin(dctr/10)`.

## {% include bc path='Edit | Options | Compatibility' %}

This section documents the {% include bc path='Edit | Options | Compatibility'%} command dialog.

Some commands have an associated ImageJ 1.x compatibility mode flag. The flag setting affects how some commands behave in ImageJ. The authors of ImageJ2 want to provide a mechanism whereby ImageJ 1.x behavior can be overridden when it makes sense. This allows breaks to be made with the past if necessary. Setting the mode to "Modern" will override some ImageJ 1.x behavior while setting it to `/libs/imagej-legacy` will maintain ImageJ 1.x behavior as much as possible.

Commands that are affected by this setting:

The Invert command - in ImageJ 1.x the Invert command inverts all pixels with respect to the minimum and maximum data values present in an image. Though the behavior is different with respect to 8-bit images which always invert relative to 0/255. When the compatibility mode setting is "Compatibility" this behavior is maintained. When its setting is "Modern" 8-bit images will also invert relative to minimum and maximum data values.

## {% include bc path='Image | Overlay | Overlay Manager' %}

ImageJ2's Overlay Manager is fairly similar to the ImageJ 1.x ROI Manager. See the [ImageJ 1.x documentation of its ROI Manager](/ij/docs/menus/analyze.html#manager).

However there are some major differences between them. For instance:

-   In ImageJ2 overlays are automatically added to the Overlay Manager; they do not need to be selected and added separately.
-   Overlays are also removed from the Overlay Manager when no references to them exist from any open image. Thus the Overlay Manager does not act like a storage bin for overlays. It is rather a tool for working with overlays. Overlays can still be saved to and restored from disk.

## PointSet Demo

The `PointSet` demo program shows off the power of `TextSpecifiedPointSet`s that are part of the ImgLib2 OPS subproject.

The dialog shows a text field that can be used to specify complex sets of points. The resulting points are displayed as a two color image with white denoting points in the set and black denoting points outside the set.

The syntax for a text specified `PointSet` is as one or more axis ranges optionally followed by equations that specify additional constraints. Each term is separated by comma values.

The axis syntax follows Haskell's list comprehension syntax. You can specify an axis name and its associated single value (i.e. `x = [10]`). Or multiple values (i.e. `x=[10,20,30]`). Or a range of values (i.e. `x = [1..25]`). Or even a range of values by a defined step size (i.e. `x = [1,3..15]` which equals [1,3,5,7,9,11,13,15]).

The constraint equations use much of the same syntax as outlined [here](#process--math--equation).

Some examples:

* X ranges from 1 to 10, y ranges from 5 to 15: `x=[1..10], y=[5..15]`
* Same set of points but further constrained such that x plus y is less than 20: `x=[1..10], y=[5..15], x + y < 20`
* A circular area centered at 50,50: `x=[1..100], y=[1..100], (x-50)^2 + (y-50)^2 <= 400`

Multiple axes can be defined as well as any number of constraints as long as they are separated by commas. All constraints are applied simultaneously (in an AND fashion). And any function that is defined by the equation language (hyperlinked earlier) can be used in the specification of the constraint.
