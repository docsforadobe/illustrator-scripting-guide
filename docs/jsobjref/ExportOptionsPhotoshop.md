<a id="jsobjref-exportoptionsphotoshop"></a>

# ExportOptionsPhotoshop

`exportOptionsPhotoshop`

**Description**

Options for exporting a document as a Photoshop file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

---

## Properties

<a id="jsobjref-exportoptionsphotoshop-antialiasing"></a>

### ExportOptionsPhotoshop.antiAliasing

`exportOptionsPhotoshop.antiAliasing`

**Description**

If `true`, the exported image should be anti-aliased. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-artboardrange"></a>

### ExportOptionsPhotoshop.artboardRange

`exportOptionsPhotoshop.artboardRange`

**Description**

If `saveMultipleArtboards` is true, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

---

<a id="jsobjref-exportoptionsphotoshop-editabletext"></a>

### ExportOptionsPhotoshop.editableText

`exportOptionsPhotoshop.editableText`

**Description**

If `true`, text objects should be exported as editable text layers. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-embediccprofile"></a>

### ExportOptionsPhotoshop.embedICCProfile

`exportOptionsPhotoshop.embedICCProfile`

**Description**

If `true`, an ICC profile should be embedded in the exported file. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-imagecolorspace"></a>

### ExportOptionsPhotoshop.imageColorSpace

`exportOptionsPhotoshop.imageColorSpace`

**Description**

The color space of the exported file. Default: `ImageColorSpace.RGB`.

**Type**

[ImageColorSpace](scripting-constants.md#jsobjref-scripting-constants-imagecolorspace)

---

<a id="jsobjref-exportoptionsphotoshop-maximumeditability"></a>

### ExportOptionsPhotoshop.maximumEditability

`exportOptionsPhotoshop.maximumEditability`

**Description**

Preserve as much of the original document’s structure as possible when exporting. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-resolution"></a>

### ExportOptionsPhotoshop.resolution

`exportOptionsPhotoshop.resolution`

**Description**

Resolution of the exported file in dots per inch (dpi). Range: 72.0 to 2400.0. Default: 150.0.

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsphotoshop-savemultipleartboards"></a>

### ExportOptionsPhotoshop.saveMultipleArtboards

`exportOptionsPhotoshop.saveMultipleArtboards`

**Description**

If `true`, all artboards or range of artboards are saved. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-typename"></a>

### ExportOptionsPhotoshop.typename

`exportOptionsPhotoshop.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-exportoptionsphotoshop-warnings"></a>

### ExportOptionsPhotoshop.warnings

`exportOptionsPhotoshop.warnings`

**Description**

If `true`, a warning dialog should be displayed in case of conflicts in the export settings. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsphotoshop-writelayers"></a>

### ExportOptionsPhotoshop.writeLayers

`exportOptionsPhotoshop.writeLayers`

**Description**

If `true`, the document layers should be presented in the exported document. Default: `true`.

**Type**

Boolean.

---

## Example

### Exporting to Photoshop format

```default
// Exports current document to dest as a PSD file with specified options,
// dest contains the full path including the file name

function exportFileToPSD(dest) {
  if (app.documents.length > 0) {
    var exportOptions = new ExportOptionsPhotoshop();
    exportOptions.resolution = 150;

    var type = ExportType.PHOTOSHOP;
    var fileSpec = new File(dest);

    app.activeDocument.exportFile(fileSpec, type, exportOptions);
  }
}
```
