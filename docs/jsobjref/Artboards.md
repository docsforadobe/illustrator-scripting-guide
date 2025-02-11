<a id="jsobjref-artboards"></a>

# Artboards

`artboards`

**Description**

A collection of Artboard objects.

## Properties

<a id="jsobjref-artboards-length"></a>

### Artboards.length

`artboards.length`

**Description**

The number of datasets in the collection

**Type**

Number; read-only.

---

<a id="jsobjref-artboards-parent"></a>

### Artboards.parent

`artboards.parent`

**Description**

The name of the object that contains this dataset

**Type**

[Artboard](Artboard.md#jsobjref-artboard); read-only.

---

<a id="jsobjref-artboards-typename"></a>

### Artboards.typename

`artboards.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

<a id="jsobjref-artboards-add"></a>

### Artboards.add()

`artboards.add(artboardRect)`

**Description**

Creates a new Artboard object.

**Parameters**

| Parameter      | Type   | Description         |
|----------------|--------|---------------------|
| `artboardRect` | Rect   | Artboard dimensions |

**Returns**

[Artboard](Artboard.md#jsobjref-artboard)

---

<a id="jsobjref-artboards-getactiveartboardindex"></a>

### Artboards.getActiveArtboardIndex()

`artboards.getActiveArtboardIndex()`

**Description**

Retrieves the index position of the active artboard in the document’s list.

Returns the 0-based index.

**Returns**

Number (long)

---

<a id="jsobjref-artboards-getbyname"></a>

### Artboards.getByName()

`artboards.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Artboard](Artboard.md#jsobjref-artboard)

---

<a id="jsobjref-artboards-insert"></a>

### Artboards.insert()

`artboards.insert(artboardRect, index)`

**Description**

Creates a new Artboard object and inserts it at the given index in the list.

**Parameters**

| Parameter      | Type          | Description                 |
|----------------|---------------|-----------------------------|
| `artboardRect` | Rect          | Artboard dimensions         |
| `index`        | Number (long) | Index to insert artboard at |

**Returns**

Nothing.

---

<a id="jsobjref-artboards-remove"></a>

### Artboards.remove()

`artboards.remove(index)`

**Description**

Deletes an artboard object. You cannot remove the last artboard in a document.

**Parameters**

| Parameter   | Type          | Description                 |
|-------------|---------------|-----------------------------|
| `index`     | Number (long) | Index of artboard to remove |

**Returns**

Nothing.

---

<a id="jsobjref-artboards-setactiveartboardindex"></a>

### Artboards.setActiveArtboardIndex()

`artboards.setActiveArtboardIndex(index)`

**Description**

Makes a specific artboard active and makes it current in the iteration order.

**Parameters**

| Parameter   | Type          | Description                     |
|-------------|---------------|---------------------------------|
| `index`     | Number (long) | Index of artboard to set active |

**Returns**

Nothing.
