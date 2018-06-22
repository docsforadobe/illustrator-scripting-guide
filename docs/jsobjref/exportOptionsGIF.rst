.. _jsobjref/exportOptionsGIF:

Export Options GIF
################################################################################

``exportOptionsGIF``

**Description**

Options for exporting a document as a GIF file, used with the :ref:`jsobjref/document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/exportOptionsGIF.antiAliasing:

exportOptionsGIF.antiAliasing
********************************************************************************

``exportOptionsGIF.antiAliasing``

**Description**

If ``true``, the exported image should be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.artBoardClipping:

exportOptionsGIF.artBoardClipping
********************************************************************************

``exportOptionsGIF.artBoardClipping``

**Description**

If ``true``, the exported image should be clipped to the art board. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.colorCount:

exportOptionsGIF.colorCount
********************************************************************************

``exportOptionsGIF.colorCount``

**Description**

The number of colors in the exported image’s color table. Range: 2 to 256. Default: 128.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsGIF.colorDither:

exportOptionsGIF.colorDither
********************************************************************************

``exportOptionsGIF.colorDither``

**Description**

The method used to dither colors in the exported image. Default: ``ColorDitherMethod.DIFFUSION``.

**Type**

:ref:`jsobjref/scriptingConstants.colorDitherMethod`

----

.. _jsobjref/exportOptionsGIF.colorReduction:

exportOptionsGIF.colorReduction
********************************************************************************

``exportOptionsGIF.colorReduction``

**Description**

The method used to reduce the number of colors in the exported image. ``Default: ColorReductionMethod.SELECTIVE``.

**Type**

:ref:`jsobjref/scriptingConstants.colorReductionMethod`

----

.. _jsobjref/exportOptionsGIF.ditherPercent:

exportOptionsGIF.ditherPercent
********************************************************************************

``exportOptionsGIF.ditherPercent``

**Description**

How much should the colors of the exported image be dithered, where 100.0 is 100%.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsGIF.horizontalScale:

exportOptionsGIF.horizontalScale
********************************************************************************

``exportOptionsGIF.horizontalScale``

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsGIF.infoLossPercent:

exportOptionsGIF.infoLossPercent
********************************************************************************

``exportOptionsGIF.infoLossPercent``

**Description**

The level of information loss allowed during compression, where 100.0 is 100%.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsGIF.interlaced:

exportOptionsGIF.interlaced
********************************************************************************

``exportOptionsGIF.interlaced``

**Description**

If ``true``, the exported image should be interlaced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.matte:

exportOptionsGIF.matte
********************************************************************************

``exportOptionsGIF.matte``

**Description**

If ``true``, the art board should be matted with a color. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.matteColor:

exportOptionsGIF.matteColor
********************************************************************************

``exportOptionsGIF.matteColor``

**Description**

The color to use when matting the art board. Default: ``WHITE``.

**Type**

// todo: add link to **RGBColor** page.

----

.. _jsobjref/exportOptionsGIF.saveAsHTML:

exportOptionsGIF.saveAsHTML
********************************************************************************

``exportOptionsGIF.saveAsHTML``

**Description**

If ``true``, the exported image should be saved with an accompanying HTML file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.transparency:

exportOptionsGIF.transparency
********************************************************************************

``exportOptionsGIF.transparency``

**Description**

If ``true``, the exported image should use transparency. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsGIF.typename:

exportOptionsGIF.typename
********************************************************************************

``exportOptionsGIF.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/exportOptionsGIF.verticalScale:

exportOptionsGIF.verticalScale
********************************************************************************

``exportOptionsGIF.verticalScale``

**Description**

The vertical scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsGIF.webSnap:

exportOptionsGIF.webSnap
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