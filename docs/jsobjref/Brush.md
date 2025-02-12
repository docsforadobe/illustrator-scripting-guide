# Brush

`app.activeDocument.brushes[index`

**Description**

A brush in an Illustrator document. Brushes are contained in documents. Additional brushes may be created by the user within Illustrator. You can access brushes within a script, but you cannot create them.

---

## Properties

### Brush.name

`app.activeDocument.brushes[index].name`

**Description**

The name of the brush

**Type**

String

---

### Brush.parent

`app.activeDocument.brushes[index].parent`

**Description**

The document that contains this brush.

**Type**

[Document](./Document.md); read-only.

---

### Brush.typename

`app.activeDocument.brushes[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

### Brush.applyTo()

`app.activeDocument.brushes[index].applyTo(artItem)`

**Description**

Applies the `brush` to a specific art item.

**Parameters**

| Parameter   | Type                                      | Description                |
|-------------|-------------------------------------------|----------------------------|
| `artItem`   | [PageItem](./PageItem.md) | Art item to apply brush to |

**Returns**

Nothing.

---

## Example

### Applying a Brush

```javascript
// Duplicates and groups all items in the current selection,
// then applies the same brush to each item in the group

if (app.documents.length > 0) {
    var docSelection = app.activeDocument.selection;
    if (docSelection.length > 0) {
        var newGroup = app.activeDocument.groupItems.add();

        for (var i = 0; i < docSelection.length; i++) {
            var newItem = docSelection[i].duplicate();
            newItem.moveToBeginning(newGroup);
        }

        var brush = app.activeDocument.brushes[1];
        brush.applyTo(newGroup);
    }
}
```
