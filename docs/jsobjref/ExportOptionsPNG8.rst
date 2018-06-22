.. _jsobjref/ExportOptionsPNG8:

ExportOptionsPNG8
################################################################################

``exportOptionsPNG8``

**Description**

Options for exporting a document as an 8-bit PNG file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsPNG8.antiAliasing:

ExportOptionsPNG8.antiAliasing
********************************************************************************

``exportOptionsPNG8.antiAliasing``

**Description**

If ``true``, the exported image should be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.artBoardClipping:

ExportOptionsPNG8.artBoardClipping
********************************************************************************

``exportOptionsPNG8.artBoardClipping``

**Description**

If ``true``, the exported image should be clipped to the art board. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.colorCount:

ExportOptionsPNG8.colorCount
********************************************************************************

``exportOptionsPNG8.colorCount``

**Description**

The number of colors in the exported image’s color table. Range: 2 to 256. Default: 128.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsPNG8.colorDither:

ExportOptionsPNG8.colorDither
********************************************************************************

``exportOptionsPNG8.colorDither``

**Description**

The method used to dither colors in the exported image. Default: ``ColorDitherMethod.Diffusion``.

**Type**

:ref:`jsobjref/scripting-constants.ColorDitherMethod`

----

.. _jsobjref/ExportOptionsPNG8.colorReduction:

ExportOptionsPNG8.colorReduction
********************************************************************************

``exportOptionsPNG8.colorReduction``

**Description**

The method used to reduce the number of colors in the exported image. Default: ``ColorReductionMethod.SELECTIVE``.

**Type**

:ref:`jsobjref/scripting-constants.ColorReductionMethod`

----

.. _jsobjref/ExportOptionsPNG8.ditherPercent:

ExportOptionsPNG8.ditherPercent
********************************************************************************

``exportOptionsPNG8.ditherPercent``

**Description**

The amount (as a percentage) that the colors of the exported image are dithered, where 100.0 is 100%. Range: 0 to 100. Default: 88.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsPNG8.horizontalScale:

ExportOptionsPNG8.horizontalScale
********************************************************************************

``exportOptionsPNG8.horizontalScale``

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsPNG8.interlaced:

ExportOptionsPNG8.interlaced
********************************************************************************

``exportOptionsPNG8.interlaced``

**Description**

If ``true``, the exported image should be interlaced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.matte:

ExportOptionsPNG8.matte
********************************************************************************

``exportOptionsPNG8.matte``

**Description**

If ``true``, the art board should be matted with a color. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.matteColor:

ExportOptionsPNG8.matteColor
********************************************************************************

``exportOptionsPNG8.matteColor``

**Description**

The color to use when matting the art board. Default: ``white``.

**Type**

:ref:`jsobjref/RGBColor`

----

.. _jsobjref/ExportOptionsPNG8.saveAsHTML:

ExportOptionsPNG8.saveAsHTML
********************************************************************************

``exportOptionsPNG8.saveAsHTML``

**Description**

If ``true``, the exported image be saved with an accompanying HTML file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.transparency:

ExportOptionsPNG8.transparency
********************************************************************************

``exportOptionsPNG8.transparency``

**Description**

If ``true``, the exported image use transparency. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG8.typename:

ExportOptionsPNG8.typename
********************************************************************************

``exportOptionsPNG8.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/ExportOptionsPNG8.verticalScale:

ExportOptionsPNG8.verticalScale
********************************************************************************

``exportOptionsPNG8.verticalScale``

**Description**

The vertical scaling factor to apply to the exported image, where 100.0 is 100. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsPNG8.webSnap:

ExportOptionsPNG8.webSnap
********************************************************************************

``exportOptionsPNG8.webSnap``

**Description**

Specifies how much the color table should be changed to match the web palette, where 100 is maximum. Default: 0.

**Type**

Number (long).

----

=======
Example
=======

Exporting to PNG8 format
********************************************************************************

::

    // Exports current document to dest as a PNG8 file with specified options,
    // dest contains the full path including the file name

    function exportFileToPNG8 (dest) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsPNG8();
            var type = ExportType.PNG8;
            var fileSpec = new File(dest);

            exportOptions.colorCount = 8;
            exportOptions.transparency = false;

            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
