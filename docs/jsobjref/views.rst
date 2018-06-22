.. _jsobjref/views:

Views
################################################################################

``app.activeDocument.views``

**Description**

A collection of :ref:`jsobjref/view` objects in a document.

----

==========
Properties
==========

.. _jsobjref/views.length:

views.length
********************************************************************************

``app.activeDocument.views.length``

**Description**

The number of objects in the collection

**Type**

Number; read-only.

----

.. _jsobjref/views.parent:

views.parent
********************************************************************************

``app.activeDocument.views.parent``

**Description**

The parent of this object.

**Type**

Object; read-only.

----

.. _jsobjref/views.typename:

views.typename
********************************************************************************

``app.activeDocument.views.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/views.index:

views.index()
********************************************************************************

``app.activeDocument.views.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/View`
