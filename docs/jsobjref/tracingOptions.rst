.. _jsobjref/tracingOptions:

TracingOptions
################################################################################

``image.tracing.tracingOptions``

**Description**

A set of options used in converting raster art to vector art by tracing.

----

==========
Properties
==========

.. _jsobjref/tracingOptions.cornerAngle:

TracingOptions.cornerAngle
********************************************************************************

``image.tracing.tracingOptions.cornerAngle``

**Description**

The sharpness, in degrees of a turn in the original image that is considered a corner in the tracing result path.

Range: 0 to 180

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.fills:

TracingOptions.fills
********************************************************************************

``image.tracing.tracingOptions.fills``

**Description**

If ``true``, trace with fills. At least one of ``fills`` or ``strokes`` must be true.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.ignoreWhite:

TracingOptions.ignoreWhite
********************************************************************************

``image.tracing.tracingOptions.ignoreWhite``

**Description**

If ``true``, ignores white fill color.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.livePaintOutput:

TracingOptions.livePaintOutput
********************************************************************************

``image.tracing.tracingOptions.livePaintOutput``

**Description**

If ``true``, result is LivePaint art. If ``false``, it is classic art.

.. note::
  A script should only set this value in preparation for a subsequent expand operation.

  Leaving a tracing on the artboard when this property is ``true`` can lead to unexpected application behavior.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.maxColors:

TracingOptions.maxColors
********************************************************************************

``image.tracing.tracingOptions.maxColors``

**Description**

The maximum number of colors allowed for automatic palette generation.

Used only if ``tracingMode`` is ``TracingModeType.TRACINGMODECOLOR`` or ``TracingModeType.TRACINGMODEGRAY``.

Range: 2 to 256

**Type**

Number (long)

----

.. _jsobjref/tracingOptions.maxStrokeWeight:

TracingOptions.maxStrokeWeight
********************************************************************************

``image.tracing.tracingOptions.maxStrokeWeight``

**Description**

The maximum stroke weight, when ``strokes`` is true.

Range: 0.01 to 100.0

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.minArea:

TracingOptions.minArea
********************************************************************************

``image.tracing.tracingOptions.minArea``

**Description**

The smallest feature, in square pixels, that is traced.

For example, if it is 4, a feature of 2 pixels wide by 2 pixels high is traced.

**Type**

Number (long)

----

.. _jsobjref/tracingOptions.minStrokeLength:

TracingOptions.minStrokeLength
********************************************************************************

``image.tracing.tracingOptions.minStrokeLength``

**Description**

The minimum length in pixels of features in the original image that can be stroked, when ``strokes`` is ``true``.

Smaller features are omitted. Range: 0.0 to 200.0. Default: 20.0

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.outputToSwatches:

TracingOptions.outputToSwatches
********************************************************************************

``image.tracing.tracingOptions.outputToSwatches``

**Description**

If ``true``, named colors (swatches) are generated for each new color created by the tracing result.

Used only if ``tracingMode`` is ``TracingModeType.TRACINGMODECOLOR`` or ``TracingModeType.TRACINGMODEGRAY``.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.palette:

TracingOptions.palette
********************************************************************************

``image.tracing.tracingOptions.palette``

**Description**

The name of a color palette to use for tracing. If the empty string, use the automatic palette.

Used only if ``tracingMode`` is ``TracingModeType.TRACINGMODECOLOR`` or ``TracingModeType.TRACINGMODEGRAY``.

**Type**

String

----

.. _jsobjref/tracingOptions.parent:

TracingOptions.parent
********************************************************************************

``image.tracing.tracingOptions.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/tracingOptions.pathFitting:

TracingOptions.pathFitting
********************************************************************************

``image.tracing.tracingOptions.pathFitting``

**Description**

The distance between the traced shape and the original pixel shape. Lower values create a tighter path fitting.

Higher values create a looser path fitting. Range: 0.0 to 10.0

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.preprocessBlur:

TracingOptions.preprocessBlur
********************************************************************************

``image.tracing.tracingOptions.preprocessBlur``

**Description**

The amount of blur used during preprocessing, in pixels. Blurring helps reduce small artifacts and smooth jagged edges in the tracing result. Range: 0.0 to 2.0

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.preset:

TracingOptions.preset
********************************************************************************

``image.tracing.tracingOptions.preset``

**Description**

The name of a preset file containing these options.

**Type**

String, read-only.

----

.. _jsobjref/tracingOptions.resample:

TracingOptions.resample
********************************************************************************

``image.tracing.tracingOptions.resample``

**Description**

If ``true``, resample when tracing. (This setting is not captured in a preset file.)

Always ``true`` when the raster source art is placed or linked.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.resampleResolution:

TracingOptions.resampleResolution
********************************************************************************

``image.tracing.tracingOptions.resampleResolution``

**Description**

The resolution to use when resampling in pixels per inch (ppi).

Lower resolution increases the speed of the tracing operation. (This setting is not captured in a preset file.)

**Type**

Number (double)

----

.. _jsobjref/tracingOptions.strokes:

TracingOptions.strokes
********************************************************************************

``image.tracing.tracingOptions.strokes``

**Description**

If ``true``, trace with strokes. At least one of fills or strokes must be true.

Used only if ``tracingMode`` is ``TracingModeType.TRACINGMODEBLACKANDWHITE``.

**Type**

Boolean

----

.. _jsobjref/tracingOptions.threshold:

TracingOptions.threshold
********************************************************************************

``image.tracing.tracingOptions.threshold``

**Description**

The threshold value of black-and-white tracing. All pixels with a grayscale value greater than this are converted to black.

Used only if ``tracingMode`` is ``TracingModeType.TRACINGMODEBLACKANDWHITE``.

Range: 0 to 255

**Type**

Number (long)

----

.. _jsobjref/tracingOptions.tracingMode:

TracingOptions.tracingMode
********************************************************************************

``image.tracing.tracingOptions.tracingMode``

**Description**

The color mode for tracing.

**Type**

:ref:`jsobjref/scriptingConstants.TracingModeType`

----

.. _jsobjref/tracingOptions.typename:

TracingOptions.typename
********************************************************************************

``image.tracing.tracingOptions.typename``

**Description**

Read-only. The class name of the object.

**Type**

String

----

.. _jsobjref/tracingOptions.viewRaster:

TracingOptions.viewRaster
********************************************************************************

``image.tracing.tracingOptions.viewRaster``

**Description**

The view for previews of the raster image. (This setting is not captured in a preset file.)

**Type**

:ref:`jsobjref/scriptingConstants.ViewRasterType`

----

.. _jsobjref/tracingOptions.viewVector:

TracingOptions.viewVector
********************************************************************************

``image.tracing.tracingOptions.viewVector``

**Description**

The view for previews of the vector result. (This setting is not captured in a preset file.)

**Type**

:ref:`jsobjref/scriptingConstants.ViewVectorType`

----

=======
Methods
=======

.. _jsobjref/tracingOptions.loadFromPreset:

TracingOptions.loadFromPreset()
********************************************************************************

``image.tracing.tracingOptions.loadFromPreset(parameter)``

**Description**

Loads a set of options from the specified preset, as found in the ``Application.tracingPresetList`` array.

**Parameters**

+----------------+--------+---------------------+
|   Parameter    |  Type  |     Description     |
+================+========+=====================+
| ``presetName`` | String | Preset name to load |
+----------------+--------+---------------------+

**Returns**

Boolean

----

.. _jsobjref/tracingOptions.storeToPreset:

TracingOptions.storeToPreset()
********************************************************************************

``image.tracing.tracingOptions.storeToPreset(parameter)``

**Description**

Saves this set of options in the specified preset.

Use a name found in the ``Application.tracingPresetList`` array, or a new name to create a new preset.

For an existing preset, overwrites an unlocked preset and returns ``true``.

Returns ``false`` if the preset is locked.

**Parameters**

+----------------+--------+------------------------+
|   Parameter    |  Type  |      Description       |
+================+========+========================+
| ``presetName`` | String | Preset name to save as |
+----------------+--------+------------------------+

**Returns**

Boolean
