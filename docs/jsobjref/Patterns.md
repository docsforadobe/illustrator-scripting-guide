# Patterns

`app.activeDocument.patterns`

**Description**

A collection of [Pattern](./Pattern.md) objects in a document.

---

## Properties

### Patterns.length

`app.activeDocument.patterns.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

### Patterns.parent

`app.activeDocument.patterns.parent`

**Description**

The object's container.

**Type**

Object, read-only.

---

### Patterns.typename

`app.activeDocument.patterns.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### Patterns.add()

`app.activeDocument.patterns.add()`

**Description**

Creates a new object.

**Returns**

[Pattern](./Pattern.md)

---

### Patterns.getByName()

`app.activeDocument.patterns.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Pattern](./Pattern.md)

---

### Patterns.index()

`app.activeDocument.patterns.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Pattern](./Pattern.md)

---

### Patterns.removeAll()

`app.activeDocument.patterns.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Removing a pattern

```default
// Deletes the last pattern from the current document.
if (app.documents.length > 0) {
    var lastIndex = app.activeDocument.patterns.length - 1;

    var patternToRemove = app.activeDocument.patterns[lastIndex];
    var patternName = patternToRemove.name;
    patternToRemove.remove();

    // Note after removing Illustrator objects, set the variable that
    // referenced the removed object to null, since it is now invalid.
    patternToRemove = null;
}
```
