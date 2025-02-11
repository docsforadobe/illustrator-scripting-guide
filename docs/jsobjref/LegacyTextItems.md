.. _jsobjref/LegacyTextItems:

LegacyTextItems
################################################################################

``legacyTextItems``

**Description**

A collection of :ref:`jsobjref/LegacyTextItem` objects.

----

==========
Properties
==========

.. _jsobjref/LegacyTextItems.length:

LegacyTextItems.length
********************************************************************************

``legacyTextItems.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/LegacyTextItems.parent:

LegacyTextItems.parent
********************************************************************************

``legacyTextItems.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/LegacyTextItems.typename:

LegacyTextItems.typename
********************************************************************************

``legacyTextItems.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/LegacyTextItems.convertToNative:

LegacyTextItems.convertToNative()
********************************************************************************

``legacyTextItems.convertToNative()``

**Description**

Creates text frames from all legacy text items; the original legacy text items are deleted. Returns ``true`` on success.

**Returns**

Boolean.

----

.. _jsobjref/LegacyTextItems.getByName:

LegacyTextItems.getByName()
********************************************************************************

``legacyTextItems.getByName(name)``

**Description**

Get the first element in the collection with the specified name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/LegacyTextItem`

----

.. _jsobjref/LegacyTextItems.index:

LegacyTextItems.index()
********************************************************************************

``legacyTextItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/LegacyTextItem`

----

.. _jsobjref/LegacyTextItems.removeAll:

LegacyTextItems.removeAll()
********************************************************************************

``legacyTextItems.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
