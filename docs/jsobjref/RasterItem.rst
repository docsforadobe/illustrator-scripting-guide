.. _jsobjref/RasterItem:

RasterItem
################################################################################

``app.activeDocument.rasterItems[index]``

**Description**

A bitmap art item in a document. A script can create a raster item from an external file, or by copying an existing raster item with the ``duplicate`` method.

----

==========
Properties
==========

.. _jsobjref/RasterItem.artworkKnockout:

RasterItem.artworkKnockout
********************************************************************************

``app.activeDocument.rasterItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/RasterItem.bitsPerChannel:

RasterItem.bitsPerChannel
********************************************************************************

``app.activeDocument.rasterItems[index].bitsPerChannel``

**Description**

The number of bits per channel.

**Type**

Number (long); read-only.

----

.. _jsobjref/RasterItem.blendingMode:

RasterItem.blendingMode
********************************************************************************

``app.activeDocument.rasterItems[index].blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/RasterItem.boundingBox:

RasterItem.boundingBox
********************************************************************************

``app.activeDocument.rasterItems[index].boundingBox``

**Description**

The dimensions of the placed art item regardless of transformations.

**Type**

Array of 4 numbers

----

.. _jsobjref/RasterItem.channels:

RasterItem.channels
********************************************************************************

``app.activeDocument.rasterItems[index].channels``

**Description**

The number of channels.

**Type**

Number (long); read-only.

----

.. _jsobjref/RasterItem.colorants:

RasterItem.colorants
********************************************************************************

``app.activeDocument.rasterItems[index].colorants``

**Description**

The colorants used in the raster art.

**Type**

Array of string; read-only.

----

.. _jsobjref/RasterItem.colorizedGrayscale:

RasterItem.colorizedGrayscale
********************************************************************************

``app.activeDocument.rasterItems[index].colorizedGrayscale``

**Description**

If ``true``, the raster art is a colorized grayscale image.

**Type**

Boolean; read-only.

----

.. _jsobjref/RasterItem.contentVariable:

RasterItem.contentVariable
********************************************************************************

``app.activeDocument.rasterItems[index].contentVariable``

**Description**

The content variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/RasterItem.controlBounds:

RasterItem.controlBounds
********************************************************************************

``app.activeDocument.rasterItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/RasterItem.editable:

RasterItem.editable
********************************************************************************

``app.activeDocument.rasterItems[index].editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean; read-only.

----

.. _jsobjref/RasterItem.embedded:

RasterItem.embedded
********************************************************************************

``app.activeDocument.rasterItems[index].embedded``

**Description**

If ``true``, the raster art item is embedded in the illustration.

**Type**

Boolean

----

.. _jsobjref/RasterItem.file:

RasterItem.file
********************************************************************************

``app.activeDocument.rasterItems[index].file``

**Description**

The file containing the artwork.

**Type**

File; read-only.

----

.. _jsobjref/RasterItem.geometricBounds:

RasterItem.geometricBounds
********************************************************************************

``app.activeDocument.rasterItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/RasterItem.height:

RasterItem.height
********************************************************************************

``app.activeDocument.rasterItems[index].height``

**Description**

The height of the group item.

**Type**

Number (double)

----

.. _jsobjref/RasterItem.hidden:

RasterItem.hidden
********************************************************************************

``app.activeDocument.rasterItems[index].hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean

----

.. _jsobjref/RasterItem.imageColorSpace:

RasterItem.imageColorSpace
********************************************************************************

``app.activeDocument.rasterItems[index].imageColorSpace``

**Description**

The color space of the raster image.

**Type**

:ref:`jsobjref/scripting-constants.ImageColorSpace`; read-only.

----

.. _jsobjref/RasterItem.isIsolated:

RasterItem.isIsolated
********************************************************************************

``app.activeDocument.rasterItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean

----

.. _jsobjref/RasterItem.layer:

RasterItem.layer
********************************************************************************

``app.activeDocument.rasterItems[index].layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`; read-only.

----

.. _jsobjref/RasterItem.left:

RasterItem.left
********************************************************************************

``app.activeDocument.rasterItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

----

.. _jsobjref/RasterItem.locked:

RasterItem.locked
********************************************************************************

``app.activeDocument.rasterItems[index].locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean

----

.. _jsobjref/RasterItem.matrix:

RasterItem.matrix
********************************************************************************

``app.activeDocument.rasterItems[index].matrix``

**Description**

The transformation matrix of the placed artwork.

**Type**

:ref:`jsobjref/Matrix`

----

.. _jsobjref/RasterItem.name:

RasterItem.name
********************************************************************************

``app.activeDocument.rasterItems[index].name``

**Description**

The name of this item.

**Type**

String

----

.. _jsobjref/RasterItem.note:

RasterItem.note
********************************************************************************

``app.activeDocument.rasterItems[index].note``

**Description**

The note assigned to this item.

**Type**

String

----

.. _jsobjref/RasterItem.opacity:

RasterItem.opacity
********************************************************************************

``app.activeDocument.rasterItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

----

.. _jsobjref/RasterItem.overprint:

RasterItem.overprint
********************************************************************************

``app.activeDocument.rasterItems[index].overprint``

**Description**

If ``true``, the raster art overprints.

**Type**

Boolean

----

.. _jsobjref/RasterItem.parent:

RasterItem.parent
********************************************************************************

``app.activeDocument.rasterItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`

----

.. _jsobjref/RasterItem.position:

RasterItem.position
********************************************************************************

``app.activeDocument.rasterItems[index].position``

**Description**

The position (in points) of the top left corner of the ``rasterItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

----

.. _jsobjref/RasterItem.selected:

RasterItem.selected
********************************************************************************

``app.activeDocument.rasterItems[index].selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean

----

.. _jsobjref/RasterItem.sliced:

RasterItem.sliced
********************************************************************************

``app.activeDocument.rasterItems[index].sliced``

**Description**

If ``true``, the item sliced.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterItem.status:

RasterItem.status
********************************************************************************

``app.activeDocument.rasterItems[index].status``

**Description**

Status of the linked image.

**Type**

:ref:`jsobjref/scripting-constants.RasterLinkState`

----

.. _jsobjref/RasterItem.tags:

RasterItem.tags
********************************************************************************

``app.activeDocument.rasterItems[index].tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`; read-only.

----

.. _jsobjref/RasterItem.top:

RasterItem.top
********************************************************************************

``app.activeDocument.rasterItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

----

.. _jsobjref/RasterItem.transparent:

RasterItem.transparent
********************************************************************************

``app.activeDocument.rasterItems[index].transparent``

**Description**

If ``true``, the raster art is transparent.

**Type**

Boolean; read-only.

----

.. _jsobjref/RasterItem.typename:

RasterItem.typename
********************************************************************************

``app.activeDocument.rasterItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

.. _jsobjref/RasterItem.uRL:

RasterItem.uRL
********************************************************************************

``app.activeDocument.rasterItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

----

.. _jsobjref/RasterItem.visibilityVariable:

RasterItem.visibilityVariable
********************************************************************************

``app.activeDocument.rasterItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/RasterItem.visibleBounds:

RasterItem.visibleBounds
********************************************************************************

``app.activeDocument.rasterItems[index].visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/RasterItem.width:

RasterItem.width
********************************************************************************

``app.activeDocument.rasterItems[index].width``

**Description**

The width of the item.

**Type**

Number (double)

----

.. _jsobjref/RasterItem.wrapInside:

RasterItem.wrapInside
********************************************************************************

``app.activeDocument.rasterItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean

----

.. _jsobjref/RasterItem.wrapOffset:

RasterItem.wrapOffset
********************************************************************************

``app.activeDocument.rasterItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

----

.. _jsobjref/RasterItem.wrapped:

RasterItem.wrapped
********************************************************************************

``app.activeDocument.rasterItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

----

.. _jsobjref/RasterItem.zOrderPosition:

RasterItem.zOrderPosition
********************************************************************************

``app.activeDocument.rasterItems[index].zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number; read-only.

----

=======
Methods
=======

.. _jsobjref/RasterItem.colorize:

RasterItem.colorize
********************************************************************************

``app.activeDocument.rasterItems[index].colorize(rasterizeColor)``

**Description**

Colorizes the raster item with a CMYK or RGB Color.

**Parameters**

+--------------------+-----------------------+-------------+
|     Parameter      |         Type          | Description |
+====================+=======================+=============+
| ``rasterizeColor`` | :ref:`jsobjref/Color` | todo        |
+--------------------+-----------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.duplicate:

RasterItem.duplicate
********************************************************************************

``app.activeDocument.rasterItems[index].duplicate([relativeObject][, insertionLocation])``

**Description**

Creates a duplicate of the selected object.

**Parameters**

+-----------------------+----------------------------------------------------------------+-------------+
|       Parameter       |                              Type                              | Description |
+=======================+================================================================+=============+
| ``relativeObject``    | Object, optional                                               | todo        |
+-----------------------+----------------------------------------------------------------+-------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | todo        |
+-----------------------+----------------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/RasterItem`

----

.. _jsobjref/RasterItem.move:

RasterItem.move
********************************************************************************

``app.activeDocument.rasterItems[index].move(relativeObject, insertionLocation)``

**Description**

Moves the object.

**Parameters**

+-----------------------+------------------------------------------------------+-------------+
|       Parameter       |                         Type                         | Description |
+=======================+======================================================+=============+
| ``relativeObject``    | Object                                               | todo        |
+-----------------------+------------------------------------------------------+-------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement` | todo        |
+-----------------------+------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/RasterItem`

----

.. _jsobjref/RasterItem.remove:

RasterItem.remove
********************************************************************************

``app.activeDocument.rasterItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.resize:

RasterItem.resize
********************************************************************************

``app.activeDocument.rasterItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])``

**Description**

Scales the art item where ``scaleX`` is the horizontal scaling factor and ``scaleY`` is the vertical scaling factor. 100.0 = 100%.

**Parameters**

+-------------------------+--------------------------------------------------------------+-------------+
|        Parameter        |                             Type                             | Description |
+=========================+==============================================================+=============+
| ``scaleX``              | Number (double)                                              | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``scaleY``              | Number (double)                                              | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changePositions``     | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeFillPatterns``  | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeFillGradients`` | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeStrokePattern`` | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeLineWidths``    | Number (double), optional                                    | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``scaleAbout``          | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+-------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.rotate:

RasterItem.rotate
********************************************************************************

``app.activeDocument.rasterItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])``

**Description**

Rotates the art item relative to the current rotation.

The object is rotated counter-clockwise if the ``angle`` value is positive, clockwise if the value is negative.

**Parameters**

+-------------------------+--------------------------------------------------------------+-------------+
|        Parameter        |                             Type                             | Description |
+=========================+==============================================================+=============+
| ``angle``               | Number (double)                                              | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changePositions``     | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeFillPatterns``  | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeFillGradients`` | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``changeStrokePattern`` | Boolean, optional                                            | todo        |
+-------------------------+--------------------------------------------------------------+-------------+
| ``rotateAbout``         | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+-------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.trace:

RasterItem.trace
********************************************************************************

``app.activeDocument.rasterItems[index].trace()``

**Description**

Converts the raster art for this object to vector art, using default options.

Reorders the raster art into the source art of a plug-in group, and converts it into a group of filled and/or stroked paths that resemble the original image.

Creates and returns a :ref:`jsobjref/PluginItem` object that references a :ref:`jsobjref/TracingObject` object.

**Returns**

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/RasterItem.transform:

RasterItem.transform
********************************************************************************

``app.activeDocument.rasterItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])``

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+--------------------------+--------------------------------------------------------------+-------------+
|        Parameter         |                             Type                             | Description |
+==========================+==============================================================+=============+
| ``transformationMatrix`` | Matrix                                                       | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``changePositions``      | Boolean, optional                                            | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``changeFillPatterns``   | Boolean, optional                                            | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``changeFillGradients``  | Boolean, optional                                            | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``changeStrokePattern``  | Boolean, optional                                            | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``changeLineWidths``     | Number (double), optional                                    | todo        |
+--------------------------+--------------------------------------------------------------+-------------+
| ``transformAbout``       | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+--------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.translate:

RasterItem.translate
********************************************************************************

``app.activeDocument.rasterItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])``

**Description**

Repositions the art item relative to the current position, where ``deltaX`` is the horizontal offset and ``deltaY`` is the vertical offset.

**Parameters**

+-----------------------------+---------------------------+-------------+
|          Parameter          |           Type            | Description |
+=============================+===========================+=============+
| ``deltaX``                  | Number (double), optional | todo        |
+-----------------------------+---------------------------+-------------+
| ``deltaY``                  | Number (double), optional | todo        |
+-----------------------------+---------------------------+-------------+
| ``transformObjects``        | Boolean, optional         | todo        |
+-----------------------------+---------------------------+-------------+
| ``transformFillPatterns``   | Boolean, optional         | todo        |
+-----------------------------+---------------------------+-------------+
| ``transformFillGradients``  | Boolean, optional         | todo        |
+-----------------------------+---------------------------+-------------+
| ``transformStrokePatterns`` | Boolean, optional         | todo        |
+-----------------------------+---------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/RasterItem.zOrder:

RasterItem.zOrder
********************************************************************************

``app.activeDocument.rasterItems[index].zOrder(zOrderCmd)``

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

+---------------+--------------------------------------------------+-------------+
|   Parameter   |                       Type                       | Description |
+===============+==================================================+=============+
| ``zOrderCmd`` | :ref:`jsobjref/scripting-constants.ZOrderMethod` | todo        |
+---------------+--------------------------------------------------+-------------+

**Returns**

Nothing.
