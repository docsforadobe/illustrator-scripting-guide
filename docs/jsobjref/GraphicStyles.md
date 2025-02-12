# GraphicStyles

`app.activeDocument.graphicStyles`

**Description**

A collection of GraphicStyle objects in a document.

---

## Properties

### GraphicStyles.length

`app.activeDocument.graphicStyles.length`

**Description**

The number of graphic styles in the document.

**Type**

Number, read-only.

---

### GraphicStyles.parent

`app.activeDocument.graphicStyles.parent`

**Description**

The document that contains this graphic styles collection.

**Type**

Object, read-only.

---

### GraphicStyles.typename

`app.activeDocument.graphicStyles.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### GraphicStyles.getByName()

`app.activeDocument.graphicStyles.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

String.

---

### GraphicStyles.index()

`app.activeDocument.graphicStyles.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

String, Number.

---

### GraphicStyles.removeAll()

`app.activeDocument.graphicStyles.removeAll()`

**Description**

Removes all elements in the referenced collection.

**Returns**

Nothing.

---

## Example

### Counting graphics styles

```javascript
// Counts the number of graphic styles in the active document
// and stores result in numberOfStyles

if (app.documents.length > 0) {
    var numberOfStyles = app.activeDocument.graphicStyles.length;
}
```
