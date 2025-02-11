<a id="jsobjref-rasteritems"></a>

# RasterItems

`app.activeDocument.rasterItems`

**Description**

A collection of [RasterItem](RasterItem.md#jsobjref-rasteritem) objects.

---

## Properties

<a id="jsobjref-rasteritems-length"></a>

### RasterItems.length

`app.activeDocument.rasterItems.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-rasteritems-parent"></a>

### RasterItems.parent

`app.activeDocument.rasterItems.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-rasteritems-typename"></a>

### RasterItems.typename

`app.activeDocument.rasterItems.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-rasteritems-getbyname"></a>

### RasterItems.getByName()

`app.activeDocument.rasterItems.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[SymbolItem](SymbolItem.md#jsobjref-symbolitem)

---

<a id="jsobjref-rasteritems-index"></a>

### RasterItems.index()

`app.activeDocument.rasterItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[SymbolItem](SymbolItem.md#jsobjref-symbolitem)

---

<a id="jsobjref-rasteritems-removeall"></a>

### RasterItems.removeAll()

`app.activeDocument.rasterItems.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Creating a raster item

```default
// Creates a new raster item in a new document from a raster file
// jpgFilePath contains the full path and file name of a jpg file
function createRasterItem(jpgFilePath) {
  var rasterFile = File(jpgFilePath);
  var myDoc = app.documents.add();

  var myPlacedItem = myDoc.placedItems.add();
  myPlacedItem.file = rasterFile;
  myPlacedItem.position = Array(0, myDoc.height);
  myPlacedItem.embed();
}
```

### Finding and examining a raster item

```default
// Examines the color space of the first raster item in the document and displays
// result in ESTK console
if (app.documents.length > 0 && app.activeDocument.rasterItems.length > 0) {
  var rasterArt = app.activeDocument.rasterItems[0];

  switch (rasterArt.imageColorSpace) {
    case ImageColorSpace.CMYK:
      $.writeln("The color space of the first raster item is CMYK");
      break;

    case ImageColorSpace.RGB:
      $.writeln("The color space of the first raster item is RGB");
      break;

    case ImageColorSpace.GRAYSCALE:
      $.writeln("The color space of the first raster item is GRAYSCALE");
      break;
  }
}
```
