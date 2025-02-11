# IllustratorSaveOptions

`illustratorSaveOptions`

**Description**

Options for saving a document as an Illustrator file, used with the [Document.saveAs()](Document.md#jsobjref-document-saveas) method. All properties are optional.

---

## Properties

### IllustratorSaveOptions.artboardRange

`illustratorSaveOptions.artboardRange`

**Description**

If `saveMultipleArtboards` is `true` (which is valid only for Illustrator 13 or earlier), the document is considered for multi-asset extraction, which specifies an artboard range. An empty string extracts all artboards. Default: empty String.

**Type**

String.

---

### IllustratorSaveOptions.compatibility

`illustratorSaveOptions.compatibility`

**Description**

Specifies the version of Illustrator file format to create. Default: `Compatibility.ILLUSTRATOR19`.

**Type**

[Compatibility](scripting-constants.md#jsobjref-scripting-constants-compatibility)

---

### IllustratorSaveOptions.compressed

`illustratorSaveOptions.compressed`

**Description**

(Illustrator version 10 or later.) If `true`, the saved file is compressed. Default: `true`.

**Type**

Boolean.

---

### IllustratorSaveOptions.embedICCProfile

`illustratorSaveOptions.embedICCProfile`

**Description**

(Illustrator version 9 or later.) If `true`, the document's ICC profile is embedded in the saved file. Default: `false`.

**Type**

Boolean.

---

### IllustratorSaveOptions.embedLinkedFiles

`illustratorSaveOptions.embedLinkedFiles`

**Description**

(Illustrator version 7 or later.) If `true`, the linked image files is embedded in the saved file. Default: `false`.

**Type**

Boolean.

---

### IllustratorSaveOptions.flattenOutput

`illustratorSaveOptions.flattenOutput`

**Description**

(Versions before Illustrator 9.) How transparency should be flattened for older file format versions. Default: `OutputFlattening.PRESERVEAPPEARANCE`.

**Type**

[OutputFlattening](scripting-constants.md#jsobjref-scripting-constants-outputflattening)

---

### IllustratorSaveOptions.fontSubsetThreshold

`illustratorSaveOptions.fontSubsetThreshold`

**Description**

(Illustrator version 9 or later.) Include a subset of fonts when less than this percentage of characters is used in the document. Range: 0.0 to 100.0. Default: 100.0.

**Type**

Number (double).

---

### IllustratorSaveOptions.pdfCompatible

`illustratorSaveOptions.pdfCompatible`

**Description**

(Illustrator version 10 or later.) If `true`, the file is saved as a PDF compatible file. Default: `true`.

**Type**

Boolean.

---

### IllustratorSaveOptions.saveMultipleArtboards

`illustratorSaveOptions.saveMultipleArtboards`

**Description**

If `true`, all artboards or range of the artboards are saved. Valid for Illustrator 13 or earlier.

**Type**

Boolean.

---

### IllustratorSaveOptions.typename

`illustratorSaveOptions.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Example

### Saving with options

```default
// Saves the current document to dest as an AI file with specified options,
// dest specifies the full path and file name of the new file

function exportFileToAI(dest) {
  if (app.documents.length > 0) {
    var ai8Doc = new File(dest);
    var saveOptions = new IllustratorSaveOptions();
    saveOptions.compatibility = Compatibility.ILLUSTRATOR8;
    saveOptions.flattenOutput = OutputFlattening.PRESERVEAPPEARANCE;

    app.activeDocument.saveAs(ai8Doc, saveOptions);
  }
}
```
