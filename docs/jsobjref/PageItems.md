# PageItems

`app.activeDocument.pageItems`

**Description**

A collection of [PageItem](PageItem.md#jsobjref-pageitem) objects. Provides complete access to all the art items in an Illustrator document in the following classes:

* [CompoundPathItem](CompoundPathItem.md)
  * [Properties](CompoundPathItem.md#properties)
  * [Methods](CompoundPathItem.md#methods)
  * [Example](CompoundPathItem.md#example)
* [GraphItem](GraphItem.md)
  * [Properties](GraphItem.md#properties)
  * [Methods](GraphItem.md#methods)
* [GroupItem](GroupItem.md)
  * [Properties](GroupItem.md#properties)
  * [Methods](GroupItem.md#methods)
  * [Example](GroupItem.md#example)
* [LegacyTextItem](LegacyTextItem.md)
  * [Properties](LegacyTextItem.md#properties)
  * [Methods](LegacyTextItem.md#methods)
* [MeshItem](MeshItem.md)
  * [Properties](MeshItem.md#properties)
  * [Methods](MeshItem.md#methods)
  * [Example](MeshItem.md#example)
* [NonNativeItem](NonNativeItem.md)
  * [Properties](NonNativeItem.md#properties)
  * [Methods](NonNativeItem.md#methods)
* [PathItem](PathItem.md)
  * [Properties](PathItem.md#properties)
  * [Methods](PathItem.md#methods)
  * [Example](PathItem.md#example)
* [PlacedItem](PlacedItem.md)
  * [Properties](PlacedItem.md#properties)
  * [Methods](PlacedItem.md#methods)
  * [Example](PlacedItem.md#example)
* [PluginItem](PluginItem.md)
  * [Properties](PluginItem.md#properties)
  * [Methods](PluginItem.md#methods)
  * [Example](PluginItem.md#example)
* [RasterItem](RasterItem.md)
  * [Properties](RasterItem.md#properties)
  * [Methods](RasterItem.md#methods)
* [SymbolItem](SymbolItem.md)
  * [Properties](SymbolItem.md#properties)
  * [Methods](SymbolItem.md#methods)
* [TextFrameItem](TextFrameItem.md)
  * [Properties](TextFrameItem.md#properties)
  * [Methods](TextFrameItem.md#methods)
  * [Example](TextFrameItem.md#example)

You can reference page items through the [PageItems](#jsobjref-pageitems) property in a [Document](Document.md#jsobjref-document), [Layer](Layer.md#jsobjref-layer), or [GroupItem](GroupItem.md#jsobjref-groupitem).

When you access an individual item in one of these collections, the reference is a page item of one of a particular type. For example, if you use [PageItems](#jsobjref-pageitems) to reference a graph item, the typename value of that object is [GraphItem](GraphItem.md#jsobjref-graphitem).

---

## Properties

### PageItems.length

`app.activeDocument.pageItems.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

### PageItems.parent

`app.activeDocument.pageItems.parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

### PageItems.typename

`app.activeDocument.pageItems.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### PageItems.getByName()

`app.activeDocument.pageItems.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[PageItem](PageItem.md#jsobjref-pageitem)

---

### PageItems.index()

`app.activeDocument.pageItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[PageItem](PageItem.md#jsobjref-pageitem)

---

### PageItems.removeAll()

`app.activeDocument.pageItems.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

---

## Example

### Getting references to external files in page items

```default
// Gets all file-references in the current document using the pageItems object,
// then displays them in a new document

if (app.documents.length > 0) {
  var fileReferences = new Array();
  var sourceDoc = app.activeDocument;

  for (var i = 0; i < sourceDoc.pageItems.length; i++) {
    var artItem = sourceDoc.pageItems[i];
    switch (artItem.typename) {
      case "PlacedItem":
        fileReferences.push(artItem.file.fsName);
        break;
      case "RasterItem":
        if (!artItem.embedded) {
          fileReferences.push(artItem.file.fsName);
        }
        break;
    }
  }

  // Write the file references to a new document
  var reportDoc = documents.add();
  var areaTextPath = reportDoc.pathItems.rectangle(reportDoc.height, 0, reportDoc.width, reportDoc.height);
  var fileNameText = reportDoc.textFrames.areaText(areaTextPath);
  fileNameText.textRange.size = 24;
  var paragraphCount = 3;
  var sourceName = sourceDoc.name;
  var text = "File references in \'" + sourceName + "\':\r\r";
  for (i = 0; i < fileReferences.length; i++) {
    text += (fileReferences[i] + "\r");
    paragraphCount++;
  }
  fileNameText.contents = text;
}
```
