.. _jsobjref/characterAttributes:

Character Attributes
################################################################################

``characterAttributes``

**Description**

Specifies the properties of a character contained in a text frame. A ``CharacterStyle`` object associates these attributes with a specific text range through its ``characterAttributes`` property.

.. note::
  Character attributes do not have default values, and are undefined until explicitly set.

// todo: get the absolute path to characterAttributes.. ``document.textFrames.textRef.textRange.characters[index].characterAttributes`` ?

----

==========
Properties
==========

.. _jsobjref/characterAttributes.akiLeft:

CharacterAttributes.akiLeft
********************************************************************************

``characterAttributes.akiLeft``

**Description**

The amount of inter-character spacing to be added to the left side of the character, in thousandths of an em (that amount will not compress or expand during full-justification).

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.akiRight:

CharacterAttributes.akiRight
********************************************************************************

``characterAttributes.akiRight``

**Description**

The amount of inter-character spacing to be added to the right side of the character, in thousandths of an em  (that amount will not compress or expand during full-justification).

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.alignment:

CharacterAttributes.alignment
********************************************************************************

``characterAttributes.alignment``

**Description**

The character alignment type.

**Type**

:ref:`jsobjref/scriptingConstants.StyleRunAlignmentType`

----

.. _jsobjref/characterAttributes.alternateGlyphs:

CharacterAttributes.alternateGlyphs
********************************************************************************

``characterAttributes.alternateGlyphs``

**Description**

The alternate glyphs form.

**Type**

:ref:`jsobjref/scriptingConstants.AlternateGlyphsForm`

----

.. _jsobjref/characterAttributes.autoLeading:

CharacterAttributes.autoLeading
********************************************************************************

``characterAttributes.autoLeading``

**Description**

If ``true``, the automatic leading should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.baselineDirection:

CharacterAttributes.baselineDirection
********************************************************************************

``characterAttributes.baselineDirection``

**Description**

The Japanese text baseline direction.

**Type**

:ref:`jsobjref/scriptingConstants.BaselineDirectionType`

----

.. _jsobjref/characterAttributes.baselinePosition:

CharacterAttributes.baselinePosition
********************************************************************************

``characterAttributes.baselinePosition``

**Description**

The baseline position of text.

**Type**

:ref:`jsobjref/scriptingConstants.FontBaselineOption`

----

.. _jsobjref/characterAttributes.baselineShift:

CharacterAttributes.baselineShift
********************************************************************************

``characterAttributes.baselineShift``

**Description**

The amount of shift in points of the text baseline.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.capitalization:

CharacterAttributes.capitalization
********************************************************************************

``characterAttributes.capitalization``

**Description**

The case of text.

**Type**

:ref:`jsobjref/scriptingConstants.FontCapsOption`

----

.. _jsobjref/characterAttributes.connectionForms:

CharacterAttributes.connectionForms
********************************************************************************

``characterAttributes.connectionForms``

**Description**

If ``true``, the OpenType® connection forms should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.contextualLigature:

CharacterAttributes.contextualLigature
********************************************************************************

``characterAttributes.contextualLigature``

**Description**

If ``true``, the contextual ligature should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.discretionaryLigature:

CharacterAttributes.discretionaryLigature
********************************************************************************

``characterAttributes.discretionaryLigature``

**Description**

If ``true``, the discretionary ligature should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.figureStyle:

CharacterAttributes.figureStyle
********************************************************************************

``characterAttributes.figureStyle``

**Description**

The number style in a OpenType font.

**Type**

:ref:`jsobjref/scriptingConstants.FigureStyleType`

----

.. _jsobjref/characterAttributes.fillColor:

CharacterAttributes.fillColor
********************************************************************************

``characterAttributes.fillColor``

**Description**

The color of the text fill.

**Type**

:ref:`jsobjref/color`

----

.. _jsobjref/characterAttributes.fractions:

CharacterAttributes.fractions
********************************************************************************

``characterAttributes.fractions``

**Description**

If ``true``, the OpenType fractions should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.horizontalScale:

CharacterAttributes.horizontalScale
********************************************************************************

``characterAttributes.horizontalScale``

**Description**

The character horizontal scaling factor expressed as a percentage (100 = 100%).

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.italics:

CharacterAttributes.italics
********************************************************************************

``characterAttributes.italics``

**Description**

If ``true``, the Japanese OpenType font supports italics.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.kerningMethod:

CharacterAttributes.kerningMethod
********************************************************************************

``characterAttributes.kerningMethod``

**Description**

The automatic kerning method to use.

**Type**

:ref:`jsobjref/scriptingConstants.AutoKernType`

----

.. _jsobjref/characterAttributes.language:

CharacterAttributes.language
********************************************************************************

``characterAttributes.language``

**Description**

The language of text.

**Type**

:ref:`jsobjref/scriptingConstants.LanguageType`

----

.. _jsobjref/characterAttributes.leading:

CharacterAttributes.leading
********************************************************************************

``characterAttributes.leading``

**Description**

The amount of space between two lines of text, in points.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.ligature:

CharacterAttributes.ligature
********************************************************************************

``characterAttributes.ligature``

**Description**

If ``true``, the ligature should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.noBreak:

CharacterAttributes.noBreak
********************************************************************************

``characterAttributes.noBreak``

**Description**

If ``true``, line breaks are not allowed.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.openTypePosition:

CharacterAttributes.openTypePosition
********************************************************************************

``characterAttributes.openTypePosition``

**Description**

The OpenType baseline position.

**Type**

:ref:`jsobjref/scriptingConstants.FontOpenTypePositionOption`

----

.. _jsobjref/characterAttributes.ordinals:

CharacterAttributes.ordinals
********************************************************************************

``characterAttributes.ordinals``

**Description**

If ``true``, the OpenType ordinals should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.ornaments:

CharacterAttributes.ornaments
********************************************************************************

``characterAttributes.ornaments``

**Description**

If ``true``, the OpenType ornaments should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.overprintFill:

CharacterAttributes.overprintFill
********************************************************************************

``characterAttributes.overprintFill``

**Description**

If ``true``, the fill of the text should be overprinted.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.overprintStroke:

CharacterAttributes.overprintStroke
********************************************************************************

``characterAttributes.overprintStroke``

**Description**

If ``true``, the stroke of the text should be overprinted.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.parent:

CharacterAttributes.parent
********************************************************************************

``characterAttributes.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/characterAttributes.proportionalMetrics:

CharacterAttributes.proportionalMetrics
********************************************************************************

``characterAttributes.proportionalMetrics``

**Description**

If ``true``, the Japanese OpenType font supports proportional glyphs.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.rotation:

CharacterAttributes.rotation
********************************************************************************

``characterAttributes.rotation``

**Description**

The character rotation angle in degrees.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.size:

CharacterAttributes.size
********************************************************************************

``characterAttributes.size``

**Description**

Font size in points.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.strikeThrough:

CharacterAttributes.strikeThrough
********************************************************************************

``characterAttributes.strikeThrough``

**Description**

If ``true``, characters use strike-through style.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.strokeColor:

CharacterAttributes.strokeColor
********************************************************************************

``characterAttributes.strokeColor``

**Description**

The color of the text stroke.

**Type**

:ref:`jsobjref/color`

----

.. _jsobjref/characterAttributes.strokeWeight:

CharacterAttributes.strokeWeight
********************************************************************************

``characterAttributes.strokeWeight``

**Description**

Line width of stroke.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.stylisticAlternates:

CharacterAttributes.stylisticAlternates
********************************************************************************

``characterAttributes.stylisticAlternates``

**Description**

If ``true``, the OpenType stylistic alternates should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.swash:

CharacterAttributes.swash
********************************************************************************

``characterAttributes.swash``

**Description**

If ``true``, the OpenType swash should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.tateChuYokoHorizontal:

CharacterAttributes.tateChuYokoHorizontal
********************************************************************************

``characterAttributes.tateChuYokoHorizontal``

**Description**

The Tate-Chu-Yoko horizontal adjustment in points.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.tateChuYokoVertical:

CharacterAttributes.tateChuYokoVertical
********************************************************************************

``characterAttributes.tateChuYokoVertical``

**Description**

The Tate-Chu-Yoko vertical adjustment in points.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.textFont:

CharacterAttributes.textFont
********************************************************************************

``characterAttributes.textFont``

**Description**

The text font.

**Type**

:ref:`jsobjref/textFont`

----

.. _jsobjref/characterAttributes.titling:

CharacterAttributes.titling
********************************************************************************

``characterAttributes.titling``

**Description**

If ``true``, the OpenType titling alternates should be used.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.tracking:

CharacterAttributes.tracking
********************************************************************************

``characterAttributes.tracking``

**Description**

The tracking or range kerning amount, in thousandths of an em.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.Tsume:

CharacterAttributes.Tsume
********************************************************************************

``characterAttributes.Tsume``

**Description**

The percentage of space reduction around a Japanese character.

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.typename:

CharacterAttributes.typename
********************************************************************************

``characterAttributes.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

.. _jsobjref/characterAttributes.underline:

CharacterAttributes.underline
********************************************************************************

``characterAttributes.underline``

**Description**

If ``true``, characters are underlined.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.verticalScale:

CharacterAttributes.verticalScale
********************************************************************************

``characterAttributes.verticalScale``

**Description**

Character vertical scaling factor expressed as a percentage (= 100%).

**Type**

Number (double)

----

.. _jsobjref/characterAttributes.wariChuCharactersAfterBreak:

CharacterAttributes.wariChuCharactersAfterBreak
********************************************************************************

``characterAttributes.wariChuCharactersAfterBreak``

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.wariChuCharactersBeforeBreak:

CharacterAttributes.wariChuCharactersBeforeBreak
********************************************************************************

``characterAttributes.wariChuCharactersBeforeBreak``

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.waiChuEnabled:

CharacterAttributes.waiChuEnabled
********************************************************************************

``characterAttributes.waiChuEnabled``

**Description**

If ``true``, Wari-Chu is enabled.

**Type**

Boolean

----

.. _jsobjref/characterAttributes.wariChuJustification:

CharacterAttributes.wariChuJustification
********************************************************************************

``characterAttributes.wariChuJustification``

**Description**

The Wari-Chu justification.

**Type**

:ref:`jsobjref/scriptingConstants.WariChuJustificationType`

----

.. _jsobjref/characterAttributes.wariChuLineGap:

CharacterAttributes.wariChuLineGap
********************************************************************************

``characterAttributes.wariChuLineGap``

**Description**

The Wari-Chu line gap.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.wariChuLines:

CharacterAttributes.wariChuLines
********************************************************************************

``characterAttributes.wariChuLines``

**Description**

The number of Wari-Chu (multiple text lines fit into a space meant for one) lines.

**Type**

Number (long)

----

.. _jsobjref/characterAttributes.wariChuScale:

CharacterAttributes.wariChuScale
********************************************************************************

``characterAttributes.wariChuScale``

**Description**

The Wari-Chu scale.

**Type**

Number (double)

----

=======
Example
=======

Setting character attributes
********************************************************************************

::

  // Creates a new document, adds a simple text item
  // then incrementally increases the horizontal and
  // vertical scale attributes of each character

  var docRef = documents.add();
  var textRef = docRef.textFrames.add();
  textRef.contents = "I Love Scripting!";
  textRef.top = 400;
  textRef.left = 100;

  // incrementally increase the scale of each character
  var charCount = textRef.textRange.characters.length;
  var size = 100;
  for(i=0; i<charCount; i++, size *= 1.2) {
    textRef.textRange.characters[i].characterAttributes.horizontalScale = size;
    textRef.textRange.characters[i].characterAttributes.verticalScale = size;
  }
