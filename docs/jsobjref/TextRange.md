<a id="jsobjref-textrange"></a>

# TextRange

`app.activeDocument.textFrames[index].textRange`

**Description**

A range of text in a specific text art item. TextRange gives you access to the text contained in text art items.

---

## Properties

<a id="jsobjref-textrange-characterattributes"></a>

### TextRange.characterAttributes

`app.activeDocument.textFrames[index].textRange.characterAttributes`

**Description**

The character properties for the text range.

**Type**

[CharacterAttributes](CharacterAttributes.md#jsobjref-characterattributes), read-only.

---

<a id="jsobjref-textrange-characteroffset"></a>

### TextRange.characterOffset

`app.activeDocument.textFrames[index].textRange.characterOffset`

**Description**

Offset of the first character.

**Type**

Number (long)

---

<a id="jsobjref-textrange-characters"></a>

### TextRange.characters

`app.activeDocument.textFrames[index].textRange.characters`

**Description**

All the characters in this text range.

**Type**

[Characters](Characters.md#jsobjref-characters), read-only.

---

<a id="jsobjref-textrange-characterstyles"></a>

### TextRange.characterStyles

`app.activeDocument.textFrames[index].textRange.characterStyles`

**Description**

All referenced character styles in the text range.

**Type**

[CharacterStyles](CharacterStyles.md#jsobjref-characterstyles), read-only.

---

<a id="jsobjref-textrange-contents"></a>

### TextRange.contents

`app.activeDocument.textFrames[index].textRange.contents`

**Description**

The text string.

**Type**

String

---

<a id="jsobjref-textrange-end"></a>

### TextRange.end

`app.activeDocument.textFrames[index].textRange.end`

**Description**

End index of the text range.

**Type**

Int32

---

<a id="jsobjref-textrange-insertionpoints"></a>

### TextRange.insertionPoints

`app.activeDocument.textFrames[index].textRange.insertionPoints`

**Description**

All the insertion points in this text range.

**Type**

[InsertionPoints](InsertionPoints.md#jsobjref-insertionpoints), read-only.

---

<a id="jsobjref-textrange-kerning"></a>

### TextRange.kerning

`app.activeDocument.textFrames[index].textRange.kerning`

**Description**

Controls the spacing between two characters, in thousandths of an em. An integer.

**Type**

Number (long)

---

<a id="jsobjref-textrange-length"></a>

### TextRange.length

`app.activeDocument.textFrames[index].textRange.length`

**Description**

The length (in characters). Minimum: 0

**Type**

Number (long)

---

<a id="jsobjref-textrange-lines"></a>

### TextRange.lines

`app.activeDocument.textFrames[index].textRange.lines`

**Description**

All the lines in this text range.

**Type**

[Lines](Lines.md#jsobjref-lines), read-only.

---

<a id="jsobjref-textrange-paragraphattributes"></a>

### TextRange.paragraphAttributes

`app.activeDocument.textFrames[index].textRange.paragraphAttributes`

**Description**

The paragraph properties for the text range.

**Type**

[ParagraphAttributes](ParagraphAttributes.md#jsobjref-paragraphattributes), read-only.

---

<a id="jsobjref-textrange-paragraphs"></a>

### TextRange.paragraphs

`app.activeDocument.textFrames[index].textRange.paragraphs`

**Description**

All the paragraphs in this text range.

**Type**

[Paragraphs](Paragraphs.md#jsobjref-paragraphs), read-only.

---

<a id="jsobjref-textrange-paragraphstyles"></a>

### TextRange.paragraphStyles

`app.activeDocument.textFrames[index].textRange.paragraphStyles`

**Description**

All referenced paragraph styles in the text range.

**Type**

[ParagraphStyles](ParagraphStyles.md#jsobjref-paragraphstyles), read-only.

---

<a id="jsobjref-textrange-parent"></a>

### TextRange.parent

`app.activeDocument.textFrames[index].textRange.parent`

**Description**

The object’s container.

**Type**

[TextRange](#jsobjref-textrange), read-only.

---

<a id="jsobjref-textrange-start"></a>

### TextRange.start

`app.activeDocument.textFrames[index].textRange.start`

**Description**

Start index of the text range.

**Type**

Int32

---

<a id="jsobjref-textrange-story"></a>

### TextRange.story

`app.activeDocument.textFrames[index].textRange.story`

**Description**

The story to which the text range belongs.

**Type**

[Story](Story.md#jsobjref-story), read-only.

---

<a id="jsobjref-textrange-textranges"></a>

### TextRange.textRanges

`app.activeDocument.textFrames[index].textRange.textRanges`

**Description**

All of the text in this text range.

**Type**

[TextRanges](TextRanges.md#jsobjref-textranges), read-only.

---

<a id="jsobjref-textrange-textselection"></a>

### TextRange.textSelection

`app.activeDocument.textFrames[index].textRange.textSelection`

**Description**

The selected text ranges in the text range.

**Type**

Array of [TextRange](#jsobjref-textrange), read-only.

---

<a id="jsobjref-textrange-typename"></a>

### TextRange.typename

`app.activeDocument.textFrames[index].textRange.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

<a id="jsobjref-textrange-words"></a>

### TextRange.words

`app.activeDocument.textFrames[index].textRange.words`

**Description**

All the words contained in this text range.

**Type**

[Words](Words.md#jsobjref-words), read-only.

---

## Methods

<a id="jsobjref-textrange-changecaseto"></a>

### TextRange.changeCaseTo()

`app.activeDocument.textFrames[index].textRange.changeCaseTo(type)`

**Description**

Changes the capitalization of text

**Parameters**

| Parameter   | Type                                                                                 | Description                      |
|-------------|--------------------------------------------------------------------------------------|----------------------------------|
| `type`      | [CaseChangeType](scripting-constants.md#jsobjref-scripting-constants-casechangetype) | Capitalization case to change to |

**Returns**

Nothing

---

<a id="jsobjref-textrange-deselect"></a>

### TextRange.deSelect()

`app.activeDocument.textFrames[index].textRange.deSelect()`

**Description**

Deselects the text range.

**Returns**

Nothing.

---

<a id="jsobjref-textrange-duplicate"></a>

### TextRange.duplicate()

`app.activeDocument.textFrames[index].textRange.duplicate([relativeObject][, insertionLocation])`

**Description**

Creates a duplicate of this object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[TextRange](#jsobjref-textrange)

---

<a id="jsobjref-textrange-getlocalcharoverridesjson"></a>

### TextRange.getLocalCharOverridesJSON()

`app.activeDocument.textFrames[index].textRange.getLocalCharOverridesJSON()`

**Description**

Gets json representation of character overrides.

**Returns**

String

---

<a id="jsobjref-textrange-getlocalparaoverridesjson"></a>

### TextRange.getLocalParaOverridesJSON()

`app.activeDocument.textFrames[index].textRange.getLocalParaOverridesJSON()`

**Description**

Gets json representation of paragraph overrides.

**Returns**

String

---

<a id="jsobjref-textrange-getparagraphlength"></a>

### TextRange.getParagraphLength()

`app.activeDocument.textFrames[index].textRange.getParagraphLength()`

**Description**

Gets the length of the first paragraph of the text range.

**Returns**

Int32

---

<a id="jsobjref-textrange-gettextrunlength"></a>

### TextRange.getTextRunLength()

`app.activeDocument.textFrames[index].textRange.getTextRunLength()`

**Description**

Gets the length of the first text run of the text range.

**Returns**

Int32

---

<a id="jsobjref-textrange-move"></a>

### TextRange.move()

`app.activeDocument.textFrames[index].textRange.move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[TextRange](#jsobjref-textrange)

---

<a id="jsobjref-textrange-remove"></a>

### TextRange.remove()

`app.activeDocument.textFrames[index].textRange.remove()`

**Description**

Deletes the object.

**Returns**

Nothing

---

<a id="jsobjref-textrange-select"></a>

### TextRange.select()

`app.activeDocument.textFrames[index].textRange.select([addToDocument])`

**Description**

Selects the text range.

**Parameters**

| Parameter       | Type              | Description                                 |
|-----------------|-------------------|---------------------------------------------|
| `addToDocument` | Boolean, optional | Whether to add or replace current selection |

**Returns**

Nothing

---

## Example

### Manipulating Text

```default
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
