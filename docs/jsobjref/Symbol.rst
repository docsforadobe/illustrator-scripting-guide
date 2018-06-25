.. _jsobjref/Symbol:

Symbol
################################################################################

``symbol``

**Description**

An art item that is stored in the Symbols palette, and can be reused one or more times in the document without duplicating the art data. Symbols are contained in documents.

Instances of ``Symbol`` in a document are associated with :ref:`jsobjref/SymbolItem` objects, which store the art object properties.

----

==========
Properties
==========

.. _jsobjref/Symbol.name:

Symbol.name
********************************************************************************

``symbol.name``

**Description**

The symbol's name

**Type**

String.

----

.. _jsobjref/Symbol.parent:

Symbol.parent
********************************************************************************

``symbol.parent``

**Description**

The object that contains the symbol object.

**Type**

Object, read-only.

----

.. _jsobjref/Symbol.typename:

Symbol.typename
********************************************************************************

``symbol.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Symbol.duplicate:

Symbol.duplicate()
********************************************************************************

``symbol.duplicate()``

**Description**

Creates a duplicate of this object.

**Returns**

:ref:`jsobjref/Symbol`

----

.. _jsobjref/Symbol.remove:

Symbol.remove()
********************************************************************************

``symbol.remove()``

**Description**

Deletes this object.

**Returns**

Nothing.
