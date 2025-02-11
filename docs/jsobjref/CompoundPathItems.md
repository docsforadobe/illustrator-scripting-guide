<a id="jsobjref-compoundpathitems"></a>

# CompoundPathItems

`app.activeDocument.activeLayer.compoundPathItems`

**Description**

A collection of [CompoundPathItem](CompoundPathItem.md#jsobjref-compoundpathitem) objects.

---

## Properties

<a id="jsobjref-compoundpathitems-length"></a>

### CompoundPathItems.length

`app.activeDocument.activeLayer.compoundPathItems.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-compoundpathitems-parent"></a>

### CompoundPathItems.parent

`app.activeDocument.activeLayer.compoundPathItems.parent`

**Description**

The parent of this collection (either a `Layer` or a `GroupItem`).

**Type**

Object, read-only.

---

<a id="jsobjref-compoundpathitems-typename"></a>

### CompoundPathItems.typename

`app.activeDocument.activeLayer.compoundPathItems.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-compoundpathitems-add"></a>

### CompoundPathItems.add()

`app.activeDocument.activeLayer.compoundPathItems.add()`

**Description**

Creates a new `CompoundPathItem`.

**Returns**

[CompoundPathItem](CompoundPathItem.md#jsobjref-compoundpathitem)

---

<a id="jsobjref-compoundpathitems-getbyname"></a>

### CompoundPathItems.getByName()

`app.activeDocument.activeLayer.compoundPathItems.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[CompoundPathItem](CompoundPathItem.md#jsobjref-compoundpathitem)

---

<a id="jsobjref-compoundpathitems-index"></a>

### CompoundPathItems.index()

`app.activeDocument.activeLayer.compoundPathItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[CompoundPathItem](CompoundPathItem.md#jsobjref-compoundpathitem)

---

<a id="jsobjref-compoundpathitems-removeall"></a>

### CompoundPathItems.removeAll()

`app.activeDocument.activeLayer.compoundPathItems.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Counting compound paths

```default
// Counts all compound path items in layer 1 of the current document
if (app.documents.length > 0) {
  var doc = app.activeDocument;
  var numCompoundPaths = doc.layers[0].compoundPathItems.length;
}
```
