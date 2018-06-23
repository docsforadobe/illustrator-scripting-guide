.. _jsobjref/Lines:

Lines
################################################################################

``lines``

**Description**

A collection of ``TextRange`` objects representing lines of text in a text frame. The elements are not named; you must access them by index.

----

==========
Properties
==========

.. _jsobjref/Lines.length:

Lines.length
********************************************************************************

``lines.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Lines.parent:

Lines.parent
********************************************************************************

``lines.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/Lines.typename:

Lines.typename
********************************************************************************

``lines.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Lines.index:

Lines.index()
********************************************************************************

``lines.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+------+-------------+
|  Parameter  | Type | Description |
+=============+======+=============+
| ``itemKey`` | Type | todo        |
+-------------+------+-------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/Lines.removeAll:

Lines.removeAll()
********************************************************************************

``lines.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
