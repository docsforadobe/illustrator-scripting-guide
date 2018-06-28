.. _jsobjref/GraphItem:

GraphItem
################################################################################

``app.activeDocument.graphItems[index``

**Description**

Any graph artwork object. See example :ref:`jsobjref/GraphItems.rotatingGraphItems`.

----

==========
Properties
==========

.. _jsobjref/GraphItem.artworkKnockout:

GraphItem.artworkKnockout
********************************************************************************

``app.activeDocument.graphItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout. You cannot set this value to ``KnockoutState.Unknown``.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/GraphItem.blendingMode:

GraphItem.blendingMode
********************************************************************************

``app.activeDocument.graphItems[index].blendingMode``

**Description**

The mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/GraphItem.contentVariable:

GraphItem.contentVariable
********************************************************************************

``app.activeDocument.graphItems[index].contentVariable``

**Description**

The content variable bound to the graph item.

It is not necessary to set the type of the ``contentVariable`` before binding. Illustrator automatically set the type to ``GRAPH``.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/GraphItem.controlBounds:

GraphItem.controlBounds
********************************************************************************

``app.activeDocument.graphItems[index].controlBounds``

**Description**

The content variable bound to the graph item.

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GraphItem.editable:

GraphItem.editable
********************************************************************************

``app.activeDocument.graphItems[index].editable``

**Description**

If ``true``, this graph item is editable.

**Type**

Boolean, read-only.

----

.. _jsobjref/GraphItem.geometricBounds:

GraphItem.geometricBounds
********************************************************************************

``app.activeDocument.graphItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GraphItem.height:

GraphItem.height
********************************************************************************

``app.activeDocument.graphItems[index].height``

**Description**

The height of the graph item.

**Type**

Number (double), read-only.

----

.. _jsobjref/GraphItem.hidden:

GraphItem.hidden
********************************************************************************

``app.activeDocument.graphItems[index].hidden``

**Description**

If ``true``, this graph item is hidden.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.isIsolated:

GraphItem.isIsolated
********************************************************************************

``app.activeDocument.graphItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.layer:

GraphItem.layer
********************************************************************************

``app.activeDocument.graphItems[index].layer``

**Description**

The layer to which this graph item belongs.

**Type**

:ref:`jsobjref/Layer`, read-only.

----

.. _jsobjref/GraphItem.left:

GraphItem.left
********************************************************************************

``app.activeDocument.graphItems[index].left``

**Description**

The offset (in points) of the left side of the graph item from the left side of the page.

**Type**

Number.

----

.. _jsobjref/GraphItem.locked:

GraphItem.locked
********************************************************************************

``app.activeDocument.graphItems[index].locked``

**Description**

If ``true``, this graph item is locked.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.name:

GraphItem.name
********************************************************************************

``app.activeDocument.graphItems[index].name``

**Description**

The name of this graph item.

**Type**

String.

----

.. _jsobjref/GraphItem.note:

GraphItem.note
********************************************************************************

``app.activeDocument.graphItems[index].note``

**Description**

The note assigned to this item.

**Type**

String.

----

.. _jsobjref/GraphItem.opacity:

GraphItem.opacity
********************************************************************************

``app.activeDocument.graphItems[index].opacity``

**Description**

The opacity of the object; the value is between 0.0 and 100.0.

**Type**

Number (double)

----

.. _jsobjref/GraphItem.parent:

GraphItem.parent
********************************************************************************

``app.activeDocument.graphItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`

----

.. _jsobjref/GraphItem.position:

GraphItem.position
********************************************************************************

``app.activeDocument.graphItems[index].position``

**Description**

The position (in points) of the top left corner of the ``graphItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

----

.. _jsobjref/GraphItem.selected:

GraphItem.selected
********************************************************************************

``app.activeDocument.graphItems[index].selected``

**Description**

If ``true``, this object is selected.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.sliced:

GraphItem.sliced
********************************************************************************

``app.activeDocument.graphItems[index].sliced``

**Description**

If ``true``, the graph item is sliced. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.tags:

GraphItem.tags
********************************************************************************

``app.activeDocument.graphItems[index].tags``

**Description**

The tags contained in this graph item.

**Type**

:ref:`jsobjref/Tags`, read-only.

----

.. _jsobjref/GraphItem.top:

GraphItem.top
********************************************************************************

``app.activeDocument.graphItems[index].top``

**Description**

The offset (in points) of the top of the graph item from the bottom of the page.

**Type**

Number (double).

----

.. _jsobjref/GraphItem.typename:

GraphItem.typename
********************************************************************************

``app.activeDocument.graphItems[index].typename``

**Description**

The type of the graph item.

**Type**

String, read-only.

----

.. _jsobjref/GraphItem.uRL:

GraphItem.uRL
********************************************************************************

``app.activeDocument.graphItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this graph item.

**Type**

String.

----

.. _jsobjref/GraphItem.visibilityVariable:

GraphItem.visibilityVariable
********************************************************************************

``app.activeDocument.graphItems[index].visibilityVariable``

**Description**

The visibility variable bound to the graph item.

It is not necessary to set the type of the ``visibilityVariable`` before binding. Illustrator automatically set the type to ``VISIBILITY``.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/GraphItem.visibleBounds:

GraphItem.visibleBounds
********************************************************************************

``app.activeDocument.graphItems[index].visibleBounds``

**Description**

The visible bounds of the graph item including stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/GraphItem.width:

GraphItem.width
********************************************************************************

``app.activeDocument.graphItems[index].width``

**Description**

The width of the graph item. Range: 0.0 to 16348.0.

**Type**

Number (double).

----

.. _jsobjref/GraphItem.wrapInside:

GraphItem.wrapInside
********************************************************************************

``app.activeDocument.graphItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean.

----

.. _jsobjref/GraphItem.wrapOffset:

GraphItem.wrapOffset
********************************************************************************

``app.activeDocument.graphItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

----

.. _jsobjref/GraphItem.wrapped:

GraphItem.wrapped
********************************************************************************

``app.activeDocument.graphItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object. (Text frame must be above the object.)

**Type**

Boolean.

----

.. _jsobjref/GraphItem.zOrderPosition:

GraphItem.zOrderPosition
********************************************************************************

``app.activeDocument.graphItems[index].zOrderPosition``

**Description**

The position of this art item within the stacking order of the group or layer (parent) that contains the art item.

**Type**

Number (long).

----

=======
Methods
=======

.. _jsobjref/GraphItem.duplicate:

GraphItem.duplicate()
********************************************************************************

``app.activeDocument.graphItems[index].duplicate([relativeObject] [,insertionLocation])``

**Description**

Creates a duplicate of the selected object.

**Parameters**

+-----------------------+----------------------------------------------------------------+----------------------------+
|       Parameter       |                              Type                              |        Description         |
+=======================+================================================================+============================+
| ``relativeObject``    | Object, optional                                               | todo                       |
+-----------------------+----------------------------------------------------------------+----------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to insert element |
+-----------------------+----------------------------------------------------------------+----------------------------+

**Returns**

:ref:`jsobjref/GraphItem`

----

.. _jsobjref/GraphItem.move:

GraphItem.move()
********************************************************************************

``app.activeDocument.graphItems[index].move(relativeObject, insertionLocation)``

**Description**

Moves the object.

**Parameters**

+-----------------------+----------------------------------------------------------------+-----------------------------+
|       Parameter       |                              Type                              |         Description         |
+=======================+================================================================+=============================+
| ``relativeObject``    | Object                                                         | todo                        |
+-----------------------+----------------------------------------------------------------+-----------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to move element to |
+-----------------------+----------------------------------------------------------------+-----------------------------+

**Returns**

:ref:`jsobjref/GraphItem`

----

.. _jsobjref/GraphItem.remove:

GraphItem.remove()
********************************************************************************

``app.activeDocument.graphItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/GraphItem.resize:

GraphItem.resize()
********************************************************************************

::

  app.activeDocument.graphItems[index].resize(scaleX, scaleY
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,scaleAbout])
  )

**Description**

Scales the art item where ``scaleX`` is the horizontal scaling factor and ``scaleY`` is the vertical scaling factor. 100.0 = 100%.

**Parameters**

+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
|        Parameter        |                             Type                             |                       Description                       |
+=========================+==============================================================+=========================================================+
| ``scaleX``              | Number (double)                                              | Horizontal scaling factor                               |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``scaleY``              | Number (double)                                              | Vertical scaling factor                                 |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changePositions``     | Boolean, optional                                            | Whether to effect art object positions and orientations |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeFillPatterns``  | Boolean, optional                                            | Whether to transform fill patterns                      |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeFillGradients`` | Boolean, optional                                            | Whether to transform fill gradients                     |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeStrokePattern`` | Boolean, optional                                            | Whether to transform stroke patterns                    |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeLineWidths``    | Number (double), optional                                    | The amount to scale line widths                         |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``scaleAbout``          | :ref:`jsobjref/scripting-constants.Transformation`, optional | The point to use as anchor, to transform about          |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+

**Returns**

Nothing.

----

.. _jsobjref/GraphItem.rotate:

GraphItem.rotate()
********************************************************************************

::

  app.activeDocument.graphItems[index].rotate(angle
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,rotateAbout]
  )

**Description**

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the ``angle`` value is positive, clockwise if the value is negative.

**Parameters**

+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
|        Parameter        |                             Type                             |                       Description                       |
+=========================+==============================================================+=========================================================+
| ``angle``               | Number (double)                                              | The angle amount to rotate the element                  |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changePositions``     | Boolean, optional                                            | Whether to effect art object positions and orientations |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeFillPatterns``  | Boolean, optional                                            | Whether to transform fill patterns                      |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeFillGradients`` | Boolean, optional                                            | Whether to transform fill gradients                     |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``changeStrokePattern`` | Boolean, optional                                            | Whether to transform stroke patterns                    |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+
| ``rotateAbout``         | :ref:`jsobjref/scripting-constants.Transformation`, optional | The point to use as anchor, to transform about          |
+-------------------------+--------------------------------------------------------------+---------------------------------------------------------+

**Returns**

Nothing.

----

.. _jsobjref/GraphItem.transform:

GraphItem.transform()
********************************************************************************

::

  app.activeDocument.graphItems[index].transform(transformationMatrix
    [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,transformAbout]
  )

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+--------------------------+--------------------------------------------------------------+------------------------------------------------+
|        Parameter         |                             Type                             |                  Description                   |
+==========================+==============================================================+================================================+
| ``transformationMatrix`` | :ref:`jsobjref/Matrix`                                       | Transformation matrix to apply                 |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``changePositions``      | Boolean, optional                                            | Whether to change Positions                    |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``changeFillPatterns``   | Boolean, optional                                            | Whether to change Fill Patterns                |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``changeFillGradients``  | Boolean, optional                                            | Whether to change Fill Gradients               |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``changeStrokePattern``  | Boolean, optional                                            | Whether to change Stroke Pattern               |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``changeLineWidths``     | Number (double), optional                                    | The amount to scale line widths                |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+
| ``transformAbout``       | :ref:`jsobjref/scripting-constants.Transformation`, optional | The point to use as anchor, to transform about |
+--------------------------+--------------------------------------------------------------+------------------------------------------------+

**Returns**

Nothing.

----

.. _jsobjref/GraphItem.translate:

GraphItem.translate()
********************************************************************************

::

  app.activeDocument.graphItems[index].translate([deltaX] [,deltaY]
    [,transformObjects] [,transformFillPatterns]
    [,transformFillGradients] [,transformStrokePatterns]
  )

**Description**

Repositions the art item relative to the current position, where ``deltaX`` is the horizontal offset and ``deltaY`` is the vertical offset.

**Parameters**

+-----------------------------+---------------------------+--------------------------------------+
|          Parameter          |           Type            |             Description              |
+=============================+===========================+======================================+
| ``deltaX``                  | Number (double), optional | Horizontal offset                    |
+-----------------------------+---------------------------+--------------------------------------+
| ``deltaY``                  | Number (double), optional | Vertical offset                      |
+-----------------------------+---------------------------+--------------------------------------+
| ``transformObjects``        | Boolean, optional         | Whether to transform Objects         |
+-----------------------------+---------------------------+--------------------------------------+
| ``transformFillPatterns``   | Boolean, optional         | Whether to transform Fill Patterns   |
+-----------------------------+---------------------------+--------------------------------------+
| ``transformFillGradients``  | Boolean, optional         | Whether to transform Fill Gradients  |
+-----------------------------+---------------------------+--------------------------------------+
| ``transformStrokePatterns`` | Boolean, optional         | Whether to transform Stroke Patterns |
+-----------------------------+---------------------------+--------------------------------------+

**Returns**

Nothing.

----

.. _jsobjref/GraphItem.zOrder:

GraphItem.zOrder()
********************************************************************************

``app.activeDocument.graphItems[index].zOrder(zOrderCmd)``

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

+---------------+--------------------------------------------------+-----------------------------------+
|   Parameter   |                       Type                       |            Description            |
+===============+==================================================+===================================+
| ``zOrderCmd`` | :ref:`jsobjref/scripting-constants.ZOrderMethod` | Stacking order arrangement method |
+---------------+--------------------------------------------------+-----------------------------------+

**Returns**

Nothing.
