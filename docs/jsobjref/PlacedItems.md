# PlacedItems

`app.activeDocument.placedItems`

#### Description

A collection of [PlacedItem](./PlacedItem.md) objects in a document.

---

## Properties

### PlacedItems.length

`app.activeDocument.placedItems.length`

#### Description

Number of elements in the collection.

#### Type

Number; read-only.

---

### PlacedItems.parent

`app.activeDocument.placedItems.parent`

#### Description

The object's container.

#### Type

Object; read-only.

---

### PlacedItems.typename

`app.activeDocument.placedItems.typename`

#### Description

The class name of the object.

#### Type

String; read-only.

---

## Methods

### PlacedItems.add()

`app.activeDocument.placedItems.add()`

#### Description

Creates a new object.

Use to place new art in a document. Use the `file` property of the resulting `placedItem` object to link the file containing the artwork. See [PlacedItem](./PlacedItem.md).

#### Returns

[PlacedItem](./PlacedItem.md)

---

### PlacedItems.getByName()

`app.activeDocument.placedItems.getByName(name)`

#### Description

Get the first element in the collection with the provided name.

#### Parameters

| Parameter |  Type  |      Description       |
| --------- | ------ | ---------------------- |
| `name`    | String | Name of element to get |

#### Returns

[PlacedItem](./PlacedItem.md)

---

### PlacedItems.index()

`app.activeDocument.placedItems.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter |      Type      |     Description      |
| --------- | -------------- | -------------------- |
| `itemKey` | String, Number | String or number key |

#### Returns

[PlacedItem](./PlacedItem.md)

---

### PlacedItems.removeAll()

`app.activeDocument.placedItems.removeAll()`

#### Description

Deletes all elements in the collection.

#### Returns

Nothing.
