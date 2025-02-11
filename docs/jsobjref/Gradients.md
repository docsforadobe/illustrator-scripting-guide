<a id="jsobjref-gradients"></a>

# Gradients

`app.activeDocument.gradients`

**Description**

A collection of [Gradient](Gradient.md#jsobjref-gradient) objects in a document.

---

## Properties

<a id="jsobjref-gradients-length"></a>

### Gradients.length

`app.activeDocument.gradients.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-gradients-parent"></a>

### Gradients.parent

`app.activeDocument.gradients.parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

<a id="jsobjref-gradients-typename"></a>

### Gradients.typename

`app.activeDocument.gradients.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-gradients-add"></a>

### Gradients.add()

`app.activeDocument.gradients.add()`

**Description**

Creates a new `Gradient` object.

**Returns**

[Gradient](Gradient.md#jsobjref-gradient)

---

<a id="jsobjref-gradients-getbyname"></a>

### Gradients.getByName()

`app.activeDocument.gradients.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Gradient](Gradient.md#jsobjref-gradient)

---

<a id="jsobjref-gradients-index"></a>

### Gradients.index()

`app.activeDocument.gradients.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Gradient](Gradient.md#jsobjref-gradient)

---

<a id="jsobjref-gradients-removeall"></a>

### Gradients.removeAll()

`app.activeDocument.gradients.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Removing a gradient

```default
// Deletes the first gradient from the current document
if (app.documents.length > 0) {
  app.activeDocument.gradients[0].remove();
}
```
