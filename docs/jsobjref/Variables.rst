.. _jsobjref/Variables:

Variables
################################################################################

``app.activeDocument.variables``

**Description**

The collection of :ref:`jsobjref/Variable` objects in the document.

For an example of how to create variables, see :ref:`jsobjref/Dataset.usingVariablesAndDatasets`.

----

==========
Properties
==========

.. _jsobjref/Variables.length:

Variables.length
********************************************************************************

``app.activeDocument.variables.length``

**Description**

The number of variables in the document

**Type**

Number; read-only.

----

.. _jsobjref/Variables.parent:

Variables.parent
********************************************************************************

``app.activeDocument.variables.parent``

**Description**

The object that contains the collection of variables

**Type**

Object; read-only.

----

.. _jsobjref/Variables.typename:

Variables.typename
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

.. _jsobjref/Variables.add:

Variables.add()
********************************************************************************

``app.activeDocument.variables.add()``

**Description**

Adds a new variable to the collection.

**Returns**

:ref:`jsobjref/Variable`

----

.. _jsobjref/Variables.getByName:

Variables.getByName()
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

.. _jsobjref/Variables.index:

Variables.index()
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

.. _jsobjref/Variables.removeAll:

Variables.removeAll()
********************************************************************************

``app.activeDocument.variables.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
