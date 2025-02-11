# ParagraphAttributes

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes`

**Description**

Specifies the properties and attributes of a paragraph contained in a text frame.

!!! note
    Paragraph attributes do not have default values, and are `undefined` untile xplicitly set.

---

## Properties

### ParagraphAttributes.autoLeadingAmount

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.autoLeadingAmount`

**Description**

Auto leading amount expressed as a percentage.

**Type**

Number (double).

---

### ParagraphAttributes.bunriKinshi

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.bunriKinshi`

**Description**

If `true`, BunriKinshi is enabled.

**Type**

Boolean.

---

### ParagraphAttributes.burasagariType

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.burasagariType`

**Description**

The Burasagari type.

**Type**

[BurasagariTypeEnum](scripting-constants.md#jsobjref-scripting-constants-burasagaritypeenum)

---

### ParagraphAttributes.desiredGlyphScaling

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.desiredGlyphScaling`

**Description**

Desired glyph scaling, expressed as a percentage of the default character width. Range: 50.0 to 200.0. At 100.0, the width of characters is not changed.

**Type**

Number (double).

---

### ParagraphAttributes.desiredLetterSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.desiredLetterSpacing`

**Description**

Desired letter, spacing expressed as a percentage of the default kerning or tracking Range: -100.0 to 500.0. At 0, no space is added between letters. At 100.0, an entire space width is added between letters.

**Type**

Number (double).

---

### ParagraphAttributes.desiredWordSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.desiredWordSpacing`

**Description**

Desired word spacing, expressed as a percentage of the default space for the font. Range: 0.0 to 1000.0; at 100.00. No space is added between words.

**Type**

Number (double).

---

### ParagraphAttributes.everyLineComposer

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.everyLineComposer`

**Description**

If `true`, the Every-line Composer is enabled. If `false`, the Single-line Composer is enabled.

**Type**

Boolean.

---

### ParagraphAttributes.firstLineIndent

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.firstLineIndent`

**Description**

First line left indent in points.

**Type**

Number (double).

---

### ParagraphAttributes.hyphenateCapitalizedWords

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.hyphenateCapitalizedWords`

**Description**

If `true`, hyphenation is enabled for capitalized words.

**Type**

Boolean.

---

### ParagraphAttributes.hyphenation

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.hyphenation`

**Description**

If `true`, hyphenation is enabled for the paragraph.

**Type**

Boolean.

---

### ParagraphAttributes.hyphenationPreference

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.hyphenationPreference`

**Description**

Hyphenation preference scale for better spacing (0) or fewer hyphens (1). Range: 0.0 to 1.0.

**Type**

Number (double).

---

### ParagraphAttributes.hyphenationZone

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.hyphenationZone`

**Description**

The distance (in points) from the right edge of the paragraph that marks the part of the line where hyphenation is not allowed.

!!! note
    0 allows all hyphenation. Valid only when [ParagraphAttributes.everyLineComposer](#jsobjref-paragraphattributes-everylinecomposer) is `false`.

**Type**

Number (double).

---

### ParagraphAttributes.justification

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.justification`

**Description**

Paragraph justification.

**Type**

[Justification](scripting-constants.md#jsobjref-scripting-constants-justification)

---

### ParagraphAttributes.kinsoku

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.kinsoku`

**Description**

The Kinsoku Shori name.

**Type**

String.

---

### ParagraphAttributes.kinsokuOrder

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.kinsokuOrder`

**Description**

The preferred Kinsoku order.

**Type**

[KinsokuOrderEnum](scripting-constants.md#jsobjref-scripting-constants-kinsokuorderenum)

---

### ParagraphAttributes.kurikaeshiMojiShori

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.kurikaeshiMojiShori`

**Description**

If `true`, KurikaeshiMojiShori is enabled.

**Type**

Boolean.

---

### ParagraphAttributes.leadingType

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.leadingType`

**Description**

Auto leading type.

**Type**

[AutoLeadingType](scripting-constants.md#jsobjref-scripting-constants-autoleadingtype)

---

### ParagraphAttributes.leftIndent

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.leftIndent`

**Description**

The left indent of margin in points.

**Type**

Number (double).

---

### ParagraphAttributes.maximumConsecutiveHyphens

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.maximumConsecutiveHyphens`

**Description**

Maximum number of consecutive hyphenated lines.

**Type**

Number (long).

---

### ParagraphAttributes.maximumGlyphScaling

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.maximumGlyphScaling`

**Description**

Maximum glyph scaling, expressed as a percentage of the default character width. Range: 50.0 to 200.0; at 100.0. The width of characters is not changed.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.maximumLetterSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.maximumLetterSpacing`

**Description**

Maximum letter spacing, expressed as a percentage of the default kerning or tracking Range: -100.0 to 500.0; at 0. No space is added between letters. At 100.0, an entire space width is added between letters.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.maximumWordSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.maximumWordSpacing`

**Description**

Maximum word spacing, expressed as a percentage of the default space for the font. Range: 0.0 to 1000.0; at 100.00. No space is added between words.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.minimumAfterHyphen

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumAfterHyphen`

**Description**

Minimum number of characters after a hyphen.

**Type**

Number (long).

---

### ParagraphAttributes.minimumBeforeHyphen

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumBeforeHyphen`

**Description**

Minimum number of characters before a hyphen.

**Type**

Number (long).

---

### ParagraphAttributes.minimumGlyphScaling

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumGlyphScaling`

**Description**

Minimum glyph scaling, expressed as a percentage of the default character width. Range: 50.0 to 200.0. At 100.0, the width of characters is not changed.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.minimumHyphenatedWordSize

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumHyphenatedWordSize`

**Description**

Minimum number of characters for a word to be hyphenated.

**Type**

Number (long).

---

### ParagraphAttributes.minimumLetterSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumLetterSpacing`

**Description**

Minimum letter spacing, expressed as a percentage of the default kerning or tracking Range: -100.0 to 500.0; at 0. No space is added between letters. At 100.0, an entire space width is added between letters.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.minimumWordSpacing

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.minimumWordSpacing`

**Description**

Minimum word spacing, expressed as a percentage of the default space for the font. Range: 0.0 to 1000.0; at 100.00. No space is added between words.

!!! note
    Valid only for justified paragraphs.

**Type**

Number (double).

---

### ParagraphAttributes.mojikumi

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.mojikumi`

**Description**

The Mojikumi name.

**Type**

String.

---

### ParagraphAttributes.parent

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.parent`

**Description**

The object's container.

**Type**

Object, read-only.

---

### ParagraphAttributes.rightIndent

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.rightIndent`

**Description**

Right indent of margin in points.

**Type**

Number (double).

---

### ParagraphAttributes.romanHanging

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.romanHanging`

**Description**

If `true`, Roman hanging punctuation is enabled.

**Type**

Boolean.

---

### ParagraphAttributes.singleWordJustification

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.singleWordJustification`

**Description**

Single word justification.

**Type**

[Justification](scripting-constants.md#jsobjref-scripting-constants-justification)

---

### ParagraphAttributes.spaceAfter

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.spaceAfter`

**Description**

Spacing after paragraph in points.

**Type**

Number (double).

---

### ParagraphAttributes.spaceBefore

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.spaceBefore`

**Description**

Spacing before paragraph in points.

**Type**

Number (double).

---

### ParagraphAttributes.tabStops

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops`

**Description**

Tab stop settings.

**Type**

[TabStopInfo](TabStopInfo.md#jsobjref-tabstopinfo)

---

### ParagraphAttributes.typename

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.typename`

**Description**

> The class name of the object.

**Type**

String, read-only.

---

## Example

### Changing justification in paragraphs

```default
// Creates a new document with 1 text frame and 3 paragraphs
// then gives each paragraph a different justification

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
```
