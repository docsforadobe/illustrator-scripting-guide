.. _jsobjref/CompoundPathItem:

CompoundPathItem
################################################################################

``app.activeDocument.activeLayer.compoundPathItems[index``

**Description**


A compound path. These objects are composed of multiple intersecting paths, resulting in transparent interior spaces where the component paths overlap. The pathItems property provides access to the paths that make up the compound path.

Paths contained within a compound path or group in a document are returned as individual paths when a script asks for the paths contained in the document. However, paths contained in a compound path or group are not returned when a script asks for the paths in a layer that contains the compound path or group.

All paths within a compound path share property values. Therefore, if you set the value of a property of any one of the paths in the compound path, the properties of all other component paths are updated with the new value.

----

==========
Properties
==========

.. _jsobjref/CompoundPathItem.artworkKnockout:

CompoundPathItem.artworkKnockout
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

:ref:`jsobjref/scripting-constants.KnockoutState`

----

.. _jsobjref/CompoundPathItem.blendingMode:

CompoundPathItem.blendingMode
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].blendingMode``

**Description**

The mode used when compositing an object.

**Type**

:ref:`jsobjref/scripting-constants.BlendModes`

----

.. _jsobjref/CompoundPathItem.controlBounds:

CompoundPathItem.controlBounds
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/CompoundPathItem.editable:

CompoundPathItem.editable
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].editable``

**Description**

If ``true``, this item is editable.

**Type**

Boolean, read-only.

----

.. _jsobjref/CompoundPathItem.geometricBounds:

CompoundPathItem.geometricBounds
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/CompoundPathItem.height:

CompoundPathItem.height
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].height``

**Description**

The height of the compound path item excluding stroke width.

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.hidden:

CompoundPathItem.hidden
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].hidden``

**Description**

If ``true``, this compound path item is hidden.

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.isIsolated:

CompoundPathItem.isIsolated
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.layer:

CompoundPathItem.layer
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].layer``

**Description**

The layer to which this compound path item belongs.

**Type**

:ref:`jsobjref/Layer`, read-only.

----

.. _jsobjref/CompoundPathItem.left:

CompoundPathItem.left
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.locked:

CompoundPathItem.locked
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].locked``

**Description**

If ``true``, this compound path item is locked.

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.name:

CompoundPathItem.name
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].name``

**Description**

The name of this compound path item.

**Type**

String.

----

.. _jsobjref/CompoundPathItem.note:

CompoundPathItem.note
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].note``

**Description**

The note assigned to this item.

**Type**

String.

----

.. _jsobjref/CompoundPathItem.opacity:

CompoundPathItem.opacity
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.parent:

CompoundPathItem.parent
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Layer` or :ref:`jsobjref/GroupItem`, read-only.

----

.. _jsobjref/CompoundPathItem.pathItems:

CompoundPathItem.pathItems
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].pathItems``

**Description**

The path art items in this compound path.

**Type**

:ref:`jsobjref/PathItems`, read-only.

----

.. _jsobjref/CompoundPathItem.position:

CompoundPathItem.position
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].position``

**Description**

The position (in points) of the top left corner of the ``compoundPathItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

----

.. _jsobjref/CompoundPathItem.selected:

CompoundPathItem.selected
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].selected``

**Description**

If ``true``, this compound path item is selected.

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.sliced:

CompoundPathItem.sliced
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].sliced``

**Description**

If ``true``, the item is sliced. Default: ``false``

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.tags:

CompoundPathItem.tags
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].tags``

**Description**

The tags contained in this object.

**Type**

:ref:`jsobjref/Tags`, read-only.

----

.. _jsobjref/CompoundPathItem.top:

CompoundPathItem.top
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.typename:

CompoundPathItem.typename
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/CompoundPathItem.uRL:

CompoundPathItem.uRL
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].uRL``

**Description**

The value of the Adobe URL tag assigned to this compound path item.

**Type**

String.

----

.. _jsobjref/CompoundPathItem.visibilityVariable:

CompoundPathItem.visibilityVariable
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

Variant.

----

.. _jsobjref/CompoundPathItem.visibleBounds:

CompoundPathItem.visibleBounds
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].visibleBounds``

**Description**

The visible bounds of the compound path item including stroke width.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/CompoundPathItem.width:

CompoundPathItem.width
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].width``

**Description**

The width of the compound path item excluding stroke width.

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.wrapInside:

CompoundPathItem.wrapInside
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.wrapOffset:

CompoundPathItem.wrapOffset
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

----

.. _jsobjref/CompoundPathItem.wrapped:

CompoundPathItem.wrapped
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

----

.. _jsobjref/CompoundPathItem.zOrderPosition:

CompoundPathItem.zOrderPosition
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].zOrderPosition``

**Description**

The position of this art item within the stacking order of the group or layer (``Parent``) that contains the art item.

**Type**

Number (long), read-only.

----

=======
Methods
=======

.. _jsobjref/CompoundPathItem.duplicate:

CompoundPathItem.duplicate()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].duplicate([relativeObject][,insertionLocation])``

**Description**

Creates a duplicate of the selected object.

**Parameters**

+-----------------------+----------------------------------------------------------------+----------------------------+
|       Parameter       |                              Type                              |        Description         |
+=======================+================================================================+============================+
| ``relativeObject``    | Object, optional                                               | Object to duplicate to     |
+-----------------------+----------------------------------------------------------------+----------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to insert element |
+-----------------------+----------------------------------------------------------------+----------------------------+

**Returns**

:ref:`jsobjref/CompoundPathItem`

----

.. _jsobjref/CompoundPathItem.move:

CompoundPathItem.move()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].move(relativeObject, insertionLocation)``

**Description**

Moves the object.

**Parameters**

+-----------------------+----------------------------------------------------------------+-------------------------------+
|       Parameter       |                              Type                              |          Description          |
+=======================+================================================================+===============================+
| ``relativeObject``    | Object                                                         | Object to move element within |
+-----------------------+----------------------------------------------------------------+-------------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to move element to   |
+-----------------------+----------------------------------------------------------------+-------------------------------+

**Returns**

Nothing.

----

.. _jsobjref/CompoundPathItem.remove:

CompoundPathItem.remove()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/CompoundPathItem.resize:

CompoundPathItem.resize()
********************************************************************************

::

    app.activeDocument.activeLayer.compoundPathItems[index].resize(
        scaleX, scaleY [,changePositions] [,changeFillPatterns] [,changeFillGradients]
        [,changeStrokePattern] [,changeLineWidths] [,scaleAbout]
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

.. _jsobjref/CompoundPathItem.rotate:

CompoundPathItem.rotate()
********************************************************************************

::

    app.activeDocument.activeLayer.compoundPathItems[index].rotate(
        angle [,changePositions] [,changeFillPatterns]
        [,changeFillGradients] [,changeStrokePattern] [,rotateAbout]
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

.. _jsobjref/CompoundPathItem.transform:

compoundPathItem.transform()
********************************************************************************

::

    app.activeDocument.activeLayer.compoundPathItems[index].transform(
        transformationMatrix [,changePositions] [,changeFillPatterns] [,changeFillGradients]
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

.. _jsobjref/CompoundPathItem.translate:

CompoundPathItem.translate()
********************************************************************************

::

    app.activeDocument.activeLayer.compoundPathItems[index].translate(
        deltaX [,deltaY] [,transformObjects] [,transformFillPatterns]
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

.. _jsobjref/CompoundPathItem.zOrder:

CompoundPathItem.zOrder()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems[index].zOrder(zOrderCmd)``

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

Selecting paths in a document
********************************************************************************

::

    // Selects all paths not part of a compound path
    if ( app.documents.length > 0 ) {
        var doc = app.activeDocument;
        var count = 0;
        if ( doc.pathItems.length > 0 ) {
            var thePaths = doc.pathItems;
            var numPaths = thePaths.length;
            for ( var i = 0; i < doc.pathItems.length; i++ ) {
            var pathArt = doc.pathItems[i];
            if ( pathArt.parent.typename != "compoundPathItem" ) {
                pathArt.selected = true;
                count++;
            }
        }
    }

Creating and modifying a compound path item
********************************************************************************

::

  // Creates a new compound path item containing 3 path
  // items, then sets the width and the color of the stroke
  // to all items in the compound path

  if (app.documents.length > 0) {
    var doc = app.activeDocument;
    var newCompoundPath = doc.activeLayer.compoundPathItems.add();

    // Create the path items
    var newPath = newCompoundPath.pathItems.add();
    newPath.setEntirePath(Array(Array(30, 50), Array(30, 100)));

    newPath = newCompoundPath.pathItems.add();
    newPath.setEntirePath(Array(Array(40, 100), Array(100, 100)));

    newPath = newCompoundPath.pathItems.add();
    newPath.setEntirePath(Array(Array(100, 110), Array(100, 300)));

    // Set stroke and width properties of the compound path
    newPath.stroked = true;
    newPath.strokeWidth = 3.5;
    newPath.strokeColor = app.activeDocument.swatches[3].color;
  }

