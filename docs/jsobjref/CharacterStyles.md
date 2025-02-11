# CharacterStyles

`app.activeDocument.characterStyles`

**Description**

A collection of CharacterStyle objects.

---

## Properties

### CharacterStyles.length

`app.activeDocument.characterStyles.length`

**Description**

The number of characters in the collection.

**Type**

Number; read-only.

---

### CharacterStyles.parent

`app.activeDocument.characterStyles.parent`

**Description**

The object's container.

**Type**

Object; read-only.

---

### CharacterStyles.typename

`app.activeDocument.characterStyles.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

## Methods

### CharacterStyles.add()

`add(name)`

**Description**

Creates a named character style.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Element name to create |

**Returns**

[CharacterStyle](CharacterStyle.md#jsobjref-characterstyle)

---

### CharacterStyles.getByName()

`getByName(name)`

**Description**

Gets the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[CharacterStyle](CharacterStyle.md#jsobjref-characterstyle)

---

### CharacterStyles.index()

`index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[CharacterStyle](CharacterStyle.md#jsobjref-characterstyle)

---

### CharacterStyles.removeAll()

`removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Using characters styles

```default
// Creates 3 text frames in a new document then creates
// a character style and applies it to each text frame.

var docRef = documents.add();
var textRef1 = docRef.textFrames.add();
textRef1.contents = "Scripting is fun!";
textRef1.top = 700;
textRef1.left = 50;

var textRef2 = docRef.textFrames.add();
textRef2.contents = "Scripting is easy!";
textRef2.top = 625;
textRef2.left = 100;

var textRef3 = docRef.textFrames.add();
textRef3.contents = "Everyone should script!";
textRef3.top = 550;
textRef3.left = 150;
redraw();

// Create a new character style
var charStyle = docRef.characterStyles.add("BigRed");

// set character attributes
var charAttr = charStyle.characterAttributes;
charAttr.size = 40;
charAttr.tracking = -50;
charAttr.capitalization = FontCapsOption.ALLCAPS;

var redColor = new RGBColor();
redColor.red = 255;
redColor.green = 0;
redColor.blue = 0;
charAttr.fillColor = redColor;

// apply to each textFrame in the document
charStyle.applyTo(textRef1.textRange);
charStyle.applyTo(textRef2.textRange);
charStyle.applyTo(textRef3.textRange);
```
