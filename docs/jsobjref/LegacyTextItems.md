<a id="jsobjref-legacytextitems"></a>

# LegacyTextItems

`legacyTextItems`

**Description**

A collection of [LegacyTextItem](LegacyTextItem.md#jsobjref-legacytextitem) objects.

---

## Properties

<a id="jsobjref-legacytextitems-length"></a>

### LegacyTextItems.length

`legacyTextItems.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-legacytextitems-parent"></a>

### LegacyTextItems.parent

`legacyTextItems.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-legacytextitems-typename"></a>

### LegacyTextItems.typename

`legacyTextItems.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-legacytextitems-converttonative"></a>

### LegacyTextItems.convertToNative()

`legacyTextItems.convertToNative()`

**Description**

Creates text frames from all legacy text items; the original legacy text items are deleted. Returns `true` on success.

**Returns**

Boolean.

---

<a id="jsobjref-legacytextitems-getbyname"></a>

### LegacyTextItems.getByName()

`legacyTextItems.getByName(name)`

**Description**

Get the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[LegacyTextItem](LegacyTextItem.md#jsobjref-legacytextitem)

---

<a id="jsobjref-legacytextitems-index"></a>

### LegacyTextItems.index()

`legacyTextItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[LegacyTextItem](LegacyTextItem.md#jsobjref-legacytextitem)

---

<a id="jsobjref-legacytextitems-removeall"></a>

### LegacyTextItems.removeAll()

`legacyTextItems.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
