.. _jsobjref/PathPoints:

PathPoints
################################################################################

``app.activeDocument.pathItems[index].pathPoints``

**Description**

A collection of :ref:`jsobjref/PathPoint` objects in a specific path.

The elements are not named; you must access them by index.

----

==========
Properties
==========

.. _jsobjref/PathPoints.length:

PathPoints.length
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/PathPoints.parent:

PathPoints.parent
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/PathPoints.typename:

PathPoints.typename
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/PathPoints.add:

PathPoints.add()
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.add()``

**Description**

Creates a new object.

**Returns**

:ref:`jsobjref/PathPoint`

----

.. _jsobjref/PathPoints.index:

PathPoints.index()
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/PathPoint`

----

.. _jsobjref/PathPoints.removeAll:

PathPoints.removeAll()
********************************************************************************

``app.activeDocument.pathItems[index].pathPoints.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

----

=======
Example
=======

Adding a path point to a path
********************************************************************************

::

  // Appends a new PathPoint to an existing path
  // and initializes its anchor and handle points.
  if (app.documents.length > 0) {
    var doc = app.activeDocument;

    var line = doc.pathItems.add();
    line.stroked = true;
    line.setEntirePath(Array(Array(220, 475), Array(375, 300)));

    // Append another point to the line
    var newPoint = doc.pathItems[0].pathPoints.add();
    newPoint.anchor = Array(220, 300);
    newPoint.leftDirection = newPoint.anchor;
    newPoint.rightDirection = newPoint.anchor;
    newPoint.pointType = PointType.CORNER;
  }
