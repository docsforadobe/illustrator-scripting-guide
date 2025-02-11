.. _jsobjref/Artboards:

Artboards
################################################################################

``artboards``

**Description**

A collection of Artboard objects.

==========
Properties
==========

.. _jsobjref/Artboards.length:

Artboards.length
********************************************************************************

``artboards.length``

**Description**

The number of datasets in the collection

**Type**

Number; read-only.

----

.. _jsobjref/Artboards.parent:

Artboards.parent
********************************************************************************

``artboards.parent``

**Description**

The name of the object that contains this dataset

**Type**

:ref:`jsobjref/Artboard`; read-only.


----

.. _jsobjref/Artboards.typename:

Artboards.typename
********************************************************************************

``artboards.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/Artboards.add:

Artboards.add()
********************************************************************************

``artboards.add(artboardRect)``

**Description**

Creates a new Artboard object.

**Parameters**

+------------------+------+---------------------+
|    Parameter     | Type |     Description     |
+==================+======+=====================+
| ``artboardRect`` | Rect | Artboard dimensions |
+------------------+------+---------------------+

**Returns**

:ref:`jsobjref/Artboard`

----

.. _jsobjref/Artboards.getActiveArtboardIndex:

Artboards.getActiveArtboardIndex()
********************************************************************************

``artboards.getActiveArtboardIndex()``

**Description**

Retrieves the index position of the active artboard in the document's list.

Returns the 0-based index.

**Returns**

Number (long)

----

.. _jsobjref/Artboards.getByName:

Artboards.getByName()
********************************************************************************

``artboards.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/Artboard`

----

.. _jsobjref/Artboards.insert:

Artboards.insert()
********************************************************************************

``artboards.insert(artboardRect, index)``

**Description**

Creates a new Artboard object and inserts it at the given index in the list.

**Parameters**

+------------------+---------------+-----------------------------+
|    Parameter     |     Type      |         Description         |
+==================+===============+=============================+
| ``artboardRect`` | Rect          | Artboard dimensions         |
+------------------+---------------+-----------------------------+
| ``index``        | Number (long) | Index to insert artboard at |
+------------------+---------------+-----------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Artboards.remove:

Artboards.remove()
********************************************************************************

``artboards.remove(index)``

**Description**

Deletes an artboard object. You cannot remove the last artboard in a document.

**Parameters**

+-----------+---------------+-----------------------------+
| Parameter |     Type      |         Description         |
+===========+===============+=============================+
| ``index`` | Number (long) | Index of artboard to remove |
+-----------+---------------+-----------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Artboards.setActiveArtboardIndex:

Artboards.setActiveArtboardIndex()
********************************************************************************

``artboards.setActiveArtboardIndex(index)``

**Description**

Makes a specific artboard active and makes it current in the iteration order.

**Parameters**

+-----------+---------------+---------------------------------+
| Parameter |     Type      |           Description           |
+===========+===============+=================================+
| ``index`` | Number (long) | Index of artboard to set active |
+-----------+---------------+---------------------------------+

**Returns**

Nothing.
