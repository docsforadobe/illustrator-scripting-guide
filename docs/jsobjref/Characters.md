# Characters

`app.activeDocument.textFrames[index].contents`

**Description**

A collection of characters (`TextRange` objects of length 1).

The elements are not named; you must access them by index.

---

## Properties

### Characters.length

`app.activeDocument.textFrames[index].contents.length`

**Description**

The number of characters in the collection.

**Type**

Number; read-only.

---

### Characters.parent

`app.activeDocument.textFrames[index].contents.parent`

**Description**

The text art item that contains this character.

**Type**

Object; read-only.

---

### Characters.typename

`app.activeDocument.textFrames[index].contents.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

### Characters.add()

`app.activeDocument.textFrames[index].contents.add(contents[,relativeObject][,insertionLocation])`

**Description**

Adds a new character with specified text contents at the specified location in the current document.

If a location is not specified, adds the new character to the containing text frame after the current text selection or insertion point.

**Parameters**

| Parameter           | Type                                                                                               | Description            |
|---------------------|----------------------------------------------------------------------------------------------------|------------------------|
| `contents`          | String                                                                                             | Text contents to add   |
| `relativeObject`    | [TextFrameItem](./TextFrameItem.md), optional                                 | Object to add item to  |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to place text |

**Returns**

[TextRange](./TextRange.md)

---

### Characters.addBefore()

`app.activeDocument.textFrames[index].contents.addBefore(contents)`

**Description**

Adds a character before the specified text selection.

**Parameters**

| Parameter   | Type   | Description          |
|-------------|--------|----------------------|
| `contents`  | String | Text contents to add |

**Returns**

[TextRange](./TextRange.md)

---

### Characters.index()

`app.activeDocument.textFrames[index].contents.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[TextRange](./TextRange.md)

---

### Characters.removeAll()

`app.activeDocument.textFrames[index].contents.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Counting characters

```javascript
// Counts all characters in the active document,
// including whitespace, and stores in numChars

if (app.documents.length > 0) {
    var doc = app.activeDocument;
    var numChars = 0;
    for (var i = 0; i < doc.textFrames.length; i++) {
        var textArtRange = doc.textFrames[i].contents;
        numChars += textArtRange.length;
    }
}
```
