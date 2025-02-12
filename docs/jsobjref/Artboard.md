# Artboard

`artboard`

#### Description

An Artboard object represents a single artboard in a document. There can be between 1 to 100 artboards in one document.

## Properties

### Artboard.artboardRect

`artboard.artboardRect`

#### Description

Size and position of the artboard.

#### Type

Rect

---

### Artboard.name

`artboard.name`

#### Description

The unique identifying name of the artboard.

#### Type

String

---

### Artboard.parent

`artboard.parent`

#### Description

The parent of this object.

#### Type

[Document](./Document.md); read-only.

---

### Artboard.rulerOrigin

`artboard.rulerOrigin`

#### Description

Ruler origin of the artboard, relative to the top left corner of the artboard.

#### Type

Point

---

### Artboard.rulerPAR

`artboard.rulerPAR`

#### Description

Pixel aspect ratio, used in ruler visualization if the units are pixels.

Range: 0.1 to 10.

#### Type

Number (double)

---

### Artboard.showCenter

`artboard.showCenter`

#### Description

Show center mark.

#### Type

Boolean

---

### Artboard.showCrossHairs

`artboard.showCrossHairs`

#### Description

Show cross hairs.

#### Type

Boolean

---

### Artboard.showSafeAreas

`artboard.showSafeAreas`

#### Description

Show title and action safe areas (for video).

#### Type

Boolean

---

### Artboard.typename

`artboard.typename`

#### Description

Read-only. The class name of this object.

#### Type

String

---

## Methods

### Artboard.remove()

`artboard.remove()`

#### Description

Deletes this artboard object. You cannot remove the last artboard in a document.

#### Returns

Nothing.
