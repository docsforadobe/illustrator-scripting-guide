# Lines

`lines`

**Description**

A collection of `TextRange` objects representing lines of text in a text frame. The elements are not named; you must access them by index.

---

## Properties

### Lines.length

`lines.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

### Lines.parent

`lines.parent`

**Description**

The object's container.

**Type**

Object, read-only.

---

### Lines.typename

`lines.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### Lines.index()

`lines.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[TextRange](./TextRange.md)

---

### Lines.removeAll()

`lines.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
