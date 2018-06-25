.. _jsobjref/LegacyTextItem:

LegacyTextItem
################################################################################

``legacyTextItems[index]``

**Description**

A text object created in Illustrator CS (version 10) or earlier, which is uneditable until converted. To convert legacy text, see :ref:`jsobjref/LegacyTextItems.convertToNative`.

You can view, move, and print legacy text, but you cant edit it. Legacy text has an “x” through its bounding box when selected.

----

==========
Properties
==========

.. _jsobjref/LegacyTextItem.artworkKnockout:

LegacyTextItem.artworkKnockout
********************************************************************************

``legacyTextItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/LegacyTextItem.blendingMode:

LegacyTextItem.blendingMode
********************************************************************************

``legacyTextItems[index].blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/LegacyTextItem.controlBounds:

LegacyTextItem.controlBounds
********************************************************************************

``legacyTextItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/LegacyTextItem.converted:

LegacyTextItem.converted
********************************************************************************

``legacyTextItems[index].converted``

**Description**

If ``true``, the legacy text item has been updated to a native text frame item.

**Type**

Boolean, read-only.

----

.. _jsobjref/LegacyTextItem.editable:

LegacyTextItem.editable
********************************************************************************

``legacyTextItems[index].editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean, read-only.

----

.. _jsobjref/LegacyTextItem.geometricBounds:

LegacyTextItem.geometricBounds
********************************************************************************

``legacyTextItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/LegacyTextItem.height:

LegacyTextItem.height
********************************************************************************

``legacyTextItems[index].height``

**Description**

The height of the group item.

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.hidden:

LegacyTextItem.hidden
********************************************************************************

``legacyTextItems[index].hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.isIsolated:

LegacyTextItem.isIsolated
********************************************************************************

``legacyTextItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.layer:

LegacyTextItem.layer
********************************************************************************

``legacyTextItems[index].layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`, read-only.

----

.. _jsobjref/LegacyTextItem.left:

LegacyTextItem.left
********************************************************************************

``legacyTextItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.locked:

LegacyTextItem.locked
********************************************************************************

``legacyTextItems[index].locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.name:

LegacyTextItem.name
********************************************************************************

``legacyTextItems[index].name``

**Description**

The name of this item.

**Type**

String.

----

.. _jsobjref/LegacyTextItem.note:

LegacyTextItem.note
********************************************************************************

``legacyTextItems[index].note``

**Description**

The note assigned to this item.

**Type**

String.

----

.. _jsobjref/LegacyTextItem.opacity:

LegacyTextItem.opacity
********************************************************************************

``legacyTextItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0.

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.parent:

LegacyTextItem.parent
********************************************************************************

``legacyTextItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`, read-only.

----

.. _jsobjref/LegacyTextItem.position:

LegacyTextItem.position
********************************************************************************

``legacyTextItems[index].position``

**Description**

The position (in points) of the top left corner of the ``legacyTextItems[index]`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

----

.. _jsobjref/LegacyTextItem.selected:

LegacyTextItem.selected
********************************************************************************

``legacyTextItems[index].selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.sliced:

LegacyTextItem.sliced
********************************************************************************

``legacyTextItems[index].sliced``

**Description**

If ``true``, the item sliced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.tags:

LegacyTextItem.tags
********************************************************************************

``legacyTextItems[index].tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`, read-only.

----

.. _jsobjref/LegacyTextItem.top:

LegacyTextItem.top
********************************************************************************

``legacyTextItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.typename:

LegacyTextItem.typename
********************************************************************************

``legacyTextItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/LegacyTextItem.uRL:

LegacyTextItem.uRL
********************************************************************************

``legacyTextItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String.

----

.. _jsobjref/LegacyTextItem.visibilityVariable:

LegacyTextItem.visibilityVariable
********************************************************************************

``legacyTextItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/LegacyTextItem.visibleBounds:

LegacyTextItem.visibleBounds
********************************************************************************

``legacyTextItems[index].visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/LegacyTextItem.width:

LegacyTextItem.width
********************************************************************************

``legacyTextItems[index].width``

**Description**

The width of the item.

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.wrapInside:

LegacyTextItem.wrapInside
********************************************************************************

``legacyTextItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.wrapOffset:

LegacyTextItem.wrapOffset
********************************************************************************

``legacyTextItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

----

.. _jsobjref/LegacyTextItem.wrapped:

LegacyTextItem.wrapped
********************************************************************************

``legacyTextItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

----

.. _jsobjref/LegacyTextItem.zOrderPosition:

LegacyTextItem.zOrderPosition
********************************************************************************

``legacyTextItems[index].zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number (long), read-only.

----

=======
Methods
=======

.. _jsobjref/LegacyTextItem.convertToNative:

LegacyTextItem.convertToNative()
********************************************************************************

``legacyTextItems[index].convertToNative()``

**Description**

Converts the legacy text item to a text frame and deletes the original legacy text.

**Returns**

:ref:`jsobjref/GroupItem`

----

.. _jsobjref/LegacyTextItem.duplicate:

LegacyTextItem.duplicate()
********************************************************************************

``legacyTextItems[index].duplicate([relativeObject] [,insertionLocation])``

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

:ref:`jsobjref/LegacyTextItem`

----

.. _jsobjref/LegacyTextItem.move:

LegacyTextItem.move()
********************************************************************************

``legacyTextItems[index].move(relativeObject, insertionLocation)``

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

:ref:`jsobjref/LegacyTextItem`

----

.. _jsobjref/LegacyTextItem.remove:

LegacyTextItem.remove()
********************************************************************************

``legacyTextItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/LegacyTextItem.resize:

LegacyTextItem.resize()
********************************************************************************

::

  legacyTextItem.resize(scaleX, scaleY
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,scaleAbout]
  )

**Description**

Scales the art item where scaleX is the horizontal scaling factor and scaleY is the vertical scaling factor. 100.0 = 100%.

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
| ``[changeLineWidths]``    | Number (double), optional                                    | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[scaleAbout]``          | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+---------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/LegacyTextItem.rotate:

LegacyTextItem.rotate()
********************************************************************************

::

  legacyTextItem.rotate(angle [,changePositions] [,changeFillPatterns]
    [,changeFillGradients] [,changeStrokePattern] [,rotateAbout]
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

.. _jsobjref/LegacyTextItem.transform:

LegacyTextItem.transform()
********************************************************************************

::

  legacyTextItem.transform(transformationMatrix
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,transformAbout]
  )

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+---------------------------+--------------------------------------------------------------+-------------+
|         Parameter         |                             Type                             | Description |
+===========================+==============================================================+=============+
| ``transformationMatrix``  | Number (double)                                              | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changePositions]``     | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillPatterns]``  | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeFillGradients]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeStrokePattern]`` | Boolean, optional                                            | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[changeLineWidths]``    | Number (double), optional                                    | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[transformAbout]``      | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+---------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/LegacyTextItem.translate:

LegacyTextItem.translate()
********************************************************************************

::

  legacyTextItem.translate([deltaX] [,deltaY]
    [,transformObjects] [,transformFillPatterns]
    [,transformFillGradients] [,transformStrokePatterns]
  )

**Description**

Repositions the art item relative to the current position, where ``deltaX`` is the horizontal offset and ``deltaY`` is the vertical offset.

**Parameters**

+-------------------------------+---------------------------+-------------+
|           Parameter           |           Type            | Description |
+===============================+===========================+=============+
| ``[deltaX]``                  | Number (double), optional | todo        |
+-------------------------------+---------------------------+-------------+
| ``[deltaY]``                  | Number (double), optional | todo        |
+-------------------------------+---------------------------+-------------+
| ``[transformObjects]``        | Boolean, optional         | todo        |
+-------------------------------+---------------------------+-------------+
| ``[transformFillPatterns]``   | Boolean, optional         | todo        |
+-------------------------------+---------------------------+-------------+
| ``[transformFillGradients]``  | Boolean, optional         | todo        |
+-------------------------------+---------------------------+-------------+
| ``[transformStrokePatterns]`` | Boolean, optional         | todo        |
+-------------------------------+---------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/LegacyTextItem.zOrder:

LegacyTextItem.zOrder()
********************************************************************************

``legacyTextItems[index].zOrder(zOrderCmd)``

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
