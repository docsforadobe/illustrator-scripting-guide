.. _jsobjref/gradients:

Gradients
################################################################################

``gradients``

**Description**

A collection of ``Gradient`` objects in a document.

----

==========
Properties
==========

.. _jsobjref/gradients.length:

gradients.length
********************************************************************************

``gradients.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/gradients.parent:

gradients.parent
********************************************************************************

``gradients.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/gradients.typename:

gradients.typename
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

.. _jsobjref/gradients.add:

gradients.add()
********************************************************************************

``app.activeDocument.gradients.add()``

**Description**

Creates a new ``Gradient`` object.

**Returns**

:ref:`jsobjref/gradient`

----

.. _jsobjref/gradients.getByName:

gradients.getByName()
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

:ref:`jsobjref/gradient`

----

.. _jsobjref/gradients.index:

gradients.index()
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

:ref:`jsobjref/gradient`

----

.. _jsobjref/gradients.removeAll:

gradients.removeAll()
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