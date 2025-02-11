<a id="jsobjref-variables"></a>

# Variables

`app.activeDocument.variables`

**Description**

The collection of [Variable](Variable.md#jsobjref-variable) objects in the document.

For an example of how to create variables, see [Using variables and datasets](Dataset.md#jsobjref-dataset-usingvariablesanddatasets).

---

## Properties

<a id="jsobjref-variables-length"></a>

### Variables.length

`app.activeDocument.variables.length`

**Description**

The number of variables in the document

**Type**

Number; read-only.

---

<a id="jsobjref-variables-parent"></a>

### Variables.parent

`app.activeDocument.variables.parent`

**Description**

The object that contains the collection of variables

**Type**

Object; read-only.

---

<a id="jsobjref-variables-typename"></a>

### Variables.typename

`app.activeDocument.variables.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

<a id="jsobjref-variables-add"></a>

### Variables.add()

`app.activeDocument.variables.add()`

**Description**

Adds a new variable to the collection.

**Returns**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-variables-getbyname"></a>

### Variables.getByName()

`app.activeDocument.variables.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-variables-index"></a>

### Variables.index()

`app.activeDocument.variables.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-variables-removeall"></a>

### Variables.removeAll()

`app.activeDocument.variables.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
