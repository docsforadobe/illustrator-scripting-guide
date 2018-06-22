.. _jsobjref/gradientStops:

Gradient Stops
################################################################################

``gradientStops``

**Description**

A collection of ``GradientStop`` objects in a specific gradient. The elements are not named; you must access them by index.

----

==========
Properties
==========

.. _jsobjref/gradientStops.length:

GradientStops.length
********************************************************************************

``gradientStops.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/gradientStops.parent:

GradientStops.parent
********************************************************************************

``gradientStops.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/gradientStops.typename:

GradientStops.typename
********************************************************************************

``gradientStops.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/gradientStops.add:

GradientStops.add()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops.add()``

**Description**

Creates a new object.

**Returns**

:ref:`jsobjref/gradientStop`

----

.. _jsobjref/gradientStops.getByName:

GradientStops.getByName()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/gradientStop`

----

.. _jsobjref/gradientStops.index:

GradientStops.index()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+--------+-------------+
|  Parameter  |  Type  | Description |
+=============+========+=============+
| ``itemKey`` | Number | todo        |
+-------------+--------+-------------+

**Returns**

:ref:`jsobjref/gradientStop`

----

.. _jsobjref/gradientStops.removeAll:

GradientStops.removeAll()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops.removeAll()``

**Description**

Deletes all objects in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Adding a new gradient stop
********************************************************************************

::

    // Adds a new gradient stop to a gradient, color of new stop is 70% gray
    if ( app.documents.length > 0 && app.activeDocument.gradients.length > 0 ) {
        // Get a reference to the gradient to change
        var changeGradient = app.activeDocument.gradients[0];

        // Get a reference to the last gradient stop
        var origCount = changeGradient.gradientStops.length;
        var lastStop = changeGradient.gradientStops[origCount-1];

        // add the new gradient stop
        var newStop = changeGradient.gradientStops.add();

        // Set the values of the new gradient stop.
        // Move the original last gradient stop a bit to the left and insert the new gradient stop at the old position
        newStop.rampPoint = lastStop.rampPoint;
        lastStop.rampPoint = lastStop.rampPoint - 10;

        // Create a new color to apply to the newly created gradient stop
        var newStopColor = new GrayColor();
        newStopColor.gray = 70.0;
        newStop.color = newStopColor;
    }
