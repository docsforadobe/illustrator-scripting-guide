.. _jsobjref/ExportOptionsFlash:

ExportOptionsFlash
################################################################################

``exportOptionsFlash``

**Description**

Options for exporting a document as a Macromedia® Flash® (SWF) file, used with the :ref:`jsobjref/Document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsFlash.artClipping:

ExportOptionsFlash.artClipping
********************************************************************************

``exportOptionsFlash.artClipping``

**Description**

How the art should be clipped during output. Default: ``ArtClippingOption.OUTPUTARTBOUNDS``.

**Type**

:ref:`jsobjref/scripting-constants.ArtClippingOption`

----

.. _jsobjref/ExportOptionsFlash.artboardRange:

ExportOptionsFlash.artboardRange
********************************************************************************

``exportOptionsFlash.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/ExportOptionsFlash.backgroundColor:

ExportOptionsFlash.backgroundColor
********************************************************************************

``exportOptionsFlash.backgroundColor``

**Description**

The background color of the exported Flash frames.

**Type**

:ref:`jsobjref/RGBColor`

----

.. _jsobjref/ExportOptionsFlash.backgroundLayers:

ExportOptionsFlash.backgroundLayers
********************************************************************************

``exportOptionsFlash.backgroundLayers``

**Description**

A list of layers to be included as the static background of the exported Flash frames.

**Type**

Array of :ref:`jsobjref/Layers`

----

.. _jsobjref/ExportOptionsFlash.blendAnimation:

ExportOptionsFlash.blendAnimation
********************************************************************************

``exportOptionsFlash.blendAnimation``

**Description**

The animation type for blended objects. Default: ``BlendAnimationType.NOBLENDANIMATION``.

**Type**

:ref:`jsobjref/scripting-constants.BlendAnimationType`

----

.. _jsobjref/ExportOptionsFlash.compressed:

ExportOptionsFlash.compressed
********************************************************************************

``exportOptionsFlash.compressed``

**Description**

If ``true``, the exported file should be exported compressed. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.convertTextToOutlines:

ExportOptionsFlash.convertTextToOutlines
********************************************************************************

``exportOptionsFlash.convertTextToOutlines``

**Description**

If ``true``, all text is converted to vector paths; preserves the visual appearance of type in all Flash players. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.curveQuality:

ExportOptionsFlash.curveQuality
********************************************************************************

``exportOptionsFlash.curveQuality``

**Description**

The amount of curve information that should be presented. Default: 7.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsFlash.exportAllSymbols:

ExportOptionsFlash.exportAllSymbols
********************************************************************************

``exportOptionsFlash.exportAllSymbols``

**Description**

If ``true``, export all symbols defined in the palette. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.exportStyle:

ExportOptionsFlash.exportStyle
********************************************************************************

``exportOptionsFlash.exportStyle``

**Description**

The style in which the exported data should be created in Flash. Default: ``FlashExportStyle.ASFLASHFILE``.

**Type**

:ref:`jsobjref/scripting-constants.FlashExportStyle`

----

.. _jsobjref/ExportOptionsFlash.exportVersion:

ExportOptionsFlash.exportVersion
********************************************************************************

``exportOptionsFlash.exportVersion``

**Description**

The version of the exported SWF file. Default: ``FlashExportVersion.FlashVersion9``.

**Type**

:ref:`jsobjref/scripting-constants.FlashExportVersion`

----

.. _jsobjref/ExportOptionsFlash.frameRate:

ExportOptionsFlash.frameRate
********************************************************************************

``exportOptionsFlash.frameRate``

**Description**

The display rate in frames per second. Range: 0.01–120.0. Default: 12.0.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsFlash.ignoreTextKerning:

ExportOptionsFlash.ignoreTextKerning
********************************************************************************

``exportOptionsFlash.ignoreTextKerning``

**Description**

If ``true``, ignore kerning information in text objects. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.imageFormat:

ExportOptionsFlash.imageFormat
********************************************************************************

``exportOptionsFlash.imageFormat``

**Description**

How should the image in the exported Flash file be compressed. Default: ``FlashImageFormat.LOSSLESS``.

**Type**

:ref:`jsobjref/scripting-constants.FlashImageFormat`

----

.. _jsobjref/ExportOptionsFlash.includeMetadata:

ExportOptionsFlash.includeMetadata
********************************************************************************

``exportOptionsFlash.includeMetadata``

**Description**

If ``true``, include minimal XMP metadata in the SWF file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.jpegMethod:

ExportOptionsFlash.jpegMethod
********************************************************************************

``exportOptionsFlash.jpegMethod``

**Description**

Specifies the JPEG method to use. Default: ``FlashJPEGMethod.Standard``.

**Type**

:ref:`jsobjref/scripting-constants.FlashJPEGMethod`

----

.. _jsobjref/ExportOptionsFlash.jpegQuality:

ExportOptionsFlash.jpegQuality
********************************************************************************

``exportOptionsFlash.jpegQuality``

**Description**

Level of compression to use. Range 1 to 10. Default: 3.

**Type**

Number (long).

----

.. _jsobjref/ExportOptionsFlash.layerOrder:

ExportOptionsFlash.layerOrder
********************************************************************************

``exportOptionsFlash.layerOrder``

**Description**

The order in which layers are exported to Flash frames. Default: ``LayerOrderType.BOTTOMUP``.

**Type**

:ref:`jsobjref/scripting-constants.LayerOrderType`

----

.. _jsobjref/ExportOptionsFlash.looping:

ExportOptionsFlash.looping
********************************************************************************

``exportOptionsFlash.looping``

**Description**

If ``true``, the Flash file is set to loop when run. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.playbackAccess:

ExportOptionsFlash.playbackAccess
********************************************************************************

``exportOptionsFlash.playbackAccess``

**Description**

The access level for the exported SWF file. Default: ``FlashPlaybackSecurity.PlaybackLocal``.

**Type**

:ref:`jsobjref/scripting-constants.FlashPlaybackSecurity`

----

.. _jsobjref/ExportOptionsFlash.preserveAppearance:

ExportOptionsFlash.preserveAppearance
********************************************************************************

``exportOptionsFlash.preserveAppearance``

**Description**

If ``true``, preserve appearance. If ``false``, preserve editability. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.readOnly:

ExportOptionsFlash.readOnly
********************************************************************************

``exportOptionsFlash.readOnly``

**Description**

If ``true``, export as read-only file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.replacing:

ExportOptionsFlash.replacing
********************************************************************************

``exportOptionsFlash.replacing``

**Description**

If a file with the same name already exists, should it be replaced. Default: ``SaveOptions.PROMPTTOSAVECHANGES``.

**Type**

:ref:`jsobjref/scripting-constants.SaveOptions`

----

.. _jsobjref/ExportOptionsFlash.resolution:

ExportOptionsFlash.resolution
********************************************************************************

``exportOptionsFlash.resolution``

**Description**

The resolution in pixels per inch. Range: 72–2400. Default: 72.

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsFlash.saveMultipleArtboards:

ExportOptionsFlash.saveMultipleArtboards
********************************************************************************

``exportOptionsFlash.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsFlash.typename:

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
