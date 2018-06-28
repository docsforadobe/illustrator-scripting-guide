.. _jsobjref/Pattern:

Pattern
################################################################################

``app.activeDocument.patterns[index]``

**Description**

An Illustrator pattern definition contained in a document.

Patterns are shown in the Swatches palette.

Each pattern is referenced by a :ref:`jsobjref/PatternColor` object, which defines the pattern’s appearance.

----

==========
Properties
==========

.. _jsobjref/Pattern.name:

Pattern.name
********************************************************************************

``app.activeDocument.patterns[index].name``

**Description**

The pattern name.

**Type**

String

----

.. _jsobjref/Pattern.parent:

Pattern.parent
********************************************************************************

``app.activeDocument.patterns[index].parent``

**Description**

The document that contains this pattern.

**Type**

:ref:`jsobjref/Document`, read-only.

----

.. _jsobjref/Pattern.typename:

Pattern.typename
********************************************************************************

``app.activeDocument.patterns[index].typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Pattern.remove:

Pattern.remove()
********************************************************************************

``app.activeDocument.patterns[index].remove()``

**Description**

Removes the referenced pattern from the document.

**Returns**

Nothing.

----

.. _jsobjref/Pattern.toString:

Pattern.toString()
********************************************************************************

``app.activeDocument.patterns[index].toString()``

**Description**

Returns the object type of a referenced object. If the object has a name, also returns the name.

**Returns**

String
