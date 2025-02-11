<a id="jsobjref-brushes"></a>

# Brushes

`app.activeDocument.brushes`

**Description**

A collection of brush objects in a document.

---

## Properties

<a id="jsobjref-brushes-length"></a>

### Brushes.length

`app.activeDocument.brushes.length`

**Description**

The number of objects in the collection

**Type**

Number; read-only.

---

<a id="jsobjref-brushes-parent"></a>

### Brushes.parent

`app.activeDocument.brushes.parent`

**Description**

The document that contains this brushes collection.

**Type**

Object; read-only.

---

<a id="jsobjref-brushes-typename"></a>

### Brushes.typename

`app.activeDocument.brushes.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

<a id="jsobjref-brushes-getbyname"></a>

### Brushes.getByName()

`app.activeDocument.brushes.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Brush](Brush.md#jsobjref-brush)

---

<a id="jsobjref-brushes-index"></a>

### Brushes.index()

`app.activeDocument.brushes.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Brush](Brush.md#jsobjref-brush)

---

## Example

### Counting brushes

```default
// Counts all brushes in the active document

if (app.documents.length > 0) {
  var numberOfBrushes = app.activeDocument.brushes.length;
}
```
