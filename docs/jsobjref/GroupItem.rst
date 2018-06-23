.. _jsobjref/GroupItem:

GroupItem
################################################################################

``app.activeDocument.groupItems[index]``

**Description**

A grouped set of art items. Group items can contain all of the same page items that a layer can contain, including other nested groups.

Paths contained in a group or compound path in a document are returned as individual paths when a script asks for the paths contained in the document. However, paths contained in a group or compound path are not returned when a script asks for the paths in a layer which contains the group or compound path.

----

==========
Properties
==========

.. _jsobjref/GroupItem.artworkKnockout:

GroupItem.artworkKnockout
********************************************************************************

``app.activeDocument.groupItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/GroupItem.blendingMode:

GroupItem.blendingMode
********************************************************************************

``app.activeDocument.groupItems[index].blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/GroupItem.clipped:

GroupItem.clipped
********************************************************************************

``app.activeDocument.groupItems[index].clipped``

**Description**

If ``true``, the group is clipped to the clipping mask.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.compoundPathItems:

GroupItem.compoundPathItems
********************************************************************************

``app.activeDocument.groupItems[index].compoundPathItems``

**Description**

The compound path items contained in this group.

**Type**

:ref:`jsobjref/CompoundPathItems`, read-only.

----

.. _jsobjref/GroupItem.controlBounds:

GroupItem.controlBounds
********************************************************************************

``app.activeDocument.groupItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GroupItem.editable:

GroupItem.editable
********************************************************************************

``app.activeDocument.groupItems[index].editable``

**Description**

If true, this item is editable.

**Type**

Boolean, read-only.

----

.. _jsobjref/GroupItem.geometricBounds:

GroupItem.geometricBounds
********************************************************************************

``app.activeDocument.groupItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GroupItem.graphItems:

GroupItem.graphItems
********************************************************************************

``app.activeDocument.groupItems[index].graphItems``

**Description**

he graph items contained in this group.

**Type**

:ref:`jsobjref/GraphItems`, read-only.

----

.. _jsobjref/GroupItem.groupItems:

GroupItem.groupItems
********************************************************************************

``app.activeDocument.groupItems[index].groupItems``

**Description**

The group items contained in this group.

**Type**

:ref:`jsobjref/GroupItems`, read-only.

----

.. _jsobjref/GroupItem.height:

GroupItem.height
********************************************************************************

``app.activeDocument.groupItems[index].height``

**Description**

The height of the group item.

**Type**

Number (double).

----

.. _jsobjref/GroupItem.hidden:

GroupItem.hidden
********************************************************************************

``app.activeDocument.groupItems[index].hidden``

**Description**

If ``true``, this group item is hidden.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.isIsolated:

GroupItem.isIsolated
********************************************************************************

``app.activeDocument.groupItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.layer:

GroupItem.layer
********************************************************************************

``app.activeDocument.groupItems[index].layer``

**Description**

The layer to which this group item belongs.

**Type**

:ref:`jsobjref/Layer`, read-only.

----

.. _jsobjref/GroupItem.left:

GroupItem.left
********************************************************************************

``app.activeDocument.groupItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

----

.. _jsobjref/GroupItem.legacyTextItems:

GroupItem.legacyTextItems
********************************************************************************

``app.activeDocument.groupItems[index].legacyTextItems``

**Description**

The legacy text items in the group.

**Type**

:ref:`jsobjref/LegacyTextItems`, read-only.

----

.. _jsobjref/GroupItem.locked:

GroupItem.locked
********************************************************************************

``app.activeDocument.groupItems[index].locked``

**Description**

If ``true``, this group item is locked.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.meshItems:

GroupItem.meshItems
********************************************************************************

``app.activeDocument.groupItems[index].meshItems``

**Description**

The mesh items contained in this group.

**Type**

:ref:`jsobjref/MeshItems`, read-only.

----

.. _jsobjref/GroupItem.name:

GroupItem.name
********************************************************************************

``app.activeDocument.groupItems[index].name``

**Description**

The name of this group item.

**Type**

String.

----

.. _jsobjref/GroupItem.nonNativeItems:

GroupItem.nonNativeItems
********************************************************************************

``app.activeDocument.groupItems[index].nonNativeItems``

**Description**

The non-native art items in this group.

**Type**

:ref:`jsobjref/NonNativeItems`

----

.. _jsobjref/GroupItem.note:

GroupItem.note
********************************************************************************

``app.activeDocument.groupItems[index].note``

**Description**

The note assigned to this item.

**Type**

String.

----

.. _jsobjref/GroupItem.opacity:

GroupItem.opacity
********************************************************************************

``app.activeDocument.groupItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0.

**Type**

Number (double).

----

.. _jsobjref/GroupItem.pageItems:

GroupItem.pageItems
********************************************************************************

``app.activeDocument.groupItems[index].pageItems``

**Description**

The page items (all art item classes) contained in this group.

**Type**

:ref:`jsobjref/PageItems`, read-only.

----

.. _jsobjref/GroupItem.parent:

GroupItem.parent
********************************************************************************

``app.activeDocument.groupItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`, read-only.

----

.. _jsobjref/GroupItem.pathItems:

GroupItem.pathItems
********************************************************************************

``app.activeDocument.groupItems[index].pathItems``

**Description**

The path items contained in this group.

**Type**

:ref:`jsobjref/PathItems`, read-only.

----

.. _jsobjref/GroupItem.placedItems:

GroupItem.placedItems
********************************************************************************

``app.activeDocument.groupItems[index].placedItems``

**Description**

The placed items contained in this group.

**Type**

:ref:`jsobjref/PlacedItems`, read-only.

----

.. _jsobjref/GroupItem.pluginItems:

GroupItem.pluginItems
********************************************************************************

``app.activeDocument.groupItems[index].pluginItems``

**Description**

The plug-in items contained in this group.

**Type**

:ref:`jsobjref/PluginItems`, read-only.

----

.. _jsobjref/GroupItem.position:

GroupItem.position
********************************************************************************

``app.activeDocument.groupItems[index].position``

**Description**

The position (in points) of the top left corner of the ``groupItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

----

.. _jsobjref/GroupItem.rasterItems:

GroupItem.rasterItems
********************************************************************************

``app.activeDocument.groupItems[index].rasterItems``

**Description**

The raster items contained in this group.

**Type**

:ref:`jsobjref/RasterItems`, read-only.

----

.. _jsobjref/GroupItem.selected:

GroupItem.selected
********************************************************************************

``app.activeDocument.groupItems[index].selected``

**Description**

If ``true``, this group item is selected.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.sliced:

GroupItem.sliced
********************************************************************************

``app.activeDocument.groupItems[index].sliced``

**Description**

If ``true``, the item sliced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.symbolItems:

GroupItem.symbolItems
********************************************************************************

``app.activeDocument.groupItems[index].symbolItems``

**Description**

The symbol item objects in this group.

**Type**

:ref:`jsobjref/SymbolItems`, read-only.

----

.. _jsobjref/GroupItem.tags:

GroupItem.tags
********************************************************************************

``app.activeDocument.groupItems[index].tags``

**Description**

The tags contained in this group.

**Type**

:ref:`jsobjref/Tags`, read-only.

----

.. _jsobjref/GroupItem.textFrames:

GroupItem.textFrames
********************************************************************************

``app.activeDocument.groupItems[index].textFrames``

**Description**

The text art items contained in this group.

**Type**

:ref:`jsobjref/TextFrameItems`, read-only.

----

.. _jsobjref/GroupItem.top:

GroupItem.top
********************************************************************************

``app.activeDocument.groupItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

----

.. _jsobjref/GroupItem.typename:

GroupItem.typename
********************************************************************************

``app.activeDocument.groupItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/GroupItem.uRL:

GroupItem.uRL
********************************************************************************

``app.activeDocument.groupItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this group item.

**Type**

String.

----

.. _jsobjref/GroupItem.visibilityVariable:

GroupItem.visibilityVariable
********************************************************************************

``app.activeDocument.groupItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/GroupItem.visibleBounds:

GroupItem.visibleBounds
********************************************************************************

``app.activeDocument.groupItems[index].visibleBounds``

**Description**

The visible bounds of the group item including stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GroupItem.width:

GroupItem.width
********************************************************************************

``app.activeDocument.groupItems[index].width``

**Description**

The width of the group item.

**Type**

Number (double).

----

.. _jsobjref/GroupItem.wrapInside:

GroupItem.wrapInside
********************************************************************************

``app.activeDocument.groupItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean.

----

.. _jsobjref/GroupItem.wrapOffset:

GroupItem.wrapOffset
********************************************************************************

``app.activeDocument.groupItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

----

.. _jsobjref/GroupItem.wrapped:

GroupItem.wrapped
********************************************************************************

``app.activeDocument.groupItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

----

.. _jsobjref/GroupItem.zOrderPosition:

GroupItem.zOrderPosition
********************************************************************************

``app.activeDocument.groupItems[index].zOrderPosition``

**Description**

 The position of this group object within the stacking order of the group or layer (``parent``) that contains the group object.

**Type**

Number (long).

----

=======
Methods
=======

.. _jsobjref/GroupItem.duplicate:

GroupItem.duplicate()
********************************************************************************

``app.activeDocument.groupItems[index].duplicate([relativeObject] [,insertionLocation])``

**Description**

Creates a duplicate of the selected object.

**Parameters**

+-------------------------+----------------------------------------------------------------+-------------+
|        Parameter        |                              Type                              | Description |
+=========================+================================================================+=============+
| ``[relativeObject]``    | Object, optional                                               | todo        |
+-------------------------+----------------------------------------------------------------+-------------+
| ``[insertionLocation]`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | todo        |
+-------------------------+----------------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/GroupItem`

----

.. _jsobjref/GroupItem.move:

GroupItem.move()
********************************************************************************

``app.activeDocument.groupItems[index].move(relativeObject, insertionLocation)``

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

:ref:`jsobjref/GroupItem`

----

.. _jsobjref/GroupItem.remove:

GroupItem.remove()
********************************************************************************

``app.activeDocument.groupItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/GroupItem.resize:

GroupItem.resize()
********************************************************************************

::

  app.activeDocument.groupItems[index].resize(scaleX, scaleY
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,scaleAbout]
  )

**Description**

Scales the art item where ``scaleX`` is the horizontal scaling factor and ``scaleY`` is the vertical scaling factor. 100.0 = 100%.

**Parameters**

+---------------------------+--------------------------------------------------------------+-------------+
|         Parameter         |                             Type                             | Description |
+===========================+==============================================================+=============+
| ``scaleX``                | Number (double)                                              | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``scaleY``                | Number (double)                                              | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changePositions]``     | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillPatterns]``  | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillGradients]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeStrokePattern]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeLineWidths]``    | Number (long), optional                                      | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[scaleAbout]``          | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+---------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/GroupItem.rotate:

GroupItem.rotate()
********************************************************************************

::

  app.activeDocument.groupItems[index].rotate(angle
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,rotateAbout]
  )

**Description**

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the ``angle`` value is positive, clockwise if the value is negative.

**Parameters**

+---------------------------+--------------------------------------------------------------+-------------+
|         Parameter         |                             Type                             | Description |
+===========================+==============================================================+=============+
| ``angle``                 | Number (double)                                              | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changePositions]``     | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillPatterns]``  | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillGradients]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeStrokePattern]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[rotateAbout]``         | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+---------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/GroupItem.transform:

GroupItem.transform()
********************************************************************************

::

  app.activeDocument.groupItems[index].transform(transformationMatrix
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,transformAbout]
  )

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+--------------------------------+--------------------------------------------------------------+-------------+
|           Parameter            |                             Type                             | Description |
+================================+==============================================================+=============+
| ``scaltransformationMatrixeX`` | Matrix                                                       | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[changePositions]``          | Boolean, optional                                            | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillPatterns]``       | Boolean, optional                                            | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillGradients]``      | Boolean, optional                                            | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[changeStrokePattern]``      | Boolean, optional                                            | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[changeLineWidths]``         | Number (long), optional                                      | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+
| ``[transformAbout]``           | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+--------------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/GroupItem.translate:

GroupItem.translate()
********************************************************************************

::

  app.activeDocument.groupItems[index].translate([deltaX] [,deltaY]
    [,transformObjects] [,transformFillPatterns]
    [,transformFillGradients] [,transformStrokePatterns]
  )

**Description**

Repositions the art item relative to the current position, where ``deltaX`` is the horizontal offset and ``deltaY`` is the vertical offset.

**Parameters**

+-------------------------------+-------------------+-------------+
|           Parameter           |       Type        | Description |
+===============================+===================+=============+
| ``[deltaX]``                  | Number (double)   | todo        |
+-------------------------------+-------------------+-------------+
| ``[deltaY]``                  | Number (double)   | todo        |
+-------------------------------+-------------------+-------------+
| ``[transformObjects]``        | Boolean, optional | todo        |
+-------------------------------+-------------------+-------------+
| ``[transformFillPatterns]``   | Boolean, optional | todo        |
+-------------------------------+-------------------+-------------+
| ``[transformFillGradients]``  | Boolean, optional | todo        |
+-------------------------------+-------------------+-------------+
| ``[transformStrokePatterns]`` | Boolean, optional | todo        |
+-------------------------------+-------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/GroupItem.zOrder:

GroupItem.zOrder()
********************************************************************************

``app.activeDocument.groupItems[index].zOrder(zOrderCmd)``

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

Modifying all objects in a group
********************************************************************************

It is easy to modify all of the objects contained in a group. This example demonstrates how to simplify your operations on multiple objects by creating group to contain them.

::

  // Creates a new group item, adds a new path item, of triangle shape, to the group,
  // then adds a new text item to the group and sets the fill color of the text to red

  if (app.documents.length > 0) {
    var triangleGroup = app.activeDocument.groupItems.add();

    // Create a triangle and add text, the new art is created inside the group
    var trianglePath = triangleGroup.pathItems.add();
    trianglePath.setEntirePath(Array(Array(100, 100), Array(300, 100), Array(200, Math.tan(1.0471975) * 100 + 100)));
    trianglePath.closed = true;
    trianglePath.stroked = true;
    trianglePath.filled = false;
    trianglePath.strokeWidth = 3;

    var captionText = triangleGroup.textFrames.add();
    captionText.position = Array(100, 150);
    captionText.textRange.size = 48;
    captionText.contents = "A triangle";

    var fillColor = new RGBColor();
    fillColor.red = 255;
    fillColor.green = 0;
    fillColor.blue = 0;
    captionText.characters.fillColor = fillColor;
  }
