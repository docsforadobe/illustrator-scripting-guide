.. _jsobjref/compoundPathItems:

Compound Path Items
################################################################################

``compoundPathItems``

**Description**

A collection of :ref:`jsobjref/compoundPathItem` objects.

----

==========
Properties
==========

.. _jsobjref/compoundPathItems.length:

compoundPathItems.length
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/compoundPathItems.parent:

compoundPathItems.parent
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.parent``

**Description**

The parent of this collection (either a ``Layer`` or a ``GroupItem``).

**Type**

Object, read-only.

----

.. _jsobjref/compoundPathItems.typename:

compoundPathItems.typename
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/compoundPathItems.add:

compoundPathItems.add()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.add()``

**Description**

Creates a new ``CompoundPathItem``.

**Returns**

:ref:`jsobjref/compoundPathItem`

----

.. _jsobjref/compoundPathItems.getByName:

compoundPathItems.getByName()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/compoundPathItem`

----

.. _jsobjref/compoundPathItems.index:

compoundPathItems.index()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/compoundPathItem`

----

.. _jsobjref/compoundPathItems.removeAll:

compoundPathItems.removeAll()
********************************************************************************

``app.activeDocument.activeLayer.compoundPathItems.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Counting compound paths
********************************************************************************

::

    // Counts all compound path items in layer 1 of the current document
    if ( app.documents.length > 0 ) {
        var doc = app.activeDocument;
        var numCompoundPaths = doc.layers[0].compoundPathItems.length;
    }
