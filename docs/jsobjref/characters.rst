.. _jsobjref/characters:

Characters
################################################################################

``characters``

**Description**

A collection of characters (``TextRange`` objects of length 1).

The elements are not named; you must access them by index.

----

==========
Properties
==========

.. _jsobjref/characters.length:

characters.length
********************************************************************************

``app.activeDocument.textFrames[index].contents.length``

**Description**

The number of characters in the collection.

**Type**

Number; read-only.

----

.. _jsobjref/characters.parent:

characters.parent
********************************************************************************

``app.activeDocument.textFrames[index].contents.parent``

**Description**

The text art item that contains this character.

**Type**

Object; read-only.

----

.. _jsobjref/characters.typename:

characters.typename
********************************************************************************

``app.activeDocument.textFrames[index].contents.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/characters.add:

characters.add()
********************************************************************************

``app.activeDocument.textFrames[index].contents.add(contents[,relativeObject][,insertionLocation])``

**Description**

Adds a new character with specified text contents at the specified location in the current document.

If a location is not specified, adds the new character to the containing text frame after the current text selection or insertion point.

**Parameters**

=======================  ==========================================  ====
``contents``             String                                      todo
``[relativeObject]``     :ref:`jsobjref/textFrameItem`, optional     todo
``[insertionLocation]``  :ref:`jsobjref/elementPlacement`, optional  todo
=======================  ==========================================  ====

**Returns**

:ref:`jsobjref/textRange`

----

.. _jsobjref/characters.addBefore:

characters.addBefore()
********************************************************************************

``app.activeDocument.textFrames[index].contents.addBefore(contents)``

**Description**

Adds a character before the specified text selection.

**Parameters**

============  ======  ====
``contents``  String  todo
============  ======  ====

**Returns**

:ref:`jsobjref/textRange`

----

.. _jsobjref/characters.index:

characters.index()
********************************************************************************

``app.activeDocument.textFrames[index].contents.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

===========  ======  ====
``itemKey``  Number  todo
===========  ======  ====

**Returns**

:ref:`jsobjref/textRange`

----

.. _jsobjref/characters.removeAll:

characters.removeAll()
********************************************************************************

``app.activeDocument.textFrames[index].contents.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

----

=======
Example
=======

Counting characters
********************************************************************************

::

  // Counts all characters in the active document,
  // including whitespace, and stores in numChars

  if ( app.documents.length > 0 ) {
    var doc = app.activeDocument;
    var numChars = 0;
    for ( i = 0; i < doc.textFrames.length; i++ ) {
      textArtRange = doc.textFrames[i].contents;
      numChars += textArtRange.length;
    }
  }
