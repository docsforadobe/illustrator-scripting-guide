# Variables

`app.activeDocument.variables`

#### Description

The collection of [Variable](./Variable.md) objects in the document.

For an example of how to create variables, see [Using variables and datasets](Dataset.md#using-variables-and-datasets).

---

## Properties

### Variables.length

`app.activeDocument.variables.length`

#### Description

The number of variables in the document

#### Type

Number; read-only.

---

### Variables.parent

`app.activeDocument.variables.parent`

#### Description

The object that contains the collection of variables

#### Type

Object; read-only.

---

### Variables.typename

`app.activeDocument.variables.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

## Methods

### Variables.add()

`app.activeDocument.variables.add()`

#### Description

Adds a new variable to the collection.

#### Returns

[Variable](./Variable.md)

---

### Variables.getByName()

`app.activeDocument.variables.getByName(name)`

#### Description

Get the first element in the collection with the provided name.

#### Parameters

| Parameter |  Type  |      Description       |
| --------- | ------ | ---------------------- |
| `name`    | String | Name of element to get |

#### Returns

[Variable](./Variable.md)

---

### Variables.index()

`app.activeDocument.variables.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter |      Type      |     Description      |
| --------- | -------------- | -------------------- |
| `itemKey` | String, Number | String or number key |

#### Returns

[Variable](./Variable.md)

---

### Variables.removeAll()

`app.activeDocument.variables.removeAll()`

#### Description

Deletes all elements in this collection.

#### Returns

Nothing.
