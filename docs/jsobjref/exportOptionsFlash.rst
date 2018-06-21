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

.. _exportOptionsFlash.artClipping:

exportOptionsFlash.artClipping
********************************************************************************

``exportOptionsFlash.artClipping``

**Description**

How the art should be clipped during output. Default: ``ArtClippingOption.OUTPUTARTBOUNDS``.

**Type**

// todo: link to **ArtClippingOption** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsFlash.artboardRange:

exportOptionsFlash.artboardRange
********************************************************************************

``exportOptionsFlash.artboardRange``

**Description**

If ``saveMultipleArtboards`` is ``true``, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _exportOptionsFlash.backgroundColor:

exportOptionsFlash.backgroundColor
********************************************************************************

``exportOptionsFlash.backgroundColor``

**Description**

The background color of the exported Flash frames.

**Type**

:ref:`jsobjref/rgbColor`

----

.. _exportOptionsFlash.backgroundLayers:

exportOptionsFlash.backgroundLayers
********************************************************************************

``exportOptionsFlash.backgroundLayers``

**Description**

A list of layers to be included as the static background of the exported Flash frames.

**Type**

Array of :ref:`jsobjref/layers`

----

.. _exportOptionsFlash.blendAnimation:

exportOptionsFlash.blendAnimation
********************************************************************************

``exportOptionsFlash.blendAnimation``

**Description**

The animation type for blended objects. Default: ``BlendAnimationType.NOBLENDANIMATION``.

**Type**

// todo: link to **BlendAnimationType** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsFlash.compressed:

exportOptionsFlash.compressed
********************************************************************************

``exportOptionsFlash.compressed``

**Description**

If ``true``, the exported file should be exported compressed. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsFlash.convertTextToOutlines:

exportOptionsFlash.convertTextToOutlines
********************************************************************************

``exportOptionsFlash.convertTextToOutlines``

**Description**

If ``true``, all text is converted to vector paths; preserves the visual appearance of type in all Flash players. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsFlash.curveQuality:

exportOptionsFlash.curveQuality
********************************************************************************

``exportOptionsFlash.curveQuality``

**Description**

The amount of curve information that should be presented. Default: 7.

**Type**

Number (long).

----

.. _exportOptionsFlash.exportAllSymbols:

exportOptionsFlash.exportAllSymbols
********************************************************************************

``exportOptionsFlash.exportAllSymbols``

**Description**

If ``true``, export all symbols defined in the palette. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsFlash.exportStyle:

exportOptionsFlash.exportStyle
********************************************************************************

``exportOptionsFlash.exportStyle``

**Description**

The style in which the exported data should be created in Flash. Default: ``FlashExportStyle.ASFLASHFILE``.

**Type**

// todo: link to **FlashExportStyle** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsFlash.exportVersion:

exportOptionsFlash.exportVersion
********************************************************************************

``exportOptionsFlash.exportVersion``

**Description**

The version of the exported SWF file. Default: ``FlashExportVersion.FlashVersion9``.

**Type**

// todo: link to **FlashExportVersion** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsFlash.frameRate:

exportOptionsFlash.frameRate
********************************************************************************

``exportOptionsFlash.frameRate``

**Description**

The display rate in frames per second. Range: 0.01–120.0. Default: 12.0.

**Type**

Number (double).

----

.. _exportOptionsFlash.ignoreTextKerning:

exportOptionsFlash.ignoreTextKerning
********************************************************************************

``exportOptionsFlash.ignoreTextKerning``

**Description**

If true, ignore kerning information in text objects. Default: false

**Type**

Boolean.

----






=======
Methods
=======


----

=======
Example
=======


********************************************************************************

::

