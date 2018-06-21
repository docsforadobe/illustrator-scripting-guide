.. _jsobjref/epsSaveOptions:

EPS Save Options
################################################################################

``epsSaveOptions``

**Description**

Options for saving a document as an Illustrator EPS file, used with the :ref:`jsobjref/document.saveAs` method.

All properties are optional.

----

==========
Properties
==========

.. _jsobjref/epsSaveOptions.artboardRange:

epsSaveOptions.artboardRange
********************************************************************************

``epsSaveOptions.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty string

**Type**

String.

----

.. _jsobjref/epsSaveOptions.cmykPostScript:

epsSaveOptions.cmykPostScript
********************************************************************************

``epsSaveOptions.cmykPostScript``

**Description**

If ``true``, use CMYK PostScript.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.compatibility:

epsSaveOptions.compatibility
********************************************************************************

``epsSaveOptions.compatibility``

**Description**

Specifies the version of the EPS file format to save.

Default: ``Compatibility.ILLUSTRATOR1719``.

**Type**

:ref:`jsobjref/scriptingConstants.compatibility`

----

.. _jsobjref/epsSaveOptions.compatibleGradientPrinting:

epsSaveOptions.compatibleGradientPrinting
********************************************************************************

``epsSaveOptions.compatibleGradientPrinting``

**Description**

If ``true``, create a raster item of the gradient or gradient mesh so that PostScript Level 2 printers can print the object.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.embedAllFonts:

epsSaveOptions.embedAllFonts
********************************************************************************

``epsSaveOptions.embedAllFonts``

**Description**

If ``true``, all fonts used by the document should be embedded in the saved file (version 7 or later).

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.embedLinkedFiles:

epsSaveOptions.embedLinkedFiles
********************************************************************************

``epsSaveOptions.embedLinkedFiles``

**Description**

If ``true``, linked image files are to be included in the saved document.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.flattenOuput:

epsSaveOptions.flattenOuput
********************************************************************************

``epsSaveOptions.flattenOuput``

**Description**

How should transparency be flattened for file formats older than Illustrator 9.

**Type**

:ref:`jsobjref/scriptingConstants.outputFlattening`

----

.. _jsobjref/epsSaveOptions.includeDocumentThumbnails:

epsSaveOptions.includeDocumentThumbnails
********************************************************************************

``epsSaveOptions.includeDocumentThumbnails``

**Description**

If ``true``, thumbnail image of the EPS artwork should be included.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.overprint:

epsSaveOptions.overprint
********************************************************************************

``epsSaveOptions.overprint``

**Description**

Whether to preserve, discard, or simulate the overprint.

Default: ``PDFOverprint.PRESERVEPDFOVERPRINT``.

**Type**

:ref:`jsobjref/scriptingConstants.pdfOverprint`

----

.. _jsobjref/epsSaveOptions.postScript:

epsSaveOptions.postScript
********************************************************************************

``epsSaveOptions.postScript``

**Description**

PostScript Language Level to use (Level 1 valid for file format version 8 or older).

Default: ``EPSPostScriptLevelEnum.LEVEL2``.

**Type**

:ref:`jsobjref/scriptingConstants.epsPostScriptLevelEnum`

----

.. _jsobjref/epsSaveOptions.preview:

epsSaveOptions.preview
********************************************************************************

``epsSaveOptions.preview``

**Description**

The format for the EPS preview image.

**Type**

:ref:`jsobjref/scriptingConstants.epsPreview`

----

.. _jsobjref/epsSaveOptions.saveMultipleArtboards:

epsSaveOptions.saveMultipleArtboards
********************************************************************************

``epsSaveOptions.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/epsSaveOptions.typename:

epsSaveOptions.typename
********************************************************************************

``epsSaveOptions.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Example
=======

Exporting to EPS format
********************************************************************************

::

    // Exports current document to destFile as an EPS file with specified options,
    // destFile contains the full path including the file name

    function exportFileAsEPS (destFile) {
        var newFile = new File(destFile);
        var saveDoc;
        if ( app.documents.length == 0 ) {
            saveDoc = app.documents.add();
        } else {
            saveDoc = app.activeDocument;
        }

        var saveOpts = new ePSSaveOptions();
        saveOpts.cmykPostScript = true;
        saveOpts.embedAllFonts = true;
        saveDoc.saveAs( newFile, saveOpts );
    }
