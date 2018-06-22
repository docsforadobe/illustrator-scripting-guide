.. _jsobjref/Gradients:

Gradients
################################################################################

``gradients``

**Description**

A collection of :ref:`jsobjref/Gradient` objects in a document.

----

==========
Properties
==========

.. _jsobjref/Gradients.length:

Gradients.length
********************************************************************************

``gradients.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Gradients.parent:

Gradients.parent
********************************************************************************

``gradients.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/Gradients.typename:

Gradients.typename
********************************************************************************

``gradients.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Gradients.add:

Gradients.add()
********************************************************************************

``app.activeDocument.gradients.add()``

**Description**

Creates a new ``Gradient`` object.

**Returns**

:ref:`jsobjref/Gradient`

----

.. _jsobjref/Gradients.getByName:

Gradients.getByName()
********************************************************************************

``app.activeDocument.gradients.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/Gradient`

----

.. _jsobjref/Gradients.index:

Gradients.index()
********************************************************************************

``app.activeDocument.gradients.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/Gradient`

----

.. _jsobjref/Gradients.removeAll:

Gradients.removeAll()
********************************************************************************

``app.activeDocument.gradients.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Removing a gradient
********************************************************************************

::

    // Deletes the first gradient from the current document
    if ( app.documents.length > 0 ) {
        app.activeDocument.gradients[0].remove();
    }