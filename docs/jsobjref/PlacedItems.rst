.. _jsobjref/PlacedItems:

PlacedItems
################################################################################

``app.activeDocument.placedItems``

**Description**

A collection of :ref:`jsobjref/PlacedItem` objects in a document.

----

==========
Properties
==========

.. _jsobjref/PlacedItems.length:

PlacedItems.length
********************************************************************************

``app.activeDocument.placedItems.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/PlacedItems.parent:

PlacedItems.parent
********************************************************************************

``app.activeDocument.placedItems.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/PlacedItems.typename:

PlacedItems.typename
********************************************************************************

``app.activeDocument.placedItems.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/PlacedItems.add:

PlacedItems.add()
********************************************************************************

``app.activeDocument.placedItems.add()``

**Description**

Creates a new object.

Use to place new art in a document. Use the ``file`` property of the resulting ``placedItem`` object to link the file containing the artwork. See :ref:`jsobjref/PlacedItem`.

**Returns**

:ref:`jsobjref/PlacedItem`

----

.. _jsobjref/PlacedItems.getByName:

PlacedItems.getByName()
********************************************************************************

``app.activeDocument.placedItems.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/PlacedItem`

----

.. _jsobjref/PlacedItems.index:

PlacedItems.index()
********************************************************************************

``app.activeDocument.placedItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/PlacedItem`

----

.. _jsobjref/PlacedItems.removeAll:

PlacedItems.removeAll()
********************************************************************************

``app.activeDocument.placedItems.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
