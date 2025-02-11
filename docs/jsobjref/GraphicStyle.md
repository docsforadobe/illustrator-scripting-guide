<a id="jsobjref-graphicstyle"></a>

# GraphicStyle

`app.activeDocument.graphicStyles[index`

**Description**

A graphic style. Each graphic style defines a set of appearance attributes that you can apply non-destructively to page items. Graphic styles are contained in documents. Scripts cannot create new graphic styles.

---

## Properties

<a id="jsobjref-graphicstyle-name"></a>

### GraphicStyle.name

`app.activeDocument.graphicStyles[index].name`

**Description**

The graphic style name.

**Type**

String.

---

<a id="jsobjref-graphicstyle-parent"></a>

### GraphicStyle.parent

`app.activeDocument.graphicStyles[index].parent`

**Description**

The document that contains this graphic style.

**Type**

[Document](Document.md#jsobjref-document), read-only.

---

<a id="jsobjref-graphicstyle-typename"></a>

### GraphicStyle.typename

`app.activeDocument.graphicStyles[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-class-applyto"></a>

### GraphicStyle.applyTo()

`app.activeDocument.graphicStyles[index].applyTo(artItem)`

**Description**

Applies this art style to a specified art item.

**Parameters**

| Parameter   | Type                                      | Description     |
|-------------|-------------------------------------------|-----------------|
| `artItem`   | [PageItem](PageItem.md#jsobjref-pageitem) | Target art item |

**Returns**

Nothing.

---

<a id="jsobjref-class-mergeto"></a>

### GraphicStyle.mergeTo()

`app.activeDocument.graphicStyles[index].mergeTo(artItem)`

**Description**

Merges this art style into the current styles of a specified art item.

**Parameters**

| Parameter   | Type                                      | Description     |
|-------------|-------------------------------------------|-----------------|
| `artItem`   | [PageItem](PageItem.md#jsobjref-pageitem) | Target art item |

**Returns**

Nothing.

---

<a id="jsobjref-class-remove"></a>

### GraphicStyle.remove()

`app.activeDocument.graphicStyles[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

## Example

### Applying a graphic style

```default
// Duplicates each path item in the selection, places the duplicate into a new group,
// then applies a graphic style to the new groups items

if (app.documents.length > 0) {
  var doc = app.activeDocument;
  var selected = doc.selection;
  var newGroup = doc.groupItems.add();
  newGroup.name = "NewGroup";
  newGroup.move(doc, ElementPlacement.PLACEATEND);

  var endIndex = selected.length;
  for (var i = 0; i < endIndex; i++) {
    if (selected[i].typename == "PathItem")
      selected[i].duplicate(newGroup, ElementPlacement.PLACEATEND);
  }

  for (i = 0; i < newGroup.pageItems.length; i++) {
    doc.graphicStyles[1].applyTo(newGroup.pageItems[i]);
  }
}
```
