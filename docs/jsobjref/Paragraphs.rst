.. _jsobjref/Paragraphs:

Paragraphs
################################################################################

``app.activeDocument.textFrames[index].paragraphs``

**Description**

A collection of :ref:`jsobjref/TextRange` objects, with each ``TextRange`` representing a paragraph. The elements are not named; you must access them by index.

----

==========
Properties
==========

.. _jsobjref/Paragraphs.length:

Paragraphs.length
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/Paragraphs.parent:

Paragraphs.parent
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/Paragraphs.typename:

Paragraphs.typename
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Paragraphs.add:

Paragraphs.add()
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.add(contents [,relativeObject] [,insertionLocation])``

**Description**

Adds a new paragraph with specified text contents at the specified location in the current document. If location is not specified, adds the new paragraph to the containing text frame after the current text selection or insertion point.

**Parameters**

+-----------------------+----------------------------------------------------------------+------------------------+
|       Parameter       |                              Type                              |      Description       |
+=======================+================================================================+========================+
| ``contents``          | String                                                         | Text contents to add   |
+-----------------------+----------------------------------------------------------------+------------------------+
| ``relativeObject``    | :ref:`jsobjref/TextFrameItem`, optional                        | Object to add item to  |
+-----------------------+----------------------------------------------------------------+------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to place text |
+-----------------------+----------------------------------------------------------------+------------------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/Paragraphs.addBefore:

Paragraphs.addBefore()
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.addBefore(contents)``

**Description**

Adds a new paragraph with specified text contents before the current text selection or insertion point.

**Parameters**

+--------------+--------+----------------------+
|  Parameter   |  Type  |     Description      |
+==============+========+======================+
| ``contents`` | String | Text contents to add |
+--------------+--------+----------------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/Paragraphs.index:

Paragraphs.index()
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/Paragraphs.removeAll:

Paragraphs.removeAll()
********************************************************************************

``app.activeDocument.textFrames[index].paragraphs.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Counting paragraphs
********************************************************************************

::

  // Counts all paragraphs in current doc and stores result in paragraphCount
  if (app.documents.length > 0) {
    var doc = app.activeDocument;
    var paragraphCount = 0;
    for (var i = 0; i < doc.textFrames.length; i++) {
      paragraphCount += doc.textFrames[i].paragraphs.length;
    }
  }
