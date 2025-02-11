<a id="jsobjref-patterns"></a>

# Patterns

`app.activeDocument.patterns`

**Description**

A collection of [Pattern](Pattern.md#jsobjref-pattern) objects in a document.

---

## Properties

<a id="jsobjref-patterns-length"></a>

### Patterns.length

`app.activeDocument.patterns.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-patterns-parent"></a>

### Patterns.parent

`app.activeDocument.patterns.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-patterns-typename"></a>

### Patterns.typename

`app.activeDocument.patterns.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-patterns-add"></a>

### Patterns.add()

`app.activeDocument.patterns.add()`

**Description**

Creates a new object.

**Returns**

[Pattern](Pattern.md#jsobjref-pattern)

---

<a id="jsobjref-patterns-getbyname"></a>

### Patterns.getByName()

`app.activeDocument.patterns.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Pattern](Pattern.md#jsobjref-pattern)

---

<a id="jsobjref-patterns-index"></a>

### Patterns.index()

`app.activeDocument.patterns.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Pattern](Pattern.md#jsobjref-pattern)

---

<a id="jsobjref-patterns-removeall"></a>

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
