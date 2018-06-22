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

Views.length
********************************************************************************

``app.activeDocument.views.length``

**Description**

The number of objects in the collection

**Type**

Number; read-only.

----

.. _jsobjref/views.parent:

Views.parent
********************************************************************************

``app.activeDocument.views.parent``

**Description**

The parent of this object.

**Type**

Object; read-only.

----

.. _jsobjref/views.typename:

Views.typename
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

Views.index()
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
