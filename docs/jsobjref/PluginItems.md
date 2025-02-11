.. _jsobjref/PluginItems:

PluginItems
################################################################################

``app.activeDocument.pluginItems``

**Description**

A collection of :ref:`jsobjref/PluginItem` objects in a document.

See :ref:`jsobjref/PluginItem.copying-a-plugin-item`.

----

==========
Properties
==========

.. _jsobjref/PluginItems.length:

PluginItems.length
********************************************************************************

``app.activeDocument.pluginItems.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/PluginItems.parent:

PluginItems.parent
********************************************************************************

``app.activeDocument.pluginItems.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/PluginItems.typename:

PluginItems.typename
********************************************************************************

``app.activeDocument.pluginItems.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/PluginItems.getByName:

PluginItems.getByName()
********************************************************************************

``app.activeDocument.pluginItems.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/PluginItems.index:

PluginItems.index()
********************************************************************************

``app.activeDocument.pluginItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/PluginItem`

----

.. _jsobjref/PluginItems.removeAll:

PluginItems.removeAll()
********************************************************************************

``app.activeDocument.pluginItems.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
