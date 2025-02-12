# InsertionPoints

`app.activeDocument.textFrames[index].insertionPoints`

#### Description

A collection of `InsertionPoint` objects.

---

## Properties

### InsertionPoints.length

`app.activeDocument.textFrames[index].insertionPoints.length`

#### Description

Number of elements in the collection.

#### Type

Number, read-only.

---

### InsertionPoints.parent

`app.activeDocument.textFrames[index].insertionPoints.parent`

#### Description

The object's container.

#### Type

Object, read-only.

---

### InsertionPoints.typename

`app.activeDocument.textFrames[index].insertionPoints.typename`

#### Description

The class name of the object.

#### Type

String, read-only.

---

## Methods

### InsertionPoints.index()

`app.activeDocument.textFrames[index].insertionPoints.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

#### Returns

[InsertionPoint](./InsertionPoint.md)

---

## Example

### Using insertion points to add spaces

```javascript
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
