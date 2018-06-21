.. _jsobjref/exportOptionsFlash:

Export Options Flash
################################################################################

``exportOptionsFlash``

**Description**

Options for exporting a document as a Macromedia® Flash® (SWF) file, used with the :ref:`document.exportFile` method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

----

==========
Properties
==========

.. _jsobjref/exportOptionsFlash.artClipping:

exportOptionsFlash.artClipping
********************************************************************************

``exportOptionsFlash.artClipping``

**Description**

How the art should be clipped during output. Default: ``ArtClippingOption.OUTPUTARTBOUNDS``.

**Type**

:ref:`jsobjref/scriptingConstants.artClippingOption`

----

.. _jsobjref/exportOptionsFlash.artboardRange:

exportOptionsFlash.artboardRange
********************************************************************************

``exportOptionsFlash.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/exportOptionsFlash.backgroundColor:

exportOptionsFlash.backgroundColor
********************************************************************************

``exportOptionsFlash.backgroundColor``

**Description**

The background color of the exported Flash frames.

**Type**

:ref:`jsobjref/rgbColor`

----

.. _jsobjref/exportOptionsFlash.backgroundLayers:

exportOptionsFlash.backgroundLayers
********************************************************************************

``exportOptionsFlash.backgroundLayers``

**Description**

A list of layers to be included as the static background of the exported Flash frames.

**Type**

Array of :ref:`jsobjref/layers`

----

.. _jsobjref/exportOptionsFlash.blendAnimation:

exportOptionsFlash.blendAnimation
********************************************************************************

``exportOptionsFlash.blendAnimation``

**Description**

The animation type for blended objects. Default: ``BlendAnimationType.NOBLENDANIMATION``.

**Type**

:ref:`jsobjref/scriptingConstants.blendAnimationType`

----

.. _jsobjref/exportOptionsFlash.compressed:

exportOptionsFlash.compressed
********************************************************************************

``exportOptionsFlash.compressed``

**Description**

If ``true``, the exported file should be exported compressed. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.convertTextToOutlines:

exportOptionsFlash.convertTextToOutlines
********************************************************************************

``exportOptionsFlash.convertTextToOutlines``

**Description**

If ``true``, all text is converted to vector paths; preserves the visual appearance of type in all Flash players. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.curveQuality:

exportOptionsFlash.curveQuality
********************************************************************************

``exportOptionsFlash.curveQuality``

**Description**

The amount of curve information that should be presented. Default: 7.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsFlash.exportAllSymbols:

exportOptionsFlash.exportAllSymbols
********************************************************************************

``exportOptionsFlash.exportAllSymbols``

**Description**

If ``true``, export all symbols defined in the palette. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.exportStyle:

exportOptionsFlash.exportStyle
********************************************************************************

``exportOptionsFlash.exportStyle``

**Description**

The style in which the exported data should be created in Flash. Default: ``FlashExportStyle.ASFLASHFILE``.

**Type**

:ref:`jsobjref/scriptingConstants.flashExportStyle`

----

.. _jsobjref/exportOptionsFlash.exportVersion:

exportOptionsFlash.exportVersion
********************************************************************************

``exportOptionsFlash.exportVersion``

**Description**

The version of the exported SWF file. Default: ``FlashExportVersion.FlashVersion9``.

**Type**

:ref:`jsobjref/scriptingConstants.flashExportVersion`

----

.. _jsobjref/exportOptionsFlash.frameRate:

exportOptionsFlash.frameRate
********************************************************************************

``exportOptionsFlash.frameRate``

**Description**

The display rate in frames per second. Range: 0.01–120.0. Default: 12.0.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsFlash.ignoreTextKerning:

exportOptionsFlash.ignoreTextKerning
********************************************************************************

``exportOptionsFlash.ignoreTextKerning``

**Description**

If ``true``, ignore kerning information in text objects. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.imageFormat:

exportOptionsFlash.imageFormat
********************************************************************************

``exportOptionsFlash.imageFormat``

**Description**

How should the image in the exported Flash file be compressed. Default: ``FlashImageFormat.LOSSLESS``.

**Type**

:ref:`jsobjref/scriptingConstants.flashImageFormat`

----

.. _jsobjref/exportOptionsFlash.includeMetadata:

exportOptionsFlash.includeMetadata
********************************************************************************

``exportOptionsFlash.includeMetadata``

**Description**

If ``true``, include minimal XMP metadata in the SWF file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.jpegMethod:

exportOptionsFlash.jpegMethod
********************************************************************************

``exportOptionsFlash.jpegMethod``

**Description**

Specifies the JPEG method to use. Default: ``FlashJPEGMethod.Standard``.

**Type**

:ref:`jsobjref/scriptingConstants.flashJPEGMethod`

----

.. _jsobjref/exportOptionsFlash.jpegQuality:

exportOptionsFlash.jpegQuality
********************************************************************************

``exportOptionsFlash.jpegQuality``

**Description**

Level of compression to use. Range 1 to 10. Default: 3.

**Type**

Number (long).

----

.. _jsobjref/exportOptionsFlash.layerOrder:

exportOptionsFlash.layerOrder
********************************************************************************

``exportOptionsFlash.layerOrder``

**Description**

The order in which layers are exported to Flash frames. Default: ``LayerOrderType.BOTTOMUP``.

**Type**

:ref:`jsobjref/scriptingConstants.layerOrderType`

----

.. _jsobjref/exportOptionsFlash.looping:

exportOptionsFlash.looping
********************************************************************************

``exportOptionsFlash.looping``

**Description**

If ``true``, the Flash file is set to loop when run. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.playbackAccess:

exportOptionsFlash.playbackAccess
********************************************************************************

``exportOptionsFlash.playbackAccess``

**Description**

The access level for the exported SWF file. Default: ``FlashPlaybackSecurity.PlaybackLocal``.

**Type**

:ref:`jsobjref/scriptingConstants.flashPlaybackSecurity`

----

.. _jsobjref/exportOptionsFlash.preserveAppearance:

exportOptionsFlash.preserveAppearance
********************************************************************************

``exportOptionsFlash.preserveAppearance``

**Description**

If ``true``, preserve appearance. If ``false``, preserve editability. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.readOnly:

exportOptionsFlash.readOnly
********************************************************************************

``exportOptionsFlash.readOnly``

**Description**

If ``true``, export as read-only file. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.replacing:

exportOptionsFlash.replacing
********************************************************************************

``exportOptionsFlash.replacing``

**Description**

If a file with the same name already exists, should it be replaced. Default: ``SaveOptions.PROMPTTOSAVECHANGES``.

**Type**

:ref:`jsobjref/scriptingConstants.saveOptions`

----

.. _jsobjref/exportOptionsFlash.resolution:

exportOptionsFlash.resolution
********************************************************************************

``exportOptionsFlash.resolution``

**Description**

The resolution in pixels per inch. Range: 72–2400. Default: 72.

**Type**

Number (double).

----

.. _jsobjref/exportOptionsFlash.saveMultipleArtboards:

exportOptionsFlash.saveMultipleArtboards
********************************************************************************

``exportOptionsFlash.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsFlash.typename:

exportOptionsFlash.typename
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