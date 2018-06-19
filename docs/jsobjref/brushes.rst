.. _jsobjref/brushes:

Brushes
################################################################################

``app.activeDocument.brushes``

**Description**

A collection of brush objects in a document.

----

==========
Properties
==========

.. _brushes.length:

brushes.length
********************************************************************************

``app.activeDocument.brushes.length``

**Description**

The number of objects in the collection

**Type**

Number; read-only.

----

.. _brushes.parent:

brushes.parent
********************************************************************************

``app.activeDocument.brushes.parent``

**Description**

The document that contains this brushes collection.

**Type**

Object; read-only.

----

.. _brushes.typename:

brushes.typename
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

.. _brushes.getByName:

brushes.getByName()
********************************************************************************

``app.activeDocument.brushes.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

========  ======  ====================
``name``  String  Brush name to get
========  ======  ====================

**Returns**

:ref:`jsobjref/brush`

----

.. _brushes.index:

brushes.index()
********************************************************************************

``app.activeDocument.brushes.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

===========  ==============  ====================
``itemKey``  String, Number  String or number key
===========  ==============  ====================

**Returns**

:ref:`jsobjref/brush`

----

=======
Example
=======

Counting brushes
********************************************************************************

::

  // Counts all brushes in the active document

  if ( app.documents.length > 0 ) {
    numberOfBrushes = app.activeDocument.brushes.length;
  }
