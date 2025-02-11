<a id="jsobjref-documentpreset"></a>

# DocumentPreset

`documentPreset`

**Description**

A preset document template to use when creating a new document. See [Documents.addDocument()](Documents.md#jsobjref-documents-adddocument).

---

## Properties

<a id="jsobjref-documentpreset-artboardlayout"></a>

### DocumentPreset.artboardLayout

`documentPreset.artboardLayout`

**Description**

The layout of artboards in the new document. Default: `GridByRow`.

**Type**

[DocumentArtboardLayout](scripting-constants.md#jsobjref-scripting-constants-documentartboardlayout)

---

<a id="jsobjref-documentpreset-artboardrowsorcols"></a>

### DocumentPreset.artboardRowsOrCols

`documentPreset.artboardRowsOrCols`

**Description**

The number of rows (for rows layout) or columns (for column layout) of artboards. Range: 1 to (`numArtboards` - 1) or 1 for single row or column layouts. Default: 1

**Type**

Number (long).

---

<a id="jsobjref-documentpreset-artboardspacing"></a>

### DocumentPreset.artboardSpacing

`documentPreset.artboardSpacing`

**Description**

The spacing between artboards in the new document. Default: 20.0

**Type**

Number (double).

---

<a id="jsobjref-documentpreset-colormode"></a>

### DocumentPreset.colorMode

`documentPreset.colorMode`

**Description**

The color space for the new document.

**Type**

[DocumentColorSpace](scripting-constants.md#jsobjref-scripting-constants-documentcolorspace)

---

<a id="jsobjref-documentpreset-documentbleedlink"></a>

### DocumentPreset.documentBleedLink

`documentPreset.documentBleedLink`

**Description**

The document link for bleed values.

**Type**

Boolean.

---

<a id="jsobjref-documentpreset-documentbleedoffsetrect"></a>

### DocumentPreset.documentBleedOffsetRect

`documentPreset.documentBleedOffsetRect`

**Description**

The document bleed offset rectangle.

**Type**

Rectangle.

---

<a id="jsobjref-documentpreset-height"></a>

### DocumentPreset.height

`documentPreset.height`

**Description**

The height in document points. Default: 792.0

**Type**

Number (double).

---

<a id="jsobjref-documentpreset-numartboards"></a>

### DocumentPreset.numArtboards

`documentPreset.numArtboards`

**Description**

The number of artboards for the new document. Range: 1 to 100. Default: 1.

**Type**

Number (long).

---

<a id="jsobjref-documentpreset-previewmode"></a>

### DocumentPreset.previewMode

`documentPreset.previewMode`

**Description**

The preview mode for the new document.

**Type**

[DocumentPreviewMode](scripting-constants.md#jsobjref-scripting-constants-documentpreviewmode)

---

<a id="jsobjref-documentpreset-rasterresolution"></a>

### DocumentPreset.rasterResolution

`documentPreset.rasterResolution`

**Description**

The raster resolution for the new document.

**Type**

[DocumentRasterResolution](scripting-constants.md#jsobjref-scripting-constants-documentrasterresolution)

---

<a id="jsobjref-documentpreset-title"></a>

### DocumentPreset.title

`documentPreset.title`

**Description**

The document title.

**Type**

String.

---

<a id="jsobjref-documentpreset-transparencygrid"></a>

### DocumentPreset.transparencyGrid

`documentPreset.transparencyGrid`

**Description**

The transparency grid color for the new document.

**Type**

[DocumentTransparencyGrid](scripting-constants.md#jsobjref-scripting-constants-documenttransparencygrid)

---

<a id="jsobjref-documentpreset-typename"></a>

### DocumentPreset.typename

`documentPreset.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-documentpreset-units"></a>

### DocumentPreset.units

`documentPreset.units`

**Description**

The ruler units for the new document.

**Type**

[RulerUnits](scripting-constants.md#jsobjref-scripting-constants-rulerunits)

---

<a id="jsobjref-documentpreset-width"></a>

### DocumentPreset.width

`documentPreset.width`

**Description**

The width in document points. Default: 612.0

**Type**

Number (double).
