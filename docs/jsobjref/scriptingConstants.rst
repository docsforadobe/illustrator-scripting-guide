.. _jsobjref/scriptingConstants:

Scripting Constants
################################################################################

This chapter lists and describes the enumerations defined for use with Illustrator JavaScript properties and methods.

----

.. _jsobjref/scriptingConstants.AlternateGlyphsForm:

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

.. _jsobjref/scriptingConstants.AntiAliasingMethod:

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

.. _jsobjref/scriptingConstants.ArtClippingOption:

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

.. _jsobjref/scriptingConstants.AutoCADColors:

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

.. _jsobjref/scriptingConstants.AutoCADCompatibility:

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

.. _jsobjref/scriptingConstants.AutoCADExportFileFormat:

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

.. _jsobjref/scriptingConstants.AutoCADExportOption:

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

.. _jsobjref/scriptingConstants.AutoCADGlobalScaleOption:

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

.. _jsobjref/scriptingConstants.AutoCADRasterFormat:

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

.. _jsobjref/scriptingConstants.AutoCADUnit:

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

.. _jsobjref/scriptingConstants.AutoKernType:

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

.. _jsobjref/scriptingConstants.AutoLeadingType:

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

.. _jsobjref/scriptingConstants.BaselineDirectionType:

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

.. _jsobjref/scriptingConstants.BlendAnimationType:

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

.. _jsobjref/scriptingConstants.BlendModes:

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

.. _jsobjref/scriptingConstants.BlendsExpandPolicy:

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

.. _jsobjref/scriptingConstants.BurasagariTypeEnum:

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

.. _jsobjref/scriptingConstants.CaseChangeType:

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

.. _jsobjref/scriptingConstants.ColorConversion:

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

.. _jsobjref/scriptingConstants.ColorConvertPurpose:

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

.. _jsobjref/scriptingConstants.ColorDestination:

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

.. _jsobjref/scriptingConstants.ColorDitherMethod:

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

.. _jsobjref/scriptingConstants.ColorModel:

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

.. _jsobjref/scriptingConstants.ColorProfile:

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

.. _jsobjref/scriptingConstants.ColorReductionMethod:

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

.. _jsobjref/scriptingConstants.ColorType:

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

.. _jsobjref/scriptingConstants.Compatibility:

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

.. _jsobjref/scriptingConstants.CompressionQuality:

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

.. _jsobjref/scriptingConstants.CoordinateSystem:

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

.. _jsobjref/scriptingConstants.CropOptions:

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

.. _jsobjref/scriptingConstants.DocumentArtboardLayout:

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

.. _jsobjref/scriptingConstants.DocumentColorSpace:

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

.. _jsobjref/scriptingConstants.DocumentLayoutStyle:

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

.. _jsobjref/scriptingConstants.DocumentPresetType:

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

.. _jsobjref/scriptingConstants.DocumentPreviewMode:

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

.. _jsobjref/scriptingConstants.DocumentRasterResolution:

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

.. _jsobjref/scriptingConstants.DocumentTransparencyGrid:

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

.. _jsobjref/scriptingConstants.DocumentType:

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

.. _jsobjref/scriptingConstants.DownsampleMethod:

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

.. _jsobjref/scriptingConstants.ElementPlacement:

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

.. _jsobjref/scriptingConstants.EPSPostScriptLevelEnum:

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

.. _jsobjref/scriptingConstants.EPSPreview:

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

.. _jsobjref/scriptingConstants.ExportType:

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

.. _jsobjref/scriptingConstants.FigureStyleType:

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

.. _jsobjref/scriptingConstants.FiltersPreservePolicy:

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

.. _jsobjref/scriptingConstants.FlashExportStyle:

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

.. _jsobjref/scriptingConstants.FlashExportVersion:

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

.. _jsobjref/scriptingConstants.FlashImageFormat:

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

.. _jsobjref/scriptingConstants.FlashJPEGMethod:

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

.. _jsobjref/scriptingConstants.FlashPlaybackSecurity:

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

.. _jsobjref/scriptingConstants.FontBaselineOption:

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

.. _jsobjref/scriptingConstants.FontCapsOption:

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

.. _jsobjref/scriptingConstants.FontOpenTypePositionOption:

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

.. _jsobjref/scriptingConstants.FontSubstitutionPolicy:

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

.. _jsobjref/scriptingConstants.FXGVersion:

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

.. _jsobjref/scriptingConstants.GradientsPreservePolicy:

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

.. _jsobjref/scriptingConstants.GradientType:

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

.. _jsobjref/scriptingConstants.ImageColorSpace:

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

.. _jsobjref/scriptingConstants.InkPrintStatus:

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

.. _jsobjref/scriptingConstants.InkType:

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

.. _jsobjref/scriptingConstants.JavaScriptExecutionMode:

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

.. _jsobjref/scriptingConstants.Justification:

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

.. _jsobjref/scriptingConstants.KinsokuOrderEnum:

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

.. _jsobjref/scriptingConstants.KnockoutState:

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

.. _jsobjref/scriptingConstants.LanguageType:

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

.. _jsobjref/scriptingConstants.LayerOrderType:

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

.. _jsobjref/scriptingConstants.LibraryType:

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

.. _jsobjref/scriptingConstants.MonochromeCompression:

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
