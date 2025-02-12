# DocumentPreset

`documentPreset`

#### Description

A preset document template to use when creating a new document. See [Documents.addDocument()](Documents.md#jsobjref-documents-adddocument).

---

## Properties

### DocumentPreset.artboardLayout

`documentPreset.artboardLayout`

#### Description

The layout of artboards in the new document.

Default: `GridByRow`.

#### Type

[DocumentArtboardLayout](scripting-constants.md#documentartboardlayout)

---

### DocumentPreset.artboardRowsOrCols

`documentPreset.artboardRowsOrCols`

#### Description

The number of rows (for rows layout) or columns (for column layout) of artboards.

Range: 1 to (`numArtboards` - 1) or 1 for single row or column layouts.

Default: 1

#### Type

Number (long).

---

### DocumentPreset.artboardSpacing

`documentPreset.artboardSpacing`

#### Description

The spacing between artboards in the new document.

Default: 20.0

#### Type

Number (double).

---

### DocumentPreset.colorMode

`documentPreset.colorMode`

#### Description

The color space for the new document.

#### Type

[DocumentColorSpace](scripting-constants.md#documentcolorspace)

---

### DocumentPreset.documentBleedLink

`documentPreset.documentBleedLink`

#### Description

The document link for bleed values.

#### Type

Boolean.

---

### DocumentPreset.documentBleedOffsetRect

`documentPreset.documentBleedOffsetRect`

#### Description

The document bleed offset rectangle.

#### Type

Rectangle.

---

### DocumentPreset.height

`documentPreset.height`

#### Description

The height in document points.

Default: 792.0

#### Type

Number (double).

---

### DocumentPreset.numArtboards

`documentPreset.numArtboards`

#### Description

The number of artboards for the new document.

Range: 1 to 100.

Default: 1.

#### Type

Number (long).

---

### DocumentPreset.previewMode

`documentPreset.previewMode`

#### Description

The preview mode for the new document.

#### Type

[DocumentPreviewMode](scripting-constants.md#documentpreviewmode)

---

### DocumentPreset.rasterResolution

`documentPreset.rasterResolution`

#### Description

The raster resolution for the new document.

#### Type

[DocumentRasterResolution](scripting-constants.md#documentrasterresolution)

---

### DocumentPreset.title

`documentPreset.title`

#### Description

The document title.

#### Type

String.

---

### DocumentPreset.transparencyGrid

`documentPreset.transparencyGrid`

#### Description

The transparency grid color for the new document.

#### Type

[DocumentTransparencyGrid](scripting-constants.md#documenttransparencygrid)

---

### DocumentPreset.typename

`documentPreset.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### DocumentPreset.units

`documentPreset.units`

#### Description

The ruler units for the new document.

#### Type

[RulerUnits](scripting-constants.md#rulerunits)

---

### DocumentPreset.width

`documentPreset.width`

#### Description

The width in document points.

Default: 612.0

#### Type

Number (double).
