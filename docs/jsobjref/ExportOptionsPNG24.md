# ExportOptionsPNG24

`exportOptionsPNG24`

#### Description

Options for exporting a document as a 24-bit PNG file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

---

## Properties

### ExportOptionsPNG24.antiAliasing

`exportOptionsPNG24.antiAliasing`

#### Description

If `true`, the exported image be anti-aliased. Default: `true`.

#### Type

Boolean.

---

### ExportOptionsPNG24.artBoardClipping

`exportOptionsPNG24.artBoardClipping`

#### Description

If `true`, the exported image be clipped to the art board. Default: `false`.

#### Type

Boolean.

---

### ExportOptionsPNG24.horizontalScale

`exportOptionsPNG24.horizontalScale`

#### Description

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

#### Type

Number (double).

---

### ExportOptionsPNG24.matte

`exportOptionsPNG24.matte`

#### Description

If `true`, the art board be matted with a color. Default: `true`.

#### Type

Boolean.

---

### ExportOptionsPNG24.matteColor

`exportOptionsPNG24.matteColor`

#### Description

The color to use when matting the art board. Default: `white`.

#### Type

[RGBColor](./RGBColor.md)

---

### ExportOptionsPNG24.saveAsHTML

`exportOptionsPNG24.saveAsHTML`

#### Description

If `true`, the exported image be saved with an accompanying HTML file. Default: `false`.

#### Type

Boolean.

---

### ExportOptionsPNG24.transparency

`exportOptionsPNG24.transparency`

#### Description

If `true`, the exported image use transparency. Default: `true`.

#### Type

Boolean.

---

### ExportOptionsPNG24.typename

`exportOptionsPNG24.typename`

#### Description

The class name of the referenced object.

#### Type

String, read-only.

---

### ExportOptionsPNG24.verticalScale

`exportOptionsPNG24.verticalScale`

#### Description

The vertical scaling factor to apply to the exported image, where 100.0 is 100. Default: 100.0.

#### Type

Number (double).

---

## Example

### Exporting to PNG24 format

```javascript
// Exports current document to dest as a PNG24 file with specified options,
// dest contains the full path including the file name,
// saveAsHTML option creates an HTML version with the PNG file in an images folder

function exportFileToPNG24(dest) {
    if (app.documents.length > 0) {
        var exportOptions = new ExportOptionsPNG24();
        exportOptions.antiAliasing = false;
        exportOptions.transparency = false;
        exportOptions.saveAsHTML = true;

        var type = ExportType.PNG24;
        var fileSpec = new File(dest);

        app.activeDocument.exportFile(fileSpec, type, exportOptions);
    }
}
```
