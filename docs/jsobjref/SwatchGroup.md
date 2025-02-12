# SwatchGroup

`swatchGroup`

#### Description

A group of [Swatch](./Swatch.md) objects.

---

## Properties

### SwatchGroup.name

`swatchGroup.name`

#### Description

The name of the swatch group.

#### Type

string

---

### SwatchGroup.parent

`swatchGroup.parent`

#### Description

The object that contains the swatch group.

#### Type

Object; read-only.

---

### SwatchGroup.typename

`swatchGroup.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only

---

## Methods

### SwatchGroup.addSpot()

`swatchGroup.addSpot(spot)`

#### Description

Adds a spot swatch to the swatch group.

#### Parameters

| Parameter |       Type        | Description |
| --------- | ----------------- | ----------- |
| `spot`    | [Spot](./Spot.md) | Spot to add |

#### Returns

Nothing.

---

### SwatchGroup.addSwatch()

`swatchGroup.addSwatch(swatch)`

#### Description

Adds a swatch to the swatch group.

#### Parameters

| Parameter |         Type          |  Description  |
| --------- | --------------------- | ------------- |
| `swatch`  | [Swatch](./Swatch.md) | Swatch to add |

#### Returns

Nothing.

---

### SwatchGroup.getAllSwatches()

`swatchGroup.getAllSwatches()`

#### Description

Gets a list of all swatches in the swatch group.

#### Returns

List of [Swatch](./Swatch.md)

---

### SwatchGroup.remove()

`swatchGroup.remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### SwatchGroup.removeAll()

`swatchGroup.removeAll()`

#### Description

Deletes all elements in the collection.

#### Returns

Nothing.
