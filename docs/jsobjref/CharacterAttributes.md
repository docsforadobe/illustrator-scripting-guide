# CharacterAttributes

`characterAttributes`

**Description**

Specifies the properties of a character contained in a text frame. A `CharacterStyle` object associates these attributes with a specific text range through its `characterAttributes` property.

!!! note
    Character attributes do not have default values, and are undefined until explicitly set.

// todo: get the absolute path to characterAttributes.. `document.textFrames.textRef.textRange.characters[index].characterAttributes` ?

---

## Properties

### CharacterAttributes.akiLeft

`characterAttributes.akiLeft`

**Description**

The amount of inter-character spacing to be added to the left side of the character, in thousandths of an em (that amount will not compress or expand during full-justification).

**Type**

Number (double)

---

### CharacterAttributes.akiRight

`characterAttributes.akiRight`

**Description**

The amount of inter-character spacing to be added to the right side of the character, in thousandths of an em  (that amount will not compress or expand during full-justification).

**Type**

Number (double)

---

### CharacterAttributes.alignment

`characterAttributes.alignment`

**Description**

The character alignment type.

**Type**

[StyleRunAlignmentType](scripting-constants.md#jsobjref-scripting-constants-stylerunalignmenttype)

---

### CharacterAttributes.alternateGlyphs

`characterAttributes.alternateGlyphs`

**Description**

The alternate glyphs form.

**Type**

[AlternateGlyphsForm](scripting-constants.md#jsobjref-scripting-constants-alternateglyphsform)

---

### CharacterAttributes.autoLeading

`characterAttributes.autoLeading`

**Description**

If `true`, the automatic leading should be used.

**Type**

Boolean

---

### CharacterAttributes.baselineDirection

`characterAttributes.baselineDirection`

**Description**

The Japanese text baseline direction.

**Type**

[BaselineDirectionType](scripting-constants.md#jsobjref-scripting-constants-baselinedirectiontype)

---

### CharacterAttributes.baselinePosition

`characterAttributes.baselinePosition`

**Description**

The baseline position of text.

**Type**

[FontBaselineOption](scripting-constants.md#jsobjref-scripting-constants-fontbaselineoption)

---

### CharacterAttributes.baselineShift

`characterAttributes.baselineShift`

**Description**

The amount of shift in points of the text baseline.

**Type**

Number (double)

---

### CharacterAttributes.capitalization

`characterAttributes.capitalization`

**Description**

The case of text.

**Type**

[FontCapsOption](scripting-constants.md#jsobjref-scripting-constants-fontcapsoption)

---

### CharacterAttributes.connectionForms

`characterAttributes.connectionForms`

**Description**

If `true`, the OpenType® connection forms should be used.

**Type**

Boolean

---

### CharacterAttributes.contextualLigature

`characterAttributes.contextualLigature`

**Description**

If `true`, the contextual ligature should be used.

**Type**

Boolean

---

### CharacterAttributes.discretionaryLigature

`characterAttributes.discretionaryLigature`

**Description**

If `true`, the discretionary ligature should be used.

**Type**

Boolean

---

### CharacterAttributes.figureStyle

`characterAttributes.figureStyle`

**Description**

The number style in a OpenType font.

**Type**

[FigureStyleType](scripting-constants.md#jsobjref-scripting-constants-figurestyletype)

---

### CharacterAttributes.fillColor

`characterAttributes.fillColor`

**Description**

The color of the text fill.

**Type**

[Color](Color.md#jsobjref-color)

---

### CharacterAttributes.fractions

`characterAttributes.fractions`

**Description**

If `true`, the OpenType fractions should be used.

**Type**

Boolean

---

### CharacterAttributes.horizontalScale

`characterAttributes.horizontalScale`

**Description**

The character horizontal scaling factor expressed as a percentage (100 = 100%).

**Type**

Number (double)

---

### CharacterAttributes.italics

`characterAttributes.italics`

**Description**

If `true`, the Japanese OpenType font supports italics.

**Type**

Boolean

---

### CharacterAttributes.kerningMethod

`characterAttributes.kerningMethod`

**Description**

The automatic kerning method to use.

**Type**

[AutoKernType](scripting-constants.md#jsobjref-scripting-constants-autokerntype)

---

### CharacterAttributes.language

`characterAttributes.language`

**Description**

The language of text.

**Type**

[LanguageType](scripting-constants.md#jsobjref-scripting-constants-languagetype)

---

### CharacterAttributes.leading

`characterAttributes.leading`

**Description**

The amount of space between two lines of text, in points.

**Type**

Number (double)

---

### CharacterAttributes.ligature

`characterAttributes.ligature`

**Description**

If `true`, the ligature should be used.

**Type**

Boolean

---

### CharacterAttributes.noBreak

`characterAttributes.noBreak`

**Description**

If `true`, line breaks are not allowed.

**Type**

Boolean

---

### CharacterAttributes.openTypePosition

`characterAttributes.openTypePosition`

**Description**

The OpenType baseline position.

**Type**

[FontOpenTypePositionOption](scripting-constants.md#jsobjref-scripting-constants-fontopentypepositionoption)

---

### CharacterAttributes.ordinals

`characterAttributes.ordinals`

**Description**

If `true`, the OpenType ordinals should be used.

**Type**

Boolean

---

### CharacterAttributes.ornaments

`characterAttributes.ornaments`

**Description**

If `true`, the OpenType ornaments should be used.

**Type**

Boolean

---

### CharacterAttributes.overprintFill

`characterAttributes.overprintFill`

**Description**

If `true`, the fill of the text should be overprinted.

**Type**

Boolean

---

### CharacterAttributes.overprintStroke

`characterAttributes.overprintStroke`

**Description**

If `true`, the stroke of the text should be overprinted.

**Type**

Boolean

---

### CharacterAttributes.parent

`characterAttributes.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

### CharacterAttributes.proportionalMetrics

`characterAttributes.proportionalMetrics`

**Description**

If `true`, the Japanese OpenType font supports proportional glyphs.

**Type**

Boolean

---

### CharacterAttributes.rotation

`characterAttributes.rotation`

**Description**

The character rotation angle in degrees.

**Type**

Number (double)

---

### CharacterAttributes.size

`characterAttributes.size`

**Description**

Font size in points.

**Type**

Number (double)

---

### CharacterAttributes.strikeThrough

`characterAttributes.strikeThrough`

**Description**

If `true`, characters use strike-through style.

**Type**

Boolean

---

### CharacterAttributes.strokeColor

`characterAttributes.strokeColor`

**Description**

The color of the text stroke.

**Type**

[Color](Color.md#jsobjref-color)

---

### CharacterAttributes.strokeWeight

`characterAttributes.strokeWeight`

**Description**

Line width of stroke.

**Type**

Number (double)

---

### CharacterAttributes.stylisticAlternates

`characterAttributes.stylisticAlternates`

**Description**

If `true`, the OpenType stylistic alternates should be used.

**Type**

Boolean

---

### CharacterAttributes.swash

`characterAttributes.swash`

**Description**

If `true`, the OpenType swash should be used.

**Type**

Boolean

---

### CharacterAttributes.tateChuYokoHorizontal

`characterAttributes.tateChuYokoHorizontal`

**Description**

The Tate-Chu-Yoko horizontal adjustment in points.

**Type**

Number (long)

---

### CharacterAttributes.tateChuYokoVertical

`characterAttributes.tateChuYokoVertical`

**Description**

The Tate-Chu-Yoko vertical adjustment in points.

**Type**

Number (long)

---

### CharacterAttributes.textFont

`characterAttributes.textFont`

**Description**

The text font.

**Type**

[TextFont](TextFont.md#jsobjref-textfont)

---

### CharacterAttributes.titling

`characterAttributes.titling`

**Description**

If `true`, the OpenType titling alternates should be used.

**Type**

Boolean

---

### CharacterAttributes.tracking

`characterAttributes.tracking`

**Description**

The tracking or range kerning amount, in thousandths of an em.

**Type**

Number (long)

---

### CharacterAttributes.Tsume

`characterAttributes.Tsume`

**Description**

The percentage of space reduction around a Japanese character.

**Type**

Number (double)

---

### CharacterAttributes.typename

`characterAttributes.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

### CharacterAttributes.underline

`characterAttributes.underline`

**Description**

If `true`, characters are underlined.

**Type**

Boolean

---

### CharacterAttributes.verticalScale

`characterAttributes.verticalScale`

**Description**

Character vertical scaling factor expressed as a percentage (= 100%).

**Type**

Number (double)

---

### CharacterAttributes.wariChuCharactersAfterBreak

`characterAttributes.wariChuCharactersAfterBreak`

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

---

### CharacterAttributes.wariChuCharactersBeforeBreak

`characterAttributes.wariChuCharactersBeforeBreak`

**Description**

Specifies how the characters in Wari-Chu text (an inset note in Japanese text) are divided into two or more lines.

**Type**

Number (long)

---

### CharacterAttributes.waiChuEnabled

`characterAttributes.waiChuEnabled`

**Description**

If `true`, Wari-Chu is enabled.

**Type**

Boolean

---

### CharacterAttributes.wariChuJustification

`characterAttributes.wariChuJustification`

**Description**

The Wari-Chu justification.

**Type**

[WariChuJustificationType](scripting-constants.md#jsobjref-scripting-constants-warichujustificationtype)

---

### CharacterAttributes.wariChuLineGap

`characterAttributes.wariChuLineGap`

**Description**

The Wari-Chu line gap.

**Type**

Number (long)

---

### CharacterAttributes.wariChuLines

`characterAttributes.wariChuLines`

**Description**

The number of Wari-Chu (multiple text lines fit into a space meant for one) lines.

**Type**

Number (long)

---

### CharacterAttributes.wariChuScale

`characterAttributes.wariChuScale`

**Description**

The Wari-Chu scale.

**Type**

Number (double)

---

## Example

### Setting character attributes

```default
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
for (var i = 0; i < charCount; i++, size *= 1.2) {
  textRef.textRange.characters[i].characterAttributes.horizontalScale = size;
  textRef.textRange.characters[i].characterAttributes.verticalScale = size;
}
```
