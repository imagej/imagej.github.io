This page documents that language that can be used to specify equations via the {{bc | Process | Math | Equation}} command.

The {{bc | Process | Math | Equation}} dialog supports a powerful language for defining equations that can be used
to fill images with data.

An equation is defined by a list of index variable declarations and a formula definition. If the formula does not
refer to any index variables they can be omitted from the definition. (Index variables are discussed a bit later)

For example here is the most basic definition: <UL>"12"</UL>
When you query this equation it returns the value 12. Note that there are no index variable definitions.

Here is an example of an equation with index variable definitions: <UL>" [ u , v ] , u + v "</UL> 
When you query this equation for a loaded image it substitutes each x index for u and each y index for v
and returns u + v (resulting in a ramp).

Note that index names do not have to be those defined in ImageJ 1.x (i.e. x, y, c, z, or t). They can be any name
you designate. The key concept is that the order of index definition is important. If your input image is defined
such that it has axes [X,Y,FREQUENCY] you want your equation to match (i.e. "[u,v,freq] , freq * 1.3" )

If you have a multidimensional set of data it is important to specify all axes as index variables. For instance for a 5d
[X,Y,Z,C,T] data set we might want an equation that sets the pixel value to 2 times the time index. If you specified it like this <UL>"[ t ] , t * 2"</UL> the input image would substitute x values for the t variable and you would not get what you want. A correct specification would be: <UL>"[x,y,z,c,t] , t * 2"</UL>

However one can underspecify a set of axes without issue if they are not used. Given an input image whose axes
are [X,Y,Z,C,T] one can legally specify a function like this: <UL>"[x,y,z], x + z"</UL> Notice that we don't care about the Y axis but we specify it to keep the positional indexes populated correctly. And we are ignoring the C and T axes.

One can also use the current image's data values as input to an equation.
For instance here is an example that does so: <UL>"img+23"</UL>
When you query this equation for a loaded image it substitutes each pixel value for the "img" function and adds 23 to it
(resulting in a brightening).

Equations are specified in pieces. The equation language supports:
  - add / subtract / multiply / divide / mod (+ - * / %)
  - raising to a power ( ^ )
  - negation ( - )
  - variable index references ( x in "[x,y] , 3 * x" )
  - an image reference ( img )
  - calls to built in functions (such as sin(v) - more listed below)
  - constants ( such as E and PI  in "E * 7" or "PI / 4" )
  - parentheses

Here are some simple examples: 
<UL>
  <LI>"7"</LI>
  <LI>"7 - PI + E"</LI>
  <LI>"[x], (3*x) - 9"</LI>
  <LI>"[x,y], 200/(y + 30)"</LI>
  <LI>"[x,y] , x^2 + y^2"</LI>
  <LI>"img"</LI>
  <LI>"[x,y] , sin(y)"</LI>
</UL>

There are numerous built in functions that can appear in an equation. For reference they are enumerated here:

<B>abs</B> : example ( "[x,y] , abs(y) " )

<UL><LI>Returns the absolute value of its input.</LI></UL>

<B>acos</B> : example ( "[x,y] , acos(y) " )

<UL><LI>Returns the angle in radians whose cosine equals the given input.</LI></UL>

<B>acosh</B> : example ( "[x,y] , acosh(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic cosine equals the given input.</LI></UL>

<B>acot</B> : example ( "[x,y] , acot(y) " )

<UL><LI>Returns the angle in radians whose cotangent equals the given input.</LI></UL>

<B>acoth</B> : example ( "[x,y] , acoth(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic cotangent equals the given input.</LI></UL>

<B>acsc</B> : example ( "[x,y] , acsc(y) " )

<UL><LI>Returns the angle in radians whose cosecant equals the given input.</LI></UL>

<B>acsch</B> : example ( "[x,y] , acsch(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic cosecant equals the given input.</LI></UL>

<B>angle</B> : example ( "[x,y,z,c,t] , angle(z,t) " ) [Note - two index variable name arguments]

<UL><LI>Returns the angle in radians of a given pixel along two specified axes.</LI></UL>

<B>asec</B> : example ( "[x,y] , asec(y) " )

<UL><LI>Returns the angle in radians whose secant equals the given input.</LI></UL>

<B>asech</B> : example ( "[x,y] , asech(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic secant equals the given input.</LI></UL>

<B>asin</B> : example ( "[x,y] , asin(y) " )

<UL><LI>Returns the angle in radians whose sine equals the given input.</LI></UL>

<B>asinh</B> : example ( "[x,y] , asinh(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic sine equals the given input.</LI></UL>

<B>atan</B> : example ( "[x,y] , atan(y) " )

<UL><LI>Returns the angle in radians whose tangent equals the given input.</LI></UL>

<B>atanh</B> : example ( "[x,y] , atanh(y) " )

<UL><LI>Returns the angle in radians whose hyperbolic tangent equals the given input.</LI></UL>

<B>cbrt</B> : example ( "[x,y] , cbrt(y) " )

<UL><LI>Returns the cube root of the given input.</LI></UL>

<B>ceil</B> : example ( "[x,y] , ceil(y) " )

<UL><LI>Returns the result of pushing a non integral input value to the next higher integral value.</LI></UL>

<B>cos</B> : example ( "[x,y] , cos(y) " )

<UL><LI>Returns the cosine of an input value.</LI></UL>

<B>cosh</B> : example ( "[x,y] , cosh(y) " )

<UL><LI>Returns the hyperbolic cosine of an input value.</LI></UL>

<B>cot</B> : example ( "[x,y] , cot(y) " )

<UL><LI>Returns the cotangent of an input value.</LI></UL>

<B>coth</B> : example ( "[x,y] , coth(y) " )

<UL><LI>Returns the hyperbolic cotangent of an input value.</LI></UL>

<B>csc</B> : example ( "[x,y] , csc(y) " )

<UL><LI>Returns the cosecant of an input value.</LI></UL>

<B>csch</B> : example ( "[x,y] , csch(y) " )

<UL><LI>Returns the hyperbolic cosecant of an input value.</LI></UL>

<B>dctr</B> : example ( "[x,y] , dctr" ) [Note - no arguments]

<UL><LI>Returns the distance from the center of the image for each input pixel.</LI></UL>

<B>dim</B> : example ( "[x,y,z], dim(z)" ) [Note - one index variable name argument]

<UL><LI>Returns the dimension of a specified axis of an input image. I.e. for a 200x500 image dim(y) would be 500.</LI></UL>

<B>exp</B> : example ( "[x,y] , exp(y) " )

<UL><LI>Returns the result of raising the constant E to the power equal to the given input.</LI></UL>

<B>expm1</B> : example ( "[x,y] , expm1(y) " )

<UL><LI>Returns the result of raising the constant E to the power equal to the given input and subtracting one.</LI></UL>

<B>floor</B> : example ( "[x,y] , floor(y) " )

<UL><LI>Returns the result of truncating an input value to an integral value.</LI></UL>

<B>gauss</B> : example ( "[x,y] , gauss(y) " )

<UL><LI>Returns a gaussian random variable of mean 0 and whose standard deviation matches the input value.</LI></UL>

<B>img</B> : example ( "[x,y] , img " ) [Note - no arguments]

<UL><LI>Returns pixel values from the currently active image.</LI></UL>

<B>log</B> : example ( "[x,y] , log(y) " )

<UL><LI>Returns the natural log of the given input.</LI></UL>

<B>log1p</B> : example ( "[x,y] , log1p(y) " )

<UL><LI>Returns the natural log of the sum of the given input and one.</LI></UL>

<B>log10</B> : example ( "[x,y] , log10(y) " )

<UL><LI>Returns the 10-based log of the given input.</LI></UL>

<B>log2</B> : example ( "[x,y] , log2(y) " )

<UL><LI>Returns the 2-based log of the given input.</LI></UL>

<B>max</B> : example ( "[x,y] , max(x,y) " )

<UL><LI>Returns the maximum of the two input values.</LI></UL>

<B>min</B> : example ( "[x,y] , min(x,y) " )

<UL><LI>Returns the minimum of the two input values.</LI></UL>

<B>rand</B> : example ( "[x,y] , rand(y) " )

<UL><LI>Returns a random number uniformly distributed on the range of 0 up to but not including the input value.</LI></UL>

<B>rint</B> : example ( "[x,y] , rint(y) " )

<UL><LI>Returns the result of rounding a given input value to the nearest integer value (redundant).</LI></UL>

<B>round</B> : example ( "[x,y] , round(y) " )

<UL><LI>Returns the result of rounding a given input value to the nearest integer value (redundant).</LI></UL>

<B>sec</B> : example ( "[x,y] , sec(y) " )

<UL><LI>Returns the secant of an input value.</LI></UL>

<B>sech</B> : example ( "[x,y] , sech(y) " )

<UL><LI>Returns the hyperbolic secant of an input value.</LI></UL>

<B>signum</B> : example ( "[x,y] , signum(y) " )

<UL><LI>Returns -1, 0, or 1 depending upon whether a given input value is negative, zero, or positive.</LI></UL>

<B>sin</B> : example ( "[x,y] , sin(y) " )

<UL><LI>Returns the sine of an input value.</LI></UL>

<B>sinc</B> : example ( "[x,y] , sinc(y) " )

<UL><LI>Returns sin(x) / x for a given input value x.</LI></UL>

<B>sincpi</B> : example ( "[x,y] , sincpi(y) " )

<UL><LI>Returns sin(PI*x) / (PI*x) for a given input value x.</LI></UL>

<B>sinh</B> : example ( "[x,y] , sinh(y) " )

<UL><LI>Returns the hyperbolic sine of an input value.</LI></UL>

<B>sqr</B> : example ( "[x,y] , sqr(y) " )

<UL><LI>Returns the square of an input value.</LI></UL>

<B>sqrt</B> : example ( "[x,y] , sqrt(y) " )

<UL><LI>Returns the square root of an input value.</LI></UL>

<B>step</B> : example ( "[x,y] , step(y) " )

<UL><LI>Returns 0 if an input value is less than 0. Otherwise returns 1.</LI></UL>

<B>tan</B> : example ( "[x,y] , tan(y) " )

<UL><LI>Returns the tangent of an input value.</LI></UL>

<B>tanh</B> : example ( "[x,y] , tanh(y) " )

<UL><LI>Returns the hyperbolic tangent of an input value.</LI></UL>

<B>tmax</B> : example ( "[x,y], tmax " ) [Note - no arguments]

<UL><LI>Returns the maximum possible value of a pixel for a given input image. For an unsigned 8-bit image the
value would be 255 and for a signed 8-bit image the value would be 127.</LI></UL>

<B>tmin</B> : example ( "[x,y], tmin " ) [Note - no arguments]
 
<UL><LI>Returns the minimum possible value of a pixel for a given input image. For an unsigned 8-bit image the
value would be 0 and for a signed 8-bit image the value would be -128.</LI></UL>

<B>ulp</B> : example ( "[x,y], ulp(y) " )
 
<UL><LI>Returns the the positive distance between the input floating-point value and the floating point value next larger in magnitude.</LI></UL>

We can compare this language to the ImageJ 1.x {{bc | Process | Math | Macro}} language. In ImageJ 1.x the default macro for the command is defined as "v = v + 50*sin(d/10)". Note that this exact string is not legal syntax in the new equation language. But it can now be specified as "img+50*sin(dctr/10)".
