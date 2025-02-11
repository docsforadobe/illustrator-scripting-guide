# GroupItems

`app.activeDocument.groupItems`

**Description**

The collection of grouped art items in a document.

---

## Properties

### GroupItems.length

`app.activeDocument.groupItems.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

### GroupItems.parent

`app.activeDocument.groupItems.parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

### GroupItems.typename

`app.activeDocument.groupItems.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### GroupItems.add()

`app.activeDocument.groupItems.add()`

**Description**

Creates a new object.

**Returns**

[GroupItem](./GroupItem.md)

---

### GroupItems.createFromFile()

`app.activeDocument.groupItems.createFromFile(imageFile)`

**Description**

Places an external vector art file as a group item in the document.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `imageFile` | File   | Vector art file to place |

**Returns**

[GroupItem](./GroupItem.md)

---

### GroupItems.getByName()

`app.activeDocument.groupItems.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[GroupItem](./GroupItem.md)

---

### GroupItems.index()

`app.activeDocument.groupItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[GroupItem](./GroupItem.md)

---

### GroupItems.removeAll()

`app.activeDocument.groupItems.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Importing a PDF as a group item

The following script shows how you can import a PDF document using the [GroupItems.createFromFile()](#jsobjref-groupitems-createfromfile) function.

!!! note
    Before running this script you must create a one page PDF file and put it in the location `/temp/testfile1.pdf`.

```default
// Embeds a new group item in to the current document from a file specified by dest
// dest should contain the full path and file name

function embedPDF(dest) {
    var embedDoc = new File(dest);
    if (app.documents.length > 0 && embedDoc.exists) {
        var doc = app.activeDocument;
        var placed = doc.groupItems.createFromFile(embedDoc);
    }
}
```
