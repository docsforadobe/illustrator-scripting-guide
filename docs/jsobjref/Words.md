<a id="jsobjref-words"></a>

# Words

`app.activeDocument.textFrames[index].words`

**Description**

A collection of words in a text item, where each word is a [TextRange](TextRange.md#jsobjref-textrange) object.

The elements are not named; you must access them by index.

---

## Properties

<a id="jsobjref-words-length"></a>

### Words.length

`app.activeDocument.textFrames[index].words.length`

**Description**

The number of objects in the collection

**Type**

Number; read-only.

---

<a id="jsobjref-words-parent"></a>

### Words.parent

`app.activeDocument.textFrames[index].words.parent`

**Description**

The parent of this object.

**Type**

Object; read-only.

---

<a id="jsobjref-words-typename"></a>

### Words.typename

`app.activeDocument.textFrames[index].words.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

<a id="jsobjref-words-add"></a>

### Words.add()

`app.activeDocument.textFrames[index].words.add(contents[, relativeObject][, inseertLocation])`

**Description**

Adds a word to the current document at the specified location.

If no location is specified, adds it to the containing text frame after the current word selection or insertion point.

**Parameters**

| Parameter           | Type                                                                                               | Description             |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------|
| `contents`          | String                                                                                             | Word to add             |
| `relativeObject`    | [TextFrameItem](TextFrameItem.md#jsobjref-textframeitem), optional                                 | Object to add item to   |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert text |

**Returns**

[TextRange](TextRange.md#jsobjref-textrange)

---

<a id="jsobjref-words-addbefore"></a>

### Words.addBefore()

`app.activeDocument.textFrames[index].words.addBefore(contents)`

**Description**

Adds a word before the current word selection or insertion point.

**Parameters**

| Parameter   | Type   | Description   |
|-------------|--------|---------------|
| `contents`  | String | Word to add   |

**Returns**

[TextRange](TextRange.md#jsobjref-textrange)

---

<a id="jsobjref-words-index"></a>

### Words.index()

`app.activeDocument.textFrames[index].words.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[TextRange](TextRange.md#jsobjref-textrange)

---

<a id="jsobjref-words-removeall"></a>

### Words.removeAll()

`app.activeDocument.textFrames[index].words.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Counting words

```default
// Counts all words in current document and stores total in numWords
if ( app.documents.length > 0 ) {
  var numWords = 0;

  for ( i = 0; i < app.activeDocument.textFrames.length; i++) {
    numWords += app.activeDocument.textFrames[i].words.length;
  }
}
```

### Applying attributes to words

```default
// Creates a new magenta color and applies the color to all words meeting a specific criteria
if (app.documents.length > 0 && app.activeDocument.textFrames.length > 0) {
  // Create the color to apply to the words
  var wordColor = new RGBColor();
  wordColor.red = 255;
  wordColor.green = 0;
  wordColor.blue = 255;

  // Set the value of the word to look for searchWord1 = "the";
  var searchWord2 = "The";
  var searchWord3 = "THE";

  // Iterate through all words in the document
  // and color the words that match searchWord

  for (var i = 0; i < app.activeDocument.textFrames.length; i++) {
    var textArt = activeDocument.textFrames[i];

    for (var j = 0; j < textArt.words.length; j++) {
      var word = textArt.words[j];

      if (word.contents == searchWord1 || word.contents == searchWord2 || word.contents == searchWord3) {
        word.filled = true;
        word.fillColor = wordColor;
      }
    }
  }
}
```
