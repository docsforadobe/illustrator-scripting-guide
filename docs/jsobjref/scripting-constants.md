<a id="jsobjref-scripting-constants"></a>

# Scripting Constants

This chapter lists and describes the enumerations defined for use with Illustrator JavaScript properties and methods.

---

<a id="jsobjref-scripting-constants-alternateglyphsform"></a>

## AlternateGlyphsForm

The alternate glyphs form of text.

| Value                                   | Description        |
|-----------------------------------------|--------------------|
| `AlternateGlyphsForm.DEFAULTFORM`       | Defaultform        |
| `AlternateGlyphsForm.TRADITIONAL`       | Traditional        |
| `AlternateGlyphsForm.EXPERT`            | Expert             |
| `AlternateGlyphsForm.JIS78FORM`         | JIS78FORM          |
| `AlternateGlyphsForm.JIS83FORM`         | JIS83FORM          |
| `AlternateGlyphsForm.HALFWIDTH`         | Half Width         |
| `AlternateGlyphsForm.THIRDWIDTH`        | Third Width        |
| `AlternateGlyphsForm.QUARTERWIDTH`      | Quarter Width      |
| `AlternateGlyphsForm.FULLWIDTH`         | Full Width         |
| `AlternateGlyphsForm.PROPORTIONALWIDTH` | Proportional Width |
| `AlternateGlyphsForm.JIS90FORM`         | JIS90FORM          |
| `AlternateGlyphsForm.JIS04FORM`         | JIS04FORM          |

**Example**

```default
textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.DEFAULTFORM;
textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.FULLWIDTH
```

---

<a id="jsobjref-scripting-constants-antialiasingmethod"></a>

## AntiAliasingMethod

The type of antialiasing method used in the rasterization.

| Value                              | Description                   |
|------------------------------------|-------------------------------|
| `AntiAliasingMethod.None`          | No antialiasing is allowed.   |
| `AntiAliasingMethod.ARTOPTIMIZED`  | Optimize for the art object.  |
| `AntiAliasingMethod.TYPEOPTIMIZED` | Optimize for the type object. |

---

<a id="jsobjref-scripting-constants-artclippingoption"></a>

## ArtClippingOption

How the art should be clipped during output.

| Value                                    | Description                               |
|------------------------------------------|-------------------------------------------|
| `ArtClippingOption.OUTPUTARTBOUNDS`      | Output size is the size of the artwork.   |
| `ArtClippingOption.OUTPUTARTBOARDBOUNDS` | Output size is the size of the artboard.  |
| `ArtClippingOption.OUTPUTCROPRECTBOUNDS` | Output size is the size of the crop area. |

---

<a id="jsobjref-scripting-constants-autocadcolors"></a>

## AutoCADColors

| Value                        | Description    |
|------------------------------|----------------|
| `AutoCADColors.Max8Colors`   | Max 8 CColors  |
| `AutoCADColors.Max16Colors`  | Max 16 Colors  |
| `AutoCADColors.Max256Colors` | Max 25 6Colors |
| `AutoCADColors.TrueColors`   | True Colors    |

---

<a id="jsobjref-scripting-constants-autocadcompatibility"></a>

## AutoCADCompatibility

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `AutoCADCompatibility.AutoCADRelease13` | Release 13    |
| `AutoCADCompatibility.AutoCADRelease18` | Release 18    |
| `AutoCADCompatibility.AutoCADRelease14` | Release 14    |
| `AutoCADCompatibility.AutoCADRelease21` | Release 21    |
| `AutoCADCompatibility.AutoCADRelease15` | Release 15    |
| `AutoCADCompatibility.AutoCADRelease24` | Release 24    |

---

<a id="jsobjref-scripting-constants-autocadexportfileformat"></a>

## AutoCADExportFileFormat

| Value                         | Description   |
|-------------------------------|---------------|
| `AutoCADExportFileFormat.DXF` | DXF           |
| `AutoCADExportFileFormat.DWG` | DWG           |

---

<a id="jsobjref-scripting-constants-autocadexportoption"></a>

## AutoCADExportOption

| Value                                     | Description          |
|-------------------------------------------|----------------------|
| `AutoCADExportOption.PreserveAppearance`  | Preserve Appearance  |
| `AutoCADExportOption.MaximizeEditability` | Maximize Editability |

---

<a id="jsobjref-scripting-constants-autocadglobalscaleoption"></a>

## AutoCADGlobalScaleOption

| Value                                   | Description    |
|-----------------------------------------|----------------|
| `AutoCADGlobalScaleOption.OriginalSize` | Original Size  |
| `AutoCADGlobalScaleOption.ScaleByValue` | Scale by Value |
| `AutoCADGlobalScaleOption.FitArtboard`  | Fit Artboard   |

---

<a id="jsobjref-scripting-constants-autocadrasterformat"></a>

## AutoCADRasterFormat

| Value                      | Description   |
|----------------------------|---------------|
| `AutoCADRasterFormat.PNG`  | PNG           |
| `AutoCADRasterFormat.JPEG` | JPEG          |

---

<a id="jsobjref-scripting-constants-autocadunit"></a>

## AutoCADUnit

| Value                     | Description   |
|---------------------------|---------------|
| `AutoCADUnit.Points`      | Points        |
| `AutoCADUnit.Picas`       | Picas         |
| `AutoCADUnit.Inches`      | Inches        |
| `AutoCADUnit.Millimeters` | Millimeters   |
| `AutoCADUnit.Centimeters` | Centimeters   |
| `AutoCADUnit.Pixels`      | Pixels        |

---

<a id="jsobjref-scripting-constants-autokerntype"></a>

## AutoKernType

The auto kern type.

| Value                           | Description   |
|---------------------------------|---------------|
| `AutoKernType.NOAUTOKERN`       | None          |
| `AutoKernType.AUTO`             | Auto          |
| `AutoKernType.OPTICAL`          | Optical       |
| `AutoKernType.METRICSROMANONLY` | Metrics       |

---

<a id="jsobjref-scripting-constants-autoleadingtype"></a>

## AutoLeadingType

The auto leading type.

| Value                            | Description      |
|----------------------------------|------------------|
| `AutoLeadingType.BOTTOMTOBOTTOM` | Bottom to Bottom |
| `AutoLeadingType.TOPTOTOP`       | Top to Top       |

---

<a id="jsobjref-scripting-constants-baselinedirectiontype"></a>

## BaselineDirectionType

The baseline direction type.

| Value                                   | Description      |
|-----------------------------------------|------------------|
| `BaselineDirectionType.Standard`        | Standard         |
| `BaselineDirectionType.VerticalRotated` | Vertical Rotated |
| `BaselineDirectionType.TateChuYoko`     | TateChuYoko      |

---

<a id="jsobjref-scripting-constants-blendanimationtype"></a>

## BlendAnimationType

| Value                                 | Description   |
|---------------------------------------|---------------|
| `BlendAnimationType.INBUILD`          | In Build      |
| `BlendAnimationType.NOBLENDANIMATION` | None          |
| `BlendAnimationType.INSEQUENCE`       | In Sequence   |

---

<a id="jsobjref-scripting-constants-blendmodes"></a>

## BlendModes

The blend mode used when compositing an object.

| Value                        | Description   |
|------------------------------|---------------|
| `BlendModes.COLORBLEND`      | Color         |
| `BlendModes.COLORBURN`       | Color Burn    |
| `BlendModes.COLORDODGE`      | Color Dodge   |
| `BlendModes.DARKEN`          | Darken        |
| `BlendModes.DIFFERENCE`      | Difference    |
| `BlendModes.EXCLUSION`       | Exclusion     |
| `BlendModes.HARDLIGHT`       | Hard Light    |
| `BlendModes.HUE`             | Hue           |
| `BlendModes.LIGHTEN`         | Lighten       |
| `BlendModes.LUMINOSITY`      | Luminosity    |
| `BlendModes.MULTIPLY`        | Multiply      |
| `BlendModes.NORMAL`          | Normal        |
| `BlendModes.OVERLAY`         | Overlay       |
| `BlendModes.SATURATIONBLEND` | Saturation    |
| `BlendModes.SCREEN`          | Screen        |
| `BlendModes.SOFTLIGHT`       | Soft Light    |

---

<a id="jsobjref-scripting-constants-blendsexpandpolicy"></a>

## BlendsExpandPolicy

Policy used by FXG file format to expand blends.

| Value                                           | Description                  |
|-------------------------------------------------|------------------------------|
| `BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS` | Automatically convert blends |
| `BlendsExpandPolicy.RASTERIZEBLENDS`            | Rasterize blends             |

---

<a id="jsobjref-scripting-constants-burasagaritypeenum"></a>

## BurasagariTypeEnum

The Burasagari type.

| Value                         | Description   |
|-------------------------------|---------------|
| `BurasagariTypeEnum.Forced`   | Forced        |
| `BurasagariTypeEnum.None`     | None          |
| `BurasagariTypeEnum.Standard` | Standard      |

---

<a id="jsobjref-scripting-constants-casechangetype"></a>

## CaseChangeType

The case change type.

| Value                         | Description                     |
|-------------------------------|---------------------------------|
| `CaseChangeType.LOWERCASE`    | Lowercase (`"hello world"`)     |
| `CaseChangeType.SENTENCECASE` | Sentence case (`"Hello world"`) |
| `CaseChangeType.TITLECASE`    | Title case (`"Hello World"`)    |
| `CaseChangeType.UPPERCASE`    | Uppercase (`"HELLO WORLD"`)     |

---

<a id="jsobjref-scripting-constants-colorconversion"></a>

## ColorConversion

The color conversion policy.

| Value                                      | Description                |
|--------------------------------------------|----------------------------|
| `ColorConversion.COLORCONVERSIONREPURPOSE` | Color Conversion Repurpose |
| `ColorConversion.COLORCONVERSIONTODEST`    | Color Conversion to Dest   |
| `ColorConversion.None`                     | None                       |

---

<a id="jsobjref-scripting-constants-colorconvertpurpose"></a>

## ColorConvertPurpose

The purpose of color conversion using the `ConvertSampleColor` method of the `Application` class.

| Value                                | Description   |
|--------------------------------------|---------------|
| `ColorConvertPurpose.defaultpurpose` | Default       |
| `ColorConvertPurpose.exportpurpose`  | Export        |
| `ColorConvertPurpose.previewpurpose` | Preview       |
| `ColorConvertPurpose.dummypurpose`   | Dummy         |

---

<a id="jsobjref-scripting-constants-colordestination"></a>

## ColorDestination

Destination profile

| Value                                          | Description   |
|------------------------------------------------|---------------|
| `ColorDestination.COLORDESTINATIONDOCCMYK`     | Doc CMYK      |
| `ColorDestination.COLORDESTINATIONDOCRGB`      | Doc RGB       |
| `ColorDestination.COLORDESTINATIONPROFILE`     | Profile       |
| `ColorDestination.COLORDESTINATIONWORKINGCMYK` | Working CMYK  |
| `ColorDestination.COLORDESTINATIONWORKINGRGB`  | Working RGB   |
| `ColorDestination.None`                        | None          |

---

<a id="jsobjref-scripting-constants-colordithermethod"></a>

## ColorDitherMethod

The method used to dither colors in exported GIF and PNG8 images.

| Value                             | Description    |
|-----------------------------------|----------------|
| `ColorDitherMethod.DIFFUSION`     | Diffusion      |
| `ColorDitherMethod.NOISE`         | Noise          |
| `ColorDitherMethod.NOREDUCTION`   | No Reduction   |
| `ColorDitherMethod.PATTERNDITHER` | Pattern Dither |

---

<a id="jsobjref-scripting-constants-colormodel"></a>

## ColorModel

The color model to use.

| Value                     | Description   |
|---------------------------|---------------|
| `ColorModel.PROCESS`      | Process       |
| `ColorModel.REGISTRATION` | Registration  |
| `ColorModel.SPOT`         | Spot          |

---

<a id="jsobjref-scripting-constants-colorprofile"></a>

## ColorProfile

| Value                                | Description             |
|--------------------------------------|-------------------------|
| `ColorProfile.INCLUDEALLPROFILE`     | Include All Profile     |
| `ColorProfile.INCLUDEDESTPROFILE`    | Include Dest Profile    |
| `ColorProfile.INCLUDERGBPROFILE`     | Include RGB Profile     |
| `ColorProfile.LEAVEPROFILEUNCHANGED` | Leave Profile Unchanged |
| `ColorProfile.None`                  | None                    |

---

<a id="jsobjref-scripting-constants-colorreductionmethod"></a>

## ColorReductionMethod

The method used to reduce the number of colors in exported GIF and PNG8 images.

| Value                             | Description   |
|-----------------------------------|---------------|
| `ColorReductionMethod.ADAPTIVE`   | Adaptive      |
| `ColorReductionMethod.SELECTIVE`  | Selective     |
| `ColorReductionMethod.PERCEPTUAL` | Perceptual    |
| `ColorReductionMethod.WEB`        | Web           |

---

<a id="jsobjref-scripting-constants-colortype"></a>

## ColorType

The color specification for an individual color.

| Value                | Description   |
|----------------------|---------------|
| `ColorType.CMYK`     | Cmyk          |
| `ColorType.GRADIENT` | Gradient      |
| `ColorType.GRAY`     | Gray          |
| `ColorType.PATTERN`  | Pattern       |
| `ColorType.RGB`      | Rgb           |
| `ColorType.SPOT`     | Spot          |
| `ColorType.NONE`     | None          |

---

<a id="jsobjref-scripting-constants-compatibility"></a>

## Compatibility

The version of the Illustrator file to create when saving an EPS or Illustrator file

| Value                            | Description        |
|----------------------------------|--------------------|
| `Compatibility.ILLUSTRATOR8`     | Illustrator 8      |
| `Compatibility.ILLUSTRATOR9`     | Illustrator 9      |
| `Compatibility.ILLUSTRATOR10`    | Illustrator 10     |
| `Compatibility.ILLUSTRATOR11`    | Illustrator 11     |
| `Compatibility.ILLUSTRATOR12`    | Illustrator 12     |
| `Compatibility.ILLUSTRATOR13`    | Illustrator 13     |
| `Compatibility.ILLUSTRATOR14`    | Illustrator 14     |
| `Compatibility.ILLUSTRATOR15`    | Illustrator 15     |
| `Compatibility.ILLUSTRATOR16`    | Illustrator 16     |
| `Compatibility.ILLUSTRATOR17`    | Illustrator 17     |
| `Compatibility.ILLUSTRATOR19`    | Illustrator 19     |
| `Compatibility.JAPANESEVERSION3` | Japanese Version 3 |

---

<a id="jsobjref-scripting-constants-compressionquality"></a>

## CompressionQuality

The quality of bitmap compression used when saving a PDF file

| Value                                          | Description   |
|------------------------------------------------|---------------|
| `CompressionQuality.AUTOMATICJPEG2000HIGH`     | todo          |
| `CompressionQuality.AUTOMATICJPEG2000LOSSLESS` | todo          |
| `CompressionQuality.AUTOMATICJPEG2000LOW`      | todo          |
| `CompressionQuality.AUTOMATICJPEG2000MAXIMUM`  | todo          |
| `CompressionQuality.AUTOMATICJPEG2000MEDIUM`   | todo          |
| `CompressionQuality.AUTOMATICJPEG2000MINIMUM`  | todo          |
| `CompressionQuality.AUTOMATICJPEGHIGH`         | todo          |
| `CompressionQuality.AUTOMATICJPEGLOW`          | todo          |
| `CompressionQuality.AUTOMATICJPEGMAXIMUM`      | todo          |
| `CompressionQuality.AUTOMATICJPEGMEDIUM`       | todo          |
| `CompressionQuality.AUTOMATICJPEGMINIMUM`      | todo          |
| `CompressionQuality.JPEG2000HIGH`              | todo          |
| `CompressionQuality.JPEG2000LOSSLESS`          | todo          |
| `CompressionQuality.JPEG2000LOW`               | todo          |
| `CompressionQuality.JPEG2000MAXIMUM`           | todo          |
| `CompressionQuality.JPEG2000MEDIUM`            | todo          |
| `CompressionQuality.JPEG2000MINIMUM`           | todo          |
| `CompressionQuality.JPEGHIGH`                  | todo          |
| `CompressionQuality.JPEGLOW`                   | todo          |
| `CompressionQuality.JPEGMAXIMUM`               | todo          |
| `CompressionQuality.JPEGMEDIUM`                | todo          |
| `CompressionQuality.JPEGMINIMUM`               | todo          |
| `CompressionQuality.ZIP4BIT`                   | todo          |
| `CompressionQuality.ZIP8BIT`                   | todo          |
| `CompressionQuality.None`                      | todo          |

---

<a id="jsobjref-scripting-constants-coordinatesystem"></a>

## CoordinateSystem

The coordinate system used by Illustrator

| Value                                       | Description   |
|---------------------------------------------|---------------|
| `CoordinateSystem.ARTBOARDCOORDINATESYSTEM` | todo          |
| `CoordinateSystem.DOCUMENTCOORDINATESYSTEM` | todo          |

---

<a id="jsobjref-scripting-constants-cropoptions"></a>

## CropOptions

The style of a document’s cropping box

| Value                  | Description   |
|------------------------|---------------|
| `CropOptions.Japanese` | Japanese      |
| `CropOptions.Standard` | Standard      |

---

<a id="jsobjref-scripting-constants-documentartboardlayout"></a>

## DocumentArtboardLayout

The layout of in the new document.

| Value                                | Description   |
|--------------------------------------|---------------|
| `DocumentArtboardLayout.Column`      | todo          |
| `DocumentArtboardLayout.GridByCol`   | todo          |
| `DocumentArtboardLayout.GridByRow`   | todo          |
| `DocumentArtboardLayout.RLGridByCol` | todo          |
| `DocumentArtboardLayout.RLGridByRow` | todo          |
| `DocumentArtboardLayout.RLRow`       | todo          |
| `DocumentArtboardLayout.Row`         | todo          |

---

<a id="jsobjref-scripting-constants-documentcolorspace"></a>

## DocumentColorSpace

The color space of a document

| Value                     | Description   |
|---------------------------|---------------|
| `DocumentColorSpace.CMYK` | CMYK          |
| `DocumentColorSpace.RGB`  | RGB           |

---

<a id="jsobjref-scripting-constants-documentlayoutstyle"></a>

## DocumentLayoutStyle

Layout style for the document

| Value                                | Description   |
|--------------------------------------|---------------|
| `DocumentLayoutStyle.CASCADE`        | todo          |
| `DocumentLayoutStyle.CONSOLIDATEALL` | todo          |
| `DocumentLayoutStyle.FLOATALL`       | todo          |
| `DocumentLayoutStyle.HORIZONTALTILE` | todo          |
| `DocumentLayoutStyle.VERTICALTILE`   | todo          |

---

<a id="jsobjref-scripting-constants-documentpresettype"></a>

## DocumentPresetType

The preset types available for new documents.

| Value                          | Description   |
|--------------------------------|---------------|
| `DocumentPresetType.BasicCMYK` | Basic CMYK    |
| `DocumentPresetType.BasicRGB`  | Basic RGB     |
| `DocumentPresetType.Mobile`    | Mobile        |
| `DocumentPresetType.Print`     | Print         |
| `DocumentPresetType.Video`     | Video         |
| `DocumentPresetType.Web`       | Web           |

---

<a id="jsobjref-scripting-constants-documentpreviewmode"></a>

## DocumentPreviewMode

The document preview mode.

| Value                                  | Description   |
|----------------------------------------|---------------|
| `DocumentPreviewMode.DefaultPreview`   | Default       |
| `DocumentPreviewMode.OverprintPreview` | Overprint     |
| `DocumentPreviewMode.PixelPreview`     | Pixel         |

---

<a id="jsobjref-scripting-constants-documentrasterresolution"></a>

## DocumentRasterResolution

The preset document raster resolution.

| Value                                       | Description       |
|---------------------------------------------|-------------------|
| `DocumentRasterResolution.ScreenResolution` | Screen Resolution |
| `DocumentRasterResolution.HighResolution`   | High Resolution   |
| `DocumentRasterResolution.MediumResolution` | Medium Resolution |

---

<a id="jsobjref-scripting-constants-documenttransparencygrid"></a>

## DocumentTransparencyGrid

Document transparency grid colors.

| Value                                             | Description   |
|---------------------------------------------------|---------------|
| `DocumentTransparencyGrid.TransparencyGridBlue`   | Blue          |
| `DocumentTransparencyGrid.TransparencyGridDark`   | Dark          |
| `DocumentTransparencyGrid.TransparencyGridGreen`  | Green         |
| `DocumentTransparencyGrid.TransparencyGridLight`  | Light         |
| `DocumentTransparencyGrid.TransparencyGridMedium` | Medium        |
| `DocumentTransparencyGrid.TransparencyGridNone`   | None          |
| `DocumentTransparencyGrid.TransparencyGridOrange` | Orange        |
| `DocumentTransparencyGrid.TransparencyGridPurple` | Purple        |
| `DocumentTransparencyGrid.TransparencyGridRed`    | Red           |

---

<a id="jsobjref-scripting-constants-documenttype"></a>

## DocumentType

The file format used to save a file.

| Value                      | Description   |
|----------------------------|---------------|
| `DocumentType.EPS`         | EPS           |
| `DocumentType.FXG`         | FXG           |
| `DocumentType.ILLUSTRATOR` | Illustrator   |
| `DocumentType.PDF`         | PDF           |

---

<a id="jsobjref-scripting-constants-downsamplemethod"></a>

## DownsampleMethod

| Value                                | Description        |
|--------------------------------------|--------------------|
| `DownsampleMethod.AVERAGEDOWNSAMPLE` | Average Downsample |
| `DownsampleMethod.BICUBICDOWNSAMPLE` | Bicubic Downsample |
| `DownsampleMethod.NODOWNSAMPLE`      | No Downsample      |
| `DownsampleMethod.SUBSAMPLE`         | Subsample          |

---

<a id="jsobjref-scripting-constants-elementplacement"></a>

## ElementPlacement

| Value                               | Description        |
|-------------------------------------|--------------------|
| `ElementPlacement.INSIDE`           | Inside             |
| `ElementPlacement.PLACEAFTER`       | Place After        |
| `ElementPlacement.PLACEATBEGINNING` | Place At Beginning |
| `ElementPlacement.PLACEATEND`       | Place At End       |
| `ElementPlacement.PLACEBEFORE`      | Place Before       |

---

<a id="jsobjref-scripting-constants-epspostscriptlevelenum"></a>

## EPSPostScriptLevelEnum

| Value                           | Description   |
|---------------------------------|---------------|
| `EPSPostScriptLevelEnum.LEVEL2` | Level 2       |
| `EPSPostScriptLevelEnum.LEVEL3` | Level 3       |

---

<a id="jsobjref-scripting-constants-epspreview"></a>

## EPSPreview

The preview image format used when saving an EPS file

| Value                             | Description   |
|-----------------------------------|---------------|
| `EPSPreview.BWTIFF`               | todo          |
| `EPSPreview.COLORTIFF`            | todo          |
| `EPSPreview.TRANSPARENTCOLORTIFF` | todo          |
| `EPSPreview.None`                 | todo          |

---

<a id="jsobjref-scripting-constants-exporttype"></a>

## ExportType

The file format used to export a file

| Value                  | Description   |
|------------------------|---------------|
| `ExportType.AutoCAD`   | AutoCAD       |
| `ExportType.FLASH`     | FLASH         |
| `ExportType.GIF`       | GIF           |
| `ExportType.JPEG`      | JPEG          |
| `ExportType.Photoshop` | Photoshop     |
| `ExportType.PNG24`     | PNG24         |
| `ExportType.PNG8`      | PNG8          |
| `ExportType.SVG`       | SVG           |
| `ExportType.TIFF`      | TIFF          |

---

<a id="jsobjref-scripting-constants-figurestyletype"></a>

## FigureStyleType

| Value                                  | Description   |
|----------------------------------------|---------------|
| `FigureStyleType.DEFAULTFIGURESTYLE`   | todo          |
| `FigureStyleType.PROPORTIONAL`         | todo          |
| `FigureStyleType.PROPORTIONALOLDSTYLE` | todo          |
| `FigureStyleType.TABULAR`              | todo          |
| `FigureStyleType.TABULAROLDSTYLE`      | todo          |

---

<a id="jsobjref-scripting-constants-filterspreservepolicy"></a>

## FiltersPreservePolicy

The filters preserve policy used by the FXG file format.

| Value                                       | Description   |
|---------------------------------------------|---------------|
| `FiltersPreservePolicy.EXPANDFILTERS`       | todo          |
| `FiltersPreservePolicy.KEEPFILTERSEDITABLE` | todo          |
| `FiltersPreservePolicy.RASTERIZEFILTERS`    | todo          |

---

<a id="jsobjref-scripting-constants-flashexportstyle"></a>

## FlashExportStyle

The method used to convert Illustrator images when exporting files

| Value                              | Description   |
|------------------------------------|---------------|
| `FlashExportStyle.ASFLASHFILE`     | todo          |
| `FlashExportStyle.LAYERSASFILES`   | todo          |
| `FlashExportStyle.LAYERSASFRAMES`  | todo          |
| `FlashExportStyle.LAYERSASSYMBOLS` | todo          |
| `FlashExportStyle.TOFILES`         | todo          |

---

<a id="jsobjref-scripting-constants-flashexportversion"></a>

## FlashExportVersion

Version for exported SWF file.

| Value                              | Description   |
|------------------------------------|---------------|
| `FlashExportVersion.FlashVersion1` | Version 1     |
| `FlashExportVersion.FlashVersion2` | Version 2     |
| `FlashExportVersion.FlashVersion3` | Version 3     |
| `FlashExportVersion.FlashVersion4` | Version 4     |
| `FlashExportVersion.FlashVersion5` | Version 5     |
| `FlashExportVersion.FlashVersion6` | Version 6     |
| `FlashExportVersion.FlashVersion7` | Version 7     |
| `FlashExportVersion.FlashVersion8` | Version 8     |
| `FlashExportVersion.FlashVersion9` | Version 9     |

---

<a id="jsobjref-scripting-constants-flashimageformat"></a>

## FlashImageFormat

The format used to store flash images.

| Value                       | Description   |
|-----------------------------|---------------|
| `FlashImageFormat.LOSSLESS` | Lossless      |
| `FlashImageFormat.LOSSY`    | Lossy         |

---

<a id="jsobjref-scripting-constants-flashjpegmethod"></a>

## FlashJPEGMethod

The method used to store JPEG images.

| Value                       | Description   |
|-----------------------------|---------------|
| `FlashJPEGMethod.Optimized` | Optimized     |
| `FlashJPEGMethod.Standard`  | Standard      |

---

<a id="jsobjref-scripting-constants-flashplaybacksecurity"></a>

## FlashPlaybackSecurity

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `FlashPlaybackSecurity.PlaybackLocal`   | Local         |
| `FlashPlaybackSecurity.PlaybackNetwork` | Network       |

---

<a id="jsobjref-scripting-constants-fontbaselineoption"></a>

## FontBaselineOption

| Value                               | Description   |
|-------------------------------------|---------------|
| `FontBaselineOption.NORMALBASELINE` | todo          |
| `FontBaselineOption.SUPERSCRIPT`    | todo          |
| `FontBaselineOption.SUBSCRIPT`      | todo          |

---

<a id="jsobjref-scripting-constants-fontcapsoption"></a>

## FontCapsOption

| Value                         | Description   |
|-------------------------------|---------------|
| `FontCapsOption.ALLCAPS`      | All Caps      |
| `FontCapsOption.ALLSMALLCAPS` | All Smallcaps |
| `FontCapsOption.NORMALCAPS`   | Normal Caps   |
| `FontCapsOption.SMALLCAPS`    | Small Caps    |

---

<a id="jsobjref-scripting-constants-fontopentypepositionoption"></a>

## FontOpenTypePositionOption

| Value                                            | Description          |
|--------------------------------------------------|----------------------|
| `FontOpenTypePositionOption.DENOMINATOR`         | Denominator          |
| `FontOpenTypePositionOption.NUMERATOR`           | Numerator            |
| `FontOpenTypePositionOption.OPENTYPEDEFAULT`     | Opentype Default     |
| `FontOpenTypePositionOption.OPENTYPESUBSCRIPT`   | Opentype Subscript   |
| `FontOpenTypePositionOption.OPENTYPESUPERSCRIPT` | Opentype Superscript |

---

<a id="jsobjref-scripting-constants-fontsubstitutionpolicy"></a>

## FontSubstitutionPolicy

| Value                                      | Description   |
|--------------------------------------------|---------------|
| `FontSubstitutionPolicy.SUBSTITUTEDEVICE`  | Device        |
| `FontSubstitutionPolicy.SUBSTITUTEOBLIQUE` | Oblique       |
| `FontSubstitutionPolicy.SUBSTITUTETINT`    | Tint          |

---

<a id="jsobjref-scripting-constants-fxgversion"></a>

## FXGVersion

The FXG file-format version.

| Value                    | Description   |
|--------------------------|---------------|
| `FXGVersion.VERSION1PT0` | Version 1 PT0 |
| `FXGVersion.VERSION2PT0` | Version 2 PT0 |

---

<a id="jsobjref-scripting-constants-gradientspreservepolicy"></a>

## GradientsPreservePolicy

The gradients preserve policy used by the FXG file format.

| Value                                                   | Description                    |
|---------------------------------------------------------|--------------------------------|
| `GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS` | Automaticaly Convert Gradients |
| `GradientsPreservePolicy.KEEPGRADIENTSEDITABLE`         | Keep Gradients Editable        |

---

<a id="jsobjref-scripting-constants-gradienttype"></a>

## GradientType

The type of gradient.

| Value                 | Description   |
|-----------------------|---------------|
| `GradientType.LINEAR` | Linear        |
| `GradientType.RADIAL` | Radial        |

---

<a id="jsobjref-scripting-constants-imagecolorspace"></a>

## ImageColorSpace

The color space of a raster item or an exported file

| Value                        | Description   |
|------------------------------|---------------|
| `ImageColorSpace.CMYK`       | CMYK          |
| `ImageColorSpace.DeviceN`    | DeviceN       |
| `ImageColorSpace.Grayscale`  | Grayscale     |
| `ImageColorSpace.Indexed`    | Indexed       |
| `ImageColorSpace.LAB`        | LAB           |
| `ImageColorSpace.RGB`        | RGB           |
| `ImageColorSpace.Separation` | Separation    |

---

<a id="jsobjref-scripting-constants-inkprintstatus"></a>

## InkPrintStatus

| Value                       | Description   |
|-----------------------------|---------------|
| `InkPrintStatus.CONVERTINK` | Convert Ink   |
| `InkPrintStatus.ENABLEINK`  | Enable Ink    |
| `InkPrintStatus.DISABLEINK` | Disable Ink   |

---

<a id="jsobjref-scripting-constants-inktype"></a>

## InkType

| Value                | Description   |
|----------------------|---------------|
| `InkType.BLACKINK`   | Black Ink     |
| `InkType.CUSTOMINK`  | Custom Ink    |
| `InkType.CYANINK`    | Cyan Ink      |
| `InkType.MAGENTAINK` | Magenta Ink   |
| `InkType.YELLOWINK`  | Yellow Ink    |

---

<a id="jsobjref-scripting-constants-javascriptexecutionmode"></a>

## JavaScriptExecutionMode

| Value                                    | Description      |
|------------------------------------------|------------------|
| `JavaScriptExecutionMode.BeforeRunning`  | Before Running   |
| `JavaScriptExecutionMode.OnRuntimeError` | On Runtime Error |
| `JavaScriptExecutionMode.never`          | Never            |

---

<a id="jsobjref-scripting-constants-justification"></a>

## Justification

The alignment or justification for a paragraph of text.

| Value                                     | Description                   |
|-------------------------------------------|-------------------------------|
| `Justification.CENTER`                    | Center                        |
| `Justification.FULLJUSTIFY`               | Full Justify                  |
| `Justification.FULLJUSTIFYLASTLINECENTER` | Full Justify Last Line Center |
| `Justification.FULLJUSTIFYLASTLINELEFT`   | Full Justify Last Line Left   |
| `Justification.FULLJUSTIFYLASTLINERIGHT`  | Full Justify Last Line Right  |
| `Justification.LEFT`                      | Left                          |
| `Justification.RIGHT`                     | Right                         |

---

<a id="jsobjref-scripting-constants-kinsokuorderenum"></a>

## KinsokuOrderEnum

| Value                           | Description   |
|---------------------------------|---------------|
| `KinsokuOrderEnum.PUSHIN`       | todo          |
| `KinsokuOrderEnum.PUSHOUTFIRST` | todo          |
| `KinsokuOrderEnum.PUSHOUTONLY`  | todo          |

---

<a id="jsobjref-scripting-constants-knockoutstate"></a>

## KnockoutState

The type of knockout to use on a page item.

| Value                     | Description   |
|---------------------------|---------------|
| `KnockoutState.DISABLED`  | Disabled      |
| `KnockoutState.ENABLED`   | Enabled       |
| `KnockoutState.INHERITED` | Inherited     |
| `KnockoutState.Unknown`   | Unknown       |

---

<a id="jsobjref-scripting-constants-languagetype"></a>

## LanguageType

| Value                                | Description   |
|--------------------------------------|---------------|
| `LanguageType.BOKMALNORWEGIAN`       | todo          |
| `LanguageType.BRAZILLIANPORTUGUESE`  | todo          |
| `LanguageType.BULGARIAN`             | todo          |
| `LanguageType.CANADIANFRENCH`        | todo          |
| `LanguageType.CATALAN`               | todo          |
| `LanguageType.CHINESE`               | todo          |
| `LanguageType.CZECH`                 | todo          |
| `LanguageType.DANISH`                | todo          |
| `LanguageType.DUTCH`                 | todo          |
| `LanguageType.DUTCH2005REFORM`       | todo          |
| `LanguageType.ENGLISH`               | todo          |
| `LanguageType.FINNISH`               | todo          |
| `LanguageType.GERMAN2006REFORM`      | todo          |
| `LanguageType.GREEK`                 | todo          |
| `LanguageType.HUNGARIAN`             | todo          |
| `LanguageType.ICELANDIC`             | todo          |
| `LanguageType.ITALIAN`               | todo          |
| `LanguageType.JAPANESE`              | todo          |
| `LanguageType.NYNORSKNORWEGIAN`      | todo          |
| `LanguageType.OLDGERMAN`             | todo          |
| `LanguageType.POLISH`                | todo          |
| `LanguageType.RUMANIAN`              | todo          |
| `LanguageType.RUSSIAN`               | todo          |
| `LanguageType.SERBIAN`               | todo          |
| `LanguageType.SPANISH`               | todo          |
| `LanguageType.STANDARDFRENCH`        | todo          |
| `LanguageType.STANDARDGERMAN`        | todo          |
| `LanguageType.STANDARDPORTUGUESE`    | todo          |
| `LanguageType.SWEDISH`               | todo          |
| `LanguageType.SWISSGERMAN`           | todo          |
| `LanguageType.SWISSGERMAN2006REFORM` | todo          |
| `LanguageType.TURKISH`               | todo          |
| `LanguageType.UKENGLISH`             | todo          |
| `LanguageType.UKRANIAN`              | todo          |

---

<a id="jsobjref-scripting-constants-layerordertype"></a>

## LayerOrderType

| Value                     | Description   |
|---------------------------|---------------|
| `LayerOrderType.TOPDOWN`  | Top Down      |
| `LayerOrderType.BOTTOMUP` | Bottom Up     |

---

<a id="jsobjref-scripting-constants-librarytype"></a>

## LibraryType

Illustrator library type.

| Value                            | Description         |
|----------------------------------|---------------------|
| `LibraryType.Brushes`            | Brushes             |
| `LibraryType.GraphicStyles`      | Graphic Styles      |
| `LibraryType.IllustratorArtwork` | Illustrator Artwork |
| `LibraryType.Swatches`           | Swatches            |
| `LibraryType.Symbols`            | Symbols             |

---

<a id="jsobjref-scripting-constants-monochromecompression"></a>

## MonochromeCompression

The type of compression to use on a monochrome bitmap item when saving a PDF file.

| Value                             | Description   |
|-----------------------------------|---------------|
| `MonochromeCompression.CCIT3`     | CCIT3         |
| `MonochromeCompression.CCIT4`     | CCIT4         |
| `MonochromeCompression.MONOZIP`   | MONOZIP       |
| `MonochromeCompression.None`      | None          |
| `MonochromeCompression.RUNLENGTH` | RUNLENGTH     |

---

<a id="jsobjref-scripting-constants-outputflattening"></a>

## OutputFlattening

How transparency should be flattened when saving EPS and Illustrator file formats with compatibility set to versions of Illustrator earlier than Illustrator 10

| Value                                 | Description         |
|---------------------------------------|---------------------|
| `OutputFlattening.PRESERVEAPPEARANCE` | Preserve Appearance |
| `OutputFlattening.PRESERVEPATHS`      | Preserve Paths      |

---

<a id="jsobjref-scripting-constants-pagemarkstypes"></a>

## PageMarksTypes

| Value                     | Description   |
|---------------------------|---------------|
| `PageMarksTypes.Japanese` | Japanese      |
| `PageMarksTypes.Roman`    | Roman         |

---

<a id="jsobjref-scripting-constants-pathpointselection"></a>

## PathPointSelection

Which points, if any, of a path are selected.

| Value                               | Description   |
|-------------------------------------|---------------|
| `PathPointSelection.ANCHORPOINT`    | todo          |
| `PathPointSelection.LEFTDIRECTION`  | todo          |
| `PathPointSelection.LEFTRIGHTPOINT` | todo          |
| `PathPointSelection.NOSELECTION`    | todo          |
| `PathPointSelection.RIGHTDIRECTION` | todo          |

---

<a id="jsobjref-scripting-constants-pdfboxtype"></a>

## PDFBoxType

| Value                       | Description   |
|-----------------------------|---------------|
| `PDFBoxType.PDFARTBOX`      | todo          |
| `PDFBoxType.PDFBLEEDBOX`    | todo          |
| `PDFBoxType.PDFBOUNDINGBOX` | todo          |
| `PDFBoxType.PDFCROPBOX`     | todo          |
| `PDFBoxType.PDFMEDIABOX`    | todo          |
| `PDFBoxType.PDFTRIMBOX`     | todo          |

---

<a id="jsobjref-scripting-constants-pdfchangesallowedenum"></a>

## PDFChangesAllowedEnum

| Value                                       | Description   |
|---------------------------------------------|---------------|
| `PDFChangesAllowedEnum.CHANGE128ANYCHANGES` | todo          |
| `PDFChangesAllowedEnum.CHANGE128COMMENTING` | todo          |
| `PDFChangesAllowedEnum.CHANGE128EDITPAGE`   | todo          |
| `PDFChangesAllowedEnum.CHANGE128FILLFORM`   | todo          |
| `PDFChangesAllowedEnum.CHANGE128NONE`       | todo          |
| `PDFChangesAllowedEnum.CHANGE40ANYCHANGES`  | todo          |
| `PDFChangesAllowedEnum.CHANGE40COMMENTING`  | todo          |
| `PDFChangesAllowedEnum.CHANGE40NONE`        | todo          |
| `PDFChangesAllowedEnum.CHANGE40PAGELAYOUT`  | todo          |

---

<a id="jsobjref-scripting-constants-pdfcompatibility"></a>

## PDFCompatibility

The version of the Acrobat file format to create when saving a PDF file

| Value                       | Description   |
|-----------------------------|---------------|
| `PDFCompatibility.ACROBAT4` | Acrobat 4     |
| `PDFCompatibility.ACROBAT5` | Acrobat 5     |
| `PDFCompatibility.ACROBAT6` | Acrobat 6     |
| `PDFCompatibility.ACROBAT7` | Acrobat 7     |
| `PDFCompatibility.ACROBAT8` | Acrobat 8     |

---

<a id="jsobjref-scripting-constants-pdfoverprint"></a>

## PDFOverprint

| Value                               | Description            |
|-------------------------------------|------------------------|
| `PDFOverprint.DISCARDPDFOVERPRINT`  | Discard Pdf Overprint  |
| `PDFOverprint.PRESERVEPDFOVERPRINT` | Preserve Pdf Overprint |

---

<a id="jsobjref-scripting-constants-pdfprintallowedenum"></a>

## PDFPrintAllowedEnum

| Value                                        | Description         |
|----------------------------------------------|---------------------|
| `PDFPrintAllowedEnum.PRINT128HIGHRESOLUTION` | 128 High Resolution |
| `PDFPrintAllowedEnum.PRINT128LOWRESOLUTION`  | 128 Low Resolution  |
| `PDFPrintAllowedEnum.PRINT128NONE`           | 128 None            |
| `PDFPrintAllowedEnum.PRINT40HIGHRESOLUTION`  | 40 High Resolution  |
| `PDFPrintAllowedEnum.PRINT40NONE`            | 40 None             |

---

<a id="jsobjref-scripting-constants-pdftrimmarkweight"></a>

## PDFTrimMarkWeight

| Value                                  | Description   |
|----------------------------------------|---------------|
| `PDFTrimMarkWeight.TRIMMARKWEIGHT0125` | Weight 0125   |
| `PDFTrimMarkWeight.TRIMMARKWEIGHT025`  | Weight 025    |
| `PDFTrimMarkWeight.TRIMMARKWEIGHT05`   | Weight 05     |

---

<a id="jsobjref-scripting-constants-pdfxstandard"></a>

## PDFXStandard

| Value                     | Description   |
|---------------------------|---------------|
| `PDFXStandard.PDFX1A2001` | PDFX1A2001    |
| `PDFXStandard.PDFX1A2003` | PDFX1A2003    |
| `PDFXStandard.PDFX32002`  | PDFX32002     |
| `PDFXStandard.PDFX32003`  | PDFX32003     |
| `PDFXStandard.PDFX42007`  | PDFX42007     |
| `PDFXStandard.PDFXNONE`   | PDFXNONE      |

---

<a id="jsobjref-scripting-constants-perspectivegridtype"></a>

## PerspectiveGridType

| Value                                               | Description                       |
|-----------------------------------------------------|-----------------------------------|
| `PerspectiveGridType.OnePointPerspectiveGridType`   | One Point Perspective Grid Type   |
| `PerspectiveGridType.TwoPointPerspectiveGridType`   | Two Point Perspective Grid Type   |
| `PerspectiveGridType.ThreePointPerspectiveGridType` | Three Point Perspective Grid Type |
| `PerspectiveGridType.InvalidPerspectiveGridType`    | Invalid Perspective Grid Type     |

---

<a id="jsobjref-scripting-constants-perspectivegridplanetype"></a>

## PerspectiveGridPlaneType

| Value                                           | Description             |
|-------------------------------------------------|-------------------------|
| `PerspectiveGridPlaneType.GRIDLEFTPLANETYPE`    | Grid Left Plane Type    |
| `PerspectiveGridPlaneType.GRIDRIGHTPLANETYPE`   | Grid Right Plane Type   |
| `PerspectiveGridPlaneType.GRIDFLOORPLANETYPE`   | Grid Floor Plane Type   |
| `PerspectiveGridPlaneType.INVALIDGRIDPLANETYPE` | Invalid Grid Plane Type |

---

<a id="jsobjref-scripting-constants-photoshopcompatibility"></a>

## PhotoshopCompatibility

| Value                               | Description   |
|-------------------------------------|---------------|
| `PhotoshopCompatibility.Photoshop6` | Photoshop 6   |
| `PhotoshopCompatibility.Photoshop8` | Photoshop 8   |

---

<a id="jsobjref-scripting-constants-pointtype"></a>

## PointType

The type of path point selected

| Value              | Description   |
|--------------------|---------------|
| `PointType.CORNER` | Corner        |
| `PointType.SMOOTH` | Smooth        |

---

<a id="jsobjref-scripting-constants-polarityvalues"></a>

## PolarityValues

| Value                     | Description   |
|---------------------------|---------------|
| `PolarityValues.NEGATIVE` | Negative      |
| `PolarityValues.POSITIVE` | Positive      |

---

<a id="jsobjref-scripting-constants-postscriptimagecompressiontype"></a>

## PostScriptImageCompressionType

| Value                                                 | Description   |
|-------------------------------------------------------|---------------|
| `PostScriptImageCompressionType.IMAGECOMPRESSIONNONE` | todo          |
| `PostScriptImageCompressionType.JPEG`                 | todo          |
| `PostScriptImageCompressionType.RLE`                  | todo          |

---

<a id="jsobjref-scripting-constants-printartworkdesignation"></a>

## PrintArtworkDesignation

| Value                                            | Description              |
|--------------------------------------------------|--------------------------|
| `PrintArtworkDesignation.ALLLAYERS`              | All Layers               |
| `PrintArtworkDesignation.VISIBLELAYERS`          | Visible Layers           |
| `PrintArtworkDesignation.VISIBLEPRINTABLELAYERS` | Visible Printable Layers |

---

<a id="jsobjref-scripting-constants-printcolorintent"></a>

## PrintColorIntent

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `PrintColorIntent.ABSOLUTECOLORIMETRIC` | todo          |
| `PrintColorIntent.PERCEPTUALINTENT`     | todo          |
| `PrintColorIntent.RELATIVECOLORIMETRIC` | todo          |
| `PrintColorIntent.SATURATIONINTENT`     | todo          |

---

<a id="jsobjref-scripting-constants-printcolorprofile"></a>

## PrintColorProfile

| Value                               | Description      |
|-------------------------------------|------------------|
| `PrintColorProfile.CUSTOMPROFILE`   | Custom Profile   |
| `PrintColorProfile.PRINTERPROFILE`  | Printer Profile  |
| `PrintColorProfile.OLDSTYLEPROFILE` | Oldstyle Profile |
| `PrintColorProfile.SOURCEPROFILE`   | Source Profile   |

---

<a id="jsobjref-scripting-constants-printcolorseparationmode"></a>

## PrintColorSeparationMode

| Value                                          | Description           |
|------------------------------------------------|-----------------------|
| `PrintColorSeparationMode.COMPOSITE`           | Composite             |
| `PrintColorSeparationMode.HOSTBASEDSEPARATION` | Host-Based Separation |
| `PrintColorSeparationMode.INRIPSEPARATION`     | Inrip Separation      |

---

<a id="jsobjref-scripting-constants-printercolormode"></a>

## PrinterColorMode

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `PrinterColorMode.BLACKANDWHITEPRINTER` | Black & White |
| `PrinterColorMode.COLORPRINTER`         | Color         |
| `PrinterColorMode.GRAYSCALEPRINTER`     | Grayscale     |

---

<a id="jsobjref-scripting-constants-printerpostscriptlevelenum"></a>

## PrinterPostScriptLevelEnum

| Value                                 | Description   |
|---------------------------------------|---------------|
| `PrinterPostScriptLevelEnum.PSLEVEL1` | PS LEVEL 1    |
| `PrinterPostScriptLevelEnum.PSLEVEL2` | PS LEVEL 2    |
| `PrinterPostScriptLevelEnum.PSLEVEL3` | PS LEVEL 3    |

---

<a id="jsobjref-scripting-constants-printertypeenum"></a>

## PrinterTypeEnum

| Value                                  | Description            |
|----------------------------------------|------------------------|
| `PrinterTypeEnum.NONPOSTSCRIPTPRINTER` | Non Postscript Printer |
| `PrinterTypeEnum.POSTSCRIPTPRINTER`    | Postscript Printer     |
| `PrinterTypeEnum.Unknown`              | Unknown                |

---

<a id="jsobjref-scripting-constants-printfontdownloadmode"></a>

## PrintFontDownloadMode

| Value                                    | Description       |
|------------------------------------------|-------------------|
| `PrintFontDownloadMode.DOWNLOADNONE`     | Download None     |
| `PrintFontDownloadMode.DOWNLOADCOMPLETE` | Download Complete |
| `PrintFontDownloadMode.DOWNLOADSUBSET`   | Download Subset   |

---

<a id="jsobjref-scripting-constants-printingbounds"></a>

## PrintingBounds

| Value                           | Description     |
|---------------------------------|-----------------|
| `PrintingBounds.ARTBOARDBOUNDS` | Artboard Bounds |
| `PrintingBounds.ARTWORKBOUNDS`  | Artwork Bounds  |

---

<a id="jsobjref-scripting-constants-printorientation"></a>

## PrintOrientation

The artwork printing orientation.

| Value                               | Description       |
|-------------------------------------|-------------------|
| `PrintOrientation.AUTOROTATE`       | Auto Rotate       |
| `PrintOrientation.LANDSCAPE`        | Landscape         |
| `PrintOrientation.PORTRAIT`         | Portrait          |
| `PrintOrientation.REVERSELANDSCAPE` | Reverse Landscape |
| `PrintOrientation.REVERSEPORTRAIT`  | Reverse Portrait  |

---

<a id="jsobjref-scripting-constants-printposition"></a>

## PrintPosition

| Value                                | Description            |
|--------------------------------------|------------------------|
| `PrintPosition.TRANSLATEBOTTOM`      | Translate Bottom       |
| `PrintPosition.TRANSLATEBOTTOMLEFT`  | Translate Bottom Left  |
| `PrintPosition.TRANSLATEBOTTOMRIGHT` | Translate Bottom Right |
| `PrintPosition.TRANSLATECENTER`      | Translate Center       |
| `PrintPosition.TRANSLATELEFT`        | Translate Left         |
| `PrintPosition.TRANSLATERIGHT`       | Translate Right        |
| `PrintPosition.TRANSLATETOP`         | Translate Top          |
| `PrintPosition.TRANSLATETOPLEFT`     | Translate Top Left     |
| `PrintPosition.TRANSLATETOPRIGHT`    | Translate Top Right    |

---

<a id="jsobjref-scripting-constants-printtiling"></a>

## PrintTiling

| Value                            | Description      |
|----------------------------------|------------------|
| `PrintTiling.TILEFULLPAGES`      | Full Pages       |
| `PrintTiling.TILESINGLEFULLPAGE` | Single Full Page |
| `PrintTiling.TILEIMAGEABLEAREAS` | Imageable Areas  |

---

<a id="jsobjref-scripting-constants-rasterizationcolormodel"></a>

## RasterizationColorModel

The color model for the rasterization.

| Value                                       | Description         |
|---------------------------------------------|---------------------|
| `RasterizationColorModel.BITMAP`            | Bitmap              |
| `RasterizationColorModel.DEFAULTCOLORMODEL` | Default Color Model |
| `RasterizationColorModel.GRAYSCALE`         | Grayscale           |

---

<a id="jsobjref-scripting-constants-rasterlinkstate"></a>

## RasterLinkState

The status of a raster item’s linked image if the image is stored externally

| Value                          | Description    |
|--------------------------------|----------------|
| `RasterLinkState.DATAFROMFILE` | Data From File |
| `RasterLinkState.DATAMODIFIED` | Data Modified  |
| `RasterLinkState.NODATA`       | No Data        |

---

<a id="jsobjref-scripting-constants-rulerunits"></a>

## RulerUnits

The default measurement units for the rulers of a document

| Value                    | Description   |
|--------------------------|---------------|
| `RulerUnits.Centimeters` | Centimeters   |
| `RulerUnits.Qs`          | Qs            |
| `RulerUnits.Inches`      | Inches        |
| `RulerUnits.Pixels`      | Pixels        |
| `RulerUnits.Millimeters` | Millimeters   |
| `RulerUnits.Unknown`     | Unknown       |
| `RulerUnits.Picas`       | Picas         |
| `RulerUnits.Points`      | Points        |

---

<a id="jsobjref-scripting-constants-saveoptions"></a>

## SaveOptions

Save options provided when closing a document.

| Value                             | Description            |
|-----------------------------------|------------------------|
| `SaveOptions.DONOTSAVECHANGES`    | Do Not Save Changes    |
| `SaveOptions.SAVECHANGES`         | Save Changes           |
| `SaveOptions.PROMPTTOSAVECHANGES` | Prompt To Save Changes |

---

<a id="jsobjref-scripting-constants-screenmode"></a>

## ScreenMode

The mode of display for a view.

| Value                    | Description   |
|--------------------------|---------------|
| `ScreenMode.DESKTOP`     | Desktop       |
| `ScreenMode.MULTIWINDOW` | Multi Window  |
| `ScreenMode.FULLSCREEN`  | Fullscreen    |

---

<a id="jsobjref-scripting-constants-spotcolorkind"></a>

## SpotColorKind

The custom color kind of a spot color.

| Value                    | Description   |
|--------------------------|---------------|
| `SpotColorKind.SpotCMYK` | CMYK          |
| `SpotColorKind.SpotLAB`  | LAB           |
| `SpotColorKind.SpotRGB`  | RGB           |

---

<a id="jsobjref-scripting-constants-strokecap"></a>

## StrokeCap

The type of line capping for a path stroke.

| Value                        | Description   |
|------------------------------|---------------|
| `StrokeCap.BUTTENDCAP`       | Butt          |
| `StrokeCap.ROUNDENDCAP`      | Round         |
| `StrokeCap.PROJECTINGENDCAP` | Projecting    |

---

<a id="jsobjref-scripting-constants-strokejoin"></a>

## StrokeJoin

The type of joints for a path stroke.

| Value                     | Description   |
|---------------------------|---------------|
| `StrokeJoin.BEVELENDJOIN` | Bevel         |
| `StrokeJoin.ROUNDENDJOIN` | Round         |
| `StrokeJoin.MITERENDJOIN` | Miter         |

---

<a id="jsobjref-scripting-constants-stylerunalignmenttype"></a>

## StyleRunAlignmentType

| Value                                 | Description    |
|---------------------------------------|----------------|
| `StyleRunAlignmentType.bottom`        | Bottom         |
| `StyleRunAlignmentType.icfTop`        | ICF Top        |
| `StyleRunAlignmentType.center`        | Center         |
| `StyleRunAlignmentType.ROMANBASELINE` | Roman Baseline |
| `StyleRunAlignmentType.icfBottom`     | ICF Bottom     |
| `StyleRunAlignmentType.top`           | Top            |

---

<a id="jsobjref-scripting-constants-svgcsspropertylocation"></a>

## SVGCSSPropertyLocation

How should the CSS properties of the document be included in an exported SVG file

| Value                                           | Description             |
|-------------------------------------------------|-------------------------|
| `SVGCSSPropertyLocation.ENTITIES`               | Entities                |
| `SVGCSSPropertyLocation.STYLEATTRIBUTES`        | Style Attributes        |
| `SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES` | Presentation Attributes |
| `SVGCSSPropertyLocation.STYLEELEMENTS`          | Style Elements          |

---

<a id="jsobjref-scripting-constants-svgdocumentencoding"></a>

## SVGDocumentEncoding

How should the text in the document be encoded when exporting an SVG file

| Value                       | Description   |
|-----------------------------|---------------|
| `SVGDocumentEncoding.ASCII` | ASCII         |
| `SVGDocumentEncoding.UTF8`  | UTF8          |
| `SVGDocumentEncoding.UTF16` | UTF16         |

---

<a id="jsobjref-scripting-constants-svgdtdversion"></a>

## SVGDTDVersion

SVG version compatibility for exported files

| Value                          | Description    |
|--------------------------------|----------------|
| `SVGDTDVersion.SVG1_0`         | SVG1_0         |
| `SVGDTDVersion.SVG1_1`         | SVG1_1         |
| `SVGDTDVersion.SVGBASIC1_1`    | SVGBASIC1_1    |
| `SVGDTDVersion.SVGTINY1_1`     | SVGTINY1_1     |
| `SVGDTDVersion.SVGTINY1_1PLUS` | SVGTINY1_1PLUS |
| `SVGDTDVersion.SVGTINY1_2`     | SVGTINY1_2     |

---

<a id="jsobjref-scripting-constants-svgfontsubsetting"></a>

## SVGFontSubsetting

What font glyphs should be included in exported SVG files

| Value                                     | Description              |
|-------------------------------------------|--------------------------|
| `SVGFontSubsetting.ALLGLYPHS`             | All Glyphs               |
| `SVGFontSubsetting.GLYPHSUSEDPLUSENGLISH` | Glyphs Used Plus English |
| `SVGFontSubsetting.COMMONENGLISH`         | Common English           |
| `SVGFontSubsetting.GLYPHSUSEDPLUSROMAN`   | Glyphs Used Plus Roman   |
| `SVGFontSubsetting.COMMONROMAN`           | Common Roman             |
| `SVGFontSubsetting.GLYPHSUSED`            | Glyphs Used              |
| `SVGFontSubsetting.None`                  | None                     |

---

<a id="jsobjref-scripting-constants-svgfonttype"></a>

## SVGFontType

Types for fonts included in exported SVG files

| Value                     | Description   |
|---------------------------|---------------|
| `SVGFontType.CEFFONT`     | CEF Font      |
| `SVGFontType.SVGFONT`     | SVG Font      |
| `SVGFontType.OUTLINEFONT` | Outline Font  |

---

<a id="jsobjref-scripting-constants-symbolregistrationpoint"></a>

## SymbolRegistrationPoint

Registration points for symbols.

| Value                                             | Description         |
|---------------------------------------------------|---------------------|
| `SymbolRegistrationPoint.SYMBOLBOTTOMLEFTPOINT`   | Bottom Left Point   |
| `SymbolRegistrationPoint.SYMBOLBOTTOMMIDDLEPOINT` | Bottom Middle Point |
| `SymbolRegistrationPoint.SYMBOLBOTTOMRIGHTPOINT`  | Bottom Right Point  |
| `SymbolRegistrationPoint.SYMBOLCENTERPOINT`       | Center Point        |
| `SymbolRegistrationPoint.SYMBOLMIDDLELEFTPOINT`   | Middle Left Point   |
| `SymbolRegistrationPoint.SYMBOLMIDDLERIGHTPOINT`  | Middle Right Point  |
| `SymbolRegistrationPoint.SYMBOLTOPLEFTPOINT`      | Top Left Point      |
| `SymbolRegistrationPoint.SYMBOLTOPMIDDLEPOINT`    | Top Middle Point    |
| `SymbolRegistrationPoint.SYMBOLTOPRIGHTPOINT`     | Top Right Point     |

---

<a id="jsobjref-scripting-constants-tabstopalignment"></a>

## TabStopAlignment

The alignment of a tab stop.

| Value                      | Description   |
|----------------------------|---------------|
| `TabStopAlignment.Center`  | Center        |
| `TabStopAlignment.Decimal` | Decimal       |
| `TabStopAlignment.Left`    | Left          |
| `TabStopAlignment.Right`   | Right         |

---

<a id="jsobjref-scripting-constants-textantialias"></a>

## TextAntialias

The type of text anti-aliasing in a text art item.

| Value                  | Description   |
|------------------------|---------------|
| `TextAntialias.CRISP`  | Crisp         |
| `TextAntialias.NONE`   | None          |
| `TextAntialias.SHARP`  | Sharp         |
| `TextAntialias.STRONG` | Strong        |

---

<a id="jsobjref-scripting-constants-textorientation"></a>

## TextOrientation

The orientation of text in a text art item.

| Value                        | Description   |
|------------------------------|---------------|
| `TextOrientation.HORIZONTAL` | Horizontal    |
| `TextOrientation.VERTICAL`   | Vertical      |

---

<a id="jsobjref-scripting-constants-textpreservepolicy"></a>

## TextPreservePolicy

The text-preserve policy used by the FXG file format.

| Value                                         | Description                |
|-----------------------------------------------|----------------------------|
| `TextPreservePolicy.AUTOMATICALLYCONVERTTEXT` | Automatically Convert Text |
| `TextPreservePolicy.OUTLINETEXT`              | Outline Text               |
| `TextPreservePolicy.KEEPTEXTEDITABLE`         | Keep Text Editable         |
| `TextPreservePolicy.RASTERIZETEXT`            | Rasterize Text             |

---

<a id="jsobjref-scripting-constants-texttype"></a>

## TextType

The type of text art displayed by this object.

| Value                | Description   |
|----------------------|---------------|
| `TextType.AREATEXT`  | Area Text     |
| `TextType.POINTTEXT` | Point Text    |
| `TextType.PATHTEXT`  | Path Text     |

---

<a id="jsobjref-scripting-constants-tiffbyteorder"></a>

## TIFFByteOrder

The byte order to use for an exported TIFF file.

| Value                     | Description   |
|---------------------------|---------------|
| `TIFFByteOrder.IBMPC`     | IBM PC        |
| `TIFFByteOrder.MACINTOSH` | Macintosh     |

---

<a id="jsobjref-scripting-constants-tracingmodetype"></a>

## TracingModeType

| Value                                      | Description   |
|--------------------------------------------|---------------|
| `TracingModeType.TRACINGMODEBLACKANDWHITE` | Black & White |
| `TracingModeType.TRACINGMODECOLOR`         | Color         |
| `TracingModeType.TRACINGMODEGRAY`          | Gray          |

---

<a id="jsobjref-scripting-constants-transformation"></a>

## Transformation

The point to use as the anchor point about which an object is rotated, resized, or transformed.

| Value                           | Description     |
|---------------------------------|-----------------|
| `Transformation.BOTTOM`         | Bottom          |
| `Transformation.BOTTOMLEFT`     | Bottom Left     |
| `Transformation.BOTTOMRIGHT`    | Bottom Right    |
| `Transformation.CENTER`         | Center          |
| `Transformation.DOCUMENTORIGIN` | Document Origin |
| `Transformation.LEFT`           | Left            |
| `Transformation.RIGHT`          | Right           |
| `Transformation.TOP`            | Top             |
| `Transformation.TOPLEFT`        | Top Left        |
| `Transformation.TOPRIGHT`       | Top Right       |

---

<a id="jsobjref-scripting-constants-trappingtype"></a>

## TrappingType

| Value                         | Description   |
|-------------------------------|---------------|
| `TrappingType.IGNOREOPAQUE`   | todo          |
| `TrappingType.OPAQUE`         | todo          |
| `TrappingType.NORMALTRAPPING` | todo          |
| `TrappingType.TRANSPARENT`    | todo          |

---

<a id="jsobjref-scripting-constants-userinteractionlevel"></a>

## UserInteractionLevel

User interface settings

| Value                                    | Description          |
|------------------------------------------|----------------------|
| `UserInteractionLevel.DISPLAYALERTS`     | Display Alerts       |
| `UserInteractionLevel.DONTDISPLAYALERTS` | Don’t Display Alerts |

---

<a id="jsobjref-scripting-constants-variablekind"></a>

## VariableKind

What type of variables are included in the document.

| Value                     | Description   |
|---------------------------|---------------|
| `VariableKind.GRAPH`      | Graph         |
| `VariableKind.IMAGE`      | Image         |
| `VariableKind.VISIBILITY` | Visibility    |
| `VariableKind.TEXTUAL`    | Textual       |
| `VariableKind.Unknown`    | Unknown       |

---

<a id="jsobjref-scripting-constants-viewrastertype"></a>

## ViewRasterType

The raster visualization mode for tracing.

| Value                                              | Description       |
|----------------------------------------------------|-------------------|
| `ViewRasterType.TRACINGVIEWRASTERADJUSTEDIMAGE`    | Adjusted Image    |
| `ViewRasterType.TRACINGVIEWRASTERNOIMAGE`          | No Image          |
| `ViewRasterType.TRACINGVIEWRASTERORIGINALIMAGE`    | Original Image    |
| `ViewRasterType.TRACINGVIEWRASTERTRANSPARENTIMAGE` | Transparent Image |

---

<a id="jsobjref-scripting-constants-viewvectortype"></a>

## ViewVectorType

The vector visualization mode for tracing.

| Value                                                 | Description           |
|-------------------------------------------------------|-----------------------|
| `ViewVectorType.TRACINGVIEWVECTORNOTRACINGRESULT`     | No Tracing Result     |
| `ViewVectorType.TRACINGVIEWVECTOROUTLINES`            | Outlines              |
| `ViewVectorType.TRACINGVIEWVECTOROUTLINESWITHTRACING` | Outlines With Tracing |
| `ViewVectorType.TRACINGVIEWVECTORTRACINGRESULT`       | Tracing Result        |

---

<a id="jsobjref-scripting-constants-warichujustificationtype"></a>

## WariChuJustificationType

| Value                                                       | Description                           |
|-------------------------------------------------------------|---------------------------------------|
| `WariChuJustificationType.Center`                           | Center                                |
| `WariChuJustificationType.Left`                             | Left                                  |
| `WariChuJustificationType.Right`                            | Right                                 |
| `WariChuJustificationType.WARICHUAUTOJUSTIFY`               | Warichu Auto Justify                  |
| `WariChuJustificationType.WARICHUFULLJUSTIFY`               | Warichu Full Justify                  |
| `WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINECENTER` | Warichu Full Justify Last Line Center |
| `WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINELEFT`   | Warichu Full Justify Last Line Left   |
| `WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINERIGHT`  | Warichu Full Justify Last Line Right  |

---

<a id="jsobjref-scripting-constants-zordermethod"></a>

## ZOrderMethod

The method used to arrange an art item’s position in the stacking order of its parent group or layer, as specified with the zOrder method

| Value                       | Description    |
|-----------------------------|----------------|
| `ZOrderMethod.BRINGFORWARD` | Bring Forward  |
| `ZOrderMethod.SENDBACKWARD` | Send Backward  |
| `ZOrderMethod.BRINGTOFRONT` | Bring To Front |
| `ZOrderMethod.SENDTOBACK`   | Send To Back   |
