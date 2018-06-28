.. _jsobjref/PlacedItem:

PlacedItem
################################################################################

``app.activeDocument.placedItems[index]``

**Description**

An artwork item placed in a document as a linked file.

For example, an artwork object created using the ``File > Place`` command in Illustrator or using the ``add()`` method of the ``placedItems`` collection object is a placed item.

For information, see :ref:`jsobjref/PlacedItems`.

----

==========
Properties
==========

.. _jsobjref/PlacedItem.artworkKnockout:

PlacedItem.artworkKnockout
********************************************************************************

``app.activeDocument.placedItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/PlacedItem.blendingMode:

PlacedItem.blendingMode
********************************************************************************

``app.activeDocument.placedItems[index].blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/PlacedItem.boundingBox:

PlacedItem.boundingBox
********************************************************************************

``app.activeDocument.placedItems[index].boundingBox``

**Description**

The dimensions of the placed art item regardless of transformations.

**Type**

Array of 4 numbers

----

.. _jsobjref/PlacedItem.contentVariable:

PlacedItem.contentVariable
********************************************************************************

``app.activeDocument.placedItems[index].contentVariable``

**Description**

The content variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/PlacedItem.controlBounds:

PlacedItem.controlBounds
********************************************************************************

``app.activeDocument.placedItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PlacedItem.editable:

PlacedItem.editable
********************************************************************************

``app.activeDocument.placedItems[index].editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean; read-only.

----

.. _jsobjref/PlacedItem.file:

PlacedItem.file
********************************************************************************

``app.activeDocument.placedItems[index].file``

**Description**

The file containing the artwork.

**Type**

File; read-only.

----

.. _jsobjref/PlacedItem.geometricBounds:

PlacedItem.geometricBounds
********************************************************************************

``app.activeDocument.placedItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PlacedItem.height:

PlacedItem.height
********************************************************************************

``app.activeDocument.placedItems[index].height``

**Description**

The height of the group item.

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.hidden:

PlacedItem.hidden
********************************************************************************

``app.activeDocument.placedItems[index].hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean

----

.. _jsobjref/PlacedItem.isIsolated:

PlacedItem.isIsolated
********************************************************************************

``app.activeDocument.placedItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean

----

.. _jsobjref/PlacedItem.layer:

PlacedItem.layer
********************************************************************************

``app.activeDocument.placedItems[index].layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`; read-only.

----

.. _jsobjref/PlacedItem.left:

PlacedItem.left
********************************************************************************

``app.activeDocument.placedItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.locked:

PlacedItem.locked
********************************************************************************

``app.activeDocument.placedItems[index].locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean

----

.. _jsobjref/PlacedItem.matrix:

PlacedItem.matrix
********************************************************************************

``app.activeDocument.placedItems[index].matrix``

**Description**

The transformation matrix of the placed artwork.

**Type**

:ref:`jsobjref/Matrix`

----

.. _jsobjref/PlacedItem.name:

PlacedItem.name
********************************************************************************

``app.activeDocument.placedItems[index].name``

**Description**

The name of this item.

**Type**

String

----

.. _jsobjref/PlacedItem.note:

PlacedItem.note
********************************************************************************

``app.activeDocument.placedItems[index].note``

**Description**

The note assigned to this item.

**Type**

String

----

.. _jsobjref/PlacedItem.opacity:

PlacedItem.opacity
********************************************************************************

``app.activeDocument.placedItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.parent:

PlacedItem.parent
********************************************************************************

``app.activeDocument.placedItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`

----

.. _jsobjref/PlacedItem.position:

PlacedItem.position
********************************************************************************

``app.activeDocument.placedItems[index].position``

**Description**

The position (in points) of the top left corner of the ``pluginItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

----

.. _jsobjref/PlacedItem.selected:

PlacedItem.selected
********************************************************************************

``app.activeDocument.placedItems[index].selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean

----

.. _jsobjref/PlacedItem.sliced:

PlacedItem.sliced
********************************************************************************

``app.activeDocument.placedItems[index].sliced``

**Description**

If ``true``, the item sliced.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PlacedItem.tags:

PlacedItem.tags
********************************************************************************

``app.activeDocument.placedItems[index].tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`; read-only.

----

.. _jsobjref/PlacedItem.top:

PlacedItem.top
********************************************************************************

``app.activeDocument.placedItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.typename:

PlacedItem.typename
********************************************************************************

``app.activeDocument.placedItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

.. _jsobjref/PlacedItem.uRL:

PlacedItem.uRL
********************************************************************************

``app.activeDocument.placedItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

----

.. _jsobjref/PlacedItem.visibilityVariable:

PlacedItem.visibilityVariable
********************************************************************************

``app.activeDocument.placedItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/PlacedItem.visibleBounds:

PlacedItem.visibleBounds
********************************************************************************

``app.activeDocument.placedItems[index].visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PlacedItem.width:

PlacedItem.width
********************************************************************************

``app.activeDocument.placedItems[index].width``

**Description**

The width of the item.

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.wrapInside:

PlacedItem.wrapInside
********************************************************************************

``app.activeDocument.placedItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean

----

.. _jsobjref/PlacedItem.wrapOffset:

PlacedItem.wrapOffset
********************************************************************************

``app.activeDocument.placedItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

----

.. _jsobjref/PlacedItem.wrapped:

PlacedItem.wrapped
********************************************************************************

``app.activeDocument.placedItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

----

.. _jsobjref/PlacedItem.zOrderPosition:

PlacedItem.zOrderPosition
********************************************************************************

``app.activeDocument.placedItems[index].zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number; read-only.

----

=======
Methods
=======

.. _jsobjref/PlacedItem.duplicate:

PlacedItem.duplicate()
********************************************************************************

``app.activeDocument.placedItems[index].duplicate([relativeObject][, insertionLocation])``

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

:ref:`jsobjref/PlacedItem`

----

.. _jsobjref/PlacedItem.embed:

PlacedItem.embed()
********************************************************************************

``app.activeDocument.placedItems[index].embed()``

**Description**

Embeds this art in the document. Converts the art to art item objects as needed and deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/PlacedItem.move:

PlacedItem.move()
********************************************************************************

``app.activeDocument.placedItems[index].move(relativeObject, insertionLocation)``

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

:ref:`jsobjref/PlacedItem`

----

.. _jsobjref/PlacedItem.relink:

PlacedItem.relink()
********************************************************************************

``app.activeDocument.placedItems[index].relink(linkFile)``

**Description**

Relinks the art object with the file that defines its content.

**Parameters**

+--------------+-------------+-------------+
|  Parameter   |    Type     | Description |
+==============+=============+=============+
| ``linkFile`` | File object | todo        |
+--------------+-------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/PlacedItem.remove:

PlacedItem.remove()
********************************************************************************

``app.activeDocument.placedItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/PlacedItem.resize:

PlacedItem.resize()
********************************************************************************

``app.activeDocument.placedItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])``

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

.. _jsobjref/PlacedItem.rotate:

PlacedItem.rotate()
********************************************************************************

``app.activeDocument.placedItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])``

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

.. _jsobjref/PlacedItem.trace:

PlacedItem.trace
********************************************************************************

``app.activeDocument.placedItems[index].trace()``

**Description**

Converts the raster art for this object to vector art, using default options.

Reorders the raster art into the source art of a plug-in group, and converts it into a group of filled and/or stroked paths that resemble the original image.

Creates and returns a :ref:`jsobjref/PluginItem` object that references a :ref:`jsobjref/TracingObject` object.

**Returns**

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/PlacedItem.transform:

PlacedItem.transform()
********************************************************************************

``app.activeDocument.placedItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])``

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

.. _jsobjref/PlacedItem.translate:

PlacedItem.translate()
********************************************************************************

``app.activeDocument.placedItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])``

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

.. _jsobjref/PlacedItem.zOrder:

PlacedItem.zOrder()
********************************************************************************

``app.activeDocument.placedItems[index].zOrder(zOrderCmd)``

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

----

=======
Example
=======

Changing the selection state of placed items
********************************************************************************

::

  // Toggles the selection state of all placed items.
  if (app.documents.length > 0) {
    for (i = 0; i < app.activeDocument.placedItems.length; i++) {
      var placedArt = app.activeDocument.placedItems[i];
      placedArt.selected = !(placedArt.selected);
    }
  }
