.. _jsobjref/datasets:

Datasets
################################################################################

``dataSets``

**Description**

A collection of :ref:`jsobjref/dataset` objects.

----

==========
Properties
==========

.. _jsobjref/datasets.length:

Datasets.length
********************************************************************************

``app.activeDocument.dataSets.length``

**Description**

The number of datasets in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/datasets.parent:

Datasets.parent
********************************************************************************

``app.activeDocument.dataSets.parent``

**Description**

The name of the object that contains this dataset.

**Type**

:ref:`jsobjref/document`, read-only.

----

.. _jsobjref/datasets.typename:

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

.. _jsobjref/datasets.add:

Datasets.add()
********************************************************************************

``app.activeDocument.dataSets.add()``

**Description**

Creates a new dataset object.

**Returns**

:ref:`jsobjref/dataset`

----

.. _jsobjref/datasets.getByName:

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

:ref:`jsobjref/dataset`

----

.. _jsobjref/datasets.index:

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

:ref:`jsobjref/dataset`

----

.. _jsobjref/datasets.removeAll:

Datasets.removeAll()
********************************************************************************

``app.activeDocument.dataSets.removeAll()``

**Description**

Removes all elements in the collection.

**Returns**

Nothing.
