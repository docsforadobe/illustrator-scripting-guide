<a id="jsobjref-pluginitems"></a>

# PluginItems

`app.activeDocument.pluginItems`

**Description**

A collection of [PluginItem](PluginItem.md#jsobjref-pluginitem) objects in a document.

See [Copying a plug-in item](PluginItem.md#jsobjref-pluginitem-copying-a-plugin-item).

---

## Properties

<a id="jsobjref-pluginitems-length"></a>

### PluginItems.length

`app.activeDocument.pluginItems.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-pluginitems-parent"></a>

### PluginItems.parent

`app.activeDocument.pluginItems.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-pluginitems-typename"></a>

### PluginItems.typename

`app.activeDocument.pluginItems.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-pluginitems-getbyname"></a>

### PluginItems.getByName()

`app.activeDocument.pluginItems.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[PluginItem](PluginItem.md#jsobjref-pluginitem)

---

<a id="jsobjref-pluginitems-index"></a>

### PluginItems.index()

`app.activeDocument.pluginItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[PluginItem](PluginItem.md#jsobjref-pluginitem)

---

<a id="jsobjref-pluginitems-removeall"></a>

### PluginItems.removeAll()

`app.activeDocument.pluginItems.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.
