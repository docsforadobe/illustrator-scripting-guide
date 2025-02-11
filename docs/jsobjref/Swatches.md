<a id="jsobjref-swatches"></a>

# Swatches

`app.activeDocument.swatches`

**Description**

The collection of [Swatch](Swatch.md#jsobjref-swatch) objects in the document.

---

## Properties

<a id="jsobjref-swatches-length"></a>

### Swatches.length

`app.activeDocument.swatches.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-swatches-parent"></a>

### Swatches.parent

`app.activeDocument.swatches.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-swatches-typename"></a>

### Swatches.typename

`app.activeDocument.swatches.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-swatches-add"></a>

### Swatches.add()

`app.activeDocument.swatches.add()`

**Description**

Creates a new [Swatch](Swatch.md#jsobjref-swatch) object.

**Returns**

[Swatch](Swatch.md#jsobjref-swatch)

---

<a id="jsobjref-swatches-getbyname"></a>

### Swatches.getByName()

`app.activeDocument.swatches.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Swatch](Swatch.md#jsobjref-swatch)

---

<a id="jsobjref-swatches-getselected"></a>

### Swatches.getSelected()

`app.activeDocument.swatches.getSelected()`

**Description**

Gets selected swatches in the document.

**Returns**

List of [Swatch](Swatch.md#jsobjref-swatch)

---

<a id="jsobjref-swatches-index"></a>

### Swatches.index()

`app.activeDocument.swatches.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description           |
|-------------|----------------|-----------------------|
| `itemKey`   | String, Number | Key of element to get |

**Returns**

[Swatch](Swatch.md#jsobjref-swatch)

---

<a id="jsobjref-swatches-removeall"></a>

### Swatches.removeAll()

`app.activeDocument.swatches.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Finding and deleting a swatch

```default
// Deletes swatch 4 from the current document
if ( app.documents.length > 0 ) {
  if (app.activeDocument.swatches.length > 4) {
    var swatchToDelete = app.activeDocument.swatches[3];
    swatchToDelete.remove();
  }
}
```
