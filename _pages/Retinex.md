{{Infobox
| software               = ImageJ
| name                   = Retinex
| maintainer             = [mailto:jimenezf_at_fi.uaemex.mx Francisco Jiménez Hernández]
| author                 = Francisco Jiménez Hernández
| source                 = {{GitHub|org=fiji|repo=Fiji_Plugins|source=Retinex_.java}}
| released               = 02/08/2010
| latest version         = 02/08/2010
| status                 = 
| category               = [[:Category:Plugins]]
| website                = 
}}
== Retinex ==

Retinex filtering is based on Land's theory of image perception, proposed to explain the perceived colour constancy of objects under varying illumination conditions. Several approaches exist to implement the retinex principles, among these the multiscale retinex with colour restoration algorithm (MSRCR) combines colour constancy with local contrast enhancement so images are rendered similarly to how human vision is believed to operate.

== Usage ==
;'''Level'''
:specifies distribution of the Gaussian blurring kernel sizes for Scale division values > 2: 
:;'''Uniform'''
::tends to treat all image intensities similarly,
:;'''Low'''
::enhances dark regions of the image, 
:;'''High'''
:;enhances the bright regions of the image.

;'''Scale'''
:specifies the depth of the retinex effect.

;'''Scale division'''
:specifies the number of iterations of the multiscale filter. Values larger than 2 exploit the "multiscale" nature of the algorithm.

;'''Dynamic'''
:adjusts the colour of the result. Large values produce less saturated images.. 

== Example ==
Original:
[[Image:Photo1.jpg]]

After Retinex (default parameters):
[[Image:Photo1-Retinex.jpg]]

== Homepage ==

Please find the original page for the Retinex plugin [http://www.mecourse.com/landinig/software/retinex/retinex.html here].

[[Category:Tutorials]]
[[Category:Plugins]]
