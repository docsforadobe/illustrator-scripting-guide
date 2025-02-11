.. _jsobjref/Layers:

Layers
################################################################################

``app.activeDocument.layers``

**Description**

The collection of layers in the document.

----

==========
Properties
==========

.. _jsobjref/Layers.length:

Layers.length
********************************************************************************

``app.activeDocument.layers.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Layers.parent:

Layers.parent
********************************************************************************

``app.activeDocument.layers.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/Layers.typename:

Layers.typename
********************************************************************************

``app.activeDocument.layers.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Layers.add:

Layers.add()
********************************************************************************

``app.activeDocument.layers.add()``

**Description**

Creates a new layer in the document.

**Returns**

:ref:`jsobjref/Layer`

----

.. _jsobjref/Layers.getByName:

Layers.getByName()
********************************************************************************

``app.activeDocument.layers.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/Layer`

----

.. _jsobjref/Layers.index:

Layers.index()
********************************************************************************

``app.activeDocument.layers.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/Layer`

----

.. _jsobjref/Layers.removeAll:

Layers.removeAll()
********************************************************************************

``app.activeDocument.layers.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Finding and deleting layers
********************************************************************************

::

  // Deletes all layers whose name begins with "Temp" in all open documents

  var layersDeleted = 0;
  for (var i = 0; i < app.documents.length; i++) {
    var targetDocument = app.documents[i];
    var layerCount = targetDocument.layers.length;

    // Loop through layers from the back, to preserve index
    // of remaining layers when we remove one
    for (var ii = layerCount - 1; ii >= 0; ii--) {
      var targetLayer = targetDocument.layers[ii];
      var layerName = new String(targetLayer.name);
      if (layerName.indexOf("Temp") == 0) {
        targetDocument.layers[ii].remove();
        layersDeleted++;
      }
    }
  }
