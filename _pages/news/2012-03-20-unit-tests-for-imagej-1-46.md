---
title: 2012-03-20 - Unit tests for ImageJ 1.46
---

Last October we ran the [unit tests for ImageJ 1.x](/develop/ij1-unit-tests) against [various versions of ImageJ 1.45](/news/2011-10-07-unit-tests-for-imagej-1-45). It has been awhile since then, so here are the results with various versions of ImageJ 1.46.

Once again, an increasing number of tests are failing with each release, which indicates changing behavior creeping into the code.

[Jenkins](/develop/jenkins) now [runs these tests automatically](http://jenkins.imagej.net/job/ImageJ1-unit-tests/) whenever a new version of [ImageJ 1.x](/software/imagej) is released, and reports failures to the [imagej-devel mailing list](/discuss/mailing-lists), so that we become aware as early as possible when regression bugs have been introduced.

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th>
        <p>Version(s)</p>
      </th>
      <th>
        <p>Results</p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>1.45q</p>
      </td>
      <td>
        <p>ALL PASS</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>1.45r</p>
      </td>
      <td>
        <p>1 FAILURE:</p>
        <ol>
          <li><strong>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</strong></li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.45s</p>
      </td>
      <td>
        <p>3 FAILURES:</p>
        <ol>
          <li><strong>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</strong></li>
          <li><strong>testGetFloatPolygon(ij.gui.RoiTest)</strong></li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46a</p>
      </td>
      <td>
        <p>7 FAILURES:</p>
        <ol>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li><strong>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;</strong></li>
          <li><strong>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</strong></li>
          <li><strong>testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;</strong></li>
          <li><strong>testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;</strong></li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
        </ol>
        <p>3 ERRORS:</p>
        <ol>
          <li><strong>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</strong></li>
          <li><strong>testAddPointIntInt(ij.gui.PointRoiTest): 0</strong></li>
          <li><strong>testSubtractPointsRoi(ij.gui.PointRoiTest)</strong></li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46b</p>
      </td>
      <td>
        <p>9 FAILURES:</p>
        <ol>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;</li>
          <li>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</li>
          <li>testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;</li>
          <li>testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;</li>
          <li><strong>testIsDrawingTool(ij.gui.RoiTest)</strong></li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li><strong>testSetRoundRectArcSize(ij.gui.RoiTest)</strong></li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
        </ol>
        <p>3 ERRORS:</p>
        <ol>
          <li>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</li>
          <li>testAddPointIntInt(ij.gui.PointRoiTest): 0</li>
          <li>testSubtractPointsRoi(ij.gui.PointRoiTest)</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46c</p>
      </td>
      <td>
        <p>DOES NOT COMPILE</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46d</p>
      </td>
      <td>
        <p>8 FAILURES:</p>
        <ol>
          <li><strong>testSetChannelLutLUT(ij.CompositeImageTest)</strong></li>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;</li>
          <li>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</li>
          <li><s>testFitSplineInt(ij.gui.PolygonRoiTest): arrays first differed at element [3]; expected:&lt;1&gt; but was:&lt;0&gt;</s></li>
          <li><s>testGetXandYCoordinates(ij.gui.PolygonRoiTest): arrays first differed at element [1]; expected:&lt;1&gt; but was:&lt;0&gt;</s></li>
          <li>testIsDrawingTool(ij.gui.RoiTest)</li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li>testSetRoundRectArcSize(ij.gui.RoiTest)</li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
        </ol>
        <p>3 ERRORS:</p>
        <ol>
          <li>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</li>
          <li>testAddPointIntInt(ij.gui.PointRoiTest): 0</li>
          <li>testSubtractPointsRoi(ij.gui.PointRoiTest)</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46e</p>
      </td>
      <td>
        <p>9 FAILURES:</p>
        <ol>
          <li>testSetChannelLutLUT(ij.CompositeImageTest)</li>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;0&gt; but was:&lt;33&gt;</li>
          <li>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</li>
          <li>testIsDrawingTool(ij.gui.RoiTest)</li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li>testSetRoundRectArcSize(ij.gui.RoiTest)</li>
          <li><strong>testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;</strong></li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
        </ol>
        <p>3 ERRORS:</p>
        <ol>
          <li>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</li>
          <li>testAddPointIntInt(ij.gui.PointRoiTest): 0</li>
          <li>testSubtractPointsRoi(ij.gui.PointRoiTest)</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46f</p>
      </td>
      <td>
        <p>DOES NOT COMPILE</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46g - 1.46h</p>
      </td>
      <td>
        <p>21 FAILURES:</p>
        <ol>
          <li>testSetChannelLutLUT(ij.CompositeImageTest)</li>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;33&gt; but was:&lt;0&gt;</li>
          <li>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</li>
          <li>testIsDrawingTool(ij.gui.RoiTest)</li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li>testSetRoundRectArcSize(ij.gui.RoiTest)</li>
          <li>testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;</li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
          <li><strong>testGetCValueInt(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;</strong></li>
          <li><strong>testGetCValueDouble(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;</strong></li>
          <li><strong>testConstants(ij.measure.CurveFitterTest): expected:&lt;y = a[*]x^b&gt; but was:&lt;y = a[]x^b&gt;</strong></li>
          <li><strong>testDoFitIntBoolean(ij.measure.CurveFitterTest): Assert.assertDoubleArraysEqual(double[],double[]) items differ at index 0: expected 2.0 and got 2.0011829468898386</strong></li>
          <li><strong>testFIntDoubleArrayDouble(ij.measure.CurveFitterTest)</strong></li>
          <li><strong>testGetResiduals(ij.measure.CurveFitterTest): expected:&lt;0.0&gt; but was:&lt;1.4006385803222656&gt;</strong></li>
          <li><strong>testGetSumResidualsSqr(ij.measure.CurveFitterTest): expected:&lt;1890.14122&gt; but was:&lt;26.43688259804273&gt;</strong></li>
          <li><strong>testGetSD(ij.measure.CurveFitterTest): expected:&lt;10.45104&gt; but was:&lt;10.444040599931316&gt;</strong></li>
          <li><strong>testGetRSquared(ij.measure.CurveFitterTest): expected:&lt;0.84155&gt; but was:&lt;0.9994373712474635&gt;</strong></li>
          <li><strong>testGetFitGoodness(ij.measure.CurveFitterTest): expected:&lt;-0.59996&gt; but was:&lt;0.9981068051417952&gt;</strong></li>
          <li><strong>testGetResultString(ij.measure.CurveFitterTest): expected:&lt;...d+(a-d)/(1+(x/c)^b)</strong></li>
          <li><strong>testGetFit(ij.measure.CurveFitterTest): expected:&lt;20&gt; but was:&lt;100&gt;</strong></li>
        </ol>
        <p>8 ERRORS:</p>
        <ol>
          <li>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</li>
          <li>testAddPointIntInt(ij.gui.PointRoiTest): 0</li>
          <li>testSubtractPointsRoi(ij.gui.PointRoiTest)</li>
          <li><strong>testDoCustomFit(ij.measure.CurveFitterTest): 2</strong></li>
          <li><strong>testGetNumParams(ij.measure.CurveFitterTest): 3</strong></li>
          <li><strong>testFDoubleArrayDouble(ij.measure.CurveFitterTest): 2</strong></li>
          <li><strong>testGetName(ij.measure.CurveFitterTest): 2</strong></li>
          <li><strong>testGetFormula(ij.measure.CurveFitterTest): 2</strong></li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <p>1.46i</p>
      </td>
      <td>
        <p>26 FAILURES:</p>
        <ol>
          <li>testSetChannelLutLUT(ij.CompositeImageTest)</li>
          <li>testGetPolygon(ij.gui.LineTest): expected:&lt;1&gt; but was:&lt;2&gt;</li>
          <li>testDrawPixelsImageProcessor(ij.gui.PolygonRoiTest): expected:&lt;33&gt; but was:&lt;0&gt;</li>
          <li>testGetPolygon(ij.gui.PolygonRoiTest): expected:&lt;2&gt; but was:&lt;1&gt;</li>
          <li>testIsDrawingTool(ij.gui.RoiTest)</li>
          <li>testGetFloatPolygon(ij.gui.RoiTest)</li>
          <li>testSetRoundRectArcSize(ij.gui.RoiTest)</li>
          <li><strong>testIsLine(ij.gui.RoiTest)</strong></li>
          <li>testToString(ij.ImagePlusTest): expected:&lt;imp[Arckle [2x1x1]]&gt; but was:&lt;imp[Arckle [(2x1x1x1x1)]]&gt;</li>
          <li>testLzwUncompress(ij.io.ImageReaderTest): array lengths differed, expected.length=13 actual.length=0</li>
          <li>testGetCValueInt(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;</li>
          <li>testGetCValueDouble(ij.measure.CalibrationTest): expected:&lt;-12.815510557964274&gt; but was:&lt;NaN&gt;</li>
          <li>testConstants(ij.measure.CurveFitterTest): expected:&lt;y = a[*]x^b&gt; but was:&lt;y = a[]x^b&gt;</li>
          <li>testDoFitIntBoolean(ij.measure.CurveFitterTest): Assert.assertDoubleArraysEqual(double[],double[]) items differ at index 0: expected 2.0 and got 2.0011829468898386</li>
          <li>testFIntDoubleArrayDouble(ij.measure.CurveFitterTest)</li>
          <li>testGetResiduals(ij.measure.CurveFitterTest): expected:&lt;0.0&gt; but was:&lt;1.4006385803222656&gt;</li>
          <li>testGetSumResidualsSqr(ij.measure.CurveFitterTest): expected:&lt;1890.14122&gt; but was:&lt;26.43688259804273&gt;</li>
          <li>testGetSD(ij.measure.CurveFitterTest): expected:&lt;10.45104&gt; but was:&lt;10.444040599931316&gt;</li>
          <li>testGetRSquared(ij.measure.CurveFitterTest): expected:&lt;0.84155&gt; but was:&lt;0.9994373712474635&gt;</li>
          <li>testGetFitGoodness(ij.measure.CurveFitterTest): expected:&lt;-0.59996&gt; but was:&lt;0.9981068051417952&gt;</li>
          <li>testGetResultString(ij.measure.CurveFitterTest): expected:&lt;...d+(a-d)/(1+(x/c)^b)</li>
          <li>testGetFit(ij.measure.CurveFitterTest): expected:&lt;20&gt; but was:&lt;100&gt;</li>
          <li><strong>testGetfIntInt(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;</strong></li>
          <li><strong>testGetfInt(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;</strong></li>
          <li><strong>testSetfIntIntFloat(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;</strong></li>
          <li><strong>testSetfIntFloat(ij.process.ColorProcessorTest): expected:&lt;33.0&gt; but was:&lt;99.0&gt;</strong></li>
        </ol>
        <p>8 ERRORS:</p>
        <ol>
          <li>testPointRoiIntArrayIntArrayInt(ij.gui.PointRoiTest)</li>
          <li>testAddPointIntInt(ij.gui.PointRoiTest): 0</li>
          <li>testSubtractPointsRoi(ij.gui.PointRoiTest)</li>
          <li>testDoCustomFit(ij.measure.CurveFitterTest): 2</li>
          <li>testGetNumParams(ij.measure.CurveFitterTest): 3</li>
          <li>testFDoubleArrayDouble(ij.measure.CurveFitterTest): 2</li>
          <li>testGetName(ij.measure.CurveFitterTest): 2</li>
          <li>testGetFormula(ij.measure.CurveFitterTest): 2</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>
{:/}

 
