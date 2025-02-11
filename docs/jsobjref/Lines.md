<a id="jsobjref-lines"></a>

# Lines

`lines`

**Description**

A collection of `TextRange` objects representing lines of text in a text frame. The elements are not named; you must access them by index.

---

## Properties

<a id="jsobjref-lines-length"></a>

### Lines.length

`lines.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-lines-parent"></a>

### Lines.parent

`lines.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-lines-typename"></a>

### Lines.typename

`lines.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-lines-index"></a>

### Lines.index()

`lines.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[TextRange](TextRange.md#jsobjref-textrange)

---

<a id="jsobjref-lines-removeall"></a>

### Lines.removeAll()

`lines.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.
