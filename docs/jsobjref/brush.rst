.. _jsobjref/brush:

Brush
################################################################################

``app.activeDocument.brushes[index]``

**Description**

A brush in an Illustrator document. Brushes are contained in documents. Additional brushes may be
created by the user within Illustrator. You can access brushes within a script, but you cannot create them.

----

==========
Properties
==========

.. _jsobjref/brush.name:

brush.name
********************************************************************************

``app.activeDocument.brushes[index].name``

**Description**

The name of the brush

**Type**

String

----

.. _jsobjref/brush.parent:

brush.parent
********************************************************************************

``app.activeDocument.brushes[index].parent``

**Description**

The document that contains this brush.

**Type**

:ref:`jsobjref/document`; read-only.

----

.. _jsobjref/brush.typename:

brush.typename
********************************************************************************

``app.activeDocument.brushes[index].typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/brush.applyTo:

brush.applyTo()
********************************************************************************

``app.activeDocument.brushes[index].applyTo(artItem)``

**Description**

Applies the ``brush`` to a specific art item.

**Parameters**

+-------------+--------------------------+----------------------------+
|  Parameter  |           Type           |        Description         |
+=============+==========================+============================+
| ``artItem`` | :ref:`jsobjref/pageItem` | Art item to apply brush to |
+-------------+--------------------------+----------------------------+

**Returns**

Nothing.

----

=======
Example
=======

Applying a Brush
********************************************************************************

::

  // Duplicates and groups all items in the current selection,
  // then applies the same brush to each item in the group

  if ( app.documents.length > 0 ) {
    docSelection = app.activeDocument.selection;
    if ( docSelection.length > 0 ) {
      newGroup = app.activeDocument.groupItems.add();

      for ( i = 0; i < docSelection.length; i++ ) {
        newItem = docSelection[i].duplicate();
        newItem.moveToBeginning( newGroup );
      }

      brush4 = app.activeDocument.brushes[1];
      brush4.applyTo( newGroup );
    }
  }
