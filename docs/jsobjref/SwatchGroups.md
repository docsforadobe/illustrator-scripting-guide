# SwatchGroups

`swatchGroups`

**Description**

A collection of [SwatchGroup](SwatchGroup.md#jsobjref-swatchgroup) objects.

---

## Properties

### SwatchGroups.length

`swatchGroups.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

### SwatchGroups.parent

`swatchGroups.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

### SwatchGroups.typename

`swatchGroups.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### SwatchGroups.add()

`swatchGroups.add()`

**Description**

Creates a swatch group.

**Returns**

[SwatchGroup](SwatchGroup.md#jsobjref-swatchgroup)

---

### SwatchGroups.getByName()

`swatchGroups.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[SwatchGroup](SwatchGroup.md#jsobjref-swatchgroup)

---

### SwatchGroups.removeAll()

`swatchGroups.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
