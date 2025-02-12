# Views

`app.activeDocument.views`

#### Description

A collection of [View](./View.md) objects in a document.

---

## Properties

### Views.length

`app.activeDocument.views.length`

#### Description

The number of objects in the collection

#### Type

Number; read-only.

---

### Views.parent

`app.activeDocument.views.parent`

#### Description

The parent of this object.

#### Type

Object; read-only.

---

### Views.typename

`app.activeDocument.views.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

## Methods

### Views.index()

`app.activeDocument.views.index(itemKey)`

#### Description

Gets an element from the collection.

#### Parameters

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

#### Returns

[View](./View.md)
