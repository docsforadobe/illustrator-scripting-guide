# RasterEffectOptions

`RasterEffectOptions`

#### Description

Specifies raster effects settings for the document. All properties are optional.

---

## Properties

### RasterEffectOptions.antiAliasing

`rasterEffectOptions.antiAliasing`

#### Description

If `true`, the image should be antialiased.

Default: `false`

#### Type

Boolean

---

### RasterEffectOptions.clippingMask

`rasterEffectOptions.clippingMask`

#### Description

If `true`, a clipping mask is created for the image.

Default: `false`

#### Type

Boolean

---

### RasterEffectOptions.colorModel

`rasterEffectOptions.colorModel`

#### Description

The color model for the rasterization.

Default: `RasterizationColorModel.DEFAULTCOLORMODEL`

#### Type

[RasterizationColorModel](scripting-constants.md#rasterizationcolormodel)

---

### RasterEffectOptions.convertSpotColors

`rasterEffectOptions.convertSpotColors`

#### Description

If `true`, all spot colors are converted to process colors for the image.

Default: `false`

#### Type

Boolean

---

### RasterEffectOptions.padding

`rasterEffectOptions.padding`

#### Description

The amount of white space (in points) to be added around the object during rasterization.

Default: .0

#### Type

Number (double)

---

### RasterEffectOptions.resolution

`rasterEffectOptions.resolution`

#### Description

The rasterization resolution in dots per inch (dpi).

Range: 72.0 to 2400.0.

Default: 300.0

#### Type

Number (double)

---

### RasterEffectOptions.transparency

`rasterEffectOptions.transparency`

#### Description

If `true`, the image should use transparency.

Default: `false`

#### Type

Boolean
