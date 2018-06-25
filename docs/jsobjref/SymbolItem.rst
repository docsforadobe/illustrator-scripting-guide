.. _jsobjref/SymbolItem:

SymbolItem
################################################################################

``app.activeDocument.textFrames[index]``

**Description**

An art item made reusable by adding it to the Symbols palette.

A ``SymbolItem`` is linked to the :ref:`jsobjref/Symbol` from which it was created and changes if you modify the associated ``Symbol`` object.

----

==========
Properties
==========

.. _jsobjref/SymbolItem.artworkKnockout:

SymbolItem.artworkKnockout
********************************************************************************

``SymbolItem.artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/SymbolItem.blendingMode:

SymbolItem.blendingMode
********************************************************************************

``SymbolItem.blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/SymbolItem.controlBounds:

SymbolItem.controlBounds
********************************************************************************

``SymbolItem.controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 Numbers; read-only.

----

.. _jsobjref/SymbolItem.editable:

SymbolItem.editable
********************************************************************************

``SymbolItem.editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean; read-only.

----

.. _jsobjref/SymbolItem.geometricBounds:

SymbolItem.geometricBounds
********************************************************************************

``SymbolItem.geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 Numbers; read-only.

----

.. _jsobjref/SymbolItem.height:

SymbolItem.height
********************************************************************************

``SymbolItem.height``

**Description**

The height of the group item.

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.hidden:

SymbolItem.hidden
********************************************************************************

``SymbolItem.hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean

----

.. _jsobjref/SymbolItem.isIsolated:

SymbolItem.isIsolated
********************************************************************************

``SymbolItem.isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean

----

.. _jsobjref/SymbolItem.layer:

SymbolItem.layer
********************************************************************************

``SymbolItem.layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`; read-only.

----

.. _jsobjref/SymbolItem.left:

SymbolItem.left
********************************************************************************

``SymbolItem.left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.locked:

SymbolItem.locked
********************************************************************************

``SymbolItem.locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean

----

.. _jsobjref/SymbolItem.name:

SymbolItem.name
********************************************************************************

``SymbolItem.name``

**Description**

The name of this item.

**Type**

String

----

.. _jsobjref/SymbolItem.note:

SymbolItem.note
********************************************************************************

``SymbolItem.note``

**Description**

The note assigned to this item.

**Type**

String

----

.. _jsobjref/SymbolItem.opacity:

SymbolItem.opacity
********************************************************************************

``SymbolItem.opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.parent:

SymbolItem.parent
********************************************************************************

``SymbolItem.parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`; read-only.

----

.. _jsobjref/SymbolItem.position:

SymbolItem.position
********************************************************************************

``SymbolItem.position``

**Description**

The position (in points) of the top left corner of the ``symbolItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 Numbers

----

.. _jsobjref/SymbolItem.selected:

SymbolItem.selected
********************************************************************************

``SymbolItem.selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean

----

.. _jsobjref/SymbolItem.sliced:

SymbolItem.sliced
********************************************************************************

``SymbolItem.sliced``

**Description**

If ``true``, the item sliced. Default: ``false``

**Type**

Boolean

----

.. _jsobjref/SymbolItem.symbol:

SymbolItem.symbol
********************************************************************************

``SymbolItem.symbol``

**Description**

The symbol that was used to create this ``symbolItem``.

**Type**

:ref:`jsobjref/Symbol`

----

.. _jsobjref/SymbolItem.tags:

SymbolItem.tags
********************************************************************************

``SymbolItem.tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`; read-only.

----

.. _jsobjref/SymbolItem.top:

SymbolItem.top
********************************************************************************

``SymbolItem.top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.typename:

SymbolItem.typename
********************************************************************************

``SymbolItem.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

.. _jsobjref/SymbolItem.uRL:

SymbolItem.uRL
********************************************************************************

``SymbolItem.uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

----

.. _jsobjref/SymbolItem.visibilityVariable:

SymbolItem.visibilityVariable
********************************************************************************

``SymbolItem.visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

Variable

----

.. _jsobjref/SymbolItem.visibleBounds:

SymbolItem.visibleBounds
********************************************************************************

``SymbolItem.visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 Numbers; read-only.

----

.. _jsobjref/SymbolItem.width:

SymbolItem.width
********************************************************************************

``SymbolItem.width``

**Description**

The width of the item.

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.wrapInside:

SymbolItem.wrapInside
********************************************************************************

``SymbolItem.wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean

----

.. _jsobjref/SymbolItem.wrapOffset:

SymbolItem.wrapOffset
********************************************************************************

``SymbolItem.wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

----

.. _jsobjref/SymbolItem.wrapped:

SymbolItem.wrapped
********************************************************************************

``SymbolItem.wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

----

.. _jsobjref/SymbolItem.zOrderPosition:

SymbolItem.zOrderPosition
********************************************************************************

``SymbolItem.zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number; read-only.

----

=======
Methods
=======

.. _jsobjref/SymbolItem.duplicate:

SymbolItem.duplicate
********************************************************************************

``app.activeDocument.textFrames[index].duplicate([relativeObject][, insertionLocation])``

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

:ref:`jsobjref/SymbolItem`

----

.. _jsobjref/SymbolItem.move:

SymbolItem.move
********************************************************************************

``app.activeDocument.textFrames[index].move(relativeObject, insertionLocation)``

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

:ref:`jsobjref/SymbolItem`

----

.. _jsobjref/SymbolItem.remove:

SymbolItem.remove
********************************************************************************

``app.activeDocument.textFrames[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/SymbolItem.resize:

SymbolItem.resize
********************************************************************************

``app.activeDocument.textFrames[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])``

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

.. _jsobjref/SymbolItem.rotate:

SymbolItem.rotate
********************************************************************************

``app.activeDocument.textFrames[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])``

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

.. _jsobjref/SymbolItem.transform:

SymbolItem.transform
********************************************************************************

``app.activeDocument.textFrames[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])``

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

.. _jsobjref/SymbolItem.translate:

SymbolItem.translate
********************************************************************************

``app.activeDocument.textFrames[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])``

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

.. _jsobjref/SymbolItem.zOrder:

SymbolItem.zOrder
********************************************************************************

``app.activeDocument.textFrames[index].zOrder(zOrderCmd)``

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
