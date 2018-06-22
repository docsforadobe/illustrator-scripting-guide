.. _jsobjref/Brushes:

Brushes
################################################################################

``app.activeDocument.brushes``

**Description**

A collection of brush objects in a document.

----

==========
Properties
==========

.. _jsobjref/Brushes.length:

Brushes.length
********************************************************************************

``app.activeDocument.brushes.length``

**Description**

The number of objects in the collection

**Type**

Number; read-only.

----

.. _jsobjref/Brushes.parent:

Brushes.parent
********************************************************************************

``app.activeDocument.brushes.parent``

**Description**

The document that contains this brushes collection.

**Type**

Object; read-only.

----

.. _jsobjref/Brushes.typename:

Brushes.typename
********************************************************************************

``app.activeDocument.brushes.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/Brushes.getByName:

Brushes.getByName()
********************************************************************************

``app.activeDocument.brushes.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------------+
| Parameter |  Type  |    Description    |
+===========+========+===================+
| ``name``  | String | Brush name to get |
+-----------+--------+-------------------+

**Returns**

:ref:`jsobjref/Brush`

----

.. _jsobjref/Brushes.index:

Brushes.index()
********************************************************************************

``app.activeDocument.brushes.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------------------+
|  Parameter  |      Type      |       Description       |
+=============+================+=========================+
| ``itemKey`` | String, Number | Index of element to get |
+-------------+----------------+-------------------------+

**Returns**

:ref:`jsobjref/Brush`

----

=======
Example
=======

Counting brushes
********************************************************************************

::

  // Counts all brushes in the active document

  if (app.documents.length > 0) {
    var numberOfBrushes = app.activeDocument.brushes.length;
  }
