.. _jsobjref/scripting-constants:

Scripting Constants
################################################################################

This chapter lists and describes the enumerations defined for use with Illustrator JavaScript properties and methods.

----

.. _jsobjref/scripting-constants.AlternateGlyphsForm:

AlternateGlyphsForm
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``AlternateGlyphsForm.DEFAULTFORM``       | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.TRADITIONAL``       | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.EXPERT``            | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.JIS78FORM``         | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.JIS83FORM``         | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.HALFWIDTH``         | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.THIRDWIDTH``        | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.QUARTERWIDTH``      | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.FULLWIDTH``         | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.PROPORTIONALWIDTH`` | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.JIS90FORM``         | todo        |
+-------------------------------------------+-------------+
| ``AlternateGlyphsForm.JIS04FORM``         | todo        |
+-------------------------------------------+-------------+

**Example**

::

  textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.DEFAULTFORM;
  textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.FULLWIDTH

----

.. _jsobjref/scripting-constants.AntiAliasingMethod:

AntiAliasingMethod
********************************************************************************

The type of antialiasing method used in the rasterization.

+--------------------------------------+-------------------------------+
|                Value                 |          Description          |
+======================================+===============================+
| ``AntiAliasingMethod.None``          | No antialiasing is allowed.   |
+--------------------------------------+-------------------------------+
| ``AntiAliasingMethod.ARTOPTIMIZED``  | Optimize for the art object.  |
+--------------------------------------+-------------------------------+
| ``AntiAliasingMethod.TYPEOPTIMIZED`` | Optimize for the type object. |
+--------------------------------------+-------------------------------+

----

.. _jsobjref/scripting-constants.ArtClippingOption:

ArtClippingOption
********************************************************************************

How the art should be clipped during output.

+--------------------------------------------+-------------------------------------------+
|                   Value                    |                Description                |
+============================================+===========================================+
| ``ArtClippingOption.OUTPUTARTBOUNDS``      | Output size is the size of the artwork.   |
+--------------------------------------------+-------------------------------------------+
| ``ArtClippingOption.OUTPUTARTBOARDBOUNDS`` | Output size is the size of the artboard.  |
+--------------------------------------------+-------------------------------------------+
| ``ArtClippingOption.OUTPUTCROPRECTBOUNDS`` | Output size is the size of the crop area. |
+--------------------------------------------+-------------------------------------------+

----

.. _jsobjref/scripting-constants.AutoCADColors:

AutoCADColors
********************************************************************************

+--------------------------------+-------------+
|             Value              | Description |
+================================+=============+
| ``AutoCADColors.Max8Colors``   | todo        |
+--------------------------------+-------------+
| ``AutoCADColors.Max16Colors``  | todo        |
+--------------------------------+-------------+
| ``AutoCADColors.Max256Colors`` | todo        |
+--------------------------------+-------------+
| ``AutoCADColors.TrueColors``   | todo        |
+--------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADCompatibility:

AutoCADCompatibility
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``AutoCADCompatibility.AutoCADRelease13`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADCompatibility.AutoCADRelease18`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADCompatibility.AutoCADRelease14`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADCompatibility.AutoCADRelease21`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADCompatibility.AutoCADRelease15`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADCompatibility.AutoCADRelease24`` | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADExportFileFormat:

AutoCADExportFileFormat
********************************************************************************

+---------------------------------+-------------+
|              Value              | Description |
+=================================+=============+
| ``AutoCADExportFileFormat.DXF`` | todo        |
+---------------------------------+-------------+
| ``AutoCADExportFileFormat.DWG`` | todo        |
+---------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADExportOption:

AutoCADExportOption
********************************************************************************

+---------------------------------------------+-------------+
|                    Value                    | Description |
+=============================================+=============+
| ``AutoCADExportOption.PreserveAppearance``  | todo        |
+---------------------------------------------+-------------+
| ``AutoCADExportOption.MaximizeEditability`` | todo        |
+---------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADGlobalScaleOption:

AutoCADGlobalScaleOption
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``AutoCADGlobalScaleOption.OriginalSize`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADGlobalScaleOption.ScaleByValue`` | todo        |
+-------------------------------------------+-------------+
| ``AutoCADGlobalScaleOption.FitArtboard``  | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADRasterFormat:

AutoCADRasterFormat
********************************************************************************

+------------------------------+-------------+
|            Value             | Description |
+==============================+=============+
| ``AutoCADRasterFormat.PNG``  | todo        |
+------------------------------+-------------+
| ``AutoCADRasterFormat.JPEG`` | todo        |
+------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoCADUnit:

AutoCADUnit
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``AutoCADUnit.Points``      | todo        |
+-----------------------------+-------------+
| ``AutoCADUnit.Picas``       | todo        |
+-----------------------------+-------------+
| ``AutoCADUnit.Inches``      | todo        |
+-----------------------------+-------------+
| ``AutoCADUnit.Millimeters`` | todo        |
+-----------------------------+-------------+
| ``AutoCADUnit.Centimeters`` | todo        |
+-----------------------------+-------------+
| ``AutoCADUnit.Pixels``      | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoKernType:

AutoKernType
********************************************************************************

+-----------------------------------+-------------+
|               Value               | Description |
+===================================+=============+
| ``AutoKernType.NOAUTOKERN``       | todo        |
+-----------------------------------+-------------+
| ``AutoKernType.AUTO``             | todo        |
+-----------------------------------+-------------+
| ``AutoKernType.OPTICAL``          | todo        |
+-----------------------------------+-------------+
| ``AutoKernType.METRICSROMANONLY`` | todo        |
+-----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.AutoLeadingType:

AutoLeadingType
********************************************************************************

+------------------------------------+-------------+
|               Value                | Description |
+====================================+=============+
| ``AutoLeadingType.BOTTOMTOBOTTOM`` | todo        |
+------------------------------------+-------------+
| ``AutoLeadingType.TOPTOTOP``       | todo        |
+------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.BaselineDirectionType:

BaselineDirectionType
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``BaselineDirectionType.Standard``        | todo        |
+-------------------------------------------+-------------+
| ``BaselineDirectionType.VerticalRotated`` | todo        |
+-------------------------------------------+-------------+
| ``BaselineDirectionType.TateChuYoko``     | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.BlendAnimationType:

BlendAnimationType
********************************************************************************

+-----------------------------------------+-------------+
|                  Value                  | Description |
+=========================================+=============+
| ``BlendAnimationType.INBUILD``          | todo        |
+-----------------------------------------+-------------+
| ``BlendAnimationType.NOBLENDANIMATION`` | todo        |
+-----------------------------------------+-------------+
| ``BlendAnimationType.INSEQUENCE``       | todo        |
+-----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.BlendModes:

BlendModes
********************************************************************************

The blend mode used when compositing an object.

+--------------------------------+-------------+
|             Value              | Description |
+================================+=============+
| ``BlendModes.COLORBLEND``      | todo        |
+--------------------------------+-------------+
| ``BlendModes.COLORBURN``       | todo        |
+--------------------------------+-------------+
| ``BlendModes.COLORDODGE``      | todo        |
+--------------------------------+-------------+
| ``BlendModes.DARKEN``          | todo        |
+--------------------------------+-------------+
| ``BlendModes.DIFFERENCE``      | todo        |
+--------------------------------+-------------+
| ``BlendModes.EXCLUSION``       | todo        |
+--------------------------------+-------------+
| ``BlendModes.HARDLIGHT``       | todo        |
+--------------------------------+-------------+
| ``BlendModes.HUE``             | todo        |
+--------------------------------+-------------+
| ``BlendModes.LIGHTEN``         | todo        |
+--------------------------------+-------------+
| ``BlendModes.LUMINOSITY``      | todo        |
+--------------------------------+-------------+
| ``BlendModes.MULTIPLY``        | todo        |
+--------------------------------+-------------+
| ``BlendModes.NORMAL``          | todo        |
+--------------------------------+-------------+
| ``BlendModes.OVERLAY``         | todo        |
+--------------------------------+-------------+
| ``BlendModes.SATURATIONBLEND`` | todo        |
+--------------------------------+-------------+
| ``BlendModes.SCREEN``          | todo        |
+--------------------------------+-------------+
| ``BlendModes.SOFTLIGHT``       | todo        |
+--------------------------------+-------------+

----

.. _jsobjref/scripting-constants.BlendsExpandPolicy:

BlendsExpandPolicy
********************************************************************************

Policy used by FXG file format to expand blends.

+---------------------------------------------------+-------------+
|                       Value                       | Description |
+===================================================+=============+
| ``BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS`` | todo        |
+---------------------------------------------------+-------------+
| ``BlendsExpandPolicy.RASTERIZEBLENDS``            | todo        |
+---------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.BurasagariTypeEnum:

BurasagariTypeEnum
********************************************************************************

+---------------------------------+-------------+
|              Value              | Description |
+=================================+=============+
| ``BurasagariTypeEnum.Forced``   | todo        |
+---------------------------------+-------------+
| ``BurasagariTypeEnum.None``     | todo        |
+---------------------------------+-------------+
| ``BurasagariTypeEnum.Standard`` | todo        |
+---------------------------------+-------------+

----

.. _jsobjref/scripting-constants.CaseChangeType:

CaseChangeType
********************************************************************************

+---------------------------------+-------------+
|              Value              | Description |
+=================================+=============+
| ``CaseChangeType.LOWERCASE``    | todo        |
+---------------------------------+-------------+
| ``CaseChangeType.SENTENCECASE`` | todo        |
+---------------------------------+-------------+
| ``CaseChangeType.TITLECASE``    | todo        |
+---------------------------------+-------------+
| ``CaseChangeType.UPPERCASE``    | todo        |
+---------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorConversion:

ColorConversion
********************************************************************************

+----------------------------------------------+-------------+
|                    Value                     | Description |
+==============================================+=============+
| ``ColorConversion.COLORCONVERSIONREPURPOSE`` | todo        |
+----------------------------------------------+-------------+
| ``ColorConversion.COLORCONVERSIONTODEST``    | todo        |
+----------------------------------------------+-------------+
| ``ColorConversion.None``                     | todo        |
+----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorConvertPurpose:

ColorConvertPurpose
********************************************************************************

The purpose of color conversion using the ``ConvertSampleColor`` method of the ``Application`` class.

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``ColorConvertPurpose.defaultpurpose`` | todo        |
+----------------------------------------+-------------+
| ``ColorConvertPurpose.exportpurpose``  | todo        |
+----------------------------------------+-------------+
| ``ColorConvertPurpose.previewpurpose`` | todo        |
+----------------------------------------+-------------+
| ``ColorConvertPurpose.dummypurpose``   | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorDestination:

ColorDestination
********************************************************************************

+--------------------------------------------------+-------------+
|                      Value                       | Description |
+==================================================+=============+
| ``ColorDestination.COLORDESTINATIONDOCCMYK``     | todo        |
+--------------------------------------------------+-------------+
| ``ColorDestination.COLORDESTINATIONDOCRGB``      | todo        |
+--------------------------------------------------+-------------+
| ``ColorDestination.COLORDESTINATIONPROFILE``     | todo        |
+--------------------------------------------------+-------------+
| ``ColorDestination.COLORDESTINATIONWORKINGCMYK`` | todo        |
+--------------------------------------------------+-------------+
| ``ColorDestination.COLORDESTINATIONWORKINGRGB``  | todo        |
+--------------------------------------------------+-------------+
| ``ColorDestination.None``                        | todo        |
+--------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorDitherMethod:

ColorDitherMethod
********************************************************************************

The method used to dither colors in exported GIF and PNG8 images.

+-------------------------------------+-------------+
|                Value                | Description |
+=====================================+=============+
| ``ColorDitherMethod.DIFFUSION``     | todo        |
+-------------------------------------+-------------+
| ``ColorDitherMethod.NOISE``         | todo        |
+-------------------------------------+-------------+
| ``ColorDitherMethod.NOREDUCTION``   | todo        |
+-------------------------------------+-------------+
| ``ColorDitherMethod.PATTERNDITHER`` | todo        |
+-------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorModel:

ColorModel
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``ColorModel.PROCESS``      | todo        |
+-----------------------------+-------------+
| ``ColorModel.REGISTRATION`` | todo        |
+-----------------------------+-------------+
| ``ColorModel.SPOT``         | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorProfile:

ColorProfile
********************************************************************************

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``ColorProfile.INCLUDEALLPROFILE``     | todo        |
+----------------------------------------+-------------+
| ``ColorProfile.INCLUDEDESTPROFILE``    | todo        |
+----------------------------------------+-------------+
| ``ColorProfile.INCLUDERGBPROFILE``     | todo        |
+----------------------------------------+-------------+
| ``ColorProfile.LEAVEPROFILEUNCHANGED`` | todo        |
+----------------------------------------+-------------+
| ``ColorProfile.None``                  | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorReductionMethod:

ColorReductionMethod
********************************************************************************

The method used to reduce the number of colors in exported GIF and PNG8 images.

+-------------------------------------+-------------+
|                Value                | Description |
+=====================================+=============+
| ``ColorReductionMethod.ADAPTIVE``   | todo        |
+-------------------------------------+-------------+
| ``ColorReductionMethod.SELECTIVE``  | todo        |
+-------------------------------------+-------------+
| ``ColorReductionMethod.PERCEPTUAL`` | todo        |
+-------------------------------------+-------------+
| ``ColorReductionMethod.WEB``        | todo        |
+-------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ColorType:

ColorType
********************************************************************************

The color specification for an individual color.

+------------------------+-------------+
|         Value          | Description |
+========================+=============+
| ``ColorType.CMYK``     | todo        |
+------------------------+-------------+
| ``ColorType.GRADIENT`` | todo        |
+------------------------+-------------+
| ``ColorType.GRAY``     | todo        |
+------------------------+-------------+
| ``ColorType.PATTERN``  | todo        |
+------------------------+-------------+
| ``ColorType.RGB``      | todo        |
+------------------------+-------------+
| ``ColorType.SPOT``     | todo        |
+------------------------+-------------+
| ``ColorType.NONE``     | todo        |
+------------------------+-------------+

----

.. _jsobjref/scripting-constants.Compatibility:

Compatibility
********************************************************************************

The version of the Illustrator file to create when saving an EPS or Illustrator file

+------------------------------------+-------------+
|               Value                | Description |
+====================================+=============+
| ``Compatibility.ILLUSTRATOR8``     | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR9``     | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR10``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR11``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR12``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR13``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR14``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR15``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR16``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR17``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.ILLUSTRATOR19``    | todo        |
+------------------------------------+-------------+
| ``Compatibility.JAPANESEVERSION3`` | todo        |
+------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.CompressionQuality:

CompressionQuality
********************************************************************************

The quality of bitmap compression used when saving a PDF file

+--------------------------------------------------+-------------+
|                      Value                       | Description |
+==================================================+=============+
| ``CompressionQuality.AUTOMATICJPEG2000HIGH``     | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEG2000LOSSLESS`` | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEG2000LOW``      | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEG2000MAXIMUM``  | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEG2000MEDIUM``   | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEG2000MINIMUM``  | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEGHIGH``         | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEGLOW``          | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEGMAXIMUM``      | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEGMEDIUM``       | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.AUTOMATICJPEGMINIMUM``      | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000HIGH``              | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000LOSSLESS``          | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000LOW``               | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000MAXIMUM``           | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000MEDIUM``            | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEG2000MINIMUM``           | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEGHIGH``                  | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEGLOW``                   | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEGMAXIMUM``               | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEGMEDIUM``                | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.JPEGMINIMUM``               | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.ZIP4BIT``                   | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.ZIP8BIT``                   | todo        |
+--------------------------------------------------+-------------+
| ``CompressionQuality.None``                      | todo        |
+--------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.CoordinateSystem:

CoordinateSystem
********************************************************************************

The coordinate system used by Illustrator

+-----------------------------------------------+-------------+
|                     Value                     | Description |
+===============================================+=============+
| ``CoordinateSystem.ARTBOARDCOORDINATESYSTEM`` | todo        |
+-----------------------------------------------+-------------+
| ``CoordinateSystem.DOCUMENTCOORDINATESYSTEM`` | todo        |
+-----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.CropOptions:

CropOptions
********************************************************************************

The style of a document’s cropping box

+--------------------------+-------------+
|          Value           | Description |
+==========================+=============+
| ``CropOptions.Japanese`` | todo        |
+--------------------------+-------------+
| ``CropOptions.Standard`` | todo        |
+--------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentArtboardLayout:

DocumentArtboardLayout
********************************************************************************

The layout of in the new document.

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``DocumentArtboardLayout.Column``      | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.GridByCol``   | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.GridByRow``   | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.RLGridByCol`` | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.RLGridByRow`` | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.RLRow``       | todo        |
+----------------------------------------+-------------+
| ``DocumentArtboardLayout.Row``         | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentColorSpace:

DocumentColorSpace
********************************************************************************

The color space of a document

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``DocumentColorSpace.CMYK`` | todo        |
+-----------------------------+-------------+
| ``DocumentColorSpace.RGB``  | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentLayoutStyle:

DocumentLayoutStyle
********************************************************************************

The color space of a document.

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``DocumentLayoutStyle.CASCADE``        | todo        |
+----------------------------------------+-------------+
| ``DocumentLayoutStyle.CONSOLIDATEALL`` | todo        |
+----------------------------------------+-------------+
| ``DocumentLayoutStyle.FLOATALL``       | todo        |
+----------------------------------------+-------------+
| ``DocumentLayoutStyle.HORIZONTALTILE`` | todo        |
+----------------------------------------+-------------+
| ``DocumentLayoutStyle.VERTICALTILE``   | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentPresetType:

DocumentPresetType
********************************************************************************

The preset types available for new documents.

+----------------------------------+-------------+
|              Value               | Description |
+==================================+=============+
| ``DocumentPresetType.BasicCMYK`` | todo        |
+----------------------------------+-------------+
| ``DocumentPresetType.BasicRGB``  | todo        |
+----------------------------------+-------------+
| ``DocumentPresetType.Mobile``    | todo        |
+----------------------------------+-------------+
| ``DocumentPresetType.Print``     | todo        |
+----------------------------------+-------------+
| ``DocumentPresetType.Video``     | todo        |
+----------------------------------+-------------+
| ``DocumentPresetType.Web``       | todo        |
+----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentPreviewMode:

DocumentPreviewMode
********************************************************************************

The document preview mode.

+------------------------------------------+-------------+
|                  Value                   | Description |
+==========================================+=============+
| ``DocumentPreviewMode.DefaultPreview``   | todo        |
+------------------------------------------+-------------+
| ``DocumentPreviewMode.OverprintPreview`` | todo        |
+------------------------------------------+-------------+
| ``DocumentPreviewMode.PixelPreview``     | todo        |
+------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentRasterResolution:

DocumentRasterResolution
********************************************************************************

The preset document raster resolution.

+-----------------------------------------------+-------------+
|                     Value                     | Description |
+===============================================+=============+
| ``DocumentRasterResolution.ScreenResolution`` | todo        |
+-----------------------------------------------+-------------+
| ``DocumentRasterResolution.HighResolution``   | todo        |
+-----------------------------------------------+-------------+
| ``DocumentRasterResolution.MediumResolution`` | todo        |
+-----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentTransparencyGrid:

DocumentTransparencyGrid
********************************************************************************

Document transparency grid colors.

+-----------------------------------------------------+-------------+
|                        Value                        | Description |
+=====================================================+=============+
| ``DocumentTransparencyGrid.TransparencyGridBlue``   | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridDark``   | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridGreen``  | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridLight``  | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridMedium`` | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridNone``   | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridOrange`` | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridPurple`` | todo        |
+-----------------------------------------------------+-------------+
| ``DocumentTransparencyGrid.TransparencyGridRed``    | todo        |
+-----------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DocumentType:

DocumentType
********************************************************************************

The file format used to save a file.

+------------------------------+-------------+
|            Value             | Description |
+==============================+=============+
| ``DocumentType.EPS``         | todo        |
+------------------------------+-------------+
| ``DocumentType.FXG``         | todo        |
+------------------------------+-------------+
| ``DocumentType.ILLUSTRATOR`` | todo        |
+------------------------------+-------------+
| ``DocumentType.PDF``         | todo        |
+------------------------------+-------------+

----

.. _jsobjref/scripting-constants.DownsampleMethod:

DownsampleMethod
********************************************************************************

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``DownsampleMethod.AVERAGEDOWNSAMPLE`` | todo        |
+----------------------------------------+-------------+
| ``DownsampleMethod.BICUBICDOWNSAMPLE`` | todo        |
+----------------------------------------+-------------+
| ``DownsampleMethod.NODOWNSAMPLE``      | todo        |
+----------------------------------------+-------------+
| ``DownsampleMethod.SUBSAMPLE``         | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ElementPlacement:

ElementPlacement
********************************************************************************

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``ElementPlacement.INSIDE``           | todo        |
+---------------------------------------+-------------+
| ``ElementPlacement.PLACEAFTER``       | todo        |
+---------------------------------------+-------------+
| ``ElementPlacement.PLACEATBEGINNING`` | todo        |
+---------------------------------------+-------------+
| ``ElementPlacement.PLACEATEND``       | todo        |
+---------------------------------------+-------------+
| ``ElementPlacement.PLACEBEFORE``      | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.EPSPostScriptLevelEnum:

EPSPostScriptLevelEnum
********************************************************************************

+-----------------------------------+-------------+
|               Value               | Description |
+===================================+=============+
| ``EPSPostScriptLevelEnum.LEVEL2`` | todo        |
+-----------------------------------+-------------+
| ``EPSPostScriptLevelEnum.LEVEL3`` | todo        |
+-----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.EPSPreview:

EPSPreview
********************************************************************************

The preview image format used when saving an EPS file

+-------------------------------------+-------------+
|                Value                | Description |
+=====================================+=============+
| ``EPSPreview.BWTIFF``               | todo        |
+-------------------------------------+-------------+
| ``EPSPreview.COLORTIFF``            | todo        |
+-------------------------------------+-------------+
| ``EPSPreview.TRANSPARENTCOLORTIFF`` | todo        |
+-------------------------------------+-------------+
| ``EPSPreview.None``                 | todo        |
+-------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ExportType:

ExportType
********************************************************************************

The file format used to export a file

+--------------------------+-------------+
|          Value           | Description |
+==========================+=============+
| ``ExportType.AutoCAD``   | todo        |
+--------------------------+-------------+
| ``ExportType.FLASH``     | todo        |
+--------------------------+-------------+
| ``ExportType.GIF``       | todo        |
+--------------------------+-------------+
| ``ExportType.JPEG``      | todo        |
+--------------------------+-------------+
| ``ExportType.Photoshop`` | todo        |
+--------------------------+-------------+
| ``ExportType.PNG24``     | todo        |
+--------------------------+-------------+
| ``ExportType.PNG8``      | todo        |
+--------------------------+-------------+
| ``ExportType.SVG``       | todo        |
+--------------------------+-------------+
| ``ExportType.TIFF``      | todo        |
+--------------------------+-------------+

----

.. _jsobjref/scripting-constants.FigureStyleType:

FigureStyleType
********************************************************************************

+------------------------------------------+-------------+
|                  Value                   | Description |
+==========================================+=============+
| ``FigureStyleType.DEFAULTFIGURESTYLE``   | todo        |
+------------------------------------------+-------------+
| ``FigureStyleType.PROPORTIONAL``         | todo        |
+------------------------------------------+-------------+
| ``FigureStyleType.PROPORTIONALOLDSTYLE`` | todo        |
+------------------------------------------+-------------+
| ``FigureStyleType.TABULAR``              | todo        |
+------------------------------------------+-------------+
| ``FigureStyleType.TABULAROLDSTYLE``      | todo        |
+------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FiltersPreservePolicy:

FiltersPreservePolicy
********************************************************************************

The filters preserve policy used by the FXG file format.

+-----------------------------------------------+-------------+
|                     Value                     | Description |
+===============================================+=============+
| ``FiltersPreservePolicy.EXPANDFILTERS``       | todo        |
+-----------------------------------------------+-------------+
| ``FiltersPreservePolicy.KEEPFILTERSEDITABLE`` | todo        |
+-----------------------------------------------+-------------+
| ``FiltersPreservePolicy.RASTERIZEFILTERS``    | todo        |
+-----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FlashExportStyle:

FlashExportStyle
********************************************************************************

The method used to convert Illustrator images when exporting files

+--------------------------------------+-------------+
|                Value                 | Description |
+======================================+=============+
| ``FlashExportStyle.ASFLASHFILE``     | todo        |
+--------------------------------------+-------------+
| ``FlashExportStyle.LAYERSASFILES``   | todo        |
+--------------------------------------+-------------+
| ``FlashExportStyle.LAYERSASFRAMES``  | todo        |
+--------------------------------------+-------------+
| ``FlashExportStyle.LAYERSASSYMBOLS`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportStyle.TOFILES``         | todo        |
+--------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FlashExportVersion:

FlashExportVersion
********************************************************************************

Version for exported SWF file.

+--------------------------------------+-------------+
|                Value                 | Description |
+======================================+=============+
| ``FlashExportVersion.FlashVersion1`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion2`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion3`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion4`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion5`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion6`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion7`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion8`` | todo        |
+--------------------------------------+-------------+
| ``FlashExportVersion.FlashVersion9`` | todo        |
+--------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FlashImageFormat:

FlashImageFormat
********************************************************************************

The format used to store flash images.

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``FlashImageFormat.LOSSLESS`` | todo        |
+-------------------------------+-------------+
| ``FlashImageFormat.LOSSY``    | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FlashJPEGMethod:

FlashJPEGMethod
********************************************************************************

The method used to store JPEG images.

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``FlashJPEGMethod.Optimized`` | todo        |
+-------------------------------+-------------+
| ``FlashJPEGMethod.Standard``  | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FlashPlaybackSecurity:

FlashPlaybackSecurity
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``FlashPlaybackSecurity.PlaybackLocal``   | todo        |
+-------------------------------------------+-------------+
| ``FlashPlaybackSecurity.PlaybackNetwork`` | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FontBaselineOption:

FontBaselineOption
********************************************************************************

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``FontBaselineOption.NORMALBASELINE`` | todo        |
+---------------------------------------+-------------+
| ``FontBaselineOption.SUPERSCRIPT``    | todo        |
+---------------------------------------+-------------+
| ``FontBaselineOption.SUBSCRIPT``      | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FontCapsOption:

FontCapsOption
********************************************************************************

+---------------------------------+-------------+
|              Value              | Description |
+=================================+=============+
| ``FontCapsOption.ALLCAPS``      | todo        |
+---------------------------------+-------------+
| ``FontCapsOption.ALLSMALLCAPS`` | todo        |
+---------------------------------+-------------+
| ``FontCapsOption.NORMALCAPS``   | todo        |
+---------------------------------+-------------+
| ``FontCapsOption.SMALLCAPS``    | todo        |
+---------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FontOpenTypePositionOption:

FontOpenTypePositionOption
********************************************************************************

+----------------------------------------------------+-------------+
|                       Value                        | Description |
+====================================================+=============+
| ``FontOpenTypePositionOption.DENOMINATOR``         | todo        |
+----------------------------------------------------+-------------+
| ``FontOpenTypePositionOption.NUMERATOR``           | todo        |
+----------------------------------------------------+-------------+
| ``FontOpenTypePositionOption.OPENTYPEDEFAULT``     | todo        |
+----------------------------------------------------+-------------+
| ``FontOpenTypePositionOption.OPENTYPESUBSCRIPT``   | todo        |
+----------------------------------------------------+-------------+
| ``FontOpenTypePositionOption.OPENTYPESUPERSCRIPT`` | todo        |
+----------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FontSubstitutionPolicy:

FontSubstitutionPolicy
********************************************************************************

+----------------------------------------------+-------------+
|                    Value                     | Description |
+==============================================+=============+
| ``FontSubstitutionPolicy.SUBSTITUTEDEVICE``  | todo        |
+----------------------------------------------+-------------+
| ``FontSubstitutionPolicy.SUBSTITUTEOBLIQUE`` | todo        |
+----------------------------------------------+-------------+
| ``FontSubstitutionPolicy.SUBSTITUTETINT``    | todo        |
+----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.FXGVersion:

FXGVersion
********************************************************************************

The FXG file-format version.

+----------------------------+-------------+
|           Value            | Description |
+============================+=============+
| ``FXGVersion.VERSION1PT0`` | todo        |
+----------------------------+-------------+
| ``FXGVersion.VERSION2PT0`` | todo        |
+----------------------------+-------------+

----

.. _jsobjref/scripting-constants.GradientsPreservePolicy:

GradientsPreservePolicy
********************************************************************************

The gradients preserve policy used by the FXG file format.

+-----------------------------------------------------------+-------------+
|                           Value                           | Description |
+===========================================================+=============+
| ``GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS`` | todo        |
+-----------------------------------------------------------+-------------+
| ``GradientsPreservePolicy.KEEPGRADIENTSEDITABLE``         | todo        |
+-----------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.GradientType:

GradientType
********************************************************************************

The type of gradient.

+-------------------------+-------------+
|          Value          | Description |
+=========================+=============+
| ``GradientType.LINEAR`` | todo        |
+-------------------------+-------------+
| ``GradientType.RADIAL`` | todo        |
+-------------------------+-------------+

----

.. _jsobjref/scripting-constants.ImageColorSpace:

ImageColorSpace
********************************************************************************

The color space of a raster item or an exported file

+--------------------------------+-------------+
|             Value              | Description |
+================================+=============+
| ``ImageColorSpace.CMYK``       | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.DeviceN``    | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.Grayscale``  | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.Indexed``    | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.LAB``        | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.RGB``        | todo        |
+--------------------------------+-------------+
| ``ImageColorSpace.Separation`` | todo        |
+--------------------------------+-------------+

----

.. _jsobjref/scripting-constants.InkPrintStatus:

InkPrintStatus
********************************************************************************

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``InkPrintStatus.CONVERTINK`` | todo        |
+-------------------------------+-------------+
| ``InkPrintStatus.ENABLEINK``  | todo        |
+-------------------------------+-------------+
| ``InkPrintStatus.DISABLEINK`` | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.InkType:

InkType
********************************************************************************

+------------------------+-------------+
|         Value          | Description |
+========================+=============+
| ``InkType.BLACKINK``   | todo        |
+------------------------+-------------+
| ``InkType.CUSTOMINK``  | todo        |
+------------------------+-------------+
| ``InkType.CYANINK``    | todo        |
+------------------------+-------------+
| ``InkType.MAGENTAINK`` | todo        |
+------------------------+-------------+
| ``InkType.YELLOWINK``  | todo        |
+------------------------+-------------+

----

.. _jsobjref/scripting-constants.JavaScriptExecutionMode:

JavaScriptExecutionMode
********************************************************************************

+--------------------------------------------+-------------+
|                   Value                    | Description |
+============================================+=============+
| ``JavaScriptExecutionMode.BeforeRunning``  | todo        |
+--------------------------------------------+-------------+
| ``JavaScriptExecutionMode.OnRuntimeError`` | todo        |
+--------------------------------------------+-------------+
| ``JavaScriptExecutionMode.never``          | todo        |
+--------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.Justification:

Justification
********************************************************************************

The alignment or justification for a paragraph of text.

+---------------------------------------------+-------------+
|                    Value                    | Description |
+=============================================+=============+
| ``Justification.CENTER``                    | todo        |
+---------------------------------------------+-------------+
| ``Justification.FULLJUSTIFY``               | todo        |
+---------------------------------------------+-------------+
| ``Justification.FULLJUSTIFYLASTLINECENTER`` | todo        |
+---------------------------------------------+-------------+
| ``Justification.FULLJUSTIFYLASTLINELEFT``   | todo        |
+---------------------------------------------+-------------+
| ``Justification.FULLJUSTIFYLASTLINERIGHT``  | todo        |
+---------------------------------------------+-------------+
| ``Justification.LEFT``                      | todo        |
+---------------------------------------------+-------------+
| ``Justification.RIGHT``                     | todo        |
+---------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.KinsokuOrderEnum:

KinsokuOrderEnum
********************************************************************************

+-----------------------------------+-------------+
|               Value               | Description |
+===================================+=============+
| ``KinsokuOrderEnum.PUSHIN``       | todo        |
+-----------------------------------+-------------+
| ``KinsokuOrderEnum.PUSHOUTFIRST`` | todo        |
+-----------------------------------+-------------+
| ``KinsokuOrderEnum.PUSHOUTONLY``  | todo        |
+-----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.KnockoutState:

KnockoutState
********************************************************************************

The type of knockout to use on a page item.

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``KnockoutState.DISABLED``  | todo        |
+-----------------------------+-------------+
| ``KnockoutState.ENABLED``   | todo        |
+-----------------------------+-------------+
| ``KnockoutState.INHERITED`` | todo        |
+-----------------------------+-------------+
| ``KnockoutState.Unknown``   | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.LanguageType:

LanguageType
********************************************************************************

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``LanguageType.BOKMALNORWEGIAN``       | todo        |
+----------------------------------------+-------------+
| ``LanguageType.BRAZILLIANPORTUGUESE``  | todo        |
+----------------------------------------+-------------+
| ``LanguageType.BULGARIAN``             | todo        |
+----------------------------------------+-------------+
| ``LanguageType.CANADIANFRENCH``        | todo        |
+----------------------------------------+-------------+
| ``LanguageType.CATALAN``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.CHINESE``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.CZECH``                 | todo        |
+----------------------------------------+-------------+
| ``LanguageType.DANISH``                | todo        |
+----------------------------------------+-------------+
| ``LanguageType.DUTCH``                 | todo        |
+----------------------------------------+-------------+
| ``LanguageType.DUTCH2005REFORM``       | todo        |
+----------------------------------------+-------------+
| ``LanguageType.ENGLISH``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.FINNISH``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.GERMAN2006REFORM``      | todo        |
+----------------------------------------+-------------+
| ``LanguageType.GREEK``                 | todo        |
+----------------------------------------+-------------+
| ``LanguageType.HUNGARIAN``             | todo        |
+----------------------------------------+-------------+
| ``LanguageType.ICELANDIC``             | todo        |
+----------------------------------------+-------------+
| ``LanguageType.ITALIAN``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.JAPANESE``              | todo        |
+----------------------------------------+-------------+
| ``LanguageType.NYNORSKNORWEGIAN``      | todo        |
+----------------------------------------+-------------+
| ``LanguageType.OLDGERMAN``             | todo        |
+----------------------------------------+-------------+
| ``LanguageType.POLISH``                | todo        |
+----------------------------------------+-------------+
| ``LanguageType.RUMANIAN``              | todo        |
+----------------------------------------+-------------+
| ``LanguageType.RUSSIAN``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.SERBIAN``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.SPANISH``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.STANDARDFRENCH``        | todo        |
+----------------------------------------+-------------+
| ``LanguageType.STANDARDGERMAN``        | todo        |
+----------------------------------------+-------------+
| ``LanguageType.STANDARDPORTUGUESE``    | todo        |
+----------------------------------------+-------------+
| ``LanguageType.SWEDISH``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.SWISSGERMAN``           | todo        |
+----------------------------------------+-------------+
| ``LanguageType.SWISSGERMAN2006REFORM`` | todo        |
+----------------------------------------+-------------+
| ``LanguageType.TURKISH``               | todo        |
+----------------------------------------+-------------+
| ``LanguageType.UKENGLISH``             | todo        |
+----------------------------------------+-------------+
| ``LanguageType.UKRANIAN``              | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.LayerOrderType:

LayerOrderType
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``LayerOrderType.TOPDOWN``  | todo        |
+-----------------------------+-------------+
| ``LayerOrderType.BOTTOMUP`` | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.LibraryType:

LibraryType
********************************************************************************

Illustrator library type.

+------------------------------------+-------------+
|               Value                | Description |
+====================================+=============+
| ``LibraryType.Brushes``            | todo        |
+------------------------------------+-------------+
| ``LibraryType.GraphicStyles``      | todo        |
+------------------------------------+-------------+
| ``LibraryType.IllustratorArtwork`` | todo        |
+------------------------------------+-------------+
| ``LibraryType.Swatches``           | todo        |
+------------------------------------+-------------+
| ``LibraryType.Symbols``            | todo        |
+------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.MonochromeCompression:

MonochromeCompression
********************************************************************************

The type of compression to use on a monochrome bitmap item when saving a PDF file.

+-------------------------------------+-------------+
|                Value                | Description |
+=====================================+=============+
| ``MonochromeCompression.CCIT3``     | todo        |
+-------------------------------------+-------------+
| ``MonochromeCompression.CCIT4``     | todo        |
+-------------------------------------+-------------+
| ``MonochromeCompression.MONOZIP``   | todo        |
+-------------------------------------+-------------+
| ``MonochromeCompression.None``      | todo        |
+-------------------------------------+-------------+
| ``MonochromeCompression.RUNLENGTH`` | todo        |
+-------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.OutputFlattening:

OutputFlattening
********************************************************************************

How transparency should be flattened when saving EPS and Illustrator file formats with compatibility set to versions of Illustrator earlier than Illustrator 10

+-----------------------------------------+-------------+
|                  Value                  | Description |
+=========================================+=============+
| ``OutputFlattening.PRESERVEAPPEARANCE`` | todo        |
+-----------------------------------------+-------------+
| ``OutputFlattening.PRESERVEPATHS``      | todo        |
+-----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PageMarksTypes:

PageMarksTypes
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``PageMarksTypes.Japanese`` | todo        |
+-----------------------------+-------------+
| ``PageMarksTypes.Roman``    | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.PathPointSelection:

PathPointSelection
********************************************************************************

Which points, if any, of a path are selected.

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``PathPointSelection.ANCHORPOINT``    | todo        |
+---------------------------------------+-------------+
| ``PathPointSelection.LEFTDIRECTION``  | todo        |
+---------------------------------------+-------------+
| ``PathPointSelection.LEFTRIGHTPOINT`` | todo        |
+---------------------------------------+-------------+
| ``PathPointSelection.NOSELECTION``    | todo        |
+---------------------------------------+-------------+
| ``PathPointSelection.RIGHTDIRECTION`` | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFBoxType:

PDFBoxType
********************************************************************************

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``PDFBoxType.PDFARTBOX``      | todo        |
+-------------------------------+-------------+
| ``PDFBoxType.PDFBLEEDBOX``    | todo        |
+-------------------------------+-------------+
| ``PDFBoxType.PDFBOUNDINGBOX`` | todo        |
+-------------------------------+-------------+
| ``PDFBoxType.PDFCROPBOX``     | todo        |
+-------------------------------+-------------+
| ``PDFBoxType.PDFMEDIABOX``    | todo        |
+-------------------------------+-------------+
| ``PDFBoxType.PDFTRIMBOX``     | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFChangesAllowedEnum:

PDFChangesAllowedEnum
********************************************************************************

+-----------------------------------------------+-------------+
|                     Value                     | Description |
+===============================================+=============+
| ``PDFChangesAllowedEnum.CHANGE128ANYCHANGES`` | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE128COMMENTING`` | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE128EDITPAGE``   | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE128FILLFORM``   | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE128NONE``       | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE40ANYCHANGES``  | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE40COMMENTING``  | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE40NONE``        | todo        |
+-----------------------------------------------+-------------+
| ``PDFChangesAllowedEnum.CHANGE40PAGELAYOUT``  | todo        |
+-----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFCompatibility:

PDFCompatibility
********************************************************************************

The version of the Acrobat file format to create when saving a PDF file

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``PDFCompatibility.ACROBAT4`` | todo        |
+-------------------------------+-------------+
| ``PDFCompatibility.ACROBAT5`` | todo        |
+-------------------------------+-------------+
| ``PDFCompatibility.ACROBAT6`` | todo        |
+-------------------------------+-------------+
| ``PDFCompatibility.ACROBAT7`` | todo        |
+-------------------------------+-------------+
| ``PDFCompatibility.ACROBAT8`` | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFOverprint:

PDFOverprint
********************************************************************************

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``PDFOverprint.DISCARDPDFOVERPRINT``  | todo        |
+---------------------------------------+-------------+
| ``PDFOverprint.PRESERVEPDFOVERPRINT`` | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFPrintAllowedEnum:

PDFPrintAllowedEnum
********************************************************************************

+------------------------------------------------+-------------+
|                     Value                      | Description |
+================================================+=============+
| ``PDFPrintAllowedEnum.PRINT128HIGHRESOLUTION`` | todo        |
+------------------------------------------------+-------------+
| ``PDFPrintAllowedEnum.PRINT128LOWRESOLUTION``  | todo        |
+------------------------------------------------+-------------+
| ``PDFPrintAllowedEnum.PRINT128NONE``           | todo        |
+------------------------------------------------+-------------+
| ``PDFPrintAllowedEnum.PRINT40HIGHRESOLUTION``  | todo        |
+------------------------------------------------+-------------+
| ``PDFPrintAllowedEnum.PRINT40NONE``            | todo        |
+------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFTrimMarkWeight:

PDFTrimMarkWeight
********************************************************************************

+------------------------------------------+-------------+
|                  Value                   | Description |
+==========================================+=============+
| ``PDFTrimMarkWeight.TRIMMARKWEIGHT0125`` | todo        |
+------------------------------------------+-------------+
| ``PDFTrimMarkWeight.TRIMMARKWEIGHT025``  | todo        |
+------------------------------------------+-------------+
| ``PDFTrimMarkWeight.TRIMMARKWEIGHT05``   | todo        |
+------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PDFXStandard:

PDFXStandard
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``PDFXStandard.PDFX1A2001`` | todo        |
+-----------------------------+-------------+
| ``PDFXStandard.PDFX1A2003`` | todo        |
+-----------------------------+-------------+
| ``PDFXStandard.PDFX32002``  | todo        |
+-----------------------------+-------------+
| ``PDFXStandard.PDFX32003``  | todo        |
+-----------------------------+-------------+
| ``PDFXStandard.PDFX42007``  | todo        |
+-----------------------------+-------------+
| ``PDFXStandard.PDFXNONE``   | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.PerspectiveGridType:

PerspectiveGridType
********************************************************************************

+-------------------------------------------------------+-------------+
|                         Value                         | Description |
+=======================================================+=============+
| ``PerspectiveGridType.OnePointPerspectiveGridType``   | todo        |
+-------------------------------------------------------+-------------+
| ``PerspectiveGridType.TwoPointPerspectiveGridType``   | todo        |
+-------------------------------------------------------+-------------+
| ``PerspectiveGridType.ThreePointPerspectiveGridType`` | todo        |
+-------------------------------------------------------+-------------+
| ``PerspectiveGridType.InvalidPerspectiveGridType``    | todo        |
+-------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PerspectiveGridPlaneType:

PerspectiveGridPlaneType
********************************************************************************

+---------------------------------------------------+-------------+
|                       Value                       | Description |
+===================================================+=============+
| ``PerspectiveGridPlaneType.GRIDLEFTPLANETYPE``    | todo        |
+---------------------------------------------------+-------------+
| ``PerspectiveGridPlaneType.GRIDRIGHTPLANETYPE``   | todo        |
+---------------------------------------------------+-------------+
| ``PerspectiveGridPlaneType.GRIDFLOORPLANETYPE``   | todo        |
+---------------------------------------------------+-------------+
| ``PerspectiveGridPlaneType.INVALIDGRIDPLANETYPE`` | todo        |
+---------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PhotoshopCompatibility:

PhotoshopCompatibility
********************************************************************************

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``PhotoshopCompatibility.Photoshop6`` | todo        |
+---------------------------------------+-------------+
| ``PhotoshopCompatibility.Photoshop8`` | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PointType:

PointType
********************************************************************************

The type of path point selected

+----------------------+-------------+
|        Value         | Description |
+======================+=============+
| ``PointType.CORNER`` | todo        |
+----------------------+-------------+
| ``PointType.SMOOTH`` | todo        |
+----------------------+-------------+

----

.. _jsobjref/scripting-constants.PolarityValues:

PolarityValues
********************************************************************************

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``PolarityValues.NEGATIVE`` | todo        |
+-----------------------------+-------------+
| ``PolarityValues.POSITIVE`` | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.PostScriptImageCompressionType:

PostScriptImageCompressionType
********************************************************************************

+---------------------------------------------------------+-------------+
|                          Value                          | Description |
+=========================================================+=============+
| ``PostScriptImageCompressionType.IMAGECOMPRESSIONNONE`` | todo        |
+---------------------------------------------------------+-------------+
| ``PostScriptImageCompressionType.JPEG``                 | todo        |
+---------------------------------------------------------+-------------+
| ``PostScriptImageCompressionType.RLE``                  | todo        |
+---------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintArtworkDesignation:

PrintArtworkDesignation
********************************************************************************

+----------------------------------------------------+-------------+
|                       Value                        | Description |
+====================================================+=============+
| ``PrintArtworkDesignation.ALLLAYERS``              | todo        |
+----------------------------------------------------+-------------+
| ``PrintArtworkDesignation.VISIBLELAYERS``          | todo        |
+----------------------------------------------------+-------------+
| ``PrintArtworkDesignation.VISIBLEPRINTABLELAYERS`` | todo        |
+----------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintColorIntent:

PrintColorIntent
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``PrintColorIntent.ABSOLUTECOLORIMETRIC`` | todo        |
+-------------------------------------------+-------------+
| ``PrintColorIntent.PERCEPTUALINTENT``     | todo        |
+-------------------------------------------+-------------+
| ``PrintColorIntent.RELATIVECOLORIMETRIC`` | todo        |
+-------------------------------------------+-------------+
| ``PrintColorIntent.SATURATIONINTENT``     | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintColorProfile:

PrintColorProfile
********************************************************************************

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``PrintColorProfile.CUSTOMPROFILE``   | todo        |
+---------------------------------------+-------------+
| ``PrintColorProfile.PRINTERPROFILE``  | todo        |
+---------------------------------------+-------------+
| ``PrintColorProfile.OLDSTYLEPROFILE`` | todo        |
+---------------------------------------+-------------+
| ``PrintColorProfile.SOURCEPROFILE``   | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintColorSeparationMode:

PrintColorSeparationMode
********************************************************************************

+--------------------------------------------------+-------------+
|                      Value                       | Description |
+==================================================+=============+
| ``PrintColorSeparationMode.COMPOSITE``           | todo        |
+--------------------------------------------------+-------------+
| ``PrintColorSeparationMode.HOSTBASEDSEPARATION`` | todo        |
+--------------------------------------------------+-------------+
| ``PrintColorSeparationMode.INRIPSEPARATION``     | todo        |
+--------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrinterColorMode:

PrinterColorMode
********************************************************************************

+-------------------------------------------+-------------+
|                   Value                   | Description |
+===========================================+=============+
| ``PrinterColorMode.BLACKANDWHITEPRINTER`` | todo        |
+-------------------------------------------+-------------+
| ``PrinterColorMode.COLORPRINTER``         | todo        |
+-------------------------------------------+-------------+
| ``PrinterColorMode.GRAYSCALEPRINTER``     | todo        |
+-------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrinterPostScriptLevelEnum:

PrinterPostScriptLevelEnum
********************************************************************************

+-----------------------------------------+-------------+
|                  Value                  | Description |
+=========================================+=============+
| ``PrinterPostScriptLevelEnum.PSLEVEL1`` | todo        |
+-----------------------------------------+-------------+
| ``PrinterPostScriptLevelEnum.PSLEVEL2`` | todo        |
+-----------------------------------------+-------------+
| ``PrinterPostScriptLevelEnum.PSLEVEL3`` | todo        |
+-----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrinterTypeEnum:

PrinterTypeEnum
********************************************************************************

+------------------------------------------+-------------+
|                  Value                   | Description |
+==========================================+=============+
| ``PrinterTypeEnum.NONPOSTSCRIPTPRINTER`` | todo        |
+------------------------------------------+-------------+
| ``PrinterTypeEnum.POSTSCRIPTPRINTER``    | todo        |
+------------------------------------------+-------------+
| ``PrinterTypeEnum.Unknown``              | todo        |
+------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintFontDownloadMode:

PrintFontDownloadMode
********************************************************************************

+--------------------------------------------+-------------+
|                   Value                    | Description |
+============================================+=============+
| ``PrintFontDownloadMode.DOWNLOADNONE``     | todo        |
+--------------------------------------------+-------------+
| ``PrintFontDownloadMode.DOWNLOADCOMPLETE`` | todo        |
+--------------------------------------------+-------------+
| ``PrintFontDownloadMode.DOWNLOADSUBSET``   | todo        |
+--------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintingBounds:

PrintingBounds
********************************************************************************

+-----------------------------------+-------------+
|               Value               | Description |
+===================================+=============+
| ``PrintingBounds.ARTBOARDBOUNDS`` | todo        |
+-----------------------------------+-------------+
| ``PrintingBounds.ARTWORKBOUNDS``  | todo        |
+-----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintOrientation:

PrintOrientation
********************************************************************************

The artwork printing orientation.

+---------------------------------------+-------------+
|                 Value                 | Description |
+=======================================+=============+
| ``PrintOrientation.AUTOROTATE``       | todo        |
+---------------------------------------+-------------+
| ``PrintOrientation.LANDSCAPE``        | todo        |
+---------------------------------------+-------------+
| ``PrintOrientation.PORTRAIT``         | todo        |
+---------------------------------------+-------------+
| ``PrintOrientation.REVERSELANDSCAPE`` | todo        |
+---------------------------------------+-------------+
| ``PrintOrientation.REVERSEPORTRAIT``  | todo        |
+---------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintPosition:

PrintPosition
********************************************************************************

+----------------------------------------+-------------+
|                 Value                  | Description |
+========================================+=============+
| ``.PrintPositionTRANSLATEBOTTOM``      | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATEBOTTOMLEFT``  | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATEBOTTOMRIGHT`` | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATECENTER``      | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATELEFT``        | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATERIGHT``       | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATETOP``         | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATETOPLEFT``     | todo        |
+----------------------------------------+-------------+
| ``.PrintPositionTRANSLATETOPRIGHT``    | todo        |
+----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.PrintTiling:

PrintTiling
********************************************************************************

+------------------------------------+-------------+
|               Value                | Description |
+====================================+=============+
| ``PrintTiling.TILEFULLPAGES``      | todo        |
+------------------------------------+-------------+
| ``PrintTiling.TILESINGLEFULLPAGE`` | todo        |
+------------------------------------+-------------+
| ``PrintTiling.TILEIMAGEABLEAREAS`` | todo        |
+------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.RasterizationColorModel:

RasterizationColorModel
********************************************************************************

The color model for the rasterization.

+-----------------------------------------------+-------------+
|                     Value                     | Description |
+===============================================+=============+
| ``RasterizationColorModel.BITMAP``            | todo        |
+-----------------------------------------------+-------------+
| ``RasterizationColorModel.DEFAULTCOLORMODEL`` | todo        |
+-----------------------------------------------+-------------+
| ``RasterizationColorModel.GRAYSCALE``         | todo        |
+-----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.RasterLinkState:

RasterLinkState
********************************************************************************

The status of a raster item’s linked image if the image is stored externally

+----------------------------------+-------------+
|              Value               | Description |
+==================================+=============+
| ``RasterLinkState.DATAFROMFILE`` | todo        |
+----------------------------------+-------------+
| ``RasterLinkState.DATAMODIFIED`` | todo        |
+----------------------------------+-------------+
| ``RasterLinkState.NODATA``       | todo        |
+----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.RulerUnits:

RulerUnits
********************************************************************************

The default measurement units for the rulers of a document

+----------------------------+-------------+
|           Value            | Description |
+============================+=============+
| ``RulerUnits.Centimeters`` | todo        |
+----------------------------+-------------+
| ``RulerUnits.Qs``          | todo        |
+----------------------------+-------------+
| ``RulerUnits.Inches``      | todo        |
+----------------------------+-------------+
| ``RulerUnits.Pixels``      | todo        |
+----------------------------+-------------+
| ``RulerUnits.Millimeters`` | todo        |
+----------------------------+-------------+
| ``RulerUnits.Unknown``     | todo        |
+----------------------------+-------------+
| ``RulerUnits.Picas``       | todo        |
+----------------------------+-------------+
| ``RulerUnits.Points``      | todo        |
+----------------------------+-------------+

----

.. _jsobjref/scripting-constants.SaveOptions:

SaveOptions
********************************************************************************

Save options provided when closing a document.

+-------------------------------------+-------------+
|                Value                | Description |
+=====================================+=============+
| ``SaveOptions.DONOTSAVECHANGES``    | todo        |
+-------------------------------------+-------------+
| ``SaveOptions.SAVECHANGES``         | todo        |
+-------------------------------------+-------------+
| ``SaveOptions.PROMPTTOSAVECHANGES`` | todo        |
+-------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ScreenMode:

ScreenMode
********************************************************************************

The mode of display for a view.

+----------------------------+-------------+
|           Value            | Description |
+============================+=============+
| ``ScreenMode.DESKTOP``     | todo        |
+----------------------------+-------------+
| ``ScreenMode.MULTIWINDOW`` | todo        |
+----------------------------+-------------+
| ``ScreenMode.FULLSCREEN``  | todo        |
+----------------------------+-------------+

----

.. _jsobjref/scripting-constants.SpotColorKind:

SpotColorKind
********************************************************************************

The custom color kind of a spot color.

+----------------------------+-------------+
|           Value            | Description |
+============================+=============+
| ``SpotColorKind.SpotCMYK`` | todo        |
+----------------------------+-------------+
| ``SpotColorKind.SpotLAB``  | todo        |
+----------------------------+-------------+
| ``SpotColorKind.SpotRGB``  | todo        |
+----------------------------+-------------+

----

.. _jsobjref/scripting-constants.StrokeCap:

StrokeCap
********************************************************************************

The type of line capping for a path stroke.

+--------------------------------+-------------+
|             Value              | Description |
+================================+=============+
| ``StrokeCap.BUTTENDCAP``       | todo        |
+--------------------------------+-------------+
| ``StrokeCap.ROUNDENDCAP``      | todo        |
+--------------------------------+-------------+
| ``StrokeCap.PROJECTINGENDCAP`` | todo        |
+--------------------------------+-------------+

----

.. _jsobjref/scripting-constants.StrokeJoin:

StrokeJoin
********************************************************************************

The type of joints for a path stroke.

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``StrokeJoin.BEVELENDJOIN`` | todo        |
+-----------------------------+-------------+
| ``StrokeJoin.ROUNDENDJOIN`` | todo        |
+-----------------------------+-------------+
| ``StrokeJoin.MITERENDJOIN`` | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.StyleRunAlignmentType:

StyleRunAlignmentType
********************************************************************************

+-----------------------------------------+-------------+
|                  Value                  | Description |
+=========================================+=============+
| ``StyleRunAlignmentType.bottom``        | todo        |
+-----------------------------------------+-------------+
| ``StyleRunAlignmentType.icfTop``        | todo        |
+-----------------------------------------+-------------+
| ``StyleRunAlignmentType.center``        | todo        |
+-----------------------------------------+-------------+
| ``StyleRunAlignmentType.ROMANBASELINE`` | todo        |
+-----------------------------------------+-------------+
| ``StyleRunAlignmentType.icfBottom``     | todo        |
+-----------------------------------------+-------------+
| ``StyleRunAlignmentType.top``           | todo        |
+-----------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.SVGCSSPropertyLocation:

SVGCSSPropertyLocation
********************************************************************************

How should the CSS properties of the document be included in an exported SVG file

+---------------------------------------------------+-------------+
|                       Value                       | Description |
+===================================================+=============+
| ``SVGCSSPropertyLocation.ENTITIES``               | todo        |
+---------------------------------------------------+-------------+
| ``SVGCSSPropertyLocation.STYLEATTRIBUTES``        | todo        |
+---------------------------------------------------+-------------+
| ``SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES`` | todo        |
+---------------------------------------------------+-------------+
| ``SVGCSSPropertyLocation.STYLEELEMENTS``          | todo        |
+---------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.SVGDocumentEncoding:

SVGDocumentEncoding
********************************************************************************

How should the text in the document be encoded when exporting an SVG file

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``SVGDocumentEncoding.ASCII`` | todo        |
+-------------------------------+-------------+
| ``SVGDocumentEncoding.UTF8``  | todo        |
+-------------------------------+-------------+
| ``SVGDocumentEncoding.UTF16`` | todo        |
+-------------------------------+-------------+

----

.. _jsobjref/scripting-constants.SVGDTDVersion:

SVGDTDVersion
********************************************************************************

SVB version compatibility for exported files

+----------------------------------+-------------+
|              Value               | Description |
+==================================+=============+
| ``SVGDTDVersion.SVG1_0``         | todo        |
+----------------------------------+-------------+
| ``SVGDTDVersion.SVG1_1``         | todo        |
+----------------------------------+-------------+
| ``SVGDTDVersion.SVGBASIC1_1``    | todo        |
+----------------------------------+-------------+
| ``SVGDTDVersion.SVGTINY1_1``     | todo        |
+----------------------------------+-------------+
| ``SVGDTDVersion.SVGTINY1_1PLUS`` | todo        |
+----------------------------------+-------------+
| ``SVGDTDVersion.SVGTINY1_2``     | todo        |
+----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.SVGFontSubsetting:

SVGFontSubsetting
********************************************************************************

What font glyphs should be included in exported SVG files

+---------------------------------------------+-------------+
|                    Value                    | Description |
+=============================================+=============+
| ``SVGFontSubsetting.ALLGLYPHS``             | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.GLYPHSUSEDPLUSENGLISH`` | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.COMMONENGLISH``         | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.GLYPHSUSEDPLUSROMAN``   | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.COMMONROMAN``           | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.GLYPHSUSED``            | todo        |
+---------------------------------------------+-------------+
| ``SVGFontSubsetting.None``                  | todo        |
+---------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.SVGFontType:

SVGFontType
********************************************************************************

Types for fonts included in exported SVG files

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``SVGFontType.CEFFONT``     | todo        |
+-----------------------------+-------------+
| ``SVGFontType.SVGFONT``     | todo        |
+-----------------------------+-------------+
| ``SVGFontType.OUTLINEFONT`` | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.SymbolRegistrationPoint:

SymbolRegistrationPoint
********************************************************************************

Registration points for symbols.

+-----------------------------------------------------+-------------+
|                        Value                        | Description |
+=====================================================+=============+
| ``SymbolRegistrationPoint.SYMBOLBOTTOMLEFTPOINT``   | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLBOTTOMMIDDLEPOINT`` | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLBOTTOMRIGHTPOINT``  | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLCENTERPOINT``       | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLMIDDLELEFTPOINT``   | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLMIDDLERIGHTPOINT``  | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLTOPLEFTPOINT``      | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLTOPMIDDLEPOINT``    | todo        |
+-----------------------------------------------------+-------------+
| ``SymbolRegistrationPoint.SYMBOLTOPRIGHTPOINT``     | todo        |
+-----------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.TabStopAlignment:

TabStopAlignment
********************************************************************************

The alignment of a tab stop.

+------------------------------+-------------+
|            Value             | Description |
+==============================+=============+
| ``TabStopAlignment.Center``  | todo        |
+------------------------------+-------------+
| ``TabStopAlignment.Decimal`` | todo        |
+------------------------------+-------------+
| ``TabStopAlignment.Left``    | todo        |
+------------------------------+-------------+
| ``TabStopAlignment.Right``   | todo        |
+------------------------------+-------------+

----

.. _jsobjref/scripting-constants.TextAntialias:

TextAntialias
********************************************************************************

The type of text anti-aliasing in a text art item.

+--------------------------+-------------+
|          Value           | Description |
+==========================+=============+
| ``TextAntialias.CRISP``  | todo        |
+--------------------------+-------------+
| ``TextAntialias.NONE``   | todo        |
+--------------------------+-------------+
| ``TextAntialias.SHARP``  | todo        |
+--------------------------+-------------+
| ``TextAntialias.STRONG`` | todo        |
+--------------------------+-------------+

----

.. _jsobjref/scripting-constants.TextOrientation:

TextOrientation
********************************************************************************

The orientation of text in a text art item.

+--------------------------------+-------------+
|             Value              | Description |
+================================+=============+
| ``TextOrientation.HORIZONTAL`` | todo        |
+--------------------------------+-------------+
| ``TextOrientation.VERTICAL``   | todo        |
+--------------------------------+-------------+

----

.. _jsobjref/scripting-constants.TextPreservePolicy:

TextPreservePolicy
********************************************************************************

The text-preserve policy used by the FXG file format.

+-------------------------------------------------+-------------+
|                      Value                      | Description |
+=================================================+=============+
| ``TextPreservePolicy.AUTOMATICALLYCONVERTTEXT`` | todo        |
+-------------------------------------------------+-------------+
| ``TextPreservePolicy.OUTLINETEXT``              | todo        |
+-------------------------------------------------+-------------+
| ``TextPreservePolicy.KEEPTEXTEDITABLE``         | todo        |
+-------------------------------------------------+-------------+
| ``TextPreservePolicy.RASTERIZETEXT``            | todo        |
+-------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.TextType:

TextType
********************************************************************************

The type of text art displayed by this object.

+------------------------+-------------+
|         Value          | Description |
+========================+=============+
| ``TextType.AREATEXT``  | todo        |
+------------------------+-------------+
| ``TextType.POINTTEXT`` | todo        |
+------------------------+-------------+
| ``TextType.PATHTEXT``  | todo        |
+------------------------+-------------+

----

.. _jsobjref/scripting-constants.TIFFByteOrder:

TIFFByteOrder
********************************************************************************

The byte order to use for an exported TIFF file.

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``TIFFByteOrder.IBMPC``     | todo        |
+-----------------------------+-------------+
| ``TIFFByteOrder.MACINTOSH`` | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.TracingModeType:

TracingModeType
********************************************************************************

+----------------------------------------------+-------------+
|                    Value                     | Description |
+==============================================+=============+
| ``TracingModeType.TRACINGMODEBLACKANDWHITE`` | todo        |
+----------------------------------------------+-------------+
| ``TracingModeType.TRACINGMODECOLOR``         | todo        |
+----------------------------------------------+-------------+
| ``TracingModeType.TRACINGMODEGRAY``          | todo        |
+----------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.Transformation:

Transformation
********************************************************************************

The point to use as the anchor point about which an object is rotated, resized, or transformed.

+-----------------------------------+-------------+
|               Value               | Description |
+===================================+=============+
| ``Transformation.BOTTOM``         | todo        |
+-----------------------------------+-------------+
| ``Transformation.BOTTOMLEFT``     | todo        |
+-----------------------------------+-------------+
| ``Transformation.BOTTOMRIGHT``    | todo        |
+-----------------------------------+-------------+
| ``Transformation.CENTER``         | todo        |
+-----------------------------------+-------------+
| ``Transformation.DOCUMENTORIGIN`` | todo        |
+-----------------------------------+-------------+
| ``Transformation.LEFT``           | todo        |
+-----------------------------------+-------------+
| ``Transformation.RIGHT``          | todo        |
+-----------------------------------+-------------+
| ``Transformation.TOP``            | todo        |
+-----------------------------------+-------------+
| ``Transformation.TOPLEFT``        | todo        |
+-----------------------------------+-------------+
| ``Transformation.TOPRIGHT``       | todo        |
+-----------------------------------+-------------+

----

.. _jsobjref/scripting-constants.TrappingType:

TrappingType
********************************************************************************

+---------------------------------+-------------+
|              Value              | Description |
+=================================+=============+
| ``TrappingType.IGNOREOPAQUE``   | todo        |
+---------------------------------+-------------+
| ``TrappingType.OPAQUE``         | todo        |
+---------------------------------+-------------+
| ``TrappingType.NORMALTRAPPING`` | todo        |
+---------------------------------+-------------+
| ``TrappingType.TRANSPARENT``    | todo        |
+---------------------------------+-------------+

----

.. _jsobjref/scripting-constants.UserInteractionLevel:

UserInteractionLevel
********************************************************************************

User interface settings

+--------------------------------------------+-------------+
|                   Value                    | Description |
+============================================+=============+
| ``UserInteractionLevel.DISPLAYALERTS``     | todo        |
+--------------------------------------------+-------------+
| ``UserInteractionLevel.DONTDISPLAYALERTS`` | todo        |
+--------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.VariableKind:

VariableKind
********************************************************************************

What type of variables are included in the document.

+-----------------------------+-------------+
|            Value            | Description |
+=============================+=============+
| ``VariableKind.GRAPH``      | todo        |
+-----------------------------+-------------+
| ``VariableKind.IMAGE``      | todo        |
+-----------------------------+-------------+
| ``VariableKind.VISIBILITY`` | todo        |
+-----------------------------+-------------+
| ``VariableKind.TEXTUAL``    | todo        |
+-----------------------------+-------------+
| ``VariableKind.Unknown``    | todo        |
+-----------------------------+-------------+

----

.. _jsobjref/scripting-constants.ViewRasterType:

ViewRasterType
********************************************************************************

The raster visualization mode for tracing.

+------------------------------------------------------+-------------+
|                        Value                         | Description |
+======================================================+=============+
| ``ViewRasterType.TRACINGVIEWRASTERADJUSTEDIMAGE``    | todo        |
+------------------------------------------------------+-------------+
| ``ViewRasterType.TRACINGVIEWRASTERNOIMAGE``          | todo        |
+------------------------------------------------------+-------------+
| ``ViewRasterType.TRACINGVIEWRASTERORIGINALIMAGE``    | todo        |
+------------------------------------------------------+-------------+
| ``ViewRasterType.TRACINGVIEWRASTERTRANSPARENTIMAGE`` | todo        |
+------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ViewVectorType:

ViewVectorType
********************************************************************************

The vector visualization mode for tracing.

+---------------------------------------------------------+-------------+
|                          Value                          | Description |
+=========================================================+=============+
| ``ViewVectorType.TRACINGVIEWVECTORNOTRACINGRESULT``     | todo        |
+---------------------------------------------------------+-------------+
| ``ViewVectorType.TRACINGVIEWVECTOROUTLINES``            | todo        |
+---------------------------------------------------------+-------------+
| ``ViewVectorType.TRACINGVIEWVECTOROUTLINESWITHTRACING`` | todo        |
+---------------------------------------------------------+-------------+
| ``ViewVectorType.TRACINGVIEWVECTORTRACINGRESULT``       | todo        |
+---------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.WariChuJustificationType:

WariChuJustificationType
********************************************************************************

+---------------------------------------------------------------+-------------+
|                             Value                             | Description |
+===============================================================+=============+
| ``WariChuJustificationType.Center``                           | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.Left``                             | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.Right``                            | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.WARICHUAUTOJUSTIFY``               | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.WARICHUFULLJUSTIFY``               | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINECENTER`` | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINELEFT``   | todo        |
+---------------------------------------------------------------+-------------+
| ``WariChuJustificationType.WARICHUFULLJUSTIFYLASTLINERIGHT``  | todo        |
+---------------------------------------------------------------+-------------+

----

.. _jsobjref/scripting-constants.ZOrderMethod:

ZOrderMethod
********************************************************************************

The method used to arrange an art item’s position in the stacking order of its parent group or layer, as specified with the zOrder method

+-------------------------------+-------------+
|             Value             | Description |
+===============================+=============+
| ``ZOrderMethod.BRINGFORWARD`` | todo        |
+-------------------------------+-------------+
| ``ZOrderMethod.SENDBACKWARD`` | todo        |
+-------------------------------+-------------+
| ``ZOrderMethod.BRINGTOFRONT`` | todo        |
+-------------------------------+-------------+
| ``ZOrderMethod.SENDTOBACK``   | todo        |
+-------------------------------+-------------+
