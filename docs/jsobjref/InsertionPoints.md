<a id="jsobjref-insertionpoints"></a>

# InsertionPoints

`app.activeDocument.textFrames[index].insertionPoints`

**Description**

A collection of `InsertionPoint` objects.

---

## Properties

<a id="jsobjref-insertionpoints-length"></a>

### InsertionPoints.length

`app.activeDocument.textFrames[index].insertionPoints.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-insertionpoints-parent"></a>

### InsertionPoints.parent

`app.activeDocument.textFrames[index].insertionPoints.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-insertionpoints-typename"></a>

### InsertionPoints.typename

`app.activeDocument.textFrames[index].insertionPoints.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-insertionpoints-index"></a>

### InsertionPoints.index()

`app.activeDocument.textFrames[index].insertionPoints.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[InsertionPoint](InsertionPoint.md#jsobjref-insertionpoint)

---

## Example

### Using insertion points to add spaces

```default
// Creates a new document, adds text then inserts a
// space between each character using insertion points

var docRef = documents.add();
var textRef = docRef.textFrames.add();
textRef.contents = "Wouldn't you rather be scripting?";
textRef.top = 400;
textRef.left = 100;
textRef.textRange.characterAttributes.size = 20;

redraw();

// Add a space between each character using insertion points.
var ip;
for (var i = 0; i < textRef.insertionPoints.length; i += 2) {
  ip = textRef.insertionPoints[i];
  ip.characters.add(" ");
}
```
