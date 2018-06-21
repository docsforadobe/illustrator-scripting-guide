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
