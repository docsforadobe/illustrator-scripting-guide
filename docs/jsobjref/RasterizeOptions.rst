.. _jsobjref/RasterizeOptions:

RasterizeOptions
################################################################################

``rasterizeOptions``

**Description**

Specifies options that may be supplied when rasterizing artwork.

All properties are optional.

----

==========
Properties
==========

.. _jsobjref/RasterizeOptions.antiAliasingMethod:

RasterizeOptions.antiAliasingMethod
********************************************************************************

``rasterizeOptions.antiAliasingMethod``

**Description**

The type of antialiasing method.

Default: ``AntiAliasingMethod.ARTOPTIMIZED``

**Type**

:ref:`jsobjref/scripting-constants.AntiAliasingMethod`

----

.. _jsobjref/RasterizeOptions.backgroundBlack:

RasterizeOptions.backgroundBlack
********************************************************************************

``rasterizeOptions.backgroundBlack``

**Description**

If ``true``, the rasterization is done against a black background (instead of white).

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterizeOptions.clippingMask:

RasterizeOptions.clippingMask
********************************************************************************

``rasterizeOptions.clippingMask``

**Description**

If ``true``, a clipping mask should be created for the image.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterizeOptions.colorModel:

RasterizeOptions.colorModel
********************************************************************************

``rasterizeOptions.colorModel``

**Description**

The color model for the rasterization.

Default: ``RasterizationColorModel.DEFAULTCOLORMODEL``

**Type**

:ref:`jsobjref/scripting-constants.RasterizationColorModel`

----

.. _jsobjref/RasterizeOptions.convertSpotColors:

RasterizeOptions.convertSpotColors
********************************************************************************

``rasterizeOptions.convertSpotColors``

**Description**

If ``true``, spot colors should be converted to process colors for the image.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterizeOptions.convertTextToOutlines:

RasterizeOptions.convertTextToOutlines
********************************************************************************

``rasterizeOptions.convertTextToOutlines``

**Description**

If ``true``, all text is converted to outlines before rasterization.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterizeOptions.includeLayers:

RasterizeOptions.includeLayers
********************************************************************************

``rasterizeOptions.includeLayers``

**Description**

If ``true``, the resulting image incorporates layer attributes (like opacity and blend mode).

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/RasterizeOptions.padding:

RasterizeOptions.padding
********************************************************************************

``rasterizeOptions.padding``

**Description**

The amount of white space (in points) to be added around the object during rasterization.

Default: .0

**Type**

Number (double)

----

.. _jsobjref/RasterizeOptions.resolution:

RasterizeOptions.resolution
********************************************************************************

``rasterizeOptions.resolution``

**Description**

The rasterization resolution in dots per inch (dpi). Range: 72.0 to 2400.0.

Default: 300.0

**Type**

Number (double)

----

.. _jsobjref/RasterizeOptions.transparency:

RasterizeOptions.transparency
********************************************************************************

``rasterizeOptions.transparency``

**Description**

If ``true``, the image should use transparency.

Default: ``false``

**Type**

Boolean
