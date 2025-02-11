<a id="jsobjref-exportoptionsgif"></a>

# ExportOptionsGIF

`exportOptionsGIF`

**Description**

Options for exporting a document as a GIF file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

---

## Properties

<a id="jsobjref-exportoptionsgif-antialiasing"></a>

### ExportOptionsGIF.antiAliasing

`exportOptionsGIF.antiAliasing`

**Description**

If `true`, the exported image should be anti-aliased. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-artboardclipping"></a>

### ExportOptionsGIF.artBoardClipping

`exportOptionsGIF.artBoardClipping`

**Description**

If `true`, the exported image should be clipped to the art board. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-colorcount"></a>

### ExportOptionsGIF.colorCount

`exportOptionsGIF.colorCount`

**Description**

The number of colors in the exported image’s color table. Range: 2 to 256. Default: 128.

**Type**

Number (long).

---

<a id="jsobjref-exportoptionsgif-colordither"></a>

### ExportOptionsGIF.colorDither

`exportOptionsGIF.colorDither`

**Description**

The method used to dither colors in the exported image. Default: `ColorDitherMethod.DIFFUSION`.

**Type**

[ColorDitherMethod](scripting-constants.md#jsobjref-scripting-constants-colordithermethod)

---

<a id="jsobjref-exportoptionsgif-colorreduction"></a>

### ExportOptionsGIF.colorReduction

`exportOptionsGIF.colorReduction`

**Description**

The method used to reduce the number of colors in the exported image. `Default: ColorReductionMethod.SELECTIVE`.

**Type**

[ColorReductionMethod](scripting-constants.md#jsobjref-scripting-constants-colorreductionmethod)

---

<a id="jsobjref-exportoptionsgif-ditherpercent"></a>

### ExportOptionsGIF.ditherPercent

`exportOptionsGIF.ditherPercent`

**Description**

How much should the colors of the exported image be dithered, where 100.0 is 100%.

**Type**

Number (long).

---

<a id="jsobjref-exportoptionsgif-horizontalscale"></a>

### ExportOptionsGIF.horizontalScale

`exportOptionsGIF.horizontalScale`

**Description**

The horizontal scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsgif-infolosspercent"></a>

### ExportOptionsGIF.infoLossPercent

`exportOptionsGIF.infoLossPercent`

**Description**

The level of information loss allowed during compression, where 100.0 is 100%.

**Type**

Number (long).

---

<a id="jsobjref-exportoptionsgif-interlaced"></a>

### ExportOptionsGIF.interlaced

`exportOptionsGIF.interlaced`

**Description**

If `true`, the exported image should be interlaced. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-matte"></a>

### ExportOptionsGIF.matte

`exportOptionsGIF.matte`

**Description**

If `true`, the art board should be matted with a color. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-mattecolor"></a>

### ExportOptionsGIF.matteColor

`exportOptionsGIF.matteColor`

**Description**

The color to use when matting the art board. Default: `WHITE`.

**Type**

[RGBColor](RGBColor.md#jsobjref-rgbcolor)

---

<a id="jsobjref-exportoptionsgif-saveashtml"></a>

### ExportOptionsGIF.saveAsHTML

`exportOptionsGIF.saveAsHTML`

**Description**

If `true`, the exported image should be saved with an accompanying HTML file. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-transparency"></a>

### ExportOptionsGIF.transparency

`exportOptionsGIF.transparency`

**Description**

If `true`, the exported image should use transparency. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsgif-typename"></a>

### ExportOptionsGIF.typename

`exportOptionsGIF.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-exportoptionsgif-verticalscale"></a>

### ExportOptionsGIF.verticalScale

`exportOptionsGIF.verticalScale`

**Description**

The vertical scaling factor to apply to the exported image, where 100.0 is 100%. Default: 100.0.

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsgif-websnap"></a>

### ExportOptionsGIF.webSnap

`exportOptionsGIF.webSnap`

**Description**

Howmuchshouldthecolortablebechangedtomatch the web palette, where 100 is maximum. Default: 0.

**Type**

Number (long).

---

## Example

### Exporting to GIF format

```default
// Exports current document to dest as a GIF file with specified options,
// dest contains the full path including the file name

function exportToGIFFile(dest) {
  if (app.documents.length > 0) {
    var exportOptions = new ExportOptionsGIF();
    exportOptions.antiAliasing = false;
    exportOptions.colorCount = 64;
    exportOptions.colorDither = ColorDitherMethod.DIFFUSION;

    var type = ExportType.GIF;
    var fileSpec = new File(dest);

    app.activeDocument.exportFile(fileSpec, type, exportOptions);
  }
}
```
