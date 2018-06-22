.. _jsobjref/ExportOptionsJPEG:

ExportOptionsJPEG
################################################################################

``exportOptionsJPEG``

**Description**

Options for exporting a document as a JPEG file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsJPEG.antiAliasing:

ExportOptionsJPEG.antiAliasing
********************************************************************************

``exportOptionsJPEG.antiAliasing``

**Description**

If ``true``, the exported image should be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsJPEG.artBoardClipping:

ExportOptionsJPEG.artBoardClipping
********************************************************************************

``exportOptionsJPEG.artBoardClipping``

**Description**

If ``true``, the exported image should be clipped to the art board.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsJPEG.blurAmount:

ExportOptionsJPEG.blurAmount
********************************************************************************

``exportOptionsJPEG.blurAmount``

**Description**

The amount of blur to apply to the exported image. Range: 0.0 to 2.0. Default: 0.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsJPEG.horizontalScale:

ExportOptionsJPEG.horizontalScale
********************************************************************************

``exportOptionsJPEG.horizontalScale``

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsJPEG.matte:

ExportOptionsJPEG.matte
********************************************************************************

``exportOptionsJPEG.matte``

**Description**

If ``true``, the art board should be matted with a color. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsJPEG.matteColor:

ExportOptionsJPEG.matteColor
********************************************************************************

``exportOptionsJPEG.matteColor``

**Description**

The color to use when matting the art board. Default: ``white``.

**Type**

:ref:`jsobjref/RGBColor`

----

.. _jsobjref/ExportOptionsJPEG.optimization:

ExportOptionsJPEG.optimization
********************************************************************************

``exportOptionsJPEG.optimization``

**Description**

If ``true``, the exported image should be optimized for web viewing. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsJPEG.qualitySetting:

ExportOptionsJPEG.qualitySetting
********************************************************************************

``exportOptionsJPEG.qualitySetting``

**Description**

The quality of the exported image. Range: 0 to 100. Default: 30.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsJPEG.saveAsHTML:

ExportOptionsJPEG.saveAsHTML
********************************************************************************

``exportOptionsJPEG.saveAsHTML``

**Description**

If ``true``, the exported image should be saved with an accompanying HTML file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsJPEG.typename:

ExportOptionsJPEG.typename
********************************************************************************

``exportOptionsJPEG.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/ExportOptionsJPEG.verticalScale:

ExportOptionsJPEG.verticalScale
********************************************************************************

``exportOptionsJPEG.verticalScale``

**Description**

The vertical scaling factor to apply to the exported image. Range: 0.0 to 776.19. Default: 100.0.

**Type**

Number (double)

----

=======
Example
=======

Exporting to JPEG format
********************************************************************************

::

    // Exports current document to dest as a JPEG file with specified options,
    // dest contains the full path including the file name

    function exportFileToJPEG (dest) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsJPEG();
            var type = ExportType.JPEG;
            var fileSpec = new File(dest);

            exportOptions.antiAliasing = false;
            exportOptions.qualitySetting = 70;

            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
