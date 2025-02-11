# TextFonts

`app.textFonts`

**Description**

A collection of [TextFont](./TextFont.md) objects.

---

## Properties

### TextFonts.length

`app.textFonts.length`

**Description**

The number of elements in the collection.

**Type**

Number; read-only.

---

### TextFonts.parent

`app.textFonts.parent`

**Description**

The object's container.

**Type**

Object; read-only.

---

### TextFonts.typename

`app.textFonts.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

### TextFonts.getByName()

`app.textFonts.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[TextFont](./TextFont.md)

---

### TextFonts.index()

`app.textFonts.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[TextFont](./TextFont.md)

---

## Example

### Finding fonts

```default
 // Creates a new A3 sized document and display a list of available fonts until the document is full.

 var edgeSpacing = 10;
 var columnSpacing = 230;
 var docPreset = new DocumentPreset;
 docPreset.width = 1191.0;
 docPreset.height = 842.0

 var docRef = documents.addDocument(DocumentColorSpace.CMYK, docPreset);
 var sFontNames = "";
 var x = edgeSpacing;
 var y = (docRef.height - edgeSpacing);

 var iCount = textFonts.length;

 for (var i=0; i<iCount; i++) {
  sFontName = textFonts[i].name;
  sFontName += " ";
  sFontNames = sFontName + textFonts[i].style;

  var textRef = docRef.textFrames.add();
  textRef.textRange.characterAttributes.size = 10;
  textRef.contents = sFontNames;
  textRef.top = y;
  textRef.left = x;

  // check wether the text frame will go off the edge of the document
  if ((x + textRef.width)> docRef.width) {
    textRef.remove();
    iCount = i;
    break;
  } else {
    // display text frame
    textRef.textRange.characterAttributes.textFont = textFonts.getByName(textFonts[i].name);
    redraw();

    if ((y-=(textRef.height)) <= 20) {
      y = (docRef.height - edgeSpacing);
      x += columnSpacing;
    }
  }
}
```
