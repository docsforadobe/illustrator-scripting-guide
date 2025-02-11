# View

`app.activeDocument.views[index]`

**Description**

A document view in an Illustrator document, which represents a window view onto a document.

Scripts cannot create new views, but can modify some properties of existing views, including the center point, screen mode, and zoom.

---

## Properties

### View.bounds

`app.activeDocument.views[index].bounds`

**Description**

Read-only. The bounding rectangle of this view relative to the current document's bounds.

**Type**

Array of 4 Numbers

---

### View.centerPoint

`app.activeDocument.views[index].centerPoint`

**Description**

The center point of this view relative to the current document's bounds.

**Type**

Array of 2 Numbers

---

### View.parent

`app.activeDocument.views[index].parent`

**Description**

Read-only. The document that contains this view.

**Type**

[Document](./Document.md)

---

### View.screenMode

`app.activeDocument.views[index].screenMode`

**Description**

The mode of display for this view.

**Type**

[ScreenMode](scripting-constants.md#jsobjref-scripting-constants-screenmode)

---

### View.typename

`app.activeDocument.views[index].typename`

**Description**

Read-only. The class name of the referenced object.

**Type**

String

---

### View.zoom

`app.activeDocument.views[index].zoom`

**Description**

The zoom factor of this view, where 100.0 is 100%.

**Type**

Number (double)
