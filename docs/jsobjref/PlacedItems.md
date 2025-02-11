<a id="jsobjref-placeditems"></a>

# PlacedItems

`app.activeDocument.placedItems`

**Description**

A collection of [PlacedItem](PlacedItem.md#jsobjref-placeditem) objects in a document.

---

## Properties

<a id="jsobjref-placeditems-length"></a>

### PlacedItems.length

`app.activeDocument.placedItems.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-placeditems-parent"></a>

### PlacedItems.parent

`app.activeDocument.placedItems.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-placeditems-typename"></a>

### PlacedItems.typename

`app.activeDocument.placedItems.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-placeditems-add"></a>

### PlacedItems.add()

`app.activeDocument.placedItems.add()`

**Description**

Creates a new object.

Use to place new art in a document. Use the `file` property of the resulting `placedItem` object to link the file containing the artwork. See [PlacedItem](PlacedItem.md#jsobjref-placeditem).

**Returns**

[PlacedItem](PlacedItem.md#jsobjref-placeditem)

---

<a id="jsobjref-placeditems-getbyname"></a>

### PlacedItems.getByName()

`app.activeDocument.placedItems.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[PlacedItem](PlacedItem.md#jsobjref-placeditem)

---

<a id="jsobjref-placeditems-index"></a>

### PlacedItems.index()

`app.activeDocument.placedItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[PlacedItem](PlacedItem.md#jsobjref-placeditem)

---

<a id="jsobjref-placeditems-removeall"></a>

### PlacedItems.removeAll()

`app.activeDocument.placedItems.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
