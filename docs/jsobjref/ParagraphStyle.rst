.. _jsobjref/ParagraphStyle:

ParagraphStyle
################################################################################

``app.activeDocument.paragraphStyles[index]``

**Description**

Associates character and paragraph attributes with a style name. The style object can be used to apply those attributes to the text in a TextFrame object. See :ref:`jsobjref/ParagraphStyles.creatingAndApplyingParagraphStyle` example.

----

==========
Properties
==========

.. _jsobjref/ParagraphStyle.characterAttributes:

ParagraphStyle.characterAttributes
********************************************************************************

``app.activeDocument.paragraphStyles[index.characterAttributes``

**Description**

The character properties for the text range.

**Type**

:ref:`jsobjref/CharacterAttributes`, read-only.

----

.. _jsobjref/ParagraphStyle.name:

ParagraphStyle.name
********************************************************************************

``app.activeDocument.paragraphStyles[index.name``

**Description**

The paragraph style’s name.

**Type**

String.

----

.. _jsobjref/ParagraphStyle.paragraphAttributes:

ParagraphStyle.paragraphAttributes
********************************************************************************

``app.activeDocument.paragraphStyles[index.paragraphAttributes``

**Description**

The paragraph properties for the text range.

**Type**

:ref:`jsobjref/CharacterAttributes`, read-only.

----

.. _jsobjref/ParagraphStyle.parent:

ParagraphStyle.parent
********************************************************************************

``app.activeDocument.paragraphStyles[index.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/ParagraphStyle.typename:

ParagraphStyle.typename
********************************************************************************

``app.activeDocument.paragraphStyles[index.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/ParagraphStyle.applyTo:

ParagraphStyle.applyTo()
********************************************************************************

``app.activeDocument.paragraphStyles[index.applyTo(textItem [,clearingOverrides])``

**Description**

Applies this paragraph style to the specified text item.

**Parameters**

+-------------------------+-------------------+-------------+
|        Parameter        |       Type        | Description |
+=========================+===================+=============+
| ``textItem``            | Object            | todo        |
+-------------------------+-------------------+-------------+
| ``[clearingOverrides]`` | Boolean, optional | todo        |
+-------------------------+-------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/ParagraphStyle.remove:

ParagraphStyle.remove()
********************************************************************************

``app.activeDocument.paragraphStyles[index.remove()``

**Description**

Deletes the object.

**Returns**

Nothing.
