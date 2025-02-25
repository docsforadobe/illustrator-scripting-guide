# CompoundPathItems

`app.activeDocument.activeLayer.compoundPathItems`

#### Description

A collection of [CompoundPathItem](./CompoundPathItem.md) objects.

---

## Properties

### CompoundPathItems.length

`app.activeDocument.activeLayer.compoundPathItems.length`

#### Description

The number of objects in the collection.

#### Type

Number; read-only.

---

### CompoundPathItems.parent

`app.activeDocument.activeLayer.compoundPathItems.parent`

#### Description

The parent of this collection (either a `Layer` or a `GroupItem`).

#### Type

Object; read-only.

---

### CompoundPathItems.typename

`app.activeDocument.activeLayer.compoundPathItems.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

## Methods

### CompoundPathItems.add()

`app.activeDocument.activeLayer.compoundPathItems.add()`

#### Description

Creates a new `CompoundPathItem`.

#### Returns

[CompoundPathItem](./CompoundPathItem.md)

---

### CompoundPathItems.getByName()

`app.activeDocument.activeLayer.compoundPathItems.getByName(name)`

#### Description

Gets the first element in the collection with the specified name.

#### Parameters

| Parameter |  Type  |      Description       |
| --------- | ------ | ---------------------- |
| `name`    | String | Name of element to get |

#### Returns

[CompoundPathItem](./CompoundPathItem.md)

---

### CompoundPathItems.index()

`app.activeDocument.activeLayer.compoundPathItems.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter |      Type      |     Description      |
| --------- | -------------- | -------------------- |
| `itemKey` | String, Number | String or number key |

#### Returns

[CompoundPathItem](./CompoundPathItem.md)

---

### CompoundPathItems.removeAll()

`app.activeDocument.activeLayer.compoundPathItems.removeAll()`

#### Description

Deletes all elements in this collection.

#### Returns

Nothing.

---

## Example

### Counting compound paths

```javascript
// Counts all compound path items in layer 1 of the current document
if (app.documents.length > 0) {
    var doc = app.activeDocument;
    var numCompoundPaths = doc.layers[0].compoundPathItems.length;
}
```
