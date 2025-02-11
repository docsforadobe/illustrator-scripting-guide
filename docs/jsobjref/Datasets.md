<a id="jsobjref-datasets"></a>

# Datasets

`app.activeDocument.dataSets`

**Description**

A collection of [Dataset](Dataset.md#jsobjref-dataset) objects.

---

## Properties

<a id="jsobjref-datasets-length"></a>

### Datasets.length

`app.activeDocument.dataSets.length`

**Description**

The number of datasets in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-datasets-parent"></a>

### Datasets.parent

`app.activeDocument.dataSets.parent`

**Description**

The name of the object that contains this dataset.

**Type**

[Document](Document.md#jsobjref-document), read-only.

---

<a id="jsobjref-datasets-typename"></a>

### Datasets.typename

`app.activeDocument.dataSets.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-datasets-add"></a>

### Datasets.add()

`app.activeDocument.dataSets.add()`

**Description**

Creates a new dataset object.

**Returns**

[Dataset](Dataset.md#jsobjref-dataset)

---

<a id="jsobjref-datasets-getbyname"></a>

### Datasets.getByName()

`app.activeDocument.dataSets.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Dataset](Dataset.md#jsobjref-dataset)

---

<a id="jsobjref-datasets-index"></a>

### Datasets.index()

`app.activeDocument.dataSets.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Dataset](Dataset.md#jsobjref-dataset)

---

<a id="jsobjref-datasets-removeall"></a>

### Datasets.removeAll()

`app.activeDocument.dataSets.removeAll()`

**Description**

Removes all elements in the collection.

**Returns**

Nothing.
