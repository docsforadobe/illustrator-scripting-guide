.. _jsobjref/NonNativeItem:

NonNativeItem
################################################################################

``nonNativeItem``

**Description**

A non-native artwork item.

----

==========
Properties
==========

.. _jsobjref/NonNativeItem.artworkKnockout:

NonNativeItem.artworkKnockout
********************************************************************************

``nonNativeItem.artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/NonNativeItem.blendingMode:

NonNativeItem.blendingMode
********************************************************************************

``nonNativeItem.blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/NonNativeItem.controlBounds:

NonNativeItem.controlBounds
********************************************************************************

``nonNativeItem.controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/NonNativeItem.editable:

NonNativeItem.editable
********************************************************************************

``nonNativeItem.editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean, read-only.

----

.. _jsobjref/NonNativeItem.geometricBounds:

NonNativeItem.geometricBounds
********************************************************************************

``nonNativeItem.geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/NonNativeItem.height:

NonNativeItem.height
********************************************************************************

``nonNativeItem.height``

**Description**

The height of the group item.

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.hidden:

NonNativeItem.hidden
********************************************************************************

``nonNativeItem.hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.isIsolated:

NonNativeItem.isIsolated
********************************************************************************

``nonNativeItem.isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.layer:

NonNativeItem.layer
********************************************************************************

``nonNativeItem.layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`, read-only.

----

.. _jsobjref/NonNativeItem.left:

NonNativeItem.left
********************************************************************************

``nonNativeItem.left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.locked:

NonNativeItem.locked
********************************************************************************

``nonNativeItem.locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.name:

NonNativeItem.name
********************************************************************************

``nonNativeItem.name``

**Description**

The name of this item.

**Type**

String.

----

.. _jsobjref/NonNativeItem.note:

NonNativeItem.note
********************************************************************************

``nonNativeItem.note``

**Description**

The note assigned to this item.

**Type**

String.

----

.. _jsobjref/NonNativeItem.opacity:

NonNativeItem.opacity
********************************************************************************

``nonNativeItem.opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0.

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.parent:

NonNativeItem.parent
********************************************************************************

``nonNativeItem.parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Document`, :ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`, read-only.

----

.. _jsobjref/NonNativeItem.position:

NonNativeItem.position
********************************************************************************

``nonNativeItem.position``

**Description**

The position (in points) of the top left corner of the ``NonNativeItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

----

.. _jsobjref/NonNativeItem.selected:

NonNativeItem.selected
********************************************************************************

``nonNativeItem.selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.sliced:

NonNativeItem.sliced
********************************************************************************

``nonNativeItem.sliced``

**Description**

If ``true``, the item sliced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.tags:

NonNativeItem.tags
********************************************************************************

``nonNativeItem.tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`, read-only.

----

.. _jsobjref/NonNativeItem.top:

NonNativeItem.top
********************************************************************************

``nonNativeItem.top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.typename:

NonNativeItem.typename
********************************************************************************

``nonNativeItem.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/NonNativeItem.uRL:

NonNativeItem.uRL
********************************************************************************

``nonNativeItem.uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String.

----

.. _jsobjref/NonNativeItem.visibilityVariable:

NonNativeItem.visibilityVariable
********************************************************************************

``nonNativeItem.visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/NonNativeItem.visibleBounds:

NonNativeItem.visibleBounds
********************************************************************************

``nonNativeItem.visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/NonNativeItem.width:

NonNativeItem.width
********************************************************************************

``nonNativeItem.width``

**Description**

The width of the item.

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.wrapInside:

NonNativeItem.wrapInside
********************************************************************************

``nonNativeItem.wrapInside``

**Description**

If ``true``, the non-native-item object should be wrapped inside this object.

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.wrapOffset:

NonNativeItem.wrapOffset
********************************************************************************

``nonNativeItem.wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

----

.. _jsobjref/NonNativeItem.wrapped:

NonNativeItem.wrapped
********************************************************************************

``nonNativeItem.wrapped``

**Description**

If ``true``, wrap non-native-item objects around this object (non-native-item object must be above the object).

**Type**

Boolean.

----

.. _jsobjref/NonNativeItem.zOrderPosition:

NonNativeItem.zOrderPosition
********************************************************************************

``nonNativeItem.zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number, read-only.

----

=======
Methods
=======

.. _jsobjref/NonNativeItem.duplicate:

NonNativeItem.duplicate()
********************************************************************************

``nonNativeItem.duplicate([relativeObject] [,insertionLocation])``

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

:ref:`jsobjref/NonNativeItem`

----

.. _jsobjref/NonNativeItem.move:

NonNativeItem.move()
********************************************************************************

``nonNativeItem.move(relativeObject, insertionLocation)``

**Description**

Moves the object.

**Parameters**

+-----------------------+----------------------------------------------------------------+-------------+
|       Parameter       |                              Type                              | Description |
+=======================+================================================================+=============+
| ``relativeObject``    | Object, optional                                               | todo        |
+-----------------------+----------------------------------------------------------------+-------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | todo        |
+-----------------------+----------------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/NonNativeItem`

----

.. _jsobjref/NonNativeItem.remove:

NonNativeItem.remove()
********************************************************************************

``nonNativeItem.remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/NonNativeItem.removeAll:

NonNativeItem.removeAll()
********************************************************************************

``nonNativeItem.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

.. _jsobjref/NonNativeItem.resize:

NonNativeItem.resize()
********************************************************************************

::

  nonNativeItem.resize(scaleX, scaleY
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
| ``[changeLineWidths]``    | Number (double), optional                                    | todo        |
+---------------------------+--------------------------------------------------------------+-------------+
| ``[scaleAbout]``          | :ref:`jsobjref/scripting-constants.Transformation`, optional | todo        |
+---------------------------+--------------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/NonNativeItem.rotate:

NonNativeItem.rotate()
********************************************************************************

::

  nonNativeItem.rotate(angle
    [,changePositions] [,changeFillPatterns]
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

.. _jsobjref/NonNativeItem.transform:

NonNativeItem.transform()
********************************************************************************

::

  nonNativeItem.transform(transformationMatrix
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,transformAbout]
  )

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+---------------------------+--------------------------------------------------------------+-------------+
|         Parameter         |                             Type                             | Description |
+===========================+==============================================================+=============+
| ``transformationMatrix``  | Matrix                                                       | todo        |
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

.. _jsobjref/NonNativeItem.translate:

NonNativeItem.translate()
********************************************************************************

::

  nonNativeItem.translate([deltaX] [,deltaY]
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

.. _jsobjref/NonNativeItem.zOrder:

NonNativeItem.zOrder()
********************************************************************************

``nonNativeItem.zOrder(zOrderCmd)``

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
