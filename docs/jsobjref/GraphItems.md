# GraphItems

`app.activeDocument.graphItems`

**Description**

A collection `GraphItems` objects, which gives you access to all the graph art items in an Illustrator document.

---

## Properties

### GraphItems.length

`app.activeDocument.graphItems.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

### GraphItems.parent

`app.activeDocument.graphItems.parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

### GraphItems.typename

`app.activeDocument.graphItems.typename`

**Description**

> The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### GraphItems.getByName()

`app.activeDocument.graphItems.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[GraphItems](#jsobjref-graphitems)

---

### GraphItems.index()

`app.activeDocument.graphItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[GraphItems](#jsobjref-graphitems)

---

### GraphItems.removeAll()

`app.activeDocument.graphItems.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Rotating graph items

```default
// Rotates each graph item in the current document 90 degrees.

// Verify a document with a graph item is open
var ok = false;

if (documents.length > 0) {
  var docRef = activeDocument;
  var iCount = docRef.graphItems.length;
  if (iCount > 0) {
    ok = true;
    for (var i = 0; i < iCount; i++) {
      var graphRef = docRef.graphItems[i];
      graphRef.selected = true;
      graphRef.rotate(90); //rotate clockwise 90 degrees
    }
    redraw();
  }
}
```
