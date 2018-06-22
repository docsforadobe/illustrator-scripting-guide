.. _jsobjref/exportOptionsFlash:

Export Options Flash
################################################################################

``exportOptionsFlash``

**Description**

Options for exporting a document as a Macromedia® Flash® (SWF) file, used with the :ref:`jsobjref/document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/exportOptionsFlash.artClipping:

ExportOptionsFlash.artClipping
********************************************************************************

``exportOptionsFlash.artClipping``

**Description**

How the art should be clipped during output. Default: ``ArtClippingOption.OUTPUTARTBOUNDS``.

**Type**

:ref:`jsobjref/scriptingConstants.artClippingOption`

----

.. _jsobjref/exportOptionsFlash.artboardRange:

ExportOptionsFlash.artboardRange
********************************************************************************

``exportOptionsFlash.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/exportOptionsFlash.backgroundColor:

ExportOptionsFlash.backgroundColor
********************************************************************************

``exportOptionsFlash.backgroundColor``

**Description**

The background color of the exported Flash frames.

**Type**

:ref:`jsobjref/rgbColor`

----

.. _jsobjref/exportOptionsFlash.backgroundLayers:

ExportOptionsFlash.backgroundLayers
********************************************************************************

``exportOptionsFlash.backgroundLayers``

**Description**

A list of layers to be included as the static background of the exported Flash frames.

**Type**

Array of :ref:`jsobjref/layers`

----

.. _jsobjref/exportOptionsFlash.blendAnimation:

ExportOptionsFlash.blendAnimation
********************************************************************************

``exportOptionsFlash.blendAnimation``

**Description**

The animation type for blended objects. Default: ``BlendAnimationType.NOBLENDANIMATION``.

**Type**

:ref:`jsobjref/scriptingConstants.blendAnimationType`

----

.. _jsobjref/exportOptionsFlash.compressed:

ExportOptionsFlash.compressed
********************************************************************************

``exportOptionsFlash.compressed``

**Description**

If ``true``, the exported file should be exported compressed. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.convertTextToOutlines:

ExportOptionsFlash.convertTextToOutlines
********************************************************************************

``exportOptionsFlash.convertTextToOutlines``

**Description**

If ``true``, all text is converted to vector paths; preserves the visual appearance of type in all Flash players. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.curveQuality:

ExportOptionsFlash.curveQuality
********************************************************************************

``exportOptionsFlash.curveQuality``

**Description**

The amount of curve information that should be presented. Default: 7.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsFlash.exportAllSymbols:

ExportOptionsFlash.exportAllSymbols
********************************************************************************

``exportOptionsFlash.exportAllSymbols``

**Description**

If ``true``, export all symbols defined in the palette. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.exportStyle:

ExportOptionsFlash.exportStyle
********************************************************************************

``exportOptionsFlash.exportStyle``

**Description**

The style in which the exported data should be created in Flash. Default: ``FlashExportStyle.ASFLASHFILE``.

**Type**

:ref:`jsobjref/scriptingConstants.FlashExportStyle`

----

.. _jsobjref/exportOptionsFlash.exportVersion:

ExportOptionsFlash.exportVersion
********************************************************************************

``exportOptionsFlash.exportVersion``

**Description**

The version of the exported SWF file. Default: ``FlashExportVersion.FlashVersion9``.

**Type**

:ref:`jsobjref/scriptingConstants.FlashExportVersion`

----

.. _jsobjref/exportOptionsFlash.frameRate:

ExportOptionsFlash.frameRate
********************************************************************************

``exportOptionsFlash.frameRate``

**Description**

The display rate in frames per second. Range: 0.01–120.0. Default: 12.0.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsFlash.ignoreTextKerning:

ExportOptionsFlash.ignoreTextKerning
********************************************************************************

``exportOptionsFlash.ignoreTextKerning``

**Description**

If ``true``, ignore kerning information in text objects. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.imageFormat:

ExportOptionsFlash.imageFormat
********************************************************************************

``exportOptionsFlash.imageFormat``

**Description**

How should the image in the exported Flash file be compressed. Default: ``FlashImageFormat.LOSSLESS``.

**Type**

:ref:`jsobjref/scriptingConstants.FlashImageFormat`

----

.. _jsobjref/exportOptionsFlash.includeMetadata:

ExportOptionsFlash.includeMetadata
********************************************************************************

``exportOptionsFlash.includeMetadata``

**Description**

If ``true``, include minimal XMP metadata in the SWF file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.jpegMethod:

ExportOptionsFlash.jpegMethod
********************************************************************************

``exportOptionsFlash.jpegMethod``

**Description**

Specifies the JPEG method to use. Default: ``FlashJPEGMethod.Standard``.

**Type**

:ref:`jsobjref/scriptingConstants.FlashJPEGMethod`

----

.. _jsobjref/exportOptionsFlash.jpegQuality:

ExportOptionsFlash.jpegQuality
********************************************************************************

``exportOptionsFlash.jpegQuality``

**Description**

Level of compression to use. Range 1 to 10. Default: 3.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsFlash.layerOrder:

ExportOptionsFlash.layerOrder
********************************************************************************

``exportOptionsFlash.layerOrder``

**Description**

The order in which layers are exported to Flash frames. Default: ``LayerOrderType.BOTTOMUP``.

**Type**

:ref:`jsobjref/scriptingConstants.LayerOrderType`

----

.. _jsobjref/exportOptionsFlash.looping:

ExportOptionsFlash.looping
********************************************************************************

``exportOptionsFlash.looping``

**Description**

If ``true``, the Flash file is set to loop when run. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.playbackAccess:

ExportOptionsFlash.playbackAccess
********************************************************************************

``exportOptionsFlash.playbackAccess``

**Description**

The access level for the exported SWF file. Default: ``FlashPlaybackSecurity.PlaybackLocal``.

**Type**

:ref:`jsobjref/scriptingConstants.FlashPlaybackSecurity`

----

.. _jsobjref/exportOptionsFlash.preserveAppearance:

ExportOptionsFlash.preserveAppearance
********************************************************************************

``exportOptionsFlash.preserveAppearance``

**Description**

If ``true``, preserve appearance. If ``false``, preserve editability. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.readOnly:

ExportOptionsFlash.readOnly
********************************************************************************

``exportOptionsFlash.readOnly``

**Description**

If ``true``, export as read-only file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.replacing:

ExportOptionsFlash.replacing
********************************************************************************

``exportOptionsFlash.replacing``

**Description**

If a file with the same name already exists, should it be replaced. Default: ``SaveOptions.PROMPTTOSAVECHANGES``.

**Type**

:ref:`jsobjref/scriptingConstants.saveOptions`

----

.. _jsobjref/exportOptionsFlash.resolution:

ExportOptionsFlash.resolution
********************************************************************************

``exportOptionsFlash.resolution``

**Description**

The resolution in pixels per inch. Range: 72–2400. Default: 72.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsFlash.saveMultipleArtboards:

ExportOptionsFlash.saveMultipleArtboards
********************************************************************************

``exportOptionsFlash.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.typename:

ExportOptionsFlash.typename
********************************************************************************

``exportOptionsFlash.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Example
=======

Exporting to Flash format
********************************************************************************

::

    // Exports current document to destFile as a flash file with specified options,
    // destFile contains the full path including the file name

    function exportToFlashFile(destFile) {
        if ( app.documents.length > 0 ) {
            var exportOptions = new ExportOptionsFlash();
            var type = ExportType.FLASH;
            var fileSpec = new File(destFile);

            exportOptions.resolution = 150;
            app.activeDocument.exportFile( fileSpec, type, exportOptions );
        }
    }
