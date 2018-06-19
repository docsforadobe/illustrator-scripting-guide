.. _jsobjref/characterStyle:

Character Style
################################################################################

``characterStyle``

**Description**

Associates character attributes with characters. For an example, see :ref:`jsobjref/characterStyles`.

----

==========
Properties
==========

.. _characterStyle.characterAttributes:

characterStyle.characterAttributes
********************************************************************************

``characterStyle.characterAttributes``

**Description**

The character properties for the style.

**Type**

:ref:`jsobjref/characterAttributes`, read-only.

----

.. _characterStyle.name:

characterStyle.name
********************************************************************************

``characterStyle.name``

**Description**

The character style’s name.

**Type**

String

----

.. _characterStyle.parent:

characterStyle.parent
********************************************************************************

``characterStyle.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _characterStyle.typename:

characterStyle.typename
********************************************************************************

``characterStyle.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _characterStyle.applyTo:

characterStyle.applyTo()
********************************************************************************

``characterStyle.applyTo(textItem [,clearingOverrides])``

**Description**

Applies the character style to the text object or objects.

**Paramaters**

=======================  =================  ====
``textItem``             Object             todo
``[clearingOverrides]``  Boolean, optional  todo
=======================  =================  ====

**Returns**

Nothing

-----

.. _characterStyle.remove:

characterStyle.remove()
********************************************************************************

``characterStyle.remove()``

**Description**

Deletes the object.

**Returns**

Nothing
