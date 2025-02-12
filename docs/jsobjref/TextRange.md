# TextRange

`app.activeDocument.textFrames[index].textRange`

#### Description

A range of text in a specific text art item. TextRange gives you access to the text contained in text art items.

---

## Properties

### TextRange.characterAttributes

`app.activeDocument.textFrames[index].textRange.characterAttributes`

#### Description

The character properties for the text range.

#### Type

[CharacterAttributes](./CharacterAttributes.md); read-only.

---

### TextRange.characterOffset

`app.activeDocument.textFrames[index].textRange.characterOffset`

#### Description

Offset of the first character.

#### Type

Number (long)

---

### TextRange.characters

`app.activeDocument.textFrames[index].textRange.characters`

#### Description

All the characters in this text range.

#### Type

[Characters](./Characters.md); read-only.

---

### TextRange.characterStyles

`app.activeDocument.textFrames[index].textRange.characterStyles`

#### Description

All referenced character styles in the text range.

#### Type

[CharacterStyles](./CharacterStyles.md); read-only.

---

### TextRange.contents

`app.activeDocument.textFrames[index].textRange.contents`

#### Description

The text string.

#### Type

String

---

### TextRange.end

`app.activeDocument.textFrames[index].textRange.end`

#### Description

End index of the text range.

#### Type

Int32

---

### TextRange.insertionPoints

`app.activeDocument.textFrames[index].textRange.insertionPoints`

#### Description

All the insertion points in this text range.

#### Type

[InsertionPoints](./InsertionPoints.md); read-only.

---

### TextRange.kerning

`app.activeDocument.textFrames[index].textRange.kerning`

#### Description

Controls the spacing between two characters, in thousandths of an em. An integer.

#### Type

Number (long)

---

### TextRange.length

`app.activeDocument.textFrames[index].textRange.length`

#### Description

The length (in characters). Minimum: 0

#### Type

Number (long)

---

### TextRange.lines

`app.activeDocument.textFrames[index].textRange.lines`

#### Description

All the lines in this text range.

#### Type

[Lines](./Lines.md); read-only.

---

### TextRange.paragraphAttributes

`app.activeDocument.textFrames[index].textRange.paragraphAttributes`

#### Description

The paragraph properties for the text range.

#### Type

[ParagraphAttributes](./ParagraphAttributes.md); read-only.

---

### TextRange.paragraphs

`app.activeDocument.textFrames[index].textRange.paragraphs`

#### Description

All the paragraphs in this text range.

#### Type

[Paragraphs](./Paragraphs.md); read-only.

---

### TextRange.paragraphStyles

`app.activeDocument.textFrames[index].textRange.paragraphStyles`

#### Description

All referenced paragraph styles in the text range.

#### Type

[ParagraphStyles](./ParagraphStyles.md); read-only.

---

### TextRange.parent

`app.activeDocument.textFrames[index].textRange.parent`

#### Description

The object's container.

#### Type

[TextRange](#jsobjref-textrange); read-only.

---

### TextRange.start

`app.activeDocument.textFrames[index].textRange.start`

#### Description

Start index of the text range.

#### Type

Int32

---

### TextRange.story

`app.activeDocument.textFrames[index].textRange.story`

#### Description

The story to which the text range belongs.

#### Type

[Story](./Story.md); read-only.

---

### TextRange.textRanges

`app.activeDocument.textFrames[index].textRange.textRanges`

#### Description

All of the text in this text range.

#### Type

[TextRanges](./TextRanges.md); read-only.

---

### TextRange.textSelection

`app.activeDocument.textFrames[index].textRange.textSelection`

#### Description

The selected text ranges in the text range.

#### Type

Array of [TextRange](#jsobjref-textrange); read-only.

---

### TextRange.typename

`app.activeDocument.textFrames[index].textRange.typename`

#### Description

The class name of the object.

#### Type

String; read-only.

---

### TextRange.words

`app.activeDocument.textFrames[index].textRange.words`

#### Description

All the words contained in this text range.

#### Type

[Words](./Words.md); read-only.

---

## Methods

### TextRange.changeCaseTo()

`app.activeDocument.textFrames[index].textRange.changeCaseTo(type)`

#### Description

Changes the capitalization of text

#### Parameters

| Parameter |                          Type                           |           Description            |
| --------- | ------------------------------------------------------- | -------------------------------- |
| `type`    | [CaseChangeType](scripting-constants.md#casechangetype) | Capitalization case to change to |

#### Returns

Nothing

---

### TextRange.deSelect()

`app.activeDocument.textFrames[index].textRange.deSelect()`

#### Description

Deselects the text range.

#### Returns

Nothing.

---

### TextRange.duplicate()

`app.activeDocument.textFrames[index].textRange.duplicate([relativeObject][, insertionLocation])`

#### Description

Creates a duplicate of this object.

#### Parameters

|      Parameter      |                                 Type                                  |        Description         |
| ------------------- | --------------------------------------------------------------------- | -------------------------- |
| `relativeObject`    | Object, optional                                                      | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to insert element |

#### Returns

[TextRange](#jsobjref-textrange)

---

### TextRange.getLocalCharOverridesJSON()

`app.activeDocument.textFrames[index].textRange.getLocalCharOverridesJSON()`

#### Description

Gets json representation of character overrides.

#### Returns

String

---

### TextRange.getLocalParaOverridesJSON()

`app.activeDocument.textFrames[index].textRange.getLocalParaOverridesJSON()`

#### Description

Gets json representation of paragraph overrides.

#### Returns

String

---

### TextRange.getParagraphLength()

`app.activeDocument.textFrames[index].textRange.getParagraphLength()`

#### Description

Gets the length of the first paragraph of the text range.

#### Returns

Int32

---

### TextRange.getTextRunLength()

`app.activeDocument.textFrames[index].textRange.getTextRunLength()`

#### Description

Gets the length of the first text run of the text range.

#### Returns

Int32

---

### TextRange.move()

`app.activeDocument.textFrames[index].textRange.move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

|      Parameter      |                                 Type                                  |          Description          |
| ------------------- | --------------------------------------------------------------------- | ----------------------------- |
| `relativeObject`    | Object                                                                | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to move element to   |

#### Returns

[TextRange](#jsobjref-textrange)

---

### TextRange.remove()

`app.activeDocument.textFrames[index].textRange.remove()`

#### Description

Deletes the object.

#### Returns

Nothing

---

### TextRange.select()

`app.activeDocument.textFrames[index].textRange.select([addToDocument])`

#### Description

Selects the text range.

#### Parameters

|    Parameter    |       Type        |                 Description                 |
| --------------- | ----------------- | ------------------------------------------- |
| `addToDocument` | Boolean, optional | Whether to add or replace current selection |

#### Returns

Nothing

---

## Example

### Manipulating Text

```javascript
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
```
