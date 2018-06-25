.. _jsobjref/Swatches:

Swatches
################################################################################

``app.activeDocument.swatches``

**Description**

The collection of :ref:`jsobjref/Swatch` objects in the document.

----

==========
Properties
==========

.. _jsobjref/Swatches.length:

Swatches.length
********************************************************************************

``app.activeDocument.swatches.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Swatches.parent:

Swatches.parent
********************************************************************************

``app.activeDocument.swatches.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/Swatches.typename:

Swatches.typename
********************************************************************************

``app.activeDocument.swatches.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Swatches.add:

Swatches.add()
********************************************************************************

``app.activeDocument.swatches.add()``

**Description**

Creates a new :ref:`jsobjref/Swatch` object.

**Returns**

:ref:`jsobjref/Swatch`

----

.. _jsobjref/Swatches.getByName:

Swatches.getByName()
********************************************************************************

``app.activeDocument.swatches.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/Swatch`

----

.. _jsobjref/Swatches.getSelected:

Swatches.getSelected()
********************************************************************************

``app.activeDocument.swatches.getSelected()``

**Description**

Gets selected swatches in the document.

**Returns**

List of :ref:`jsobjref/Swatch`

----

.. _jsobjref/Swatches.index:

Swatches.index()
********************************************************************************

``app.activeDocument.swatches.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-----------------------+
|  Parameter  |      Type      |      Description      |
+=============+================+=======================+
| ``itemKey`` | String, Number | Key of element to get |
+-------------+----------------+-----------------------+

**Returns**

:ref:`jsobjref/Swatch`

----

.. _jsobjref/Swatches.removeAll:

Swatches.removeAll()
********************************************************************************

``app.activeDocument.swatches.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

----

=======
Example
=======

Finding and deleting a swatch
********************************************************************************

::

  // Deletes swatch 4 from the current document
  if ( app.documents.length > 0 ) {
    if (app.activeDocument.swatches.length > 4) {
      var swatchToDelete = app.activeDocument.swatches[3];
      swatchToDelete.remove();
    }
  }
