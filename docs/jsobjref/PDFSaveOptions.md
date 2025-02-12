# PDFSaveOptions

`new PDFSaveOptions()`

#### Description

Options for saving a document as an Adobe PDF file, used with the [Document.saveAs()](Document.md#documentsave) method.

All properties are optional.

---

## Properties

### PDFSaveOptions.acrobatLayers

`pDFSaveOptions.acrobatLayers`

#### Description

Optional. Create Acrobat® layers from top-level layers. Acrobat 6 only.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.artboardRange

`pDFSaveOptions.artboardRange`

#### Description

Optional. This is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards.

Default: empty string

#### Type

String

---

### PDFSaveOptions.bleedLink

`pDFSaveOptions.bleedLink`

#### Description

Optional. Link 4 bleed values.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.bleedOffsetRect

`pDFSaveOptions.bleedOffsetRect`

#### Description

The bleed offset rectangle.

#### Type

Array of 4 numbers

---

### PDFSaveOptions.colorBars

`pDFSaveOptions.colorBars`

#### Description

Optional. Draw color bars.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.colorCompression

`pDFSaveOptions.colorCompression`

#### Description

Optional. The type of color bitmap compression used.

Default: `CompressionQuality.None`

#### Type

[CompressionQuality](scripting-constants.md#compressionquality)

---

### PDFSaveOptions.colorConversionID

`pDFSaveOptions.colorConversionID`

#### Description

Optional. The PDF color conversion policy.

Default: `ColorConversion.None`

#### Type

[ColorConversion](scripting-constants.md#colorconversion)

---

### PDFSaveOptions.colorDestinationID

`pDFSaveOptions.colorDestinationID`

#### Description

Optional. The conversion target for color conversion.

Default: `ColorDestination.None`

#### Type

[ColorDestination](scripting-constants.md#colordestination)

---

### PDFSaveOptions.colorDownsampling

`pDFSaveOptions.colorDownsampling`

#### Description

Optional. The color downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 150.0

#### Type

Number (double)

---

### PDFSaveOptions.colorDownsamplingImageThreshold

`pDFSaveOptions.colorDownsamplingImageThreshold`

#### Description

Optional. Downsample if the image's resolution is above this value.

Default: 225.0

#### Type

Number (double)

---

### PDFSaveOptions.colorDownsamplingMethod

`pDFSaveOptions.colorDownsamplingMethod`

#### Description

Optional. How color bitmap images should be resampled.

Default: `DownsampleMethod.NODOWNSAMPLE`

#### Type

[DownsampleMethod](scripting-constants.md#downsamplemethod)

---

### PDFSaveOptions.colorProfileID

`pDFSaveOptions.colorProfileID`

#### Description

Optional. The color profile to include.

Default: `ColorProfile.None`

#### Type

[ColorProfile](scripting-constants.md#colorprofile)

---

### PDFSaveOptions.colorTileSize

`pDFSaveOptions.colorTileSize`

#### Description

Optional. Tile size when compressing with JPEG2000.

Default: 256

#### Type

Number (long)

---

### PDFSaveOptions.compatibility

`pDFSaveOptions.compatibility`

#### Description

Optional. The version of the Acrobat file format to create.

Default: `PDFCompatibility.Acrobat5`

#### Type

[PDFCompatibility](scripting-constants.md#pdfcompatibility)

---

### PDFSaveOptions.compressArt

`pDFSaveOptions.compressArt`

#### Description

Optional. If `true`, the line art and text should be compressed.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.documentPassword

`pDFSaveOptions.documentPassword`

#### Description

Optional. A password string to open the document.

Default: no string

#### Type

String

---

### PDFSaveOptions.enableAccess

`pDFSaveOptions.enableAccess`

#### Description

Optional. If `true`, enable accessing 128-bit.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.enableCopy

`pDFSaveOptions.enableCopy`

#### Description

Optional. If `true`, enable copying of text 128-bit.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.enableCopyAccess

`pDFSaveOptions.enableCopyAccess`

#### Description

Optional. If `true`, enable copying and accessing 40-bit.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.enablePlainText

`pDFSaveOptions.enablePlainText`

#### Description

Optional. If `true`, enable plaintext metadata 128-bit. Available only for Acrobat 6.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.flattenerOptions

`pDFSaveOptions.flattenerOptions`

#### Description

Optional. The printing flattener options.

#### Type

[PrintFlattenerOptions](./PrintFlattenerOptions.md)

---

### PDFSaveOptions.flattenerPreset

`pDFSaveOptions.flattenerPreset`

#### Description

Optional. The transparency flattener preset name.

#### Type

String.

---

### PDFSaveOptions.fontSubsetThreshold

`pDFSaveOptions.fontSubsetThreshold`

#### Description

Optional. Include a subset of fonts when less than this percentage of characters is used in the document. Valid for Illustrator 9 file format.

Range: 0.0 to 100.0.

Default: 100.0

#### Type

Number (double)

---

### PDFSaveOptions.generateThumbnails

`pDFSaveOptions.generateThumbnails`

#### Description

Optional. If `true`, thumbnail images are generated with the saved file.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.grayscaleCompression

`pDFSaveOptions.grayscaleCompression`

#### Description

Optional. Quality of grayscale bitmap compression.

Default: `CompressionQuality.None`

#### Type

[CompressionQuality](scripting-constants.md#compressionquality)

---

### PDFSaveOptions.grayscaleDownsampling

`pDFSaveOptions.grayscaleDownsampling`

#### Description

Optional. Downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 150.0

#### Type

Number (double)

---

### PDFSaveOptions.grayscaleDownsamplingImageThreshold

`pDFSaveOptions.grayscaleDownsamplingImageThreshold`

#### Description

Optional. Downsample if the image's resolution is above this value.

Default: 225.0

#### Type

Number (double)

---

### PDFSaveOptions.grayscaleDownsamplingMethod

`pDFSaveOptions.grayscaleDownsamplingMethod`

#### Description

Optional. How grayscale bitmap images should be resampled

Default: `DownSampleMethod.NODOWNSAMPLE`

#### Type

[DownsampleMethod](scripting-constants.md#downsamplemethod)

---

### PDFSaveOptions.grayscaleTileSize

`pDFSaveOptions.grayscaleTileSize`

#### Description

Optional. Tile size when compressing with JPEG2000.

Default: 256

#### Type

Number (long)

---

### PDFSaveOptions.monochromeCompression

`pDFSaveOptions.monochromeCompression`

#### Description

Optional. Type of monochrome bitmap compression used.

Default: `MonochromeCompression.None`

#### Type

[MonochromeCompression](scripting-constants.md#monochromecompression)

---

### PDFSaveOptions.monochromeDownsampling

`pDFSaveOptions.monochromeDownsampling`

#### Description

Optional. Downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 300

#### Type

Number (double)

---

### PDFSaveOptions.monochromeDownsamplingImageThreshold

`pDFSaveOptions.monochromeDownsamplingImageThreshold`

#### Description

Optional. Downsample if the image's resolution is above this value.

Default: 450.0

#### Type

Number (double)

---

### PDFSaveOptions.monochromeDownsamplingMethod

`pDFSaveOptions.monochromeDownsamplingMethod`

#### Description

Optional. How monochrome bitmap images should be resampled.

Default: `DownSampleMethod.NODOWNSAMPLE`

#### Type

[DownsampleMethod](scripting-constants.md#downsamplemethod)

---

### PDFSaveOptions.offset

`pDFSaveOptions.offset`

#### Description

Optional. Custom offset in points for using the custom paper.

Default: 0.0

#### Type

Number (double)

---

### PDFSaveOptions.optimization

`pDFSaveOptions.optimization`

#### Description

Optional. If `true`, the PDF document should be optimized for fast web viewing.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.outputCondition

`pDFSaveOptions.outputCondition`

#### Description

Optional. An optional comment to add to the PDF file, describing the intended printing condition.

Default: not included

#### Type

String

---

### PDFSaveOptions.outputConditionID

`pDFSaveOptions.outputConditionID`

#### Description

Optional. The name of a registered printing condition.

Default: not included

#### Type

String

---

### PDFSaveOptions.pageInformation

`pDFSaveOptions.pageInformation`

#### Description

Optional. If `true`, raw page information.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.pageMarksType

`pDFSaveOptions.pageMarksType`

#### Description

Optional. The page marks style.

Default: PageMarksType.Roman

#### Type

[PageMarksTypes](scripting-constants.md#pagemarkstypes)

---

### PDFSaveOptions.pDFAllowPrinting

`pDFSaveOptions.pDFAllowPrinting`

#### Description

Optional. PDF security printing permission.

Default: `PDFPrintAllowedEnum.PRINT128HIGHRESOLUTION`

#### Type

[PDFPrintAllowedEnum](scripting-constants.md#pdfprintallowedenum)

---

### PDFSaveOptions.pDFChangesAllowed

`pDFSaveOptions.pDFChangesAllowed`

#### Description

Optional. Security changes allowed.

Default: `PDFChangeAllowedEnum.CHANGE128ANYCHANGES`

#### Type

[PDFChangesAllowedEnum](scripting-constants.md#pdfchangesallowedenum)

---

### PDFSaveOptions.pDFPreset

`pDFSaveOptions.pDFPreset`

#### Description

Optional. Name of PDF preset to use.

#### Type

String

---

### PDFSaveOptions.pDFXStandard

`pDFSaveOptions.pDFXStandard`

#### Description

Optional. The PDF standard with which this document complies.

Default: `PDFXStandard.PDFXNONE`

#### Type

[PDFXStandard](scripting-constants.md#pdfxstandard)

---

### PDFSaveOptions.pDFXStandardDescription

`pDFSaveOptions.pDFXStandardDescription`

#### Description

Optional. A description of the PDF standard from the selected preset.

#### Type

String

---

### PDFSaveOptions.permissionPassword

`pDFSaveOptions.permissionPassword`

#### Description

Optional. A password string to restrict editing security settings.

Default: no string

#### Type

String

---

### PDFSaveOptions.preserveEditability

`pDFSaveOptions.preserveEditability`

#### Description

Optional. If `true`, Illustrator editing capabilities should be preserved when saving the document.

Default: `true`

#### Type

Boolean

---

### PDFSaveOptions.printerResolution

`pDFSaveOptions.printerResolution`

#### Description

Optional. Flattening printer resolution.

Default: 800.0

#### Type

Number (double)

---

### PDFSaveOptions.registrationMarks

`pDFSaveOptions.registrationMarks`

#### Description

Optional. If `true`, draw registration marks.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.requireDocumentPassword

`pDFSaveOptions.requireDocumentPassword`

#### Description

Optional. Require a password to open the document.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.requirePermissionPassword

`pDFSaveOptions.requirePermissionPassword`

#### Description

Optional. Use a password to restrict editing security settings.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.trapped

`pDFSaveOptions.trapped`

#### Description

Optional. If `true`, manual trapping has been prepared for the document.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.trimMarks

`pDFSaveOptions.trimMarks`

#### Description

Optional. Draw trim marks.

Default: `false`

#### Type

Boolean

---

### PDFSaveOptions.trimMarkWeight

`pDFSaveOptions.trimMarkWeight`

#### Description

Optional. The trim mark weight.

Default: `PDFTrimMarkWeight.TRIMMARKWEIGHT0125`

#### Type

[PDFTrimMarkWeight](scripting-constants.md#pdftrimmarkweight)

---

### PDFSaveOptions.typename

`pDFSaveOptions.typename`

#### Description

Optional. Read-only. The class name of the referenced object.

#### Type

String

---

### PDFSaveOptions.viewAfterSaving

`pDFSaveOptions.viewAfterSaving`

#### Description

Optional. View PDF after saving.

Default: `false`

#### Type

Boolean

---

## Example

### Saving to PDF format

```javascript
// Saves the current document as PDF to dest with specified options
// dest contains the full path and file name to save to
function saveFileToPDF(dest) {
    var doc = app.activeDocument;

    if (app.documents.length > 0) {
        var saveName = new File(dest);
        saveOpts = new PDFSaveOptions();

        saveOpts.compatibility = PDFCompatibility.ACROBAT5;
        saveOpts.generateThumbnails = true;
        saveOpts.preserveEditability = true;

        doc.saveAs(saveName, saveOpts);
    }
}
```
