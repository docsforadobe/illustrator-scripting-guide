.. _jsobjref/TextRange:

TextRange
################################################################################

``app.activeDocument.textFrames[index].textRange``

**Description**

A range of text in a specific text art item. TextRange gives you access to the text contained in text art items.

----

==========
Properties
==========

.. _jsobjref/TextRange.characterAttributes:

TextRange.characterAttributes
********************************************************************************

``app.activeDocument.textFrames[index].textRange.characterAttributes``

**Description**

The character properties for the text range.

**Type**

:ref:`jsobjref/CharacterAttributes`, read-only.

----

.. _jsobjref/TextRange.characterOffset:

TextRange.characterOffset
********************************************************************************

``app.activeDocument.textFrames[index].textRange.characterOffset``

**Description**

Offset of the first character.

**Type**

Number (long)

----

.. _jsobjref/TextRange.characters:

TextRange.characters
********************************************************************************

``app.activeDocument.textFrames[index].textRange.characters``

**Description**

All the characters in this text range.

**Type**

:ref:`jsobjref/Characters`, read-only.

----

.. _jsobjref/TextRange.characterStyles:

TextRange.characterStyles
********************************************************************************

``app.activeDocument.textFrames[index].textRange.characterStyles``

**Description**

All referenced character styles in the text range.

**Type**

:ref:`jsobjref/CharacterStyles`, read-only.

----

.. _jsobjref/TextRange.contents:

TextRange.contents
********************************************************************************

``app.activeDocument.textFrames[index].textRange.contents``

**Description**

The text string.

**Type**

String

----

.. _jsobjref/TextRange.end:

TextRange.end
********************************************************************************

``app.activeDocument.textFrames[index].textRange.end``

**Description**

End index of the text range.

**Type**

Int32

----

.. _jsobjref/TextRange.insertionPoints:

TextRange.insertionPoints
********************************************************************************

``app.activeDocument.textFrames[index].textRange.insertionPoints``

**Description**

All the insertion points in this text range.

**Type**

:ref:`jsobjref/InsertionPoints`, read-only.

----

.. _jsobjref/TextRange.kerning:

TextRange.kerning
********************************************************************************

``app.activeDocument.textFrames[index].textRange.kerning``

**Description**

Controls the spacing between two characters, in thousandths of an em. An integer.

**Type**

Number (long)

----

.. _jsobjref/TextRange.length:

TextRange.length
********************************************************************************

``app.activeDocument.textFrames[index].textRange.length``

**Description**

The length (in characters). Minimum: 0

**Type**

Number (long)

----

.. _jsobjref/TextRange.lines:

TextRange.lines
********************************************************************************

``app.activeDocument.textFrames[index].textRange.lines``

**Description**

All the lines in this text range.

**Type**

:ref:`jsobjref/Lines`, read-only.

----

.. _jsobjref/TextRange.paragraphAttributes:

TextRange.paragraphAttributes
********************************************************************************

``app.activeDocument.textFrames[index].textRange.paragraphAttributes``

**Description**

The paragraph properties for the text range.

**Type**

:ref:`jsobjref/ParagraphAttributes`, read-only.

----

.. _jsobjref/TextRange.paragraphs:

TextRange.paragraphs
********************************************************************************

``app.activeDocument.textFrames[index].textRange.paragraphs``

**Description**

All the paragraphs in this text range.

**Type**

:ref:`jsobjref/Paragraphs`, read-only.

----

.. _jsobjref/TextRange.paragraphStyles:

TextRange.paragraphStyles
********************************************************************************

``app.activeDocument.textFrames[index].textRange.paragraphStyles``

**Description**

All referenced paragraph styles in the text range.

**Type**

:ref:`jsobjref/ParagraphStyles`, read-only.

----

.. _jsobjref/TextRange.parent:

TextRange.parent
********************************************************************************

``app.activeDocument.textFrames[index].textRange.parent``

**Description**

The object’s container.

**Type**

:ref:`jsobjref/TextRange`, read-only.

----

.. _jsobjref/TextRange.start:

TextRange.start
********************************************************************************

``app.activeDocument.textFrames[index].textRange.start``

**Description**

Start index of the text range.

**Type**

Int32

----

.. _jsobjref/TextRange.story:

TextRange.story
********************************************************************************

``app.activeDocument.textFrames[index].textRange.story``

**Description**

The story to which the text range belongs.

**Type**

:ref:`jsobjref/Story`, read-only.

----

.. _jsobjref/TextRange.textRanges:

TextRange.textRanges
********************************************************************************

``app.activeDocument.textFrames[index].textRange.textRanges``

**Description**

All of the text in this text range.

**Type**

:ref:`jsobjref/TextRanges`, read-only.

----

.. _jsobjref/TextRange.textSelection:

TextRange.textSelection
********************************************************************************

``app.activeDocument.textFrames[index].textRange.textSelection``

**Description**

The selected text ranges in the text range.

**Type**

Array of :ref:`jsobjref/TextRange`, read-only.

----

.. _jsobjref/TextRange.typename:

TextRange.typename
********************************************************************************

``app.activeDocument.textFrames[index].textRange.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

.. _jsobjref/TextRange.words:

TextRange.words
********************************************************************************

``app.activeDocument.textFrames[index].textRange.words``

**Description**

All the words contained in this text range.

**Type**

:ref:`jsobjref/Words`, read-only.

----

=======
Methods
=======

.. _jsobjref/TextRange.changeCaseTo:

TextRange.changeCaseTo()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.changeCaseTo(type)``

**Description**

Changes the capitalization of text

**Parameters**

+-----------+----------------------------------------------------+----------------------------------+
| Parameter |                        Type                        |           Description            |
+===========+====================================================+==================================+
| ``type``  | :ref:`jsobjref/scripting-constants.CaseChangeType` | Capitalization case to change to |
+-----------+----------------------------------------------------+----------------------------------+

**Returns**

Nothing

----

.. _jsobjref/TextRange.deSelect:

TextRange.deSelect()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.deSelect()``

**Description**

Deselects the text range.

**Returns**

Nothing.

----

.. _jsobjref/TextRange.duplicate:

TextRange.duplicate()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.duplicate([relativeObject][, insertionLocation])``

**Description**

Creates a duplicate of this object.

**Parameters**

+-----------------------+----------------------------------------------------------------+----------------------------+
|       Parameter       |                              Type                              |        Description         |
+=======================+================================================================+============================+
| ``relativeObject``    | Object, optional                                               | Object to duplicate to     |
+-----------------------+----------------------------------------------------------------+----------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to insert element |
+-----------------------+----------------------------------------------------------------+----------------------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/TextRange.getLocalCharOverridesJSON:

TextRange.getLocalCharOverridesJSON()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.getLocalCharOverridesJSON()``

**Description**

Gets json representation of character overrides.

**Returns**

String

----

.. _jsobjref/TextRange.getLocalParaOverridesJSON:

TextRange.getLocalParaOverridesJSON()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.getLocalParaOverridesJSON()``

**Description**

Gets json representation of paragraph overrides.

**Returns**

String

----

.. _jsobjref/TextRange.getParagraphLength:

TextRange.getParagraphLength()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.getParagraphLength()``

**Description**

Gets the length of the first paragraph of the text range.

**Returns**

Int32

----

.. _jsobjref/TextRange.getTextRunLength:

TextRange.getTextRunLength()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.getTextRunLength()``

**Description**

Gets the length of the first text run of the text range.

**Returns**

Int32

----

.. _jsobjref/TextRange.move:

TextRange.move()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.move(relativeObject, insertionLocation)``

**Description**

Moves the object.

**Parameters**


+-----------------------+----------------------------------------------------------------+-------------------------------+
|       Parameter       |                              Type                              |          Description          |
+=======================+================================================================+===============================+
| ``relativeObject``    | Object                                                         | Object to move element within |
+-----------------------+----------------------------------------------------------------+-------------------------------+
| ``insertionLocation`` | :ref:`jsobjref/scripting-constants.ElementPlacement`, optional | Location to move element to   |
+-----------------------+----------------------------------------------------------------+-------------------------------+

**Returns**

:ref:`jsobjref/TextRange`

----

.. _jsobjref/TextRange.remove:

TextRange.remove()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.remove()``

**Description**

Deletes the object.

**Returns**

Nothing

----

.. _jsobjref/TextRange.select:

TextRange.select()
********************************************************************************

``app.activeDocument.textFrames[index].textRange.select([addToDocument])``

**Description**

Selects the text range.

**Parameters**

+-------------------+-------------------+---------------------------------------------+
|     Parameter     |       Type        |                 Description                 |
+===================+===================+=============================================+
| ``addToDocument`` | Boolean, optional | Whether to add or replace current selection |
+-------------------+-------------------+---------------------------------------------+

**Returns**

Nothing

----

=======
Example
=======

Manipulating Text
********************************************************************************

::

  // Changes size of the first character of each word in the
  // current document by changing the size attribute of each character

  if ( app.documents.length > 0 ) {
    for ( i = 0; i < app.activeDocument.textFrames.length; i++ ) {
      var text = app.activeDocument.textFrames[i].textRange;
      for ( j = 0 ; j < text.words.length; j++ ) {
        //each word is a textRange object
        var textWord = text.words[j];

        // Characters are textRanges too.
        // Get the first character of each word and increase it's size.

        var firstChars = textWord.characters[0];
        firstChars.size = firstChars.size * 1.5;
      }
    }
  }
