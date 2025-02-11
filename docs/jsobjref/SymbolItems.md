.. _jsobjref/SymbolItems:

SymbolItems
################################################################################

``app.activeDocument.symbolItems``

**Description**

The collection of :ref:`jsobjref/SymbolItem` objects in the document.

----

==========
Properties
==========

.. _jsobjref/SymbolItems.length:

SymbolItems.length
********************************************************************************

``app.activeDocument.symbolItems.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/SymbolItems.parent:

SymbolItems.parent
********************************************************************************

``app.activeDocument.symbolItems.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/SymbolItems.typename:

SymbolItems.typename
********************************************************************************

``app.activeDocument.symbolItems.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/SymbolItems.add:

SymbolItems.add()
********************************************************************************

``app.activeDocument.symbolItems.add(symbol)``

**Description**

Creates an instance of the specified symbol.

**Parameters**

+------------+------------------------+--------------------+
| Parameter  |          Type          |    Description     |
+============+========================+====================+
| ``symbol`` | :ref:`jsobjref/Symbol` | Symbol to instance |
+------------+------------------------+--------------------+

**Returns**

:ref:`jsobjref/SymbolItem`

----

.. _jsobjref/SymbolItems.getByName:

SymbolItems.getByName()
********************************************************************************

``app.activeDocument.symbolItems.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/SymbolItem`

----

.. _jsobjref/SymbolItems.index:

SymbolItems.index()
********************************************************************************

``app.activeDocument.symbolItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/SymbolItem`

----

.. _jsobjref/SymbolItems.removeAll:

SymbolItems.removeAll()
********************************************************************************

``app.activeDocument.symbolItems.removeAll()``

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
    docRef.symbolItems.add(pathRef);
  }
