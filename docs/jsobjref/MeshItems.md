.. _jsobjref/MeshItems:

MeshItems
################################################################################

``app.activeDocument.meshItems``

**Description**

A collection of :ref:`jsobjref/MeshItem` objects.

----

==========
Properties
==========

.. _jsobjref/MeshItems.length:

MeshItems.length
********************************************************************************

``app.activeDocument.meshItems.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/MeshItems.parent:

MeshItems.parent
********************************************************************************

``app.activeDocument.meshItems.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/MeshItems.typename:

MeshItems.typename
********************************************************************************

``app.activeDocument.meshItems.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/MeshItems.getByName:

MeshItems.getByName()
********************************************************************************

``app.activeDocument.meshItems.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/MeshItem`

----

.. _jsobjref/MeshItems.index:

MeshItems.index()
********************************************************************************

``app.activeDocument.meshItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/MeshItem`

----

.. _jsobjref/MeshItems.removeAll:

MeshItems.removeAll()
********************************************************************************

``app.activeDocument.meshItems.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Copying mesh items to another document
********************************************************************************

To run this script, have two open documents. One document should contain at least one mesh item, the other document can be empty. Make the empty document the frontmost before running the script.

::

  // Copies all mesh items from one document to a new document
  if (app.documents.length > 0) {
    var srcDoc = documents[0];
    var locationOffset = 0;
    var targetDoc = documents.add();
    for (var i = 0; i < srcDoc.meshItems.length; i++) {
      var srcItem = srcDoc.meshItems[i];
      var dupItem = srcDoc.meshItems[i].duplicate(targetDoc, ElementPlacement.PLACEATEND);

      // offset the copied items' position on the y axis
      dupItem.position = Array(100, 50 + locationOffset);
      locationOffset += 50;
    }
  }
