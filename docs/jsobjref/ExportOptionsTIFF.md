# ExportOptionsTIFF

`exportOptionsTIFF`

**Description**

Options for exporting a document as a TIFF file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

---

## Properties

### ExportOptionsTIFF.antiAliasing

`exportOptionsTIFF.antiAliasing`

**Description**

If `true`, the exported image should be anti-aliased. Default: `true`.

**Type**

Boolean.

---

### ExportOptionsTIFF.artboardRange

`exportOptionsTIFF.artboardRange`

**Description**

If `saveMultipleArtboards` is `true`, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

---

### ExportOptionsTIFF.byteOrder

`exportOptionsTIFF.byteOrder`

**Description**

The byte order to use in the new file.

**Type**

[TIFFByteOrder](scripting-constants.md#jsobjref-scripting-constants-tiffbyteorder)

---

### ExportOptionsTIFF.imageColorSpace

`exportOptionsTIFF.imageColorSpace`

**Description**

The color space of the exported file. Default: `ImageColorSpace.RGB`.

**Type**

[ImageColorSpace](scripting-constants.md#jsobjref-scripting-constants-imagecolorspace)

---

### ExportOptionsTIFF.lZWCompression

`exportOptionsTIFF.lZWCompression`

!!! note
    This property was erroneously written as "IZWCompression" (with a capital "I"), as opposed to "lzwCompression" (with a lowercase "L"). Note that the latter is correct, and this doc has been updated to reflect this.

**Description**

If `true`, use IZW compression in the new file.

**Type**

Boolean.

---

### ExportOptionsTIFF.resolution

`exportOptionsTIFF.resolution`

**Description**

Resolution of the exported file in dots per inch (dpi). Range: 72.0 to 2400.0. Default: 150.0.

**Type**

Number (double).

---

### ExportOptionsTIFF.saveMultipleArtboards

`exportOptionsTIFF.saveMultipleArtboards`

**Description**

If `true`, all artboards or range of artboards are saved. Default: `false`.

**Type**

Number (double).

---

## Example

### Exporting to TIFF format

```default
// Exports current document to dest as a TIFF file with specified options,
// dest contains the full path including the file name

function exportFileToPSD(dest) {
  if (app.documents.length > 0) {
    var exportOptions = new ExportOptionsTIFF();
    exportOptions.resolution = 150;
    exportOptions.byteOrder = TIFFByteOrder.IBMPC;
    exportOptions.lZWCompression = false;

    var type = ExportType.TIFF;
    var fileSpec = new File(dest);

    app.activeDocument.exportFile(fileSpec, type, exportOptions);
  }
}
```
