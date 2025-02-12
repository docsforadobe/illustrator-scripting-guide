# Scripting Constants

This chapter lists and describes the enumerations defined for use with Illustrator JavaScript properties and methods.

---

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

#### Example

```javascript
textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.DEFAULTFORM;
textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.FULLWIDTH
```

---

## AntiAliasingMethod

The type of antialiasing method used in the rasterization.

| Value                              | Description                   |
|------------------------------------|-------------------------------|
| `AntiAliasingMethod.None`          | No antialiasing is allowed.   |
| `AntiAliasingMethod.ARTOPTIMIZED`  | Optimize for the art object.  |
| `AntiAliasingMethod.TYPEOPTIMIZED` | Optimize for the type object. |

---

## ArtClippingOption

How the art should be clipped during output.

| Value                                    | Description                               |
|------------------------------------------|-------------------------------------------|
| `ArtClippingOption.OUTPUTARTBOUNDS`      | Output size is the size of the artwork.   |
| `ArtClippingOption.OUTPUTARTBOARDBOUNDS` | Output size is the size of the artboard.  |
| `ArtClippingOption.OUTPUTCROPRECTBOUNDS` | Output size is the size of the crop area. |

---

## AutoCADColors

| Value                        | Description    |
|------------------------------|----------------|
| `AutoCADColors.Max8Colors`   | Max 8 CColors  |
| `AutoCADColors.Max16Colors`  | Max 16 Colors  |
| `AutoCADColors.Max256Colors` | Max 25 6Colors |
| `AutoCADColors.TrueColors`   | True Colors    |

---

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

## AutoCADExportFileFormat

| Value                         | Description   |
|-------------------------------|---------------|
| `AutoCADExportFileFormat.DXF` | DXF           |
| `AutoCADExportFileFormat.DWG` | DWG           |

---

## AutoCADExportOption

| Value                                     | Description          |
|-------------------------------------------|----------------------|
| `AutoCADExportOption.PreserveAppearance`  | Preserve Appearance  |
| `AutoCADExportOption.MaximizeEditability` | Maximize Editability |

---

## AutoCADGlobalScaleOption

| Value                                   | Description    |
|-----------------------------------------|----------------|
| `AutoCADGlobalScaleOption.OriginalSize` | Original Size  |
| `AutoCADGlobalScaleOption.ScaleByValue` | Scale by Value |
| `AutoCADGlobalScaleOption.FitArtboard`  | Fit Artboard   |

---

## AutoCADRasterFormat

| Value                      | Description   |
|----------------------------|---------------|
| `AutoCADRasterFormat.PNG`  | PNG           |
| `AutoCADRasterFormat.JPEG` | JPEG          |

---

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

## AutoKernType

The auto kern type.

| Value                           | Description   |
|---------------------------------|---------------|
| `AutoKernType.NOAUTOKERN`       | None          |
| `AutoKernType.AUTO`             | Auto          |
| `AutoKernType.OPTICAL`          | Optical       |
| `AutoKernType.METRICSROMANONLY` | Metrics       |

---

## AutoLeadingType

The auto leading type.

| Value                            | Description      |
|----------------------------------|------------------|
| `AutoLeadingType.BOTTOMTOBOTTOM` | Bottom to Bottom |
| `AutoLeadingType.TOPTOTOP`       | Top to Top       |

---

## BaselineDirectionType

The baseline direction type.

| Value                                   | Description      |
|-----------------------------------------|------------------|
| `BaselineDirectionType.Standard`        | Standard         |
| `BaselineDirectionType.VerticalRotated` | Vertical Rotated |
| `BaselineDirectionType.TateChuYoko`     | TateChuYoko      |

---

## BlendAnimationType

| Value                                 | Description   |
|---------------------------------------|---------------|
| `BlendAnimationType.INBUILD`          | In Build      |
| `BlendAnimationType.NOBLENDANIMATION` | None          |
| `BlendAnimationType.INSEQUENCE`       | In Sequence   |

---

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

## BlendsExpandPolicy

Policy used by FXG file format to expand blends.

| Value                                           | Description                  |
|-------------------------------------------------|------------------------------|
| `BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS` | Automatically convert blends |
| `BlendsExpandPolicy.RASTERIZEBLENDS`            | Rasterize blends             |

---

## BurasagariTypeEnum

The Burasagari type.

| Value                         | Description   |
|-------------------------------|---------------|
| `BurasagariTypeEnum.Forced`   | Forced        |
| `BurasagariTypeEnum.None`     | None          |
| `BurasagariTypeEnum.Standard` | Standard      |

---

## CaseChangeType

The case change type.

| Value                         | Description                     |
|-------------------------------|---------------------------------|
| `CaseChangeType.LOWERCASE`    | Lowercase (`"hello world"`)     |
| `CaseChangeType.SENTENCECASE` | Sentence case (`"Hello world"`) |
| `CaseChangeType.TITLECASE`    | Title case (`"Hello World"`)    |
| `CaseChangeType.UPPERCASE`    | Uppercase (`"HELLO WORLD"`)     |

---

## ColorConversion

The color conversion policy.

| Value                                      | Description                |
|--------------------------------------------|----------------------------|
| `ColorConversion.COLORCONVERSIONREPURPOSE` | Color Conversion Repurpose |
| `ColorConversion.COLORCONVERSIONTODEST`    | Color Conversion to Dest   |
| `ColorConversion.None`                     | None                       |

---

## ColorConvertPurpose

The purpose of color conversion using the `ConvertSampleColor` method of the `Application` class.

| Value                                | Description   |
|--------------------------------------|---------------|
| `ColorConvertPurpose.defaultpurpose` | Default       |
| `ColorConvertPurpose.exportpurpose`  | Export        |
| `ColorConvertPurpose.previewpurpose` | Preview       |
| `ColorConvertPurpose.dummypurpose`   | Dummy         |

---

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

## ColorDitherMethod

The method used to dither colors in exported GIF and PNG8 images.

| Value                             | Description    |
|-----------------------------------|----------------|
| `ColorDitherMethod.DIFFUSION`     | Diffusion      |
| `ColorDitherMethod.NOISE`         | Noise          |
| `ColorDitherMethod.NOREDUCTION`   | No Reduction   |
| `ColorDitherMethod.PATTERNDITHER` | Pattern Dither |

---

## ColorModel

The color model to use.

| Value                     | Description   |
|---------------------------|---------------|
| `ColorModel.PROCESS`      | Process       |
| `ColorModel.REGISTRATION` | Registration  |
| `ColorModel.SPOT`         | Spot          |

---

## ColorProfile

| Value                                | Description             |
|--------------------------------------|-------------------------|
| `ColorProfile.INCLUDEALLPROFILE`     | Include All Profile     |
| `ColorProfile.INCLUDEDESTPROFILE`    | Include Dest Profile    |
| `ColorProfile.INCLUDERGBPROFILE`     | Include RGB Profile     |
| `ColorProfile.LEAVEPROFILEUNCHANGED` | Leave Profile Unchanged |
| `ColorProfile.None`                  | None                    |

---

## ColorReductionMethod

The method used to reduce the number of colors in exported GIF and PNG8 images.

| Value                             | Description   |
|-----------------------------------|---------------|
| `ColorReductionMethod.ADAPTIVE`   | Adaptive      |
| `ColorReductionMethod.SELECTIVE`  | Selective     |
| `ColorReductionMethod.PERCEPTUAL` | Perceptual    |
| `ColorReductionMethod.WEB`        | Web           |

---

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

## CoordinateSystem

The coordinate system used by Illustrator

| Value                                       | Description   |
|---------------------------------------------|---------------|
| `CoordinateSystem.ARTBOARDCOORDINATESYSTEM` | todo          |
| `CoordinateSystem.DOCUMENTCOORDINATESYSTEM` | todo          |

---

## CropOptions

The style of a document's cropping box

| Value                  | Description   |
|------------------------|---------------|
| `CropOptions.Japanese` | Japanese      |
| `CropOptions.Standard` | Standard      |

---

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

## DocumentColorSpace

The color space of a document

| Value                     | Description   |
|---------------------------|---------------|
| `DocumentColorSpace.CMYK` | CMYK          |
| `DocumentColorSpace.RGB`  | RGB           |

---

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

## DocumentPreviewMode

The document preview mode.

| Value                                  | Description   |
|----------------------------------------|---------------|
| `DocumentPreviewMode.DefaultPreview`   | Default       |
| `DocumentPreviewMode.OverprintPreview` | Overprint     |
| `DocumentPreviewMode.PixelPreview`     | Pixel         |

---

## DocumentRasterResolution

The preset document raster resolution.

| Value                                       | Description       |
|---------------------------------------------|-------------------|
| `DocumentRasterResolution.ScreenResolution` | Screen Resolution |
| `DocumentRasterResolution.HighResolution`   | High Resolution   |
| `DocumentRasterResolution.MediumResolution` | Medium Resolution |

---

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

## DocumentType

The file format used to save a file.

| Value                      | Description   |
|----------------------------|---------------|
| `DocumentType.EPS`         | EPS           |
| `DocumentType.FXG`         | FXG           |
| `DocumentType.ILLUSTRATOR` | Illustrator   |
| `DocumentType.PDF`         | PDF           |

---

## DownsampleMethod

| Value                                | Description        |
|--------------------------------------|--------------------|
| `DownsampleMethod.AVERAGEDOWNSAMPLE` | Average Downsample |
| `DownsampleMethod.BICUBICDOWNSAMPLE` | Bicubic Downsample |
| `DownsampleMethod.NODOWNSAMPLE`      | No Downsample      |
| `DownsampleMethod.SUBSAMPLE`         | Subsample          |

---

## ElementPlacement

| Value                               | Description        |
|-------------------------------------|--------------------|
| `ElementPlacement.INSIDE`           | Inside             |
| `ElementPlacement.PLACEAFTER`       | Place After        |
| `ElementPlacement.PLACEATBEGINNING` | Place At Beginning |
| `ElementPlacement.PLACEATEND`       | Place At End       |
| `ElementPlacement.PLACEBEFORE`      | Place Before       |

---

## EPSPostScriptLevelEnum

| Value                           | Description   |
|---------------------------------|---------------|
| `EPSPostScriptLevelEnum.LEVEL2` | Level 2       |
| `EPSPostScriptLevelEnum.LEVEL3` | Level 3       |

---

## EPSPreview

The preview image format used when saving an EPS file

| Value                             | Description   |
|-----------------------------------|---------------|
| `EPSPreview.BWTIFF`               | todo          |
| `EPSPreview.COLORTIFF`            | todo          |
| `EPSPreview.TRANSPARENTCOLORTIFF` | todo          |
| `EPSPreview.None`                 | todo          |

---

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

## FigureStyleType

| Value                                  | Description   |
|----------------------------------------|---------------|
| `FigureStyleType.DEFAULTFIGURESTYLE`   | todo          |
| `FigureStyleType.PROPORTIONAL`         | todo          |
| `FigureStyleType.PROPORTIONALOLDSTYLE` | todo          |
| `FigureStyleType.TABULAR`              | todo          |
| `FigureStyleType.TABULAROLDSTYLE`      | todo          |

---

## FiltersPreservePolicy

The filters preserve policy used by the FXG file format.

| Value                                       | Description   |
|---------------------------------------------|---------------|
| `FiltersPreservePolicy.EXPANDFILTERS`       | todo          |
| `FiltersPreservePolicy.KEEPFILTERSEDITABLE` | todo          |
| `FiltersPreservePolicy.RASTERIZEFILTERS`    | todo          |

---

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

## FlashImageFormat

The format used to store flash images.

| Value                       | Description   |
|-----------------------------|---------------|
| `FlashImageFormat.LOSSLESS` | Lossless      |
| `FlashImageFormat.LOSSY`    | Lossy         |

---

## FlashJPEGMethod

The method used to store JPEG images.

| Value                       | Description   |
|-----------------------------|---------------|
| `FlashJPEGMethod.Optimized` | Optimized     |
| `FlashJPEGMethod.Standard`  | Standard      |

---

## FlashPlaybackSecurity

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `FlashPlaybackSecurity.PlaybackLocal`   | Local         |
| `FlashPlaybackSecurity.PlaybackNetwork` | Network       |

---

## FontBaselineOption

| Value                               | Description   |
|-------------------------------------|---------------|
| `FontBaselineOption.NORMALBASELINE` | todo          |
| `FontBaselineOption.SUPERSCRIPT`    | todo          |
| `FontBaselineOption.SUBSCRIPT`      | todo          |

---

## FontCapsOption

| Value                         | Description   |
|-------------------------------|---------------|
| `FontCapsOption.ALLCAPS`      | All Caps      |
| `FontCapsOption.ALLSMALLCAPS` | All Smallcaps |
| `FontCapsOption.NORMALCAPS`   | Normal Caps   |
| `FontCapsOption.SMALLCAPS`    | Small Caps    |

---

## FontOpenTypePositionOption

| Value                                            | Description          |
|--------------------------------------------------|----------------------|
| `FontOpenTypePositionOption.DENOMINATOR`         | Denominator          |
| `FontOpenTypePositionOption.NUMERATOR`           | Numerator            |
| `FontOpenTypePositionOption.OPENTYPEDEFAULT`     | Opentype Default     |
| `FontOpenTypePositionOption.OPENTYPESUBSCRIPT`   | Opentype Subscript   |
| `FontOpenTypePositionOption.OPENTYPESUPERSCRIPT` | Opentype Superscript |

---

## FontSubstitutionPolicy

| Value                                      | Description   |
|--------------------------------------------|---------------|
| `FontSubstitutionPolicy.SUBSTITUTEDEVICE`  | Device        |
| `FontSubstitutionPolicy.SUBSTITUTEOBLIQUE` | Oblique       |
| `FontSubstitutionPolicy.SUBSTITUTETINT`    | Tint          |

---

## FXGVersion

The FXG file-format version.

| Value                    | Description   |
|--------------------------|---------------|
| `FXGVersion.VERSION1PT0` | Version 1 PT0 |
| `FXGVersion.VERSION2PT0` | Version 2 PT0 |

---

## GradientsPreservePolicy

The gradients preserve policy used by the FXG file format.

| Value                                                   | Description                    |
|---------------------------------------------------------|--------------------------------|
| `GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS` | Automaticaly Convert Gradients |
| `GradientsPreservePolicy.KEEPGRADIENTSEDITABLE`         | Keep Gradients Editable        |

---

## GradientType

The type of gradient.

| Value                 | Description   |
|-----------------------|---------------|
| `GradientType.LINEAR` | Linear        |
| `GradientType.RADIAL` | Radial        |

---

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

## InkPrintStatus

| Value                       | Description   |
|-----------------------------|---------------|
| `InkPrintStatus.CONVERTINK` | Convert Ink   |
| `InkPrintStatus.ENABLEINK`  | Enable Ink    |
| `InkPrintStatus.DISABLEINK` | Disable Ink   |

---

## InkType

| Value                | Description   |
|----------------------|---------------|
| `InkType.BLACKINK`   | Black Ink     |
| `InkType.CUSTOMINK`  | Custom Ink    |
| `InkType.CYANINK`    | Cyan Ink      |
| `InkType.MAGENTAINK` | Magenta Ink   |
| `InkType.YELLOWINK`  | Yellow Ink    |

---

## JavaScriptExecutionMode

| Value                                    | Description      |
|------------------------------------------|------------------|
| `JavaScriptExecutionMode.BeforeRunning`  | Before Running   |
| `JavaScriptExecutionMode.OnRuntimeError` | On Runtime Error |
| `JavaScriptExecutionMode.never`          | Never            |

---

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

## KinsokuOrderEnum

| Value                           | Description   |
|---------------------------------|---------------|
| `KinsokuOrderEnum.PUSHIN`       | todo          |
| `KinsokuOrderEnum.PUSHOUTFIRST` | todo          |
| `KinsokuOrderEnum.PUSHOUTONLY`  | todo          |

---

## KnockoutState

The type of knockout to use on a page item.

| Value                     | Description   |
|---------------------------|---------------|
| `KnockoutState.DISABLED`  | Disabled      |
| `KnockoutState.ENABLED`   | Enabled       |
| `KnockoutState.INHERITED` | Inherited     |
| `KnockoutState.Unknown`   | Unknown       |

---

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

## LayerOrderType

| Value                     | Description   |
|---------------------------|---------------|
| `LayerOrderType.TOPDOWN`  | Top Down      |
| `LayerOrderType.BOTTOMUP` | Bottom Up     |

---

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

## OutputFlattening

How transparency should be flattened when saving EPS and Illustrator file formats with compatibility set to versions of Illustrator earlier than Illustrator 10

| Value                                 | Description         |
|---------------------------------------|---------------------|
| `OutputFlattening.PRESERVEAPPEARANCE` | Preserve Appearance |
| `OutputFlattening.PRESERVEPATHS`      | Preserve Paths      |

---

## PageMarksTypes

| Value                     | Description   |
|---------------------------|---------------|
| `PageMarksTypes.Japanese` | Japanese      |
| `PageMarksTypes.Roman`    | Roman         |

---

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

## PDFOverprint

| Value                               | Description            |
|-------------------------------------|------------------------|
| `PDFOverprint.DISCARDPDFOVERPRINT`  | Discard Pdf Overprint  |
| `PDFOverprint.PRESERVEPDFOVERPRINT` | Preserve Pdf Overprint |

---

## PDFPrintAllowedEnum

| Value                                        | Description         |
|----------------------------------------------|---------------------|
| `PDFPrintAllowedEnum.PRINT128HIGHRESOLUTION` | 128 High Resolution |
| `PDFPrintAllowedEnum.PRINT128LOWRESOLUTION`  | 128 Low Resolution  |
| `PDFPrintAllowedEnum.PRINT128NONE`           | 128 None            |
| `PDFPrintAllowedEnum.PRINT40HIGHRESOLUTION`  | 40 High Resolution  |
| `PDFPrintAllowedEnum.PRINT40NONE`            | 40 None             |

---

## PDFTrimMarkWeight

| Value                                  | Description   |
|----------------------------------------|---------------|
| `PDFTrimMarkWeight.TRIMMARKWEIGHT0125` | Weight 0125   |
| `PDFTrimMarkWeight.TRIMMARKWEIGHT025`  | Weight 025    |
| `PDFTrimMarkWeight.TRIMMARKWEIGHT05`   | Weight 05     |

---

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

## PerspectiveGridType

| Value                                               | Description                       |
|-----------------------------------------------------|-----------------------------------|
| `PerspectiveGridType.OnePointPerspectiveGridType`   | One Point Perspective Grid Type   |
| `PerspectiveGridType.TwoPointPerspectiveGridType`   | Two Point Perspective Grid Type   |
| `PerspectiveGridType.ThreePointPerspectiveGridType` | Three Point Perspective Grid Type |
| `PerspectiveGridType.InvalidPerspectiveGridType`    | Invalid Perspective Grid Type     |

---

## PerspectiveGridPlaneType

| Value                                           | Description             |
|-------------------------------------------------|-------------------------|
| `PerspectiveGridPlaneType.GRIDLEFTPLANETYPE`    | Grid Left Plane Type    |
| `PerspectiveGridPlaneType.GRIDRIGHTPLANETYPE`   | Grid Right Plane Type   |
| `PerspectiveGridPlaneType.GRIDFLOORPLANETYPE`   | Grid Floor Plane Type   |
| `PerspectiveGridPlaneType.INVALIDGRIDPLANETYPE` | Invalid Grid Plane Type |

---

## PhotoshopCompatibility

| Value                               | Description   |
|-------------------------------------|---------------|
| `PhotoshopCompatibility.Photoshop6` | Photoshop 6   |
| `PhotoshopCompatibility.Photoshop8` | Photoshop 8   |

---

## PointType

The type of path point selected

| Value              | Description   |
|--------------------|---------------|
| `PointType.CORNER` | Corner        |
| `PointType.SMOOTH` | Smooth        |

---

## PolarityValues

| Value                     | Description   |
|---------------------------|---------------|
| `PolarityValues.NEGATIVE` | Negative      |
| `PolarityValues.POSITIVE` | Positive      |

---

## PostScriptImageCompressionType

| Value                                                 | Description   |
|-------------------------------------------------------|---------------|
| `PostScriptImageCompressionType.IMAGECOMPRESSIONNONE` | todo          |
| `PostScriptImageCompressionType.JPEG`                 | todo          |
| `PostScriptImageCompressionType.RLE`                  | todo          |

---

## PrintArtworkDesignation

| Value                                            | Description              |
|--------------------------------------------------|--------------------------|
| `PrintArtworkDesignation.ALLLAYERS`              | All Layers               |
| `PrintArtworkDesignation.VISIBLELAYERS`          | Visible Layers           |
| `PrintArtworkDesignation.VISIBLEPRINTABLELAYERS` | Visible Printable Layers |

---

## PrintColorIntent

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `PrintColorIntent.ABSOLUTECOLORIMETRIC` | todo          |
| `PrintColorIntent.PERCEPTUALINTENT`     | todo          |
| `PrintColorIntent.RELATIVECOLORIMETRIC` | todo          |
| `PrintColorIntent.SATURATIONINTENT`     | todo          |

---

## PrintColorProfile

| Value                               | Description      |
|-------------------------------------|------------------|
| `PrintColorProfile.CUSTOMPROFILE`   | Custom Profile   |
| `PrintColorProfile.PRINTERPROFILE`  | Printer Profile  |
| `PrintColorProfile.OLDSTYLEPROFILE` | Oldstyle Profile |
| `PrintColorProfile.SOURCEPROFILE`   | Source Profile   |

---

## PrintColorSeparationMode

| Value                                          | Description           |
|------------------------------------------------|-----------------------|
| `PrintColorSeparationMode.COMPOSITE`           | Composite             |
| `PrintColorSeparationMode.HOSTBASEDSEPARATION` | Host-Based Separation |
| `PrintColorSeparationMode.INRIPSEPARATION`     | Inrip Separation      |

---

## PrinterColorMode

| Value                                   | Description   |
|-----------------------------------------|---------------|
| `PrinterColorMode.BLACKANDWHITEPRINTER` | Black & White |
| `PrinterColorMode.COLORPRINTER`         | Color         |
| `PrinterColorMode.GRAYSCALEPRINTER`     | Grayscale     |

---

## PrinterPostScriptLevelEnum

| Value                                 | Description   |
|---------------------------------------|---------------|
| `PrinterPostScriptLevelEnum.PSLEVEL1` | PS LEVEL 1    |
| `PrinterPostScriptLevelEnum.PSLEVEL2` | PS LEVEL 2    |
| `PrinterPostScriptLevelEnum.PSLEVEL3` | PS LEVEL 3    |

---

## PrinterTypeEnum

| Value                                  | Description            |
|----------------------------------------|------------------------|
| `PrinterTypeEnum.NONPOSTSCRIPTPRINTER` | Non Postscript Printer |
| `PrinterTypeEnum.POSTSCRIPTPRINTER`    | Postscript Printer     |
| `PrinterTypeEnum.Unknown`              | Unknown                |

---

## PrintFontDownloadMode

| Value                                    | Description       |
|------------------------------------------|-------------------|
| `PrintFontDownloadMode.DOWNLOADNONE`     | Download None     |
| `PrintFontDownloadMode.DOWNLOADCOMPLETE` | Download Complete |
| `PrintFontDownloadMode.DOWNLOADSUBSET`   | Download Subset   |

---

## PrintingBounds

| Value                           | Description     |
|---------------------------------|-----------------|
| `PrintingBounds.ARTBOARDBOUNDS` | Artboard Bounds |
| `PrintingBounds.ARTWORKBOUNDS`  | Artwork Bounds  |

---

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

## PrintTiling

| Value                            | Description      |
|----------------------------------|------------------|
| `PrintTiling.TILEFULLPAGES`      | Full Pages       |
| `PrintTiling.TILESINGLEFULLPAGE` | Single Full Page |
| `PrintTiling.TILEIMAGEABLEAREAS` | Imageable Areas  |

---

## RasterizationColorModel

The color model for the rasterization.

| Value                                       | Description         |
|---------------------------------------------|---------------------|
| `RasterizationColorModel.BITMAP`            | Bitmap              |
| `RasterizationColorModel.DEFAULTCOLORMODEL` | Default Color Model |
| `RasterizationColorModel.GRAYSCALE`         | Grayscale           |

---

## RasterLinkState

The status of a raster item's linked image if the image is stored externally

| Value                          | Description    |
|--------------------------------|----------------|
| `RasterLinkState.DATAFROMFILE` | Data From File |
| `RasterLinkState.DATAMODIFIED` | Data Modified  |
| `RasterLinkState.NODATA`       | No Data        |

---

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

## SaveOptions

Save options provided when closing a document.

| Value                             | Description            |
|-----------------------------------|------------------------|
| `SaveOptions.DONOTSAVECHANGES`    | Do Not Save Changes    |
| `SaveOptions.SAVECHANGES`         | Save Changes           |
| `SaveOptions.PROMPTTOSAVECHANGES` | Prompt To Save Changes |

---

## ScreenMode

The mode of display for a view.

| Value                    | Description   |
|--------------------------|---------------|
| `ScreenMode.DESKTOP`     | Desktop       |
| `ScreenMode.MULTIWINDOW` | Multi Window  |
| `ScreenMode.FULLSCREEN`  | Fullscreen    |

---

## SpotColorKind

The custom color kind of a spot color.

| Value                    | Description   |
|--------------------------|---------------|
| `SpotColorKind.SpotCMYK` | CMYK          |
| `SpotColorKind.SpotLAB`  | LAB           |
| `SpotColorKind.SpotRGB`  | RGB           |

---

## StrokeCap

The type of line capping for a path stroke.

| Value                        | Description   |
|------------------------------|---------------|
| `StrokeCap.BUTTENDCAP`       | Butt          |
| `StrokeCap.ROUNDENDCAP`      | Round         |
| `StrokeCap.PROJECTINGENDCAP` | Projecting    |

---

## StrokeJoin

The type of joints for a path stroke.

| Value                     | Description   |
|---------------------------|---------------|
| `StrokeJoin.BEVELENDJOIN` | Bevel         |
| `StrokeJoin.ROUNDENDJOIN` | Round         |
| `StrokeJoin.MITERENDJOIN` | Miter         |

---

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

## SVGCSSPropertyLocation

How should the CSS properties of the document be included in an exported SVG file

| Value                                           | Description             |
|-------------------------------------------------|-------------------------|
| `SVGCSSPropertyLocation.ENTITIES`               | Entities                |
| `SVGCSSPropertyLocation.STYLEATTRIBUTES`        | Style Attributes        |
| `SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES` | Presentation Attributes |
| `SVGCSSPropertyLocation.STYLEELEMENTS`          | Style Elements          |

---

## SVGDocumentEncoding

How should the text in the document be encoded when exporting an SVG file

| Value                       | Description   |
|-----------------------------|---------------|
| `SVGDocumentEncoding.ASCII` | ASCII         |
| `SVGDocumentEncoding.UTF8`  | UTF8          |
| `SVGDocumentEncoding.UTF16` | UTF16         |

---

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

## SVGFontType

Types for fonts included in exported SVG files

| Value                     | Description   |
|---------------------------|---------------|
| `SVGFontType.CEFFONT`     | CEF Font      |
| `SVGFontType.SVGFONT`     | SVG Font      |
| `SVGFontType.OUTLINEFONT` | Outline Font  |

---

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

## TabStopAlignment

The alignment of a tab stop.

| Value                      | Description   |
|----------------------------|---------------|
| `TabStopAlignment.Center`  | Center        |
| `TabStopAlignment.Decimal` | Decimal       |
| `TabStopAlignment.Left`    | Left          |
| `TabStopAlignment.Right`   | Right         |

---

## TextAntialias

The type of text anti-aliasing in a text art item.

| Value                  | Description   |
|------------------------|---------------|
| `TextAntialias.CRISP`  | Crisp         |
| `TextAntialias.NONE`   | None          |
| `TextAntialias.SHARP`  | Sharp         |
| `TextAntialias.STRONG` | Strong        |

---

## TextOrientation

The orientation of text in a text art item.

| Value                        | Description   |
|------------------------------|---------------|
| `TextOrientation.HORIZONTAL` | Horizontal    |
| `TextOrientation.VERTICAL`   | Vertical      |

---

## TextPreservePolicy

The text-preserve policy used by the FXG file format.

| Value                                         | Description                |
|-----------------------------------------------|----------------------------|
| `TextPreservePolicy.AUTOMATICALLYCONVERTTEXT` | Automatically Convert Text |
| `TextPreservePolicy.OUTLINETEXT`              | Outline Text               |
| `TextPreservePolicy.KEEPTEXTEDITABLE`         | Keep Text Editable         |
| `TextPreservePolicy.RASTERIZETEXT`            | Rasterize Text             |

---

## TextType

The type of text art displayed by this object.

| Value                | Description   |
|----------------------|---------------|
| `TextType.AREATEXT`  | Area Text     |
| `TextType.POINTTEXT` | Point Text    |
| `TextType.PATHTEXT`  | Path Text     |

---

## TIFFByteOrder

The byte order to use for an exported TIFF file.

| Value                     | Description   |
|---------------------------|---------------|
| `TIFFByteOrder.IBMPC`     | IBM PC        |
| `TIFFByteOrder.MACINTOSH` | Macintosh     |

---

## TracingModeType

| Value                                      | Description   |
|--------------------------------------------|---------------|
| `TracingModeType.TRACINGMODEBLACKANDWHITE` | Black & White |
| `TracingModeType.TRACINGMODECOLOR`         | Color         |
| `TracingModeType.TRACINGMODEGRAY`          | Gray          |

---

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

## TrappingType

| Value                         | Description   |
|-------------------------------|---------------|
| `TrappingType.IGNOREOPAQUE`   | todo          |
| `TrappingType.OPAQUE`         | todo          |
| `TrappingType.NORMALTRAPPING` | todo          |
| `TrappingType.TRANSPARENT`    | todo          |

---

## UserInteractionLevel

User interface settings

| Value                                    | Description          |
|------------------------------------------|----------------------|
| `UserInteractionLevel.DISPLAYALERTS`     | Display Alerts       |
| `UserInteractionLevel.DONTDISPLAYALERTS` | Don't Display Alerts |

---

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

## ViewRasterType

The raster visualization mode for tracing.

| Value                                              | Description       |
|----------------------------------------------------|-------------------|
| `ViewRasterType.TRACINGVIEWRASTERADJUSTEDIMAGE`    | Adjusted Image    |
| `ViewRasterType.TRACINGVIEWRASTERNOIMAGE`          | No Image          |
| `ViewRasterType.TRACINGVIEWRASTERORIGINALIMAGE`    | Original Image    |
| `ViewRasterType.TRACINGVIEWRASTERTRANSPARENTIMAGE` | Transparent Image |

---

## ViewVectorType

The vector visualization mode for tracing.

| Value                                                 | Description           |
|-------------------------------------------------------|-----------------------|
| `ViewVectorType.TRACINGVIEWVECTORNOTRACINGRESULT`     | No Tracing Result     |
| `ViewVectorType.TRACINGVIEWVECTOROUTLINES`            | Outlines              |
| `ViewVectorType.TRACINGVIEWVECTOROUTLINESWITHTRACING` | Outlines With Tracing |
| `ViewVectorType.TRACINGVIEWVECTORTRACINGRESULT`       | Tracing Result        |

---

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

## ZOrderMethod

The method used to arrange an art item's position in the stacking order of its parent group or layer, as specified with the zOrder method

| Value                       | Description    |
|-----------------------------|----------------|
| `ZOrderMethod.BRINGFORWARD` | Bring Forward  |
| `ZOrderMethod.SENDBACKWARD` | Send Backward  |
| `ZOrderMethod.BRINGTOFRONT` | Bring To Front |
| `ZOrderMethod.SENDTOBACK`   | Send To Back   |
