.. _jsobjref/exportOptionsSVG:

Export Options SVG
################################################################################

``exportOptionsSVG``

**Description**

Options for exporting a document as a SVG file, used with the :ref:`jsobjref/document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/exportOptionsSVG.artboardRange:

ExportOptionsSVG.artboardRange
********************************************************************************

``exportOptionsSVG.artboardRange``

**Description**

A range of artboards to save, if ``saveMultipleArtboards`` is ``true``. A comma-delimited list of artboard names., or the empty string to save all artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/exportOptionsSVG.compressed:

ExportOptionsSVG.compressed
********************************************************************************

``exportOptionsSVG.compressed``

**Description**

If ``true``, the exported file should be compressed. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.coordinatePrecision:

ExportOptionsSVG.coordinatePrecision
********************************************************************************

``exportOptionsSVG.coordinatePrecision``

**Description**

The decimal precision for element coordinate values. Range: 1 to 7. Default: 3.

**Type**

Number (long)

----

.. _jsobjref/exportOptionsSVG.cssProperties:

ExportOptionsSVG.cssProperties
********************************************************************************

``exportOptionsSVG.cssProperties``

**Description**

How the CSS properties of the document should be included in the exported file. Default: ``SVGCSSPropertyLocation.STYLEATTRIBUTES``.

**Type**

:ref:`jsobjref/scriptingConstants.SVGCSSPropertyLocation`

----

.. _jsobjref/exportOptionsSVG.documentEncoding:

ExportOptionsSVG.documentEncoding
********************************************************************************

``exportOptionsSVG.documentEncoding``

**Description**

How the text in the document should be encoded. Default: ``SVGDocumentEncoding.ASCII``.

**Type**

:ref:`jsobjref/scriptingConstants.SVGDocumentEncoding`

----

.. _jsobjref/exportOptionsSVG.DTD:

ExportOptionsSVG.DTD
********************************************************************************

``exportOptionsSVG.DTD``

**Description**

The SVG version to which the file should conform. Default: ``SVGDTDVersion.SVG1_1``.

**Type**

:ref:`jsobjref/scriptingConstants.SVGDTDVersion`

----

.. _jsobjref/exportOptionsSVG.embedRasterImages:

ExportOptionsSVG.embedRasterImages
********************************************************************************

``exportOptionsSVG.embedRasterImages``

**Description**

If ``true``, the raster images contained in the document should be embedded in the exported file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.fontSubsetting:

ExportOptionsSVG.fontSubsetting
********************************************************************************

``exportOptionsSVG.fontSubsetting``

**Description**

Which font glyphs should be included in the exported file. Default: ``SVGFontSubsetting.ALLGLYPHS``.

**Type**

:ref:`jsobjref/scriptingConstants.SVGFontSubsetting`

----

.. _jsobjref/exportOptionsSVG.fontType:

ExportOptionsSVG.fontType
********************************************************************************

``exportOptionsSVG.fontType``

**Description**

The type of font to included in the exported file. Default: ``SVGFontType.CEFFONT``.

**Type**

:ref:`jsobjref/scriptingConstants.SVGFontType`

----

.. _jsobjref/exportOptionsSVG.includeFileInfo:

ExportOptionsSVG.includeFileInfo
********************************************************************************

``exportOptionsSVG.includeFileInfo``

**Description**

If ``true``, file information should be saved in the exported file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.includeUnusedStyles:

ExportOptionsSVG.includeUnusedStyles
********************************************************************************

``exportOptionsSVG.includeUnusedStyles``

**Description**

If ``true``, save unused styles in the exported file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.includeVariablesAndDatasets:

ExportOptionsSVG.includeVariablesAndDatasets
********************************************************************************

``exportOptionsSVG.includeVariablesAndDatasets``

**Description**

If ``true``, variables and datasets should be saved in the exported file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.optimizeForSVGViewer:

ExportOptionsSVG.optimizeForSVGViewer
********************************************************************************

``exportOptionsSVG.optimizeForSVGViewer``

**Description**

If ``true``, the exported file should be optimized for the SVG Viewer. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.preserveEditability:

ExportOptionsSVG.preserveEditability
********************************************************************************

``exportOptionsSVG.preserveEditability``

**Description**

If ``true``, Illustrator editing capabilities should be preserved when exporting the document. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.saveMultipleArtboards:

ExportOptionsSVG.saveMultipleArtboards
********************************************************************************

``exportOptionsSVG.saveMultipleArtboards``

**Description**

If ``true``, save the artboards specified by artboardRange in the exported file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.slices:

ExportOptionsSVG.slices
********************************************************************************

``exportOptionsSVG.slices``

**Description**

If ``true``, slice data should be exported with the file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.sVGAutoKerning:

ExportOptionsSVG.sVGAutoKerning
********************************************************************************

``exportOptionsSVG.sVGAutoKerning``

**Description**

If ``true``, SVG automatic kerning is allowed in the file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.sVGTextOnPath:

ExportOptionsSVG.sVGTextOnPath
********************************************************************************

``exportOptionsSVG.sVGTextOnPath``

**Description**

If ``true``, the SVG text-on-path construct is allowed in the file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsSVG.typename:

ExportOptionsSVG.typename
********************************************************************************

``exportOptionsSVG.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Example
=======

Exporting to SVG format
********************************************************************************

::

    // Exports current document to dest as an SVG file with specified options,
    // dest contains the full path including the file name

    function exportFileToSVG (dest) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsSVG();
            var type = ExportType.SVG;
            var fileSpec = new File(dest);

            exportOptions.embedRasterImages = true;
            exportOptions.embedAllFonts = false;
            exportOptions.fontSubsetting = SVGFontSubsetting.GLYPHSUSED;

            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
