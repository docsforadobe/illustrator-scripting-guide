.. _jsobjref/Variable:

Variable
################################################################################

``app.activeDocument.variables[index]``

**Description**

A document-level variable that can be imported or exported.

A variable is a dynamic object used to create data-driven graphics.

For an example, see :ref:`jsobjref/Dataset`.

Variables are accessed in Illustrator through the Variables palette.

----

==========
Properties
==========

.. _jsobjref/Variable.kind:

Variable.kind
********************************************************************************

``app.activeDocument.variables[index].kind``

**Description**

The variable’s type.

**Type**

:ref:`jsobjref/scripting-constants.VariableKind`

----

.. _jsobjref/Variable.name:

Variable.name
********************************************************************************

``app.activeDocument.variables[index].name``

**Description**

The name of the variable.

**Type**

string

----

.. _jsobjref/Variable.pageItems:

Variable.pageItems
********************************************************************************

``app.activeDocument.variables[index].pageItems``

**Description**

All of the artwork in the variable.

**Type**

:ref:`jsobjref/PageItems`, read-only

----

.. _jsobjref/Variable.parent:

Variable.parent
********************************************************************************

``app.activeDocument.variables[index].parent``

**Description**

Read-only. The object that contains the variable.

**Type**

Object

----

.. _jsobjref/Variable.typename:

Variable.typename
********************************************************************************

``app.activeDocument.variables[index].typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only

----

=======
Methods
=======

.. _jsobjref/Variable.remove:

Variable.remove()
********************************************************************************

``app.activeDocument.variables[index].remove()``

**Description**

Removes the variable from the collection of variables.

**Returns**

Nothing.
