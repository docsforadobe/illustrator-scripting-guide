.. _jsobjref/Views:

Views
################################################################################

``app.activeDocument.views``

**Description**

A collection of :ref:`jsobjref/View` objects in a document.

----

==========
Properties
==========

.. _jsobjref/Views.length:

Views.length
********************************************************************************

``app.activeDocument.views.length``

**Description**

The number of objects in the collection

**Type**

Number; read-only.

----

.. _jsobjref/Views.parent:

Views.parent
********************************************************************************

``app.activeDocument.views.parent``

**Description**

The parent of this object.

**Type**

Object; read-only.

----

.. _jsobjref/Views.typename:

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

.. _jsobjref/Views.index:

Views.index()
********************************************************************************

``app.activeDocument.views.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/View`
