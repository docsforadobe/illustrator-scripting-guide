<a id="jsobjref-epssaveoptions"></a>

# EPSSaveOptions

`epsSaveOptions`

**Description**

Options for saving a document as an Illustrator EPS file, used with the [Document.saveAs()](Document.md#jsobjref-document-saveas) method.

All properties are optional.

---

## Properties

<a id="jsobjref-epssaveoptions-artboardrange"></a>

### EPSSaveOptions.artboardRange

`epsSaveOptions.artboardRange`

**Description**

If `saveMultipleArtboards` is `true`, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty string

**Type**

String.

---

<a id="jsobjref-epssaveoptions-cmykpostscript"></a>

### EPSSaveOptions.cmykPostScript

`epsSaveOptions.cmykPostScript`

**Description**

If `true`, use CMYK PostScript.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-compatibility"></a>

### EPSSaveOptions.compatibility

`epsSaveOptions.compatibility`

**Description**

Specifies the version of the EPS file format to save.

Default: `Compatibility.ILLUSTRATOR1719`.

**Type**

[Compatibility](scripting-constants.md#jsobjref-scripting-constants-compatibility)

---

<a id="jsobjref-epssaveoptions-compatiblegradientprinting"></a>

### EPSSaveOptions.compatibleGradientPrinting

`epsSaveOptions.compatibleGradientPrinting`

**Description**

If `true`, create a raster item of the gradient or gradient mesh so that PostScript Level 2 printers can print the object.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-embedallfonts"></a>

### EPSSaveOptions.embedAllFonts

`epsSaveOptions.embedAllFonts`

**Description**

If `true`, all fonts used by the document should be embedded in the saved file (version 7 or later).

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-embedlinkedfiles"></a>

### EPSSaveOptions.embedLinkedFiles

`epsSaveOptions.embedLinkedFiles`

**Description**

If `true`, linked image files are to be included in the saved document.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-flattenouput"></a>

### EPSSaveOptions.flattenOuput

`epsSaveOptions.flattenOuput`

**Description**

How should transparency be flattened for file formats older than Illustrator 9.

**Type**

[OutputFlattening](scripting-constants.md#jsobjref-scripting-constants-outputflattening)

---

<a id="jsobjref-epssaveoptions-includedocumentthumbnails"></a>

### EPSSaveOptions.includeDocumentThumbnails

`epsSaveOptions.includeDocumentThumbnails`

**Description**

If `true`, thumbnail image of the EPS artwork should be included.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-overprint"></a>

### EPSSaveOptions.overprint

`epsSaveOptions.overprint`

**Description**

Whether to preserve, discard, or simulate the overprint.

Default: `PDFOverprint.PRESERVEPDFOVERPRINT`.

**Type**

[PDFOverprint](scripting-constants.md#jsobjref-scripting-constants-pdfoverprint)

---

<a id="jsobjref-epssaveoptions-postscript"></a>

### EPSSaveOptions.postScript

`epsSaveOptions.postScript`

**Description**

PostScript Language Level to use (Level 1 valid for file format version 8 or older).

Default: `EPSPostScriptLevelEnum.LEVEL2`.

**Type**

[EPSPostScriptLevelEnum](scripting-constants.md#jsobjref-scripting-constants-epspostscriptlevelenum)

---

<a id="jsobjref-epssaveoptions-preview"></a>

### EPSSaveOptions.preview

`epsSaveOptions.preview`

**Description**

The format for the EPS preview image.

**Type**

[EPSPreview](scripting-constants.md#jsobjref-scripting-constants-epspreview)

---

<a id="jsobjref-epssaveoptions-savemultipleartboards"></a>

### EPSSaveOptions.saveMultipleArtboards

`epsSaveOptions.saveMultipleArtboards`

**Description**

If `true`, all artboards or range of artboards are saved.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-epssaveoptions-typename"></a>

### EPSSaveOptions.typename

`epsSaveOptions.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Example

### Exporting to EPS format

```default
// Exports current document to destFile as an EPS file with specified options,
// destFile contains the full path including the file name

function exportFileAsEPS(destFile) {
  var newFile = new File(destFile);
  var saveDoc;
  if (app.documents.length == 0) {
    saveDoc = app.documents.add();
  } else {
    saveDoc = app.activeDocument;
  }

  var saveOpts = new ePSSaveOptions();
  saveOpts.cmykPostScript = true;
  saveOpts.embedAllFonts = true;

  saveDoc.saveAs(newFile, saveOpts);
}
```
