.. _jsobjref/TextFont:

TextFont
################################################################################

``app.textFonts[index``

**Description**

Information about a font in the document, found in a :ref:`jsobjref/CharacterAttributes` object.

----

==========
Properties
==========

.. _jsobjref/TextFont.family:

TextFont.family
********************************************************************************

``app.textFonts[index].family``

**Description**

The font’s family name.

**Type**

String, read-only.

----

.. _jsobjref/TextFont.name:

TextFont.name
********************************************************************************

``app.textFonts[index].name``

**Description**

The font’s full name.

**Type**

String, read-only.

----

.. _jsobjref/TextFont.parent:

TextFont.parent
********************************************************************************

``app.textFonts[index].parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/TextFont.style:

TextFont.style
********************************************************************************

``app.textFonts[index].style``

**Description**

The font’s style name.

**Type**

String, read-only.

----

.. _jsobjref/TextFont.typename:

TextFont.typename
********************************************************************************

``app.textFonts[index].typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Example
=======

Setting the font of text
********************************************************************************

::

  // Sets the font of all the text in the document to the first font
  if ( app.documents.length > 0 ) {

  // Iterate through all text art and apply font 0
    for ( i = 0; i< app.activeDocument.textFrames.length; i++) {
      textArtRange = app.activeDocument.textFrames[i].textRange;
      textArtRange.characterAttributes.textFont = app.textFonts[0];
    }
  }
