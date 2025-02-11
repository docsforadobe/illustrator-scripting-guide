<a id="jsobjref-pdfsaveoptions"></a>

# PDFSaveOptions

`new PDFSaveOptions()`

**Description**

Options for saving a document as an Adobe PDF file, used with the [Document.saveAs()](Document.md#jsobjref-document-saveas) method.

All properties are optional.

---

## Properties

<a id="jsobjref-pdfsaveoptions-acrobatlayers"></a>

### PDFSaveOptions.acrobatLayers

`pDFSaveOptions.acrobatLayers`

**Description**

Optional. Create Acrobat® layers from top-level layers. Acrobat 6 only.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-artboardrange"></a>

### PDFSaveOptions.artboardRange

`pDFSaveOptions.artboardRange`

**Description**

Optional. This is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards.

Default: empty string

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-bleedlink"></a>

### PDFSaveOptions.bleedLink

`pDFSaveOptions.bleedLink`

**Description**

Optional. Link 4 bleed values.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-bleedoffsetrect"></a>

### PDFSaveOptions.bleedOffsetRect

`pDFSaveOptions.bleedOffsetRect`

**Description**

The bleed offset rectangle.

**Type**

Array of 4 numbers

---

<a id="jsobjref-pdfsaveoptions-colorbars"></a>

### PDFSaveOptions.colorBars

`pDFSaveOptions.colorBars`

**Description**

Optional. Draw color bars.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-colorcompression"></a>

### PDFSaveOptions.colorCompression

`pDFSaveOptions.colorCompression`

**Description**

Optional. The type of color bitmap compression used.

Default: `CompressionQuality.None`

**Type**

[CompressionQuality](scripting-constants.md#jsobjref-scripting-constants-compressionquality)

---

<a id="jsobjref-pdfsaveoptions-colorconversionid"></a>

### PDFSaveOptions.colorConversionID

`pDFSaveOptions.colorConversionID`

**Description**

Optional. The PDF color conversion policy.

Default: `ColorConversion.None`

**Type**

[ColorConversion](scripting-constants.md#jsobjref-scripting-constants-colorconversion)

---

<a id="jsobjref-pdfsaveoptions-colordestinationid"></a>

### PDFSaveOptions.colorDestinationID

`pDFSaveOptions.colorDestinationID`

**Description**

Optional. The conversion target for color conversion.

Default: `ColorDestination.None`

**Type**

[ColorDestination](scripting-constants.md#jsobjref-scripting-constants-colordestination)

---

<a id="jsobjref-pdfsaveoptions-colordownsampling"></a>

### PDFSaveOptions.colorDownsampling

`pDFSaveOptions.colorDownsampling`

**Description**

Optional. The color downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 150.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-colordownsamplingimagethreshold"></a>

### PDFSaveOptions.colorDownsamplingImageThreshold

`pDFSaveOptions.colorDownsamplingImageThreshold`

**Description**

Optional. Downsample if the image’s resolution is above  this value.

Default: 225.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-colordownsamplingmethod"></a>

### PDFSaveOptions.colorDownsamplingMethod

`pDFSaveOptions.colorDownsamplingMethod`

**Description**

Optional. How color bitmap images should be resampled.

Default: `DownsampleMethod.NODOWNSAMPLE`

**Type**

[DownsampleMethod](scripting-constants.md#jsobjref-scripting-constants-downsamplemethod)

---

<a id="jsobjref-pdfsaveoptions-colorprofileid"></a>

### PDFSaveOptions.colorProfileID

`pDFSaveOptions.colorProfileID`

**Description**

Optional. The color profile to include.

Default: `ColorProfile.None`

**Type**

[ColorProfile](scripting-constants.md#jsobjref-scripting-constants-colorprofile)

---

<a id="jsobjref-pdfsaveoptions-colortilesize"></a>

### PDFSaveOptions.colorTileSize

`pDFSaveOptions.colorTileSize`

**Description**

Optional. Tile size when compressing with JPEG2000.

Default: 256

**Type**

Number (long)

---

<a id="jsobjref-pdfsaveoptions-compatibility"></a>

### PDFSaveOptions.compatibility

`pDFSaveOptions.compatibility`

**Description**

Optional. The version of the Acrobat file format to create.

Default: `PDFCompatibility.Acrobat5`

**Type**

[PDFCompatibility](scripting-constants.md#jsobjref-scripting-constants-pdfcompatibility)

---

<a id="jsobjref-pdfsaveoptions-compressart"></a>

### PDFSaveOptions.compressArt

`pDFSaveOptions.compressArt`

**Description**

Optional. If `true`, the line art and text should be compressed.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-documentpassword"></a>

### PDFSaveOptions.documentPassword

`pDFSaveOptions.documentPassword`

**Description**

Optional. A password string to open the document.

Default: no string

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-enableaccess"></a>

### PDFSaveOptions.enableAccess

`pDFSaveOptions.enableAccess`

**Description**

Optional. If `true`, enable accessing 128-bit.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-enablecopy"></a>

### PDFSaveOptions.enableCopy

`pDFSaveOptions.enableCopy`

**Description**

Optional. If `true`, enable copying of text 128-bit.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-enablecopyaccess"></a>

### PDFSaveOptions.enableCopyAccess

`pDFSaveOptions.enableCopyAccess`

**Description**

Optional. If `true`, enable copying and accessing 40-bit.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-enableplaintext"></a>

### PDFSaveOptions.enablePlainText

`pDFSaveOptions.enablePlainText`

**Description**

Optional. If `true`, enable plaintext metadata 128-bit. Available only for Acrobat 6.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-flatteneroptions"></a>

### PDFSaveOptions.flattenerOptions

`pDFSaveOptions.flattenerOptions`

**Description**

Optional. The printing flattener options.

**Type**

[PrintFlattenerOptions](PrintFlattenerOptions.md#jsobjref-printflatteneroptions)

---

<a id="jsobjref-pdfsaveoptions-flattenerpreset"></a>

### PDFSaveOptions.flattenerPreset

`pDFSaveOptions.flattenerPreset`

**Description**

Optional. The transparency flattener preset name.

**Type**

String.

---

<a id="jsobjref-pdfsaveoptions-fontsubsetthreshold"></a>

### PDFSaveOptions.fontSubsetThreshold

`pDFSaveOptions.fontSubsetThreshold`

**Description**

Optional. Include a subset of fonts when less than this percentage of characters is used in the document. Valid for Illustrator 9 file format. Range: 0.0 to 100.0.

Default: 100.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-generatethumbnails"></a>

### PDFSaveOptions.generateThumbnails

`pDFSaveOptions.generateThumbnails`

**Description**

Optional. If `true`, thumbnail images are generated with the saved file.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-grayscalecompression"></a>

### PDFSaveOptions.grayscaleCompression

`pDFSaveOptions.grayscaleCompression`

**Description**

Optional. Quality of grayscale bitmap compression.

Default: `CompressionQuality.None`

**Type**

[CompressionQuality](scripting-constants.md#jsobjref-scripting-constants-compressionquality)

---

<a id="jsobjref-pdfsaveoptions-grayscaledownsampling"></a>

### PDFSaveOptions.grayscaleDownsampling

`pDFSaveOptions.grayscaleDownsampling`

**Description**

Optional. Downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 150.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-grayscaledownsamplingimagethreshold"></a>

### PDFSaveOptions.grayscaleDownsamplingImageThreshold

`pDFSaveOptions.grayscaleDownsamplingImageThreshold`

**Description**

Optional. Downsample if the image’s resolution is above this value.

Default: 225.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-grayscaledownsamplingmethod"></a>

### PDFSaveOptions.grayscaleDownsamplingMethod

`pDFSaveOptions.grayscaleDownsamplingMethod`

**Description**

Optional. How grayscale bitmap images should be resampled

Default: `DownSampleMethod.NODOWNSAMPLE`

**Type**

[DownsampleMethod](scripting-constants.md#jsobjref-scripting-constants-downsamplemethod)

---

<a id="jsobjref-pdfsaveoptions-grayscaletilesize"></a>

### PDFSaveOptions.grayscaleTileSize

`pDFSaveOptions.grayscaleTileSize`

**Description**

Optional. Tile size when compressing with JPEG2000.

Default: 256

**Type**

Number (long)

---

<a id="jsobjref-pdfsaveoptions-monochromecompression"></a>

### PDFSaveOptions.monochromeCompression

`pDFSaveOptions.monochromeCompression`

**Description**

Optional. Type of monochrome bitmap compression used.

Default: `MonochromeCompression.None`

**Type**

[MonochromeCompression](scripting-constants.md#jsobjref-scripting-constants-monochromecompression)

---

<a id="jsobjref-pdfsaveoptions-monochromedownsampling"></a>

### PDFSaveOptions.monochromeDownsampling

`pDFSaveOptions.monochromeDownsampling`

**Description**

Optional. Downsampling resolution in dots per inch (dpi). If 0, no downsampling is performed.

Default: 300

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-monochromedownsamplingimagethreshold"></a>

### PDFSaveOptions.monochromeDownsamplingImageThreshold

`pDFSaveOptions.monochromeDownsamplingImageThreshold`

**Description**

Optional. Downsample if the image’s resolution is above  this value.

Default: 450.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-monochromedownsamplingmethod"></a>

### PDFSaveOptions.monochromeDownsamplingMethod

`pDFSaveOptions.monochromeDownsamplingMethod`

**Description**

Optional. How monochrome bitmap images should be resampled.

Default: `DownSampleMethod.NODOWNSAMPLE`

**Type**

[DownsampleMethod](scripting-constants.md#jsobjref-scripting-constants-downsamplemethod)

---

<a id="jsobjref-pdfsaveoptions-offset"></a>

### PDFSaveOptions.offset

`pDFSaveOptions.offset`

**Description**

Optional. Custom offset in points for using the custom paper.

Default: 0.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-optimization"></a>

### PDFSaveOptions.optimization

`pDFSaveOptions.optimization`

**Description**

Optional. If `true`, the PDF document should be optimized for fast web viewing.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-outputcondition"></a>

### PDFSaveOptions.outputCondition

`pDFSaveOptions.outputCondition`

**Description**

Optional. An optional comment to add to the PDF file, describing the intended printing condition.

Default: not included

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-outputconditionid"></a>

### PDFSaveOptions.outputConditionID

`pDFSaveOptions.outputConditionID`

**Description**

Optional. The name of a registered printing condition.

Default: not included

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-pageinformation"></a>

### PDFSaveOptions.pageInformation

`pDFSaveOptions.pageInformation`

**Description**

Optional. If `true`, raw page information.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-pagemarkstype"></a>

### PDFSaveOptions.pageMarksType

`pDFSaveOptions.pageMarksType`

**Description**

Optional. The page marks style.

Default: PageMarksType.Roman

**Type**

[PageMarksTypes](scripting-constants.md#jsobjref-scripting-constants-pagemarkstypes)

---

<a id="jsobjref-pdfsaveoptions-pdfallowprinting"></a>

### PDFSaveOptions.pDFAllowPrinting

`pDFSaveOptions.pDFAllowPrinting`

**Description**

Optional. PDF security printing permission.

Default: `PDFPrintAllowedEnum.PRINT128HIGHRESOLUTION`

**Type**

[PDFPrintAllowedEnum](scripting-constants.md#jsobjref-scripting-constants-pdfprintallowedenum)

---

<a id="jsobjref-pdfsaveoptions-pdfchangesallowed"></a>

### PDFSaveOptions.pDFChangesAllowed

`pDFSaveOptions.pDFChangesAllowed`

**Description**

Optional. Security changes allowed.

Default: `PDFChangeAllowedEnum.CHANGE128ANYCHANGES`

**Type**

[PDFChangesAllowedEnum](scripting-constants.md#jsobjref-scripting-constants-pdfchangesallowedenum)

---

<a id="jsobjref-pdfsaveoptions-pdfpreset"></a>

### PDFSaveOptions.pDFPreset

`pDFSaveOptions.pDFPreset`

**Description**

Optional. Name of PDF preset to use.

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-pdfxstandard"></a>

### PDFSaveOptions.pDFXStandard

`pDFSaveOptions.pDFXStandard`

**Description**

Optional. The PDF standard with which this document complies.

Default: `PDFXStandard.PDFXNONE`

**Type**

[PDFXStandard](scripting-constants.md#jsobjref-scripting-constants-pdfxstandard)

---

<a id="jsobjref-pdfsaveoptions-pdfxstandarddescription"></a>

### PDFSaveOptions.pDFXStandardDescription

`pDFSaveOptions.pDFXStandardDescription`

**Description**

Optional. A description of the PDF standard from the selected preset.

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-permissionpassword"></a>

### PDFSaveOptions.permissionPassword

`pDFSaveOptions.permissionPassword`

**Description**

Optional. A password string to restrict editing security settings.

Default: no string

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-preserveeditability"></a>

### PDFSaveOptions.preserveEditability

`pDFSaveOptions.preserveEditability`

**Description**

Optional. If `true`, Illustrator editing capabilities should be preserved when saving the document.

Default: `true`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-printerresolution"></a>

### PDFSaveOptions.printerResolution

`pDFSaveOptions.printerResolution`

**Description**

Optional. Flattening printer resolution.

Default: 800.0

**Type**

Number (double)

---

<a id="jsobjref-pdfsaveoptions-registrationmarks"></a>

### PDFSaveOptions.registrationMarks

`pDFSaveOptions.registrationMarks`

**Description**

Optional. If `true`, draw registration marks.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-requiredocumentpassword"></a>

### PDFSaveOptions.requireDocumentPassword

`pDFSaveOptions.requireDocumentPassword`

**Description**

Optional. Require a password to open the document.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-requirepermissionpassword"></a>

### PDFSaveOptions.requirePermissionPassword

`pDFSaveOptions.requirePermissionPassword`

**Description**

Optional. Use a password to restrict editing security settings.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-trapped"></a>

### PDFSaveOptions.trapped

`pDFSaveOptions.trapped`

**Description**

Optional. If `true`, manual trapping has been prepared for the document.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-trimmarks"></a>

### PDFSaveOptions.trimMarks

`pDFSaveOptions.trimMarks`

**Description**

Optional. Draw trim marks.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pdfsaveoptions-trimmarkweight"></a>

### PDFSaveOptions.trimMarkWeight

`pDFSaveOptions.trimMarkWeight`

**Description**

Optional. The trim mark weight.

Default: `PDFTrimMarkWeight.TRIMMARKWEIGHT0125`

**Type**

[PDFTrimMarkWeight](scripting-constants.md#jsobjref-scripting-constants-pdftrimmarkweight)

---

<a id="jsobjref-pdfsaveoptions-typename"></a>

### PDFSaveOptions.typename

`pDFSaveOptions.typename`

**Description**

Optional. Read-only. The class name of the referenced object.

**Type**

String

---

<a id="jsobjref-pdfsaveoptions-viewaftersaving"></a>

### PDFSaveOptions.viewAfterSaving

`pDFSaveOptions.viewAfterSaving`

**Description**

Optional. View PDF after saving.

Default: `false`

**Type**

Boolean

---

## Example

### Saving to PDF format

```default
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
