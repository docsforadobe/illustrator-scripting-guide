.. _jsobjref/artboards:

Artboards
################################################################################

``artboards``

**Description**

A collection of Artboard objects.

==========
Properties
==========

.. _artboards.length:

artboards.length
********************************************************************************

``artboards.length``

**Description**

The number of datasets in the collection

**Type**

Number; read-only.

----

.. _artboards.parent:

artboards.parent
********************************************************************************

``artboards.parent``

**Description**

The name of the object that contains this dataset

**Type**

:ref:`jsobjref/artboard`; read-only.


----

.. _artboards.typename:

artboards.typename
********************************************************************************

``artboards.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _artboards.add:

artboards.add()
********************************************************************************

``artboards.add(artboardRect)``

**Description**

Creates a new Artboard object.

**Parameters**

================  ====  ===================
``artboardRect``  Rect  Artboard dimensions
================  ====  ===================

**Returns**

:ref:`jsobjref/artboard`

----

.. _artboards.getActiveArtboardIndex:

artboards.getActiveArtboardIndex()
********************************************************************************

``artboards.getActiveArtboardIndex()``

**Description**

Retrieves the index position of the active artboard in the document's list.

Returns the 0-based index.

**Returns**

Number (long)

----

.. _artboards.getByName:

artboards.getByName()
********************************************************************************

``artboards.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

========  ======  ====================
``name``  String  Artboard name to get
========  ======  ====================

**Returns**

:ref:`jsobjref/artboard`

----

.. _artboards.insert:

artboards.insert()
********************************************************************************

``artboards.insert(artboardRect, index)``

**Description**

Creates a new Artboard object and inserts it at the given index in the list.

**Parameters**

================  =============  ===========================
``artboardRect``  Rect           Artboard dimensions
``index``         Number (long)  Index to insert artboard at
================  =============  ===========================

**Returns**

Nothing.

----

.. _artboards.remove:

artboards.remove()
********************************************************************************

``artboards.remove(index)``

**Description**

Deletes an artboard object. You cannot remove the last artboard in a document.

**Parameters**

=========  =============  ===========================
``index``  Number (long)  Index of artboard to remove
=========  =============  ===========================

**Returns**

Nothing.

----

.. _artboards.setActiveArtboardIndex:

artboards.setActiveArtboardIndex()
********************************************************************************

``artboards.setActiveArtboardIndex(index)``

**Description**

Makes a specific artboard active and makes it current in the iteration order.

**Parameters**

=========  =============  ===============================
``index``  Number (long)  Index of artboard to set active
=========  =============  ===============================

**Returns**

Nothing.
