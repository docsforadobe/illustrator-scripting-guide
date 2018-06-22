.. _jsobjref/ExportOptionsPNG24:

ExportOptionsPNG24
################################################################################

``exportOptionsPNG24``

**Description**

Options for exporting a document as a 24-bit PNG file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsPNG24.antiAliasing:

ExportOptionsPNG24.antiAliasing
********************************************************************************

``exportOptionsPNG24.antiAliasing``

**Description**

If ``true``, the exported image be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG24.artBoardClipping:

ExportOptionsPNG24.artBoardClipping
********************************************************************************

``exportOptionsPNG24.artBoardClipping``

**Description**

If ``true``, the exported image be clipped to the art board. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG24.horizontalScale:

ExportOptionsPNG24.horizontalScale
********************************************************************************

``exportOptionsPNG24.horizontalScale``

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsPNG24.matte:

ExportOptionsPNG24.matte
********************************************************************************

``exportOptionsPNG24.matte``

**Description**

If ``true``, the art board be matted with a color. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG24.matteColor:

ExportOptionsPNG24.matteColor
********************************************************************************

``exportOptionsPNG24.matteColor``

**Description**

The color to use when matting the art board. Default: ``white``.

**Type**

:ref:`jsobjref/RGBColor`

----

.. _jsobjref/ExportOptionsPNG24.saveAsHTML:

ExportOptionsPNG24.saveAsHTML
********************************************************************************

``exportOptionsPNG24.saveAsHTML``

**Description**

If ``true``, the exported image be saved with an accompanying HTML file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG24.transparency:

ExportOptionsPNG24.transparency
********************************************************************************

``exportOptionsPNG24.transparency``

**Description**

If ``true``, the exported image use transparency. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsPNG24.typename:

ExportOptionsPNG24.typename
********************************************************************************

``exportOptionsPNG24.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/ExportOptionsPNG24.verticalScale:

ExportOptionsPNG24.verticalScale
********************************************************************************

``exportOptionsPNG24.verticalScale``

**Description**

The vertical scaling factor to apply to the exported image, where 100.0 is 100. Default: 100.0.

**Type**

Number (double).

----

=======
Example
=======

Exporting to PNG24 format
********************************************************************************

::

    // Exports current document to dest as a PNG24 file with specified options,
    // dest contains the full path including the file name,
    // saveAsHTML option creates an HTML version with the PNG file in an images folder

    function exportFileToPNG24 (dest) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsPNG24();
            var type = ExportType.PNG24;
            var fileSpec = new File(dest);

            exportOptions.antiAliasing = false;
            exportOptions.transparency = false;
            exportOptions.saveAsHTML = true;

            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
