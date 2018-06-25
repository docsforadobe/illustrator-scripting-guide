.. _jsobjref/SwatchGroups:

SwatchGroups
################################################################################

``swatchGroups``

**Description**

A collection of :ref:`jsobjref/SwatchGroup` objects.

----

==========
Properties
==========

.. _jsobjref/SwatchGroups.length:

SwatchGroups.length
********************************************************************************

``swatchGroups.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/SwatchGroups.parent:

SwatchGroups.parent
********************************************************************************

``swatchGroups.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/SwatchGroups.typename:

SwatchGroups.typename
********************************************************************************

``swatchGroups.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/SwatchGroups.add:

SwatchGroups.add()
********************************************************************************

``swatchGroups.add()``

**Description**

Creates a swatch group.

**Returns**

:ref:`jsobjref/SwatchGroup`

----

.. _jsobjref/SwatchGroups.getByName:

SwatchGroups.getByName()
********************************************************************************

``swatchGroups.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/SwatchGroup`

----

.. _jsobjref/SwatchGroups.removeAll:

SwatchGroups.removeAll()
********************************************************************************

``swatchGroups.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
