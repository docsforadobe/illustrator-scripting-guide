# Tags

`app.activeDocument.selection[index].tags`

**Description**

A collection of [Tag](./Tag.md) objects.

---

## Properties

### Tags.length

`app.activeDocument.selection[index].tags.length`

**Description**

The number of elements in the collection.

**Type**

Number; read-only.

---

### Tags.parent

`app.activeDocument.selection[index].tags.parent`

**Description**

The object's container.

**Type**

Object; read-only.

---

### Tags.typename

`app.activeDocument.selection[index].tags.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

### Tags.add()

`app.activeDocument.selection[index].tags.add()`

**Description**

Creates a new [Tag](./Tag.md) object.

**Returns**

[Tag](./Tag.md)

---

### Tags.getByName()

`app.activeDocument.selection[index].tags.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Tag](./Tag.md)

---

### Tags.index()

`app.activeDocument.selection[index].tags.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Tag](./Tag.md)

---

### Tags.removeAll()

`app.activeDocument.selection[index].tags.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Setting tag values

```default
// Adds tags to all RasterItems and PlacedItems in the current document
if ( app.documents.length > 0 ) {
  var doc = app.activeDocument;

  if ( doc.placedItems.length + doc.rasterItems.length > 0 ) {
    for ( i = 0; i < doc.pageItems.length; i++ ) {
      var imageArt = doc.pageItems[i];

      if ( imageArt.typename == "PlacedItem" || imageArt.typename == "RasterItem") {
        // Create a new Tag with the name AdobeURL and the
        // value of the www link

        var urlTAG = imageArt.tags.add();
        urlTAG.name = "AdobeWebSite";
        urlTAG.value = "http://www.adobe.com/";
      }
    }
  } else {
    alert( "No placed or raster items in the document" );
  }
}
```
