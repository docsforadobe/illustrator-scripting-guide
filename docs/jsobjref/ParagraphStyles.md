.. _jsobjref/ParagraphStyles:

ParagraphStyles
################################################################################

``app.activeDocument.paragraphStyles``

**Description**

A collection of :ref:`jsobjref/ParagraphStyle` objects.

----

==========
Properties
==========

.. _jsobjref/ParagraphStyles.length:

ParagraphStyles.length
********************************************************************************

``app.activeDocument.paragraphStyles.length``

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/ParagraphStyles.parent:

ParagraphStyles.parent
********************************************************************************

``app.activeDocument.paragraphStyles.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/ParagraphStyles.typename:

ParagraphStyles.typename
********************************************************************************

``app.activeDocument.paragraphStyles.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/ParagraphStyles.add:

ParagraphStyles.add()
********************************************************************************

``app.activeDocument.paragraphStyles.add(name)``

**Description**

Creates a named paragraph style.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/CharacterAttributes`

----

.. _jsobjref/ParagraphStyles.getByName:

ParagraphStyles.getByName()
********************************************************************************

``app.activeDocument.paragraphStyles.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/CharacterAttributes`

----

.. _jsobjref/ParagraphStyles.index:

ParagraphStyles.index()
********************************************************************************

``app.activeDocument.paragraphStyles.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/CharacterAttributes`

----

.. _jsobjref/ParagraphStyles.removeAll:

ParagraphStyles.removeAll()
********************************************************************************

``app.activeDocument.paragraphStyles.removeAll()``

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

----

=======
Example
=======

.. _jsobjref/ParagraphStyles.creatingAndApplyingParagraphStyle:

Creating and applying a paragraph style
********************************************************************************

::

  // Creates a new document with 1 text frame and 3 paragraphs
  // gives each paragraph a different justification, then creates
  // a paragraph style and applies it to all paragraphs

  var docRef = documents.add();
  var pathRef = docRef.pathItems.rectangle(600, 200, 200, 400);
  var textRef = docRef.textFrames.areaText(pathRef);
  textRef.paragraphs.add("Left justified paragraph.");
  textRef.paragraphs.add("Center justified paragraph.");
  textRef.paragraphs.add("Right justified paragraph.");
  textRef.textRange.characterAttributes.size = 28;

  // change the justification of each paragraph
  // using the paragraph attributes object
  var paraAttr_0 = textRef.paragraphs[0].paragraphAttributes;
  paraAttr_0.justification = Justification.RIGHT;

  var paraAttr_1 = textRef.paragraphs[1].paragraphAttributes;
  paraAttr_1.justification = Justification.CENTER;

  var paraAttr_2 = textRef.paragraphs[2].paragraphAttributes;
  paraAttr_2.justification = Justification.LEFT;

  // create a new paragraph style
  var paraStyle = docRef.paragraphStyles.add("LeftIndent");

  // add some paragraph attributes
  var paraAttr = paraStyle.paragraphAttributes;
  paraAttr.justification = Justification.LEFT;
  paraAttr.firstLineIndent = 10;

  // apply the style to each item in the document
  var iCount = textRef.paragraphs.length;
  for (var i = 0; i < iCount; i++) {
    paraStyle.applyTo(textRef.paragraphs[i], true);
  }
  redraw();
