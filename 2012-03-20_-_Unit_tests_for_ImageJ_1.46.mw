Last October we ran the [[unit tests for ImageJ1]] against [[2011-10-07 - Unit tests for ImageJ 1.45|various versions of ImageJ 1.45]]. It has been awhile since then, so here are the results with various versions of ImageJ 1.46.

Once again, an increasing number of tests are failing with each release, which indicates changing behavior creeping into the code.

[[Jenkins]] now [http://jenkins.imagej.net/job/ImageJ1-unit-tests/ runs these tests automatically] whenever a new version of [[ImageJ 1.x]] is released, and reports failures to the [[Mailing Lists|imagej-devel mailing list]], so that we become aware as early as possible when regression bugs have been introduced.

{| class="wikitable"
|-
! Version(s)
! Results
|-
| 1.45q
| ALL PASS
|-
|- 
| 1.45r
| 1 FAILURE:
# '''testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0'''
|- 
| 1.45s
| 3 FAILURES:
# '''testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;'''
# '''testGetFloatPolygon(ij.gui.RoiTest)'''
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0
|- 
| 1.46a
| 7 FAILURES:
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# '''testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;'''
# '''testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;'''
# '''testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;'''
# '''testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;'''
# testGetFloatPolygon(ij.gui.RoiTest)
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0

3 ERRORS:

# '''testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)'''
# '''testAddPointIntInt(ij.gui.PointRoiTest): 0'''
# '''testSubtractPointsRoi(ij.gui.PointRoiTest)'''
|- 
| 1.46b
| 9 FAILURES:
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;
# testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;
# testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;
# testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;
# '''testIsDrawingTool(ij.gui.RoiTest)'''
# testGetFloatPolygon(ij.gui.RoiTest)
# '''testSetRoundRectArcSize(ij.gui.RoiTest)'''
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0

3 ERRORS:

# testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)
# testAddPointIntInt(ij.gui.PointRoiTest): 0
# testSubtractPointsRoi(ij.gui.PointRoiTest)
|- 
| 1.46c
| DOES NOT COMPILE
|- 
| 1.46d
| 8 FAILURES:
# '''testSetChannelLutLUT(ij.CompositeImageTest)'''
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;
# testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;
# <s>testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;</s>
# <s>testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;</s>
# testIsDrawingTool(ij.gui.RoiTest)
# testGetFloatPolygon(ij.gui.RoiTest)
# testSetRoundRectArcSize(ij.gui.RoiTest)
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0

3 ERRORS:

# testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)
# testAddPointIntInt(ij.gui.PointRoiTest): 0
# testSubtractPointsRoi(ij.gui.PointRoiTest)
|- 
| 1.46e
| 9 FAILURES:
# testSetChannelLutLUT(ij.CompositeImageTest)
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;
# testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;
# testIsDrawingTool(ij.gui.RoiTest)
# testGetFloatPolygon(ij.gui.RoiTest)
# testSetRoundRectArcSize(ij.gui.RoiTest)
# '''testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;'''
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0

3 ERRORS:

# testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)
# testAddPointIntInt(ij.gui.PointRoiTest): 0
# testSubtractPointsRoi(ij.gui.PointRoiTest)
|- 
| 1.46f
| DOES NOT COMPILE
|- 
| 1.46g - 1.46h
| 21 FAILURES:
# testSetChannelLutLUT(ij.CompositeImageTest)
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;33&gt; but was:&lt;0&gt;
# testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;
# testIsDrawingTool(ij.gui.RoiTest)
# testGetFloatPolygon(ij.gui.RoiTest)
# testSetRoundRectArcSize(ij.gui.RoiTest)
# testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0
# '''testGetCValueInt(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;'''
# '''testGetCValueDouble(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;'''
# '''testConstants(ij.measure.CurveFitterTest): expected:&lt;y = a[*]x^b&gt; but was:&lt;y = a[]x^b&gt;'''
# '''testDoFitIntBoolean(ij.measure.CurveFitterTest): Assert.assertDoubleArraysEqual(double[],double[]) items differ at index 0: expected 2.0 and got 2.0011829468898386'''
# '''testFIntDoubleArrayDouble(ij.measure.CurveFitterTest)'''
# '''testGetResiduals(ij.measure.CurveFitterTest): expected:&lt;0.0&gt; but was:&lt;1.4006385803222656&gt;'''
# '''testGetSumResidualsSqr(ij.measure.CurveFitterTest): expected:&lt;1890.14122&gt; but was:&lt;26.43688259804273&gt;'''
# '''testGetSD(ij.measure.CurveFitterTest): expected:&lt;10.45104&gt; but was:&lt;10.444040599931316&gt;'''
# '''testGetRSquared(ij.measure.CurveFitterTest): expected:&lt;0.84155&gt; but was:&lt;0.9994373712474635&gt;'''
# '''testGetFitGoodness(ij.measure.CurveFitterTest): expected:&lt;-0.59996&gt; but was:&lt;0.9981068051417952&gt;'''
# '''testGetResultString(ij.measure.CurveFitterTest): expected:&lt;...d+(a-d)/(1+(x/c)^b)'''
# '''testGetFit(ij.measure.CurveFitterTest): expected:&lt;20&gt; but was:&lt;100&gt;'''

8 ERRORS:

# testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)
# testAddPointIntInt(ij.gui.PointRoiTest): 0
# testSubtractPointsRoi(ij.gui.PointRoiTest)
# '''testDoCustomFit(ij.measure.CurveFitterTest): 2'''
# '''testGetNumParams(ij.measure.CurveFitterTest): 3'''
# '''testFDoubleArrayDouble(ij.measure.CurveFitterTest): 2'''
# '''testGetName(ij.measure.CurveFitterTest): 2'''
# '''testGetFormula(ij.measure.CurveFitterTest): 2'''
|- 
| 1.46i
| 26 FAILURES:
# testSetChannelLutLUT(ij.CompositeImageTest)
# testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;
# testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;33&gt; but was:&lt;0&gt;
# testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;
# testIsDrawingTool(ij.gui.RoiTest)
# testGetFloatPolygon(ij.gui.RoiTest)
# testSetRoundRectArcSize(ij.gui.RoiTest)
# '''testIsLine(ij.gui.RoiTest)'''
# testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;
# testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0
# testGetCValueInt(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;
# testGetCValueDouble(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;
# testConstants(ij.measure.CurveFitterTest): expected:&lt;y = a[*]x^b&gt; but was:&lt;y = a[]x^b&gt;
# testDoFitIntBoolean(ij.measure.CurveFitterTest): Assert.assertDoubleArraysEqual(double[],double[]) items differ at index 0: expected 2.0 and got 2.0011829468898386
# testFIntDoubleArrayDouble(ij.measure.CurveFitterTest)
# testGetResiduals(ij.measure.CurveFitterTest): expected:&lt;0.0&gt; but was:&lt;1.4006385803222656&gt;
# testGetSumResidualsSqr(ij.measure.CurveFitterTest): expected:&lt;1890.14122&gt; but was:&lt;26.43688259804273&gt;
# testGetSD(ij.measure.CurveFitterTest): expected:&lt;10.45104&gt; but was:&lt;10.444040599931316&gt;
# testGetRSquared(ij.measure.CurveFitterTest): expected:&lt;0.84155&gt; but was:&lt;0.9994373712474635&gt;
# testGetFitGoodness(ij.measure.CurveFitterTest): expected:&lt;-0.59996&gt; but was:&lt;0.9981068051417952&gt;
# testGetResultString(ij.measure.CurveFitterTest): expected:&lt;...d+(a-d)/(1+(x/c)^b)
# testGetFit(ij.measure.CurveFitterTest): expected:&lt;20&gt; but was:&lt;100&gt;
# '''testGetfIntInt(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;'''
# '''testGetfInt(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;'''
# '''testSetfIntIntFloat(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;'''
# '''testSetfIntFloat(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;'''

8 ERRORS:

# testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)
# testAddPointIntInt(ij.gui.PointRoiTest): 0
# testSubtractPointsRoi(ij.gui.PointRoiTest)
# testDoCustomFit(ij.measure.CurveFitterTest): 2
# testGetNumParams(ij.measure.CurveFitterTest): 3
# testFDoubleArrayDouble(ij.measure.CurveFitterTest): 2
# testGetName(ij.measure.CurveFitterTest): 2
# testGetFormula(ij.measure.CurveFitterTest): 2
|}

[[Category:News]]
[[Category:ImageJ2]]
