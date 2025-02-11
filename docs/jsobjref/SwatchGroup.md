<a id="jsobjref-swatchgroup"></a>

# SwatchGroup

`swatchGroup`

**Description**

A group of [Swatch](Swatch.md#jsobjref-swatch) objects.

---

## Properties

<a id="jsobjref-swatchgroup-name"></a>

### SwatchGroup.name

`swatchGroup.name`

**Description**

The name of the swatch group.

**Type**

string

---

<a id="jsobjref-swatchgroup-parent"></a>

### SwatchGroup.parent

`swatchGroup.parent`

**Description**

The object that contains the swatch group.

**Type**

Object, read-only.

---

<a id="jsobjref-swatchgroup-typename"></a>

### SwatchGroup.typename

`swatchGroup.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only

---

## Methods

<a id="jsobjref-swatchgroup-addspot"></a>

### SwatchGroup.addSpot()

`swatchGroup.addSpot(spot)`

**Description**

Adds a spot swatch to the swatch group.

**Parameters**

| Parameter   | Type                          | Description   |
|-------------|-------------------------------|---------------|
| `spot`      | [Spot](Spot.md#jsobjref-spot) | Spot to add   |

**Returns**

Nothing.

---

<a id="jsobjref-swatchgroup-addswatch"></a>

### SwatchGroup.addSwatch()

`swatchGroup.addSwatch(swatch)`

**Description**

Adds a swatch to the swatch group.

**Parameters**

| Parameter   | Type                                | Description   |
|-------------|-------------------------------------|---------------|
| `swatch`    | [Swatch](Swatch.md#jsobjref-swatch) | Swatch to add |

**Returns**

Nothing.

---

<a id="jsobjref-swatchgroup-getallswatches"></a>

### SwatchGroup.getAllSwatches()

`swatchGroup.getAllSwatches()`

**Description**

Gets a list of all swatches in the swatch group.

**Returns**

List of [Swatch](Swatch.md#jsobjref-swatch)

---

<a id="jsobjref-swatchgroup-remove"></a>

### SwatchGroup.remove()

`swatchGroup.remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

<a id="jsobjref-swatchgroup-removeall"></a>

### SwatchGroup.removeAll()

`swatchGroup.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
