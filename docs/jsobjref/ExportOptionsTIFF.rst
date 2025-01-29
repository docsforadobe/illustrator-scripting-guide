.. _jsobjref/ExportOptionsTIFF:

ExportOptionsTIFF
################################################################################

``exportOptionsTIFF``

**Description**

Options for exporting a document as a TIFF file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsTIFF.antiAliasing:

ExportOptionsTIFF.antiAliasing
********************************************************************************

``exportOptionsTIFF.antiAliasing``

**Description**

If ``true``, the exported image should be anti-aliased. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsTIFF.artboardRange:

ExportOptionsTIFF.artboardRange
********************************************************************************

``exportOptionsTIFF.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/ExportOptionsTIFF.byteOrder:

ExportOptionsTIFF.byteOrder
********************************************************************************

``exportOptionsTIFF.byteOrder``

**Description**

The byte order to use in the new file.

**Type**

:ref:`jsobjref/scripting-constants.TIFFByteOrder`

----

.. _jsobjref/ExportOptionsTIFF.imageColorSpace:

ExportOptionsTIFF.imageColorSpace
********************************************************************************

``exportOptionsTIFF.imageColorSpace``

**Description**

The color space of the exported file. Default: ``ImageColorSpace.RGB``.

**Type**

:ref:`jsobjref/scripting-constants.ImageColorSpace`

----

.. _jsobjref/ExportOptionsTIFF.lZWCompression:

ExportOptionsTIFF.lZWCompression
********************************************************************************

``exportOptionsTIFF.lZWCompression``

.. note::
   This property was erroneously written as "IZWCompression" (with a capital "I"), as opposed to "lzwCompression" (with a lowercase "L"). Note that the latter is correct, and this doc has been updated to reflect this.

**Description**

If ``true``, use IZW compression in the new file.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsTIFF.resolution:

ExportOptionsTIFF.resolution
********************************************************************************

``exportOptionsTIFF.resolution``

**Description**

Resolution of the exported file in dots per inch (dpi). Range: 72.0 to 2400.0. Default: 150.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsTIFF.saveMultipleArtboards:

ExportOptionsTIFF.saveMultipleArtboards
********************************************************************************

``exportOptionsTIFF.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Number (double).

----

=======
Example
=======

Exporting to TIFF format
********************************************************************************

::

  // Exports current document to dest as a TIFF file with specified options,
  // dest contains the full path including the file name

  function exportFileToPSD(dest) {
    if (app.documents.length > 0) {
      var exportOptions = new ExportOptionsTIFF();
      exportOptions.resolution = 150;
      exportOptions.byteOrder = TIFFByteOrder.IBMPC;
      exportOptions.lZWCompression = false;

      var type = ExportType.TIFF;
      var fileSpec = new File(dest);

      app.activeDocument.exportFile(fileSpec, type, exportOptions);
    }
  }
