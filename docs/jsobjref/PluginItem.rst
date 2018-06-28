.. _jsobjref/PluginItem:

PluginItem
################################################################################

``app.activeDocument.pluginItems[index``

**Description**

An art item created by an Illustrator plug-in.

Scripts can create a plug-in item using :ref:`jsobjref/PlacedItem.trace` or :ref:`jsobjref/RasterItem.trace`, and can copy existing plug-in items using the ``duplicate`` method, but cannot create ``PluginItem`` objects directly.

----

==========
Properties
==========

.. _jsobjref/PluginItem.artworkKnockout:

PluginItem.artworkKnockout
********************************************************************************

``app.activeDocument.pluginItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/PluginItem.blendingMode:

PluginItem.blendingMode
********************************************************************************

``app.activeDocument.pluginItems[index].blendingMode``

**Description**

The blend mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/PluginItem.controlBounds:

PluginItem.controlBounds
********************************************************************************

``app.activeDocument.pluginItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PluginItem.editable:

PluginItem.editable
********************************************************************************

``app.activeDocument.pluginItems[index].editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean; read-only.

----

.. _jsobjref/PluginItem.geometricBounds:

PluginItem.geometricBounds
********************************************************************************

``app.activeDocument.pluginItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PluginItem.height:

PluginItem.height
********************************************************************************

``app.activeDocument.pluginItems[index].height``

**Description**

The height of the group item.

**Type**

Number (double)

----

.. _jsobjref/PluginItem.hidden:

PluginItem.hidden
********************************************************************************

``app.activeDocument.pluginItems[index].hidden``

**Description**

If ``true``, this item is hidden.

**Type**

Boolean

----

.. _jsobjref/PluginItem.isIsolated:

PluginItem.isIsolated
********************************************************************************

``app.activeDocument.pluginItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean

----

.. _jsobjref/PluginItem.isTracing:

PluginItem.isTracing
********************************************************************************

``app.activeDocument.pluginItems[index].isTracing``

**Description**

If ``true``, this plug-in group represents a vector art item created by tracing a raster art item.

The ``tracing`` property contains the tracing object associated with the options used to create it.

**Type**

Boolean

----

.. _jsobjref/PluginItem.layer:

PluginItem.layer
********************************************************************************

``app.activeDocument.pluginItems[index].layer``

**Description**

The layer to which this item belongs.

**Type**

:ref:`jsobjref/Layer`; read-only.

----

.. _jsobjref/PluginItem.left:

PluginItem.left
********************************************************************************

``app.activeDocument.pluginItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

----

.. _jsobjref/PluginItem.locked:

PluginItem.locked
********************************************************************************

``app.activeDocument.pluginItems[index].locked``

**Description**

If ``true``, this item is locked.

**Type**

Boolean

----

.. _jsobjref/PluginItem.name:

PluginItem.name
********************************************************************************

``app.activeDocument.pluginItems[index].name``

**Description**

The name of this item.

**Type**

String

----

.. _jsobjref/PluginItem.note:

PluginItem.note
********************************************************************************

``app.activeDocument.pluginItems[index].note``

**Description**

The note assigned to this item.

**Type**

String

----

.. _jsobjref/PluginItem.opacity:

PluginItem.opacity
********************************************************************************

``app.activeDocument.pluginItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

----

.. _jsobjref/PluginItem.parent:

PluginItem.parent
********************************************************************************

``app.activeDocument.pluginItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`

----

.. _jsobjref/PluginItem.position:

PluginItem.position
********************************************************************************

``app.activeDocument.pluginItems[index].position``

**Description**

The position (in points) of the top left corner of the ``pluginItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

----

.. _jsobjref/PluginItem.selected:

PluginItem.selected
********************************************************************************

``app.activeDocument.pluginItems[index].selected``

**Description**

If ``true``, this item is selected.

**Type**

Boolean

----

.. _jsobjref/PluginItem.sliced:

PluginItem.sliced
********************************************************************************

``app.activeDocument.pluginItems[index].sliced``

**Description**

If ``true``, the item sliced.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PluginItem.tags:

PluginItem.tags
********************************************************************************

``app.activeDocument.pluginItems[index].tags``

**Description**

The tags contained in this item.

**Type**

:ref:`jsobjref/Tags`; read-only.

----

.. _jsobjref/PluginItem.top:

PluginItem.top
********************************************************************************

``app.activeDocument.pluginItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

----

.. _jsobjref/PluginItem.tracing:

PluginItem.tracing
********************************************************************************

``app.activeDocument.pluginItems[index].tracing``

**Description**

When this plug-in group was created by tracing (``isTracing`` is ``true``), the tracing object associated with the options used to create it.

**Type**

:ref:`jsobjref/TracingObject`

----

.. _jsobjref/PluginItem.typename:

PluginItem.typename
********************************************************************************

``app.activeDocument.pluginItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

.. _jsobjref/PluginItem.uRL:

PluginItem.uRL
********************************************************************************

``app.activeDocument.pluginItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

----

.. _jsobjref/PluginItem.visibilityVariable:

PluginItem.visibilityVariable
********************************************************************************

``app.activeDocument.pluginItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

:ref:`jsobjref/Variable`

----

.. _jsobjref/PluginItem.visibleBounds:

PluginItem.visibleBounds
********************************************************************************

``app.activeDocument.pluginItems[index].visibleBounds``

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

----

.. _jsobjref/PluginItem.width:

PluginItem.width
********************************************************************************

``app.activeDocument.pluginItems[index].width``

**Description**

The width of the item.

**Type**

Number (double)

----

.. _jsobjref/PluginItem.wrapInside:

PluginItem.wrapInside
********************************************************************************

``app.activeDocument.pluginItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean

----

.. _jsobjref/PluginItem.wrapOffset:

PluginItem.wrapOffset
********************************************************************************

``app.activeDocument.pluginItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

----

.. _jsobjref/PluginItem.wrapped:

PluginItem.wrapped
********************************************************************************

``app.activeDocument.pluginItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

----

.. _jsobjref/PluginItem.zOrderPosition:

PluginItem.zOrderPosition
********************************************************************************

``app.activeDocument.pluginItems[index].zOrderPosition``

**Description**

The position of this item within the stacking order of the group or layer (``parent``) that contains the item.

**Type**

Number; read-only.

----

=======
Methods
=======

.. _jsobjref/PluginItem.duplicate:

PluginItem.duplicate()
********************************************************************************

``app.activeDocument.pluginItems[index].duplicate([relativeObject][, insertionLocation])``

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

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/PluginItem.move:

PluginItem.move()
********************************************************************************

``app.activeDocument.pluginItems[index].move(relativeObject, insertionLocation)``

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

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/PluginItem.remove:

PluginItem.remove()
********************************************************************************

``app.activeDocument.pluginItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/PluginItem.resize:

PluginItem.resize()
********************************************************************************

``app.activeDocument.pluginItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])``

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

.. _jsobjref/PluginItem.rotate:

PluginItem.rotate()
********************************************************************************

``app.activeDocument.pluginItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])``

**Description**

Rotates the art item relative to the current rotation.

The object is rotated counter-clockwise if the ``angle`` value is positive, clockwise if the value is negative.

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

.. _jsobjref/PluginItem.transform:

PluginItem.transform()
********************************************************************************

``app.activeDocument.pluginItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])``

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

.. _jsobjref/PluginItem.translate:

PluginItem.translate()
********************************************************************************

``app.activeDocument.pluginItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])``

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

.. _jsobjref/PluginItem.zOrder:

PluginItem.zOrder()
********************************************************************************

``app.activeDocument.pluginItems[index].zOrder(zOrderCmd)``

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

----

=======
Example
=======

.. _jsobjref/PluginItem.copying-a-plugin-item:

Copying a plug-in item
********************************************************************************

::

  // Creates new plug-in art by copying an existing plug-in art item
  if (app.documents.length > 0 && app.activeDocument.pluginItems.length > 0) {
    var doc = app.activeDocument;
    var pluginArt = doc.pluginItems[0];
    pluginArt.duplicate(pluginArt.parent, ElementPlacement.PLACEATBEGINNING);
  }
