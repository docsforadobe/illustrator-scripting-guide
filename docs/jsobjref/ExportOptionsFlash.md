<a id="jsobjref-exportoptionsflash"></a>

# ExportOptionsFlash

`exportOptionsFlash`

**Description**

Options for exporting a document as a Macromedia® Flash® (SWF) file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method. All properties are optional.

When you export a document, the appropriate file extension is appended automatically. You should not include any file extension in the file specification.

---

## Properties

<a id="jsobjref-exportoptionsflash-artclipping"></a>

### ExportOptionsFlash.artClipping

`exportOptionsFlash.artClipping`

**Description**

How the art should be clipped during output. Default: `ArtClippingOption.OUTPUTARTBOUNDS`.

**Type**

[ArtClippingOption](scripting-constants.md#jsobjref-scripting-constants-artclippingoption)

---

<a id="jsobjref-exportoptionsflash-artboardrange"></a>

### ExportOptionsFlash.artboardRange

`exportOptionsFlash.artboardRange`

**Description**

If `saveMultipleArtboards` is `true`, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

---

<a id="jsobjref-exportoptionsflash-backgroundcolor"></a>

### ExportOptionsFlash.backgroundColor

`exportOptionsFlash.backgroundColor`

**Description**

The background color of the exported Flash frames.

**Type**

[RGBColor](RGBColor.md#jsobjref-rgbcolor)

---

<a id="jsobjref-exportoptionsflash-backgroundlayers"></a>

### ExportOptionsFlash.backgroundLayers

`exportOptionsFlash.backgroundLayers`

**Description**

A list of layers to be included as the static background of the exported Flash frames.

**Type**

Array of [Layers](Layers.md#jsobjref-layers)

---

<a id="jsobjref-exportoptionsflash-blendanimation"></a>

### ExportOptionsFlash.blendAnimation

`exportOptionsFlash.blendAnimation`

**Description**

The animation type for blended objects. Default: `BlendAnimationType.NOBLENDANIMATION`.

**Type**

[BlendAnimationType](scripting-constants.md#jsobjref-scripting-constants-blendanimationtype)

---

<a id="jsobjref-exportoptionsflash-compressed"></a>

### ExportOptionsFlash.compressed

`exportOptionsFlash.compressed`

**Description**

If `true`, the exported file should be exported compressed. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-converttexttooutlines"></a>

### ExportOptionsFlash.convertTextToOutlines

`exportOptionsFlash.convertTextToOutlines`

**Description**

If `true`, all text is converted to vector paths; preserves the visual appearance of type in all Flash players. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-curvequality"></a>

### ExportOptionsFlash.curveQuality

`exportOptionsFlash.curveQuality`

**Description**

The amount of curve information that should be presented. Default: 7.

**Type**

Number (long).

---

<a id="jsobjref-exportoptionsflash-exportallsymbols"></a>

### ExportOptionsFlash.exportAllSymbols

`exportOptionsFlash.exportAllSymbols`

**Description**

If `true`, export all symbols defined in the palette. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-exportstyle"></a>

### ExportOptionsFlash.exportStyle

`exportOptionsFlash.exportStyle`

**Description**

The style in which the exported data should be created in Flash. Default: `FlashExportStyle.ASFLASHFILE`.

**Type**

[FlashExportStyle](scripting-constants.md#jsobjref-scripting-constants-flashexportstyle)

---

<a id="jsobjref-exportoptionsflash-exportversion"></a>

### ExportOptionsFlash.exportVersion

`exportOptionsFlash.exportVersion`

**Description**

The version of the exported SWF file. Default: `FlashExportVersion.FlashVersion9`.

**Type**

[FlashExportVersion](scripting-constants.md#jsobjref-scripting-constants-flashexportversion)

---

<a id="jsobjref-exportoptionsflash-framerate"></a>

### ExportOptionsFlash.frameRate

`exportOptionsFlash.frameRate`

**Description**

The display rate in frames per second. Range: 0.01–120.0. Default: 12.0.

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsflash-ignoretextkerning"></a>

### ExportOptionsFlash.ignoreTextKerning

`exportOptionsFlash.ignoreTextKerning`

**Description**

If `true`, ignore kerning information in text objects. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-imageformat"></a>

### ExportOptionsFlash.imageFormat

`exportOptionsFlash.imageFormat`

**Description**

How should the image in the exported Flash file be compressed. Default: `FlashImageFormat.LOSSLESS`.

**Type**

[FlashImageFormat](scripting-constants.md#jsobjref-scripting-constants-flashimageformat)

---

<a id="jsobjref-exportoptionsflash-includemetadata"></a>

### ExportOptionsFlash.includeMetadata

`exportOptionsFlash.includeMetadata`

**Description**

If `true`, include minimal XMP metadata in the SWF file. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-jpegmethod"></a>

### ExportOptionsFlash.jpegMethod

`exportOptionsFlash.jpegMethod`

**Description**

Specifies the JPEG method to use. Default: `FlashJPEGMethod.Standard`.

**Type**

[FlashJPEGMethod](scripting-constants.md#jsobjref-scripting-constants-flashjpegmethod)

---

<a id="jsobjref-exportoptionsflash-jpegquality"></a>

### ExportOptionsFlash.jpegQuality

`exportOptionsFlash.jpegQuality`

**Description**

Level of compression to use. Range 1 to 10. Default: 3.

**Type**

Number (long).

---

<a id="jsobjref-exportoptionsflash-layerorder"></a>

### ExportOptionsFlash.layerOrder

`exportOptionsFlash.layerOrder`

**Description**

The order in which layers are exported to Flash frames. Default: `LayerOrderType.BOTTOMUP`.

**Type**

[LayerOrderType](scripting-constants.md#jsobjref-scripting-constants-layerordertype)

---

<a id="jsobjref-exportoptionsflash-looping"></a>

### ExportOptionsFlash.looping

`exportOptionsFlash.looping`

**Description**

If `true`, the Flash file is set to loop when run. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-playbackaccess"></a>

### ExportOptionsFlash.playbackAccess

`exportOptionsFlash.playbackAccess`

**Description**

The access level for the exported SWF file. Default: `FlashPlaybackSecurity.PlaybackLocal`.

**Type**

[FlashPlaybackSecurity](scripting-constants.md#jsobjref-scripting-constants-flashplaybacksecurity)

---

<a id="jsobjref-exportoptionsflash-preserveappearance"></a>

### ExportOptionsFlash.preserveAppearance

`exportOptionsFlash.preserveAppearance`

**Description**

If `true`, preserve appearance. If `false`, preserve editability. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-readonly"></a>

### ExportOptionsFlash.readOnly

`exportOptionsFlash.readOnly`

**Description**

If `true`, export as read-only file. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-replacing"></a>

### ExportOptionsFlash.replacing

`exportOptionsFlash.replacing`

**Description**

If a file with the same name already exists, should it be replaced. Default: `SaveOptions.PROMPTTOSAVECHANGES`.

**Type**

[SaveOptions](scripting-constants.md#jsobjref-scripting-constants-saveoptions)

---

<a id="jsobjref-exportoptionsflash-resolution"></a>

### ExportOptionsFlash.resolution

`exportOptionsFlash.resolution`

**Description**

The resolution in pixels per inch. Range: 72–2400. Default: 72.

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsflash-savemultipleartboards"></a>

### ExportOptionsFlash.saveMultipleArtboards

`exportOptionsFlash.saveMultipleArtboards`

**Description**

If `true`, all artboards or range of artboards are saved. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsflash-typename"></a>

### ExportOptionsFlash.typename

`exportOptionsFlash.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Example

### Exporting to Flash format

```default
// Exports current document to destFile as a flash file with specified options,
// destFile contains the full path including the file name

function exportToFlashFile(destFile) {
  if (app.documents.length > 0) {
    var exportOptions = new ExportOptionsFlash();
    exportOptions.resolution = 150;

    var type = ExportType.FLASH;
    var fileSpec = new File(destFile);

    app.activeDocument.exportFile(fileSpec, type, exportOptions);
  }
}
```
