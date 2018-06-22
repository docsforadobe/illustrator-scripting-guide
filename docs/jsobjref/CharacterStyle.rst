.. _jsobjref/CharacterStyle:

CharacterStyle
################################################################################

``characterStyle``

**Description**

Associates character attributes with characters. For an example, see :ref:`jsobjref/CharacterStyles`.

----

==========
Properties
==========

.. _jsobjref/CharacterStyle.characterAttributes:

CharacterStyle.characterAttributes
********************************************************************************

``characterStyle.characterAttributes``

**Description**

The character properties for the style.

**Type**

:ref:`jsobjref/CharacterAttributes`, read-only.

----

.. _jsobjref/CharacterStyle.name:

CharacterStyle.name
********************************************************************************

``characterStyle.name``

**Description**

The character style’s name.

**Type**

String

----

.. _jsobjref/CharacterStyle.parent:

CharacterStyle.parent
********************************************************************************

``characterStyle.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/CharacterStyle.typename:

CharacterStyle.typename
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

.. _jsobjref/CharacterStyle.applyTo:

CharacterStyle.applyTo()
********************************************************************************

``characterStyle.applyTo(textItem [,clearingOverrides])``

**Description**

Applies the character style to the text object or objects.

**Paramaters**

+-------------------------+-------------------+-------------+
|        Parameter        |       Type        | Description |
+=========================+===================+=============+
| ``textItem``            | Object            | todo        |
+-------------------------+-------------------+-------------+
| ``[clearingOverrides]`` | Boolean, optional | todo        |
+-------------------------+-------------------+-------------+

**Returns**

Nothing

-----

.. _jsobjref/CharacterStyle.remove:

CharacterStyle.remove()
********************************************************************************

``characterStyle.remove()``

**Description**

Deletes the object.

**Returns**

Nothing.
