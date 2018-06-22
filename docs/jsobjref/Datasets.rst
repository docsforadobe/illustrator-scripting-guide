.. _jsobjref/Datasets:

Datasets
################################################################################

``dataSets``

**Description**

A collection of :ref:`jsobjref/Dataset` objects.

----

==========
Properties
==========

.. _jsobjref/Datasets.length:

Datasets.length
********************************************************************************

``app.activeDocument.dataSets.length``

**Description**

The number of datasets in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Datasets.parent:

Datasets.parent
********************************************************************************

``app.activeDocument.dataSets.parent``

**Description**

The name of the object that contains this dataset.

**Type**

:ref:`jsobjref/Document`, read-only.

----

.. _jsobjref/Datasets.typename:

Datasets.typename
********************************************************************************

``app.activeDocument.dataSets.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Datasets.add:

Datasets.add()
********************************************************************************

``app.activeDocument.dataSets.add()``

**Description**

Creates a new dataset object.

**Returns**

:ref:`jsobjref/Dataset`

----

.. _jsobjref/Datasets.getByName:

Datasets.getByName()
********************************************************************************

``app.activeDocument.dataSets.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/Dataset`

----

.. _jsobjref/Datasets.index:

Datasets.index()
********************************************************************************

``app.activeDocument.dataSets.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/Dataset`

----

.. _jsobjref/Datasets.removeAll:

Datasets.removeAll()
********************************************************************************

``app.activeDocument.dataSets.removeAll()``

**Description**

Removes all elements in the collection.

**Returns**

Nothing.
