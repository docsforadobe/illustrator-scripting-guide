.. _jsobjref/SwatchGroup:

SwatchGroup
################################################################################

``swatchGroup``

**Description**

A group of :ref:`jsobjref/Swatch` objects.

----

==========
Properties
==========

.. _jsobjref/SwatchGroup.name:

SwatchGroup.name
********************************************************************************

``swatchGroup.name``

**Description**

The name of the swatch group.

**Type**

string

----

.. _jsobjref/SwatchGroup.parent:

SwatchGroup.parent
********************************************************************************

``swatchGroup.parent``

**Description**

The object that contains the swatch group.

**Type**

Object, read-only.

----

.. _jsobjref/SwatchGroup.typename:

SwatchGroup.typename
********************************************************************************

``swatchGroup.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only

----

=======
Methods
=======

.. _jsobjref/SwatchGroup.addSpot:

SwatchGroup.addSpot()
********************************************************************************

``swatchGroup.addSpot(spot)``

**Description**

Adds a spot swatch to the swatch group.

**Parameters**

+-----------+----------------------+-------------+
| Parameter |         Type         | Description |
+===========+======================+=============+
| ``spot``  | :ref:`jsobjref/Spot` | Spot to add |
+-----------+----------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/SwatchGroup.addSwatch:

SwatchGroup.addSwatch()
********************************************************************************

``swatchGroup.addSwatch(swatch)``

**Description**

Adds a swatch to the swatch group.

**Parameters**

+------------+------------------------+---------------+
| Parameter  |          Type          |  Description  |
+============+========================+===============+
| ``swatch`` | :ref:`jsobjref/Swatch` | Swatch to add |
+------------+------------------------+---------------+

**Returns**

Nothing.

----

.. _jsobjref/SwatchGroup.getAllSwatches:

SwatchGroup.getAllSwatches()
********************************************************************************

``swatchGroup.getAllSwatches()``

**Description**

Gets a list of all swatches in the swatch group.

**Returns**

List of :ref:`jsobjref/Swatch`

----

.. _jsobjref/SwatchGroup.remove:

SwatchGroup.remove()
********************************************************************************

``swatchGroup.remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _jsobjref/SwatchGroup.removeAll:

SwatchGroup.removeAll()
********************************************************************************

``swatchGroup.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
