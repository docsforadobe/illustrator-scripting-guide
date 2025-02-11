<a id="jsobjref-rasterizeoptions"></a>

# RasterizeOptions

`rasterizeOptions`

**Description**

Specifies options that may be supplied when rasterizing artwork.

All properties are optional.

---

## Properties

<a id="jsobjref-rasterizeoptions-antialiasingmethod"></a>

### RasterizeOptions.antiAliasingMethod

`rasterizeOptions.antiAliasingMethod`

**Description**

The type of antialiasing method.

Default: `AntiAliasingMethod.ARTOPTIMIZED`

**Type**

[AntiAliasingMethod](scripting-constants.md#jsobjref-scripting-constants-antialiasingmethod)

---

<a id="jsobjref-rasterizeoptions-backgroundblack"></a>

### RasterizeOptions.backgroundBlack

`rasterizeOptions.backgroundBlack`

**Description**

If `true`, the rasterization is done against a black background (instead of white).

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasterizeoptions-clippingmask"></a>

### RasterizeOptions.clippingMask

`rasterizeOptions.clippingMask`

**Description**

If `true`, a clipping mask should be created for the image.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasterizeoptions-colormodel"></a>

### RasterizeOptions.colorModel

`rasterizeOptions.colorModel`

**Description**

The color model for the rasterization.

Default: `RasterizationColorModel.DEFAULTCOLORMODEL`

**Type**

[RasterizationColorModel](scripting-constants.md#jsobjref-scripting-constants-rasterizationcolormodel)

---

<a id="jsobjref-rasterizeoptions-convertspotcolors"></a>

### RasterizeOptions.convertSpotColors

`rasterizeOptions.convertSpotColors`

**Description**

If `true`, spot colors should be converted to process colors for the image.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasterizeoptions-converttexttooutlines"></a>

### RasterizeOptions.convertTextToOutlines

`rasterizeOptions.convertTextToOutlines`

**Description**

If `true`, all text is converted to outlines before rasterization.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasterizeoptions-includelayers"></a>

### RasterizeOptions.includeLayers

`rasterizeOptions.includeLayers`

**Description**

If `true`, the resulting image incorporates layer attributes (like opacity and blend mode).

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasterizeoptions-padding"></a>

### RasterizeOptions.padding

`rasterizeOptions.padding`

**Description**

The amount of white space (in points) to be added around the object during rasterization.

Default: .0

**Type**

Number (double)

---

<a id="jsobjref-rasterizeoptions-resolution"></a>

### RasterizeOptions.resolution

`rasterizeOptions.resolution`

**Description**

The rasterization resolution in dots per inch (dpi). Range: 72.0 to 2400.0.

Default: 300.0

**Type**

Number (double)

---

<a id="jsobjref-rasterizeoptions-transparency"></a>

### RasterizeOptions.transparency

`rasterizeOptions.transparency`

**Description**

If `true`, the image should use transparency.

Default: `false`

**Type**

Boolean
