.. _jsobjref/compoundPathItem:

Compound Path Item
################################################################################

``compoundPathItem``

**Description**


A compound path. These objects are composed of multiple intersecting paths, resulting in transparent interior spaces where the component paths overlap. The pathItems property provides access to the paths that make up the compound path.

Paths contained within a compound path or group in a document are returned as individual paths when a script asks for the paths contained in the document. However, paths contained in a compound path or group are not returned when a script asks for the paths in a layer that contains the compound path or group.

All paths within a compound path share property values. Therefore, if you set the value of a property of any one of the paths in the compound path, the properties of all other component paths are updated with the new value.

----

==========
Properties
==========

.. _compoundPathItem.artworkKnockout:

compoundPathItem.artworkKnockout
********************************************************************************

``compoundPathItem.artworkKnockout``

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

// todo: link to KnockoutState in Chapter #2 "Scripting Constants"..
KnockoutState.

----

.. _compoundPathItem.blendingMode:

compoundPathItem.blendingMode
********************************************************************************

``compoundPathItem.blendingMode``

**Description**

The mode used when compositing an object.

**Type**

// todo: link to BlendModes in Chapter #2 "Scripting Constants"..
BlendModes.

----

.. _compoundPathItem.controlBounds:

compoundPathItem.controlBounds
********************************************************************************

``compoundPathItem.controlBounds``

**Description**

The bounds of the object including stroke width and controls.

**Type**

``array`` of 4 numbers; read-only.

----

.. _compoundPathItem.editable:

compoundPathItem.editable
********************************************************************************

``compoundPathItem.editable``

**Description**

If ``true``, this item is editable.

**Type**

``boolean``; read-only.

----

.. _compoundPathItem.geometricBounds:

compoundPathItem.geometricBounds
********************************************************************************

``compoundPathItem.geometricBounds``

**Description**

The bounds of the object excluding stroke width.

**Type**

``array`` of 4 numbers; read-only.

----

.. _compoundPathItem.height:

compoundPathItem.height
********************************************************************************

``compoundPathItem.height``

**Description**

The height of the compound path item excluding stroke width.

**Type**

``number (double)``

----

.. _compoundPathItem.hidden:

compoundPathItem.hidden
********************************************************************************

``compoundPathItem.hidden``

**Description**

If ``true``, this compound path item is hidden.

**Type**

``boolean``

----

.. _compoundPathItem.isIsolated:

compoundPathItem.isIsolated
********************************************************************************

``compoundPathItem.isIsolated``

**Description**

If ``true``, this object is isolated.

**Type**

``boolean``

----

.. _compoundPathItem.layer:

compoundPathItem.layer
********************************************************************************

``compoundPathItem.layer``

**Description**

The layer to which this compound path item belongs.

**Type**

// todo: link to Layer in Chapter #1 "JavaScript Object Reference"..
Layer; read-only.

----

.. _compoundPathItem.left:

compoundPathItem.left
********************************************************************************

``compoundPathItem.left``

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

``number (double)``

----

.. _compoundPathItem.locked:

compoundPathItem.locked
********************************************************************************

``compoundPathItem.locked``

**Description**

If ``true``, this compound path item is locked.

**Type**

``boolean``

----

.. _compoundPathItem.name:

compoundPathItem.name
********************************************************************************

``compoundPathItem.name``

**Description**

The name of this compound path item.

**Type**

``string``

----

.. _compoundPathItem.note:

compoundPathItem.note
********************************************************************************

``compoundPathItem.note``

**Description**

The note assigned to this item.

**Type**

``string``

----

.. _compoundPathItem.opacity:

compoundPathItem.opacity
********************************************************************************

``compoundPathItem.opacity``

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

``number (double)``

----

.. _compoundPathItem.parent:

compoundPathItem.parent
********************************************************************************

``compoundPathItem.parent``

**Description**

The parent of this object.

**Type**

// todo: link to ``Layer`` and ``GroupItem`` in Chapter #1 "JavaScript Object Reference"..
Layer or GroupItem; read-only.

----

.. _compoundPathItem.pathItems:

compoundPathItem.pathItems
********************************************************************************

``compoundPathItem.pathItems``

**Description**

The path art items in this compound path.

**Type**

// todo: link to ``PathItems`` in Chapter #1 "JavaScript Object Reference"..
PathItems; read-only.

----

.. _compoundPathItem.position:

compoundPathItem.position
********************************************************************************

``compoundPathItem.pathItems``

**Description**

The position (in points) of the top left corner of the ``compoundPathItem`` object in the format [x, y]. Does not include stroke weight.

**Type**

``array`` of 2 numbers

----

.. _compoundPathItem.selected:

compoundPathItem.selected
********************************************************************************

``compoundPathItem.pathItems``

**Description**

If ``true``, this compound path item is selected.

**Type**

``boolean``

----

.. _compoundPathItem.sliced:

compoundPathItem.sliced
********************************************************************************

``compoundPathItem.sliced``

**Description**

If ``true``, the item is sliced. Default: ``false``

**Type**

``boolean``

----

.. _compoundPathItem.tags:

compoundPathItem.tags
********************************************************************************

``compoundPathItem.tags``

**Description**

The tags contained in this object.

**Type**

// todo: link to ``Tags`` in Chapter #1 "JavaScript Object Reference"..
Tags; Read-only.

----

.. _compoundPathItem.top:

compoundPathItem.top
********************************************************************************

``compoundPathItem.top``

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

``number (double)``

----

.. _compoundPathItem.typename:

compoundPathItem.typename
********************************************************************************

``compoundPathItem.typename``

**Description**

The class name of the referenced object.

**Type**

``string``; read-only.

----

.. _compoundPathItem.uRL:

compoundPathItem.uRL
********************************************************************************

``compoundPathItem.uRL``

**Description**

The value of the Adobe URL tag assigned to this compound path item.

**Type**

``string``

----

.. _compoundPathItem.visibilityVariable:

compoundPathItem.visibilityVariable
********************************************************************************

``compoundPathItem.visibilityVariable``

**Description**

The visibility variable bound to the item.

**Type**

``Variant``

----

.. _compoundPathItem.visibleBounds:

compoundPathItem.visibleBounds
********************************************************************************

``compoundPathItem.visibleBounds``

**Description**

The visible bounds of the compound path item including stroke width.

**Type**

``array`` of 4 numbers; read-only.

----

.. _compoundPathItem.width:

compoundPathItem.width
********************************************************************************

``compoundPathItem.width``

**Description**

The width of the compound path item excluding stroke width.

**Type**

``number (double)``

----

.. _compoundPathItem.wrapInside:

compoundPathItem.wrapInside
********************************************************************************

``compoundPathItem.wrapInside``

**Description**

If ``true``, the text frame object should be wrapped inside this object.

**Type**

``boolean``

----

.. _compoundPathItem.wrapOffset:

compoundPathItem.wrapOffset
********************************************************************************

``compoundPathItem.wrapOffset``

**Description**

The offset to use when wrapping text around this object.

**Type**

``number (double)``

----

.. _compoundPathItem.wrapped:

compoundPathItem.wrapped
********************************************************************************

``compoundPathItem.wrapped``

**Description**

If ``true``, wrap text frame objects around this object (text frame must be above the object).

**Type**

``boolean``

----

.. _compoundPathItem.zOrderPosition:

compoundPathItem.zOrderPosition
********************************************************************************

``compoundPathItem.zOrderPosition``

**Description**

The position of this art item within the stacking order of the group or layer (``Parent``) that contains the art item.

**Type**

``number (long)``; read-only.

----

=======
Methods
=======

.. _compoundPathItem.duplicate:

compoundPathItem.duplicate()
********************************************************************************

``compoundPathItem.duplicate``

**Description**

Creates a duplicate of the selected object.

**Parameters**

+-------------------------+----------------------------------+
|        Parameter        |          Parameter Type          |
+=========================+==================================+
| ``[relativeObject]``    | object                           |
+-------------------------+----------------------------------+
| ``[insertionLocation]`` | :ref:`jsobjref/elementPlacement` |
+-------------------------+----------------------------------+

**Returns**

:ref:`jsobjref/compoundPathItem`

----

.. _compoundPathItem.move:

compoundPathItem.move()
********************************************************************************

``compoundPathItem.move``

**Description**

Moves the object.

**Parameters**

+-----------------------+----------------------------------+
|       Parameter       |          Parameter Type          |
+=======================+==================================+
| ``relativeObject``    | object                           |
+-----------------------+----------------------------------+
| ``insertionLocation`` | :ref:`jsobjref/elementPlacement` |
+-----------------------+----------------------------------+

**Returns**

Nothing

----

.. _compoundPathItem.remove:

compoundPathItem.remove()
********************************************************************************

``compoundPathItem.remove``

**Description**

Deletes this object.

**Parameters**

None

**Returns**

Nothing

----

.. _compoundPathItem.resize:

compoundPathItem.resize()
********************************************************************************

``compoundPathItem.resize``

**Description**

Scales the art item where ``scaleX`` is the horizontal scaling factor and ``scaleY`` is the vertical scaling factor. 100.0 = 100%.

**Parameters**

+---------------------------+--------------------------------+
|         Parameter         |         Parameter Type         |
+===========================+================================+
| ``scaleX``                | ``number (double)``            |
+---------------------------+--------------------------------+
| ``scaleY``                | ``number (double)``            |
+---------------------------+--------------------------------+
| ``[changePositions]``     | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillPatterns]``  | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillGradients]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeStrokePattern]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeLineWidths]``    | ``number (double)``            |
+---------------------------+--------------------------------+
| ``[scaleAbout]``          | :ref:`jsobjref/transformation` |
+---------------------------+--------------------------------+

**Returns**

Nothing

----

.. _compoundPathItem.rotate:

compoundPathItem.rotate()
********************************************************************************

``compoundPathItem.rotate``

**Description**

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the ``angle`` value is positive, clockwise if the value is negative.

**Parameters**

+---------------------------+--------------------------------+
|         Parameter         |         Parameter Type         |
+===========================+================================+
| ``angle``                 | ``number (double)``            |
+---------------------------+--------------------------------+
| ``[changePositions]``     | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillPatterns]``  | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillGradients]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeStrokePattern]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[rotateAbout]``         | :ref:`jsobjref/transformation` |
+---------------------------+--------------------------------+

**Returns**

Nothing

----

.. _compoundPathItem.transform:

compoundPathItem.transform()
********************************************************************************

``compoundPathItem.transform``

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

+---------------------------+--------------------------------+
|         Parameter         |         Parameter Type         |
+===========================+================================+
| ``transformationMatrix``  | ``Matrix``                     |
+---------------------------+--------------------------------+
| ``[changePositions]``     | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillPatterns]``  | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeFillGradients]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeStrokePattern]`` | ``boolean``                    |
+---------------------------+--------------------------------+
| ``[changeLineWidths]``    | ``number (double)``            |
+---------------------------+--------------------------------+
| ``[transformAbout]``      | :ref:`jsobjref/transformation` |
+---------------------------+--------------------------------+

**Returns**

Nothing

----

.. _compoundPathItem.translate:

compoundPathItem.translate()
********************************************************************************

``compoundPathItem.translate``

**Description**

Repositions the art item relative to the current position, where ``deltaX`` is the horizontal offset and ``deltaY`` is the vertical offset.

**Parameters**

+-------------------------------+---------------------+
|           Parameter           |   Parameter Type    |
+===============================+=====================+
| ``[deltaX]``                  | ``number (double)`` |
+-------------------------------+---------------------+
| ``[deltaY]``                  | ``number (double)`` |
+-------------------------------+---------------------+
| ``[transformObjects]``        | ``boolean``         |
+-------------------------------+---------------------+
| ``[transformFillPatterns]``   | ``boolean``         |
+-------------------------------+---------------------+
| ``[transformFillGradients]``  | ``boolean``         |
+-------------------------------+---------------------+
| ``[transformStrokePatterns]`` | ``boolean``         |
+-------------------------------+---------------------+

**Returns**

Nothing

----

.. _compoundPathItem.zOrder:

compoundPathItem.zOrder()
********************************************************************************

``compoundPathItem.zOrder``

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

+---------------+------------------------------+
|   Parameter   |        Parameter Type        |
+===============+==============================+
| ``zOrderCmd`` | :ref:`jsobjref/ZOrderMethod` |
+---------------+------------------------------+

**Returns**

Nothing

----

=======
Example
=======

Selecting paths in a document
********************************************************************************

::

    // Selects all paths not part of a compound path
    if ( app.documents.length > 0 ) {
        doc = app.activeDocument;
        count = 0;
        if ( doc.pathItems.length > 0 ) {
            thePaths = doc.pathItems;
            numPaths = thePaths.length;
            for ( i = 0; i < doc.pathItems.length; i++ ) {
            pathArt = doc.pathItems[i];
            if ( pathArt.parent.typename != "CompoundPathItem" ) {
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

    if ( app.documents.length > 0 ) {
        doc = app.activeDocument;
        newCompoundPath = doc.activeLayer.compoundPathItems.add();
        
        // Create the path items
        newPath = newCompoundPath.pathItems.add();
        newPath.setEntirePath( Array( Array(30, 50), Array(30, 100) ) );
        
        newPath = newCompoundPath.pathItems.add();
        newPath.setEntirePath( Array( Array(40, 100), Array(100, 100) ) );

        newPath = newCompoundPath.pathItems.add();
        newPath.setEntirePath( Array( Array(100, 110), Array(100, 300) ) );

        // Set stroke and width properties of the compound path
        newPath.stroked = true;
        newPath.strokeWidth = 3.5;
        newPath.strokeColor = app.activeDocument.swatches[3].color;
    }