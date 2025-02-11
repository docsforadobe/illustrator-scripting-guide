# ImageCaptureOptions

`imageCaptureOptions`

**Description**

Options for image capture, used with the [Document.imageCapture()](Document.md#jsobjref-document-imagecapture) method. All properties are optional.

---

## Properties

### ImageCaptureOptions.antiAliasing

`imageCaptureOptions.antiAliasing`

**Description**

If `true`, the image result is anti-aliased. Default: `false`.

**Type**

Boolean

---

### ImageCaptureOptions.matte

`imageCaptureOptions.matte`

**Description**

If `true`, the artboard is matted with a color. Default: `false`.

**Type**

Boolean

---

### ImageCaptureOptions.matteColor

`imageCaptureOptions.matteColor`

**Description**

The color to use for the artboard matte. Default: white.

**Type**

[RGBColor](RGBColor.md#jsobjref-rgbcolor)

---

### ImageCaptureOptions.resolution

`imageCaptureOptions.resolution`

**Description**

The resolution of the captured image file in points-per-inch (PPI), in the range [72.0 … 2400.0]. Default: 150.

**Type**

Number (double).

---

### ImageCaptureOptions.transparency

`imageCaptureOptions.transparency`

**Description**

If `true`, the image result is transparent. Default: `false`.

**Type**

Boolean.

---

### ImageCaptureOptions.typename

`imageCaptureOptions.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.
