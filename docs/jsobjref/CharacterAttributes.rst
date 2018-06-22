.. _jsobjref/CharacterAttributes:

CharacterAttributes
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

.. _jsobjref/CharacterAttributes.akiLeft:

CharacterAttributes.akiLeft
********************************************************************************

``characterAttributes.akiLeft``

**Description**

The amount of inter-character spacing to be added to the left side of the character, in thousandths of an em (that amount will not compress or expand during full-justification).

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.akiRight:

CharacterAttributes.akiRight
********************************************************************************

``characterAttributes.akiRight``

**Description**

The amount of inter-character spacing to be added to the right side of the character, in thousandths of an em  (that amount will not compress or expand during full-justification).

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.alignment:

CharacterAttributes.alignment
********************************************************************************

``characterAttributes.alignment``

**Description**

The character alignment type.

**Type**

:ref:`jsobjref/scripting-constants.StyleRunAlignmentType`

----

.. _jsobjref/CharacterAttributes.alternateGlyphs:

CharacterAttributes.alternateGlyphs
********************************************************************************

``characterAttributes.alternateGlyphs``

**Description**

The alternate glyphs form.

**Type**

:ref:`jsobjref/scripting-constants.AlternateGlyphsForm`

----

.. _jsobjref/CharacterAttributes.autoLeading:

CharacterAttributes.autoLeading
********************************************************************************

``characterAttributes.autoLeading``

**Description**

If ``true``, the automatic leading should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.baselineDirection:

CharacterAttributes.baselineDirection
********************************************************************************

``characterAttributes.baselineDirection``

**Description**

The Japanese text baseline direction.

**Type**

:ref:`jsobjref/scripting-constants.BaselineDirectionType`

----

.. _jsobjref/CharacterAttributes.baselinePosition:

CharacterAttributes.baselinePosition
********************************************************************************

``characterAttributes.baselinePosition``

**Description**

The baseline position of text.

**Type**

:ref:`jsobjref/scripting-constants.FontBaselineOption`

----

.. _jsobjref/CharacterAttributes.baselineShift:

CharacterAttributes.baselineShift
********************************************************************************

``characterAttributes.baselineShift``

**Description**

The amount of shift in points of the text baseline.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.capitalization:

CharacterAttributes.capitalization
********************************************************************************

``characterAttributes.capitalization``

**Description**

The case of text.

**Type**

:ref:`jsobjref/scripting-constants.FontCapsOption`

----

.. _jsobjref/CharacterAttributes.connectionForms:

CharacterAttributes.connectionForms
********************************************************************************

``characterAttributes.connectionForms``

**Description**

If ``true``, the OpenType® connection forms should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.contextualLigature:

CharacterAttributes.contextualLigature
********************************************************************************

``characterAttributes.contextualLigature``

**Description**

If ``true``, the contextual ligature should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.discretionaryLigature:

CharacterAttributes.discretionaryLigature
********************************************************************************

``characterAttributes.discretionaryLigature``

**Description**

If ``true``, the discretionary ligature should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.figureStyle:

CharacterAttributes.figureStyle
********************************************************************************

``characterAttributes.figureStyle``

**Description**

The number style in a OpenType font.

**Type**

:ref:`jsobjref/scripting-constants.FigureStyleType`

----

.. _jsobjref/CharacterAttributes.fillColor:

CharacterAttributes.fillColor
********************************************************************************

``characterAttributes.fillColor``

**Description**

The color of the text fill.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/CharacterAttributes.fractions:

CharacterAttributes.fractions
********************************************************************************

``characterAttributes.fractions``

**Description**

If ``true``, the OpenType fractions should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.horizontalScale:

CharacterAttributes.horizontalScale
********************************************************************************

``characterAttributes.horizontalScale``

**Description**

The character horizontal scaling factor expressed as a percentage (100 = 100%).

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.italics:

CharacterAttributes.italics
********************************************************************************

``characterAttributes.italics``

**Description**

If ``true``, the Japanese OpenType font supports italics.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.kerningMethod:

CharacterAttributes.kerningMethod
********************************************************************************

``characterAttributes.kerningMethod``

**Description**

The automatic kerning method to use.

**Type**

:ref:`jsobjref/scripting-constants.AutoKernType`

----

.. _jsobjref/CharacterAttributes.language:

CharacterAttributes.language
********************************************************************************

``characterAttributes.language``

**Description**

The language of text.

**Type**

:ref:`jsobjref/scripting-constants.LanguageType`

----

.. _jsobjref/CharacterAttributes.leading:

CharacterAttributes.leading
********************************************************************************

``characterAttributes.leading``

**Description**

The amount of space between two lines of text, in points.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.ligature:

CharacterAttributes.ligature
********************************************************************************

``characterAttributes.ligature``

**Description**

If ``true``, the ligature should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.noBreak:

CharacterAttributes.noBreak
********************************************************************************

``characterAttributes.noBreak``

**Description**

If ``true``, line breaks are not allowed.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.openTypePosition:

CharacterAttributes.openTypePosition
********************************************************************************

``characterAttributes.openTypePosition``

**Description**

The OpenType baseline position.

**Type**

:ref:`jsobjref/scripting-constants.FontOpenTypePositionOption`

----

.. _jsobjref/CharacterAttributes.ordinals:

CharacterAttributes.ordinals
********************************************************************************

``characterAttributes.ordinals``

**Description**

If ``true``, the OpenType ordinals should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.ornaments:

CharacterAttributes.ornaments
********************************************************************************

``characterAttributes.ornaments``

**Description**

If ``true``, the OpenType ornaments should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.overprintFill:

CharacterAttributes.overprintFill
********************************************************************************

``characterAttributes.overprintFill``

**Description**

If ``true``, the fill of the text should be overprinted.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.overprintStroke:

CharacterAttributes.overprintStroke
********************************************************************************

``characterAttributes.overprintStroke``

**Description**

If ``true``, the stroke of the text should be overprinted.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.parent:

CharacterAttributes.parent
********************************************************************************

``characterAttributes.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/CharacterAttributes.proportionalMetrics:

CharacterAttributes.proportionalMetrics
********************************************************************************

``characterAttributes.proportionalMetrics``

**Description**

If ``true``, the Japanese OpenType font supports proportional glyphs.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.rotation:

CharacterAttributes.rotation
********************************************************************************

``characterAttributes.rotation``

**Description**

The character rotation angle in degrees.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.size:

CharacterAttributes.size
********************************************************************************

``characterAttributes.size``

**Description**

Font size in points.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.strikeThrough:

CharacterAttributes.strikeThrough
********************************************************************************

``characterAttributes.strikeThrough``

**Description**

If ``true``, characters use strike-through style.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.strokeColor:

CharacterAttributes.strokeColor
********************************************************************************

``characterAttributes.strokeColor``

**Description**

The color of the text stroke.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/CharacterAttributes.strokeWeight:

CharacterAttributes.strokeWeight
********************************************************************************

``characterAttributes.strokeWeight``

**Description**

Line width of stroke.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.stylisticAlternates:

CharacterAttributes.stylisticAlternates
********************************************************************************

``characterAttributes.stylisticAlternates``

**Description**

If ``true``, the OpenType stylistic alternates should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.swash:

CharacterAttributes.swash
********************************************************************************

``characterAttributes.swash``

**Description**

If ``true``, the OpenType swash should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.tateChuYokoHorizontal:

CharacterAttributes.tateChuYokoHorizontal
********************************************************************************

``characterAttributes.tateChuYokoHorizontal``

**Description**

The Tate-Chu-Yoko horizontal adjustment in points.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.tateChuYokoVertical:

CharacterAttributes.tateChuYokoVertical
********************************************************************************

``characterAttributes.tateChuYokoVertical``

**Description**

The Tate-Chu-Yoko vertical adjustment in points.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.textFont:

CharacterAttributes.textFont
********************************************************************************

``characterAttributes.textFont``

**Description**

The text font.

**Type**

:ref:`jsobjref/TextFont`

----

.. _jsobjref/CharacterAttributes.titling:

CharacterAttributes.titling
********************************************************************************

``characterAttributes.titling``

**Description**

If ``true``, the OpenType titling alternates should be used.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.tracking:

CharacterAttributes.tracking
********************************************************************************

``characterAttributes.tracking``

**Description**

The tracking or range kerning amount, in thousandths of an em.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.Tsume:

CharacterAttributes.Tsume
********************************************************************************

``characterAttributes.Tsume``

**Description**

The percentage of space reduction around a Japanese character.

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.typename:

CharacterAttributes.typename
********************************************************************************

``characterAttributes.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

.. _jsobjref/CharacterAttributes.underline:

CharacterAttributes.underline
********************************************************************************

``characterAttributes.underline``

**Description**

If ``true``, characters are underlined.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.verticalScale:

CharacterAttributes.verticalScale
********************************************************************************

``characterAttributes.verticalScale``

**Description**

Character vertical scaling factor expressed as a percentage (= 100%).

**Type**

Number (double)

----

.. _jsobjref/CharacterAttributes.wariChuCharactersAfterBreak:

CharacterAttributes.wariChuCharactersAfterBreak
********************************************************************************

``characterAttributes.wariChuCharactersAfterBreak``

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.wariChuCharactersBeforeBreak:

CharacterAttributes.wariChuCharactersBeforeBreak
********************************************************************************

``characterAttributes.wariChuCharactersBeforeBreak``

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.waiChuEnabled:

CharacterAttributes.waiChuEnabled
********************************************************************************

``characterAttributes.waiChuEnabled``

**Description**

If ``true``, Wari-Chu is enabled.

**Type**

Boolean

----

.. _jsobjref/CharacterAttributes.wariChuJustification:

CharacterAttributes.wariChuJustification
********************************************************************************

``characterAttributes.wariChuJustification``

**Description**

The Wari-Chu justification.

**Type**

:ref:`jsobjref/scripting-constants.WariChuJustificationType`

----

.. _jsobjref/CharacterAttributes.wariChuLineGap:

CharacterAttributes.wariChuLineGap
********************************************************************************

``characterAttributes.wariChuLineGap``

**Description**

The Wari-Chu line gap.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.wariChuLines:

CharacterAttributes.wariChuLines
********************************************************************************

``characterAttributes.wariChuLines``

**Description**

The number of Wari-Chu (multiple text lines fit into a space meant for one) lines.

**Type**

Number (long)

----

.. _jsobjref/CharacterAttributes.wariChuScale:

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
