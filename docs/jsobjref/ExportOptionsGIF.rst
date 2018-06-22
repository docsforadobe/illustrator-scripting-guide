.. _jsobjref/ExportOptionsGIF:

ExportOptionsGIF
################################################################################

``exportOptionsGIF``

**Description**

Options for exporting a document as a GIF file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsGIF.antiAliasing:

ExportOptionsGIF.antiAliasing
********************************************************************************

``exportOptionsGIF.antiAliasing``

**Description**

If ``true``, the exported image should be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.artBoardClipping:

ExportOptionsGIF.artBoardClipping
********************************************************************************

``exportOptionsGIF.artBoardClipping``

**Description**

If ``true``, the exported image should be clipped to the art board. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.colorCount:

ExportOptionsGIF.colorCount
********************************************************************************

``exportOptionsGIF.colorCount``

**Description**

The number of colors in the exported image’s color table. Range: 2 to 256. Default: 128.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsGIF.colorDither:

ExportOptionsGIF.colorDither
********************************************************************************

``exportOptionsGIF.colorDither``

**Description**

The method used to dither colors in the exported image. Default: ``ColorDitherMethod.DIFFUSION``.

**Type**

:ref:`jsobjref/scripting-constants.ColorDitherMethod`

----

.. _jsobjref/ExportOptionsGIF.colorReduction:

ExportOptionsGIF.colorReduction
********************************************************************************

``exportOptionsGIF.colorReduction``

**Description**

The method used to reduce the number of colors in the exported image. ``Default: ColorReductionMethod.SELECTIVE``.

**Type**

:ref:`jsobjref/scripting-constants.ColorReductionMethod`

----

.. _jsobjref/ExportOptionsGIF.ditherPercent:

ExportOptionsGIF.ditherPercent
********************************************************************************

``exportOptionsGIF.ditherPercent``

**Description**

How much should the colors of the exported image be dithered, where 100.0 is 100%.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsGIF.horizontalScale:

ExportOptionsGIF.horizontalScale
********************************************************************************

``exportOptionsGIF.horizontalScale``

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsGIF.infoLossPercent:

ExportOptionsGIF.infoLossPercent
********************************************************************************

``exportOptionsGIF.infoLossPercent``

**Description**

The level of information loss allowed during compression, where 100.0 is 100%.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsGIF.interlaced:

ExportOptionsGIF.interlaced
********************************************************************************

``exportOptionsGIF.interlaced``

**Description**

If ``true``, the exported image should be interlaced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.matte:

ExportOptionsGIF.matte
********************************************************************************

``exportOptionsGIF.matte``

**Description**

If ``true``, the art board should be matted with a color. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.matteColor:

ExportOptionsGIF.matteColor
********************************************************************************

``exportOptionsGIF.matteColor``

**Description**

The color to use when matting the art board. Default: ``WHITE``.

**Type**

:ref:`jsobjref/RGBColor`

----

.. _jsobjref/ExportOptionsGIF.saveAsHTML:

ExportOptionsGIF.saveAsHTML
********************************************************************************

``exportOptionsGIF.saveAsHTML``

**Description**

If ``true``, the exported image should be saved with an accompanying HTML file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.transparency:

ExportOptionsGIF.transparency
********************************************************************************

``exportOptionsGIF.transparency``

**Description**

If ``true``, the exported image should use transparency. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsGIF.typename:

ExportOptionsGIF.typename
********************************************************************************

``exportOptionsGIF.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/ExportOptionsGIF.verticalScale:

ExportOptionsGIF.verticalScale
********************************************************************************

``exportOptionsGIF.verticalScale``

**Description**

The vertical scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsGIF.webSnap:

ExportOptionsGIF.webSnap
********************************************************************************

``exportOptionsGIF.webSnap``

**Description**

Howmuchshouldthecolortablebechangedtomatch the web palette, where 100 is maximum. Default: 0.

**Type**

Number (long).

----

=======
Example
=======

Exporting to GIF format
********************************************************************************

::

    // Exports current document to dest as a GIF file with specified options,
    // dest contains the full path including the file name

    function exportToGIFFile(dest) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsGIF();
            var type = ExportType.GIF;
            var fileSpec = new File(dest);

            exportOptions.antiAliasing = false;
            exportOptions.colorCount = 64;
            exportOptions.colorDither = ColorDitherMethod.DIFFUSION;

            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
