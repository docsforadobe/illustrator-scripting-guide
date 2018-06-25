.. _jsobjref/Symbols:

Symbols
################################################################################

``app.activeDocument.symbols``

**Description**

The collection of :ref:`jsobjref/Symbol` objects in the document.

----

==========
Properties
==========

.. _jsobjref/Symbols.length:

Symbols.length
********************************************************************************

``app.activeDocument.symbols.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Symbols.parent:

Symbols.parent
********************************************************************************

``app.activeDocument.symbols.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/Symbols.typename:

Symbols.typename
********************************************************************************

``app.activeDocument.symbols.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Symbols.add:

Symbols.add()
********************************************************************************

``app.activeDocument.symbols.add(sourceArt[, registrationPoint])``

**Description**

Returns a symbol object created from the source art item, any of the following:

- :ref:`jsobjref/CompoundPathItems`
- :ref:`jsobjref/GroupItems`
- :ref:`jsobjref/MeshItems`
- :ref:`jsobjref/NonNativeItems`
- :ref:`jsobjref/PageItems`
- :ref:`jsobjref/PathItems`
- :ref:`jsobjref/RasterItems`
- :ref:`jsobjref/SymbolItems`
- :ref:`jsobjref/TextFrameItems`

The default registration point is ``SymbolRegistrationPoint.SYMBOLCENTERPOINT``.

**Parameters**

+-----------------------+-----------------------------------------------------------------------+-------------+
|       Parameter       |                                 Type                                  | Description |
+=======================+=======================================================================+=============+
| ``sourceArt``         | :ref:`jsobjref/PageItem`                                              | todo        |
| ``registrationPoint`` | :ref:`jsobjref/scripting-constants.SymbolRegistrationPoint`, optional | todo        |
+-----------------------+-----------------------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/Symbol`

----

.. _jsobjref/Symbols.getByName:

Symbols.getByName()
********************************************************************************

``app.activeDocument.symbols.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/Symbol`

----

.. _jsobjref/Symbols.index:

Symbols.index()
********************************************************************************

``app.activeDocument.symbols.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/Symbol`

----

.. _jsobjref/Symbols.removeAll:

Symbols.removeAll()
********************************************************************************

``app.activeDocument.symbols.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

----

=======
Example
=======

Creating a symbol
********************************************************************************

::

  // Creates a path item from each graphic style
  // then adds each item as a new symbol

  var docRef = documents.add();
  var y = 750;
  var x = 25;

  var iCount = docRef.graphicStyles.length;

  for (var i=0; i<iCount; i++) {

    var pathRef = docRef.pathItems.rectangle( y, x, 20, 20 );
    docRef.graphicStyles[i].applyTo(pathRef);

    // are we at bottom?
    if ( (y-=60) <= 60 ) {
      y = 750; // go back to the top.
      x+= 200
    }

    redraw();
    docRef.symbols.add(pathRef);
  }
