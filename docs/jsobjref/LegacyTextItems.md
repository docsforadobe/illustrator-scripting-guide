# LegacyTextItems

`legacyTextItems`

#### Description

A collection of [LegacyTextItem](./LegacyTextItem.md) objects.

---

## Properties

### LegacyTextItems.length

`legacyTextItems.length`

#### Description

Number of elements in the collection.

#### Type

Number, read-only.

---

### LegacyTextItems.parent

`legacyTextItems.parent`

#### Description

The object's container.

#### Type

Object, read-only.

---

### LegacyTextItems.typename

`legacyTextItems.typename`

#### Description

The class name of the object.

#### Type

String, read-only.

---

## Methods

### LegacyTextItems.convertToNative()

`legacyTextItems.convertToNative()`

#### Description

Creates text frames from all legacy text items; the original legacy text items are deleted. Returns `true` on success.

#### Returns

Boolean.

---

### LegacyTextItems.getByName()

`legacyTextItems.getByName(name)`

#### Description

Get the first element in the collection with the specified name.

#### Parameters

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

#### Returns

[LegacyTextItem](./LegacyTextItem.md)

---

### LegacyTextItems.index()

`legacyTextItems.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

#### Returns

[LegacyTextItem](./LegacyTextItem.md)

---

### LegacyTextItems.removeAll()

`legacyTextItems.removeAll()`

#### Description

Deletes all elements in this collection.

#### Returns

Nothing.
