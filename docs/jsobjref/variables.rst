.. _jsobjref/variables:

Variables
################################################################################

``app.activeDocument.variables``

**Description**

The collection of Variable objects in the document.

For an example of how to create variables, see :ref:`jsobjref/dataset.usingVariablesAndDatasets`.

----

==========
Properties
==========

.. _jsobjref/variables.length:

variables.length
********************************************************************************

``app.activeDocument.variables.length``

**Description**

The number of variables in the document

**Type**

Number; read-only.

----

.. _jsobjref/variables.parent:

variables.parent
********************************************************************************

``app.activeDocument.variables.parent``

**Description**

The object that contains the collection of variables

**Type**

Object; read-only.

----

.. _jsobjref/variables.typename:

variables.typename
********************************************************************************

``app.activeDocument.variables.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/variables.add:

variables.add()
********************************************************************************

``app.activeDocument.variables.add()``

**Description**

Adds a new variable to the collection.

**Returns**

:ref:`jsobjref/Variable`

----

.. _jsobjref/variables.getByName:

variables.getByName()
********************************************************************************

``app.activeDocument.variables.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/Variable`

----

.. _jsobjref/variables.index:

variables.index()
********************************************************************************

``app.activeDocument.variables.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/Variable`

----

.. _jsobjref/variables.removeAll:

variables.removeAll()
********************************************************************************

``app.activeDocument.variables.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
