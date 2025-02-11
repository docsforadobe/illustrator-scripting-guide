<a id="jsobjref-rasteritem"></a>

# RasterItem

`app.activeDocument.rasterItems[index`

**Description**

A bitmap art item in a document. A script can create a raster item from an external file, or by copying an existing raster item with the `duplicate` method.

---

## Properties

<a id="jsobjref-rasteritem-artworkknockout"></a>

### RasterItem.artworkKnockout

`app.activeDocument.rasterItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

<a id="jsobjref-rasteritem-bitsperchannel"></a>

### RasterItem.bitsPerChannel

`app.activeDocument.rasterItems[index].bitsPerChannel`

**Description**

The number of bits per channel.

**Type**

Number (long); read-only.

---

<a id="jsobjref-rasteritem-blendingmode"></a>

### RasterItem.blendingMode

`app.activeDocument.rasterItems[index].blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

<a id="jsobjref-rasteritem-boundingbox"></a>

### RasterItem.boundingBox

`app.activeDocument.rasterItems[index].boundingBox`

**Description**

The dimensions of the placed art item regardless of transformations.

**Type**

Array of 4 numbers

---

<a id="jsobjref-rasteritem-channels"></a>

### RasterItem.channels

`app.activeDocument.rasterItems[index].channels`

**Description**

The number of channels.

**Type**

Number (long); read-only.

---

<a id="jsobjref-rasteritem-colorants"></a>

### RasterItem.colorants

`app.activeDocument.rasterItems[index].colorants`

**Description**

The colorants used in the raster art.

**Type**

Array of string; read-only.

---

<a id="jsobjref-rasteritem-colorizedgrayscale"></a>

### RasterItem.colorizedGrayscale

`app.activeDocument.rasterItems[index].colorizedGrayscale`

**Description**

If `true`, the raster art is a colorized grayscale image.

**Type**

Boolean; read-only.

---

<a id="jsobjref-rasteritem-contentvariable"></a>

### RasterItem.contentVariable

`app.activeDocument.rasterItems[index].contentVariable`

**Description**

The content variable bound to the item.

**Type**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-rasteritem-controlbounds"></a>

### RasterItem.controlBounds

`app.activeDocument.rasterItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-rasteritem-editable"></a>

### RasterItem.editable

`app.activeDocument.rasterItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean; read-only.

---

<a id="jsobjref-rasteritem-embedded"></a>

### RasterItem.embedded

`app.activeDocument.rasterItems[index].embedded`

**Description**

If `true`, the raster art item is embedded in the illustration.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-file"></a>

### RasterItem.file

`app.activeDocument.rasterItems[index].file`

**Description**

The file containing the artwork.

**Type**

File; read-only.

---

<a id="jsobjref-rasteritem-geometricbounds"></a>

### RasterItem.geometricBounds

`app.activeDocument.rasterItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-rasteritem-height"></a>

### RasterItem.height

`app.activeDocument.rasterItems[index].height`

**Description**

The height of the group item.

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-hidden"></a>

### RasterItem.hidden

`app.activeDocument.rasterItems[index].hidden`

**Description**

If `true`, this item is hidden.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-imagecolorspace"></a>

### RasterItem.imageColorSpace

`app.activeDocument.rasterItems[index].imageColorSpace`

**Description**

The color space of the raster image.

**Type**

[ImageColorSpace](scripting-constants.md#jsobjref-scripting-constants-imagecolorspace); read-only.

---

<a id="jsobjref-rasteritem-isisolated"></a>

### RasterItem.isIsolated

`app.activeDocument.rasterItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-layer"></a>

### RasterItem.layer

`app.activeDocument.rasterItems[index].layer`

**Description**

The layer to which this item belongs.

**Type**

[Layer](Layer.md#jsobjref-layer); read-only.

---

<a id="jsobjref-rasteritem-left"></a>

### RasterItem.left

`app.activeDocument.rasterItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-locked"></a>

### RasterItem.locked

`app.activeDocument.rasterItems[index].locked`

**Description**

If `true`, this item is locked.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-matrix"></a>

### RasterItem.matrix

`app.activeDocument.rasterItems[index].matrix`

**Description**

The transformation matrix of the placed artwork.

**Type**

[Matrix](Matrix.md#jsobjref-matrix)

---

<a id="jsobjref-rasteritem-name"></a>

### RasterItem.name

`app.activeDocument.rasterItems[index].name`

**Description**

The name of this item.

**Type**

String

---

<a id="jsobjref-rasteritem-note"></a>

### RasterItem.note

`app.activeDocument.rasterItems[index].note`

**Description**

The note assigned to this item.

**Type**

String

---

<a id="jsobjref-rasteritem-opacity"></a>

### RasterItem.opacity

`app.activeDocument.rasterItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-overprint"></a>

### RasterItem.overprint

`app.activeDocument.rasterItems[index].overprint`

**Description**

If `true`, the raster art overprints.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-parent"></a>

### RasterItem.parent

`app.activeDocument.rasterItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](Layer.md#jsobjref-layer) or [GroupItem](GroupItem.md#jsobjref-groupitem)

---

<a id="jsobjref-rasteritem-position"></a>

### RasterItem.position

`app.activeDocument.rasterItems[index].position`

**Description**

The position (in points) of the top left corner of the `rasterItem` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

---

<a id="jsobjref-rasteritem-selected"></a>

### RasterItem.selected

`app.activeDocument.rasterItems[index].selected`

**Description**

If `true`, this item is selected.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-sliced"></a>

### RasterItem.sliced

`app.activeDocument.rasterItems[index].sliced`

**Description**

If `true`, the item sliced.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-rasteritem-status"></a>

### RasterItem.status

`app.activeDocument.rasterItems[index].status`

**Description**

Status of the linked image.

**Type**

[RasterLinkState](scripting-constants.md#jsobjref-scripting-constants-rasterlinkstate)

---

<a id="jsobjref-rasteritem-tags"></a>

### RasterItem.tags

`app.activeDocument.rasterItems[index].tags`

**Description**

The tags contained in this item.

**Type**

[Tags](Tags.md#jsobjref-tags); read-only.

---

<a id="jsobjref-rasteritem-top"></a>

### RasterItem.top

`app.activeDocument.rasterItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-transparent"></a>

### RasterItem.transparent

`app.activeDocument.rasterItems[index].transparent`

**Description**

If `true`, the raster art is transparent.

**Type**

Boolean; read-only.

---

<a id="jsobjref-rasteritem-typename"></a>

### RasterItem.typename

`app.activeDocument.rasterItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

<a id="jsobjref-rasteritem-url"></a>

### RasterItem.uRL

`app.activeDocument.rasterItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

---

<a id="jsobjref-rasteritem-visibilityvariable"></a>

### RasterItem.visibilityVariable

`app.activeDocument.rasterItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-rasteritem-visiblebounds"></a>

### RasterItem.visibleBounds

`app.activeDocument.rasterItems[index].visibleBounds`

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-rasteritem-width"></a>

### RasterItem.width

`app.activeDocument.rasterItems[index].width`

**Description**

The width of the item.

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-wrapinside"></a>

### RasterItem.wrapInside

`app.activeDocument.rasterItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean

---

<a id="jsobjref-rasteritem-wrapoffset"></a>

### RasterItem.wrapOffset

`app.activeDocument.rasterItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

---

<a id="jsobjref-rasteritem-wrapped"></a>

### RasterItem.wrapped

`app.activeDocument.rasterItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

---

<a id="jsobjref-rasteritem-zorderposition"></a>

### RasterItem.zOrderPosition

`app.activeDocument.rasterItems[index].zOrderPosition`

**Description**

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

**Type**

Number; read-only.

---

## Methods

<a id="jsobjref-rasteritem-colorize"></a>

### RasterItem.colorize()

`app.activeDocument.rasterItems[index].colorize(rasterizeColor)`

**Description**

Colorizes the raster item with a CMYK or RGB Color.

**Parameters**

| Parameter        | Type                             | Description                         |
|------------------|----------------------------------|-------------------------------------|
| `rasterizeColor` | [Color](Color.md#jsobjref-color) | CMYK or RGB Color to rasterize with |

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-duplicate"></a>

### RasterItem.duplicate()

`app.activeDocument.rasterItems[index].duplicate([relativeObject][, insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[RasterItem](#jsobjref-rasteritem)

---

<a id="jsobjref-rasteritem-move"></a>

### RasterItem.move()

`app.activeDocument.rasterItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[RasterItem](#jsobjref-rasteritem)

---

<a id="jsobjref-rasteritem-remove"></a>

### RasterItem.remove()

`app.activeDocument.rasterItems[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-resize"></a>

### RasterItem.resize()

`app.activeDocument.rasterItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])`

**Description**

Scales the art item where `scaleX` is the horizontal scaling factor and `scaleY` is the vertical scaling factor. 100.0 = 100%.

**Parameters**

| Parameter             | Type                                                                                           | Description                                             |
|-----------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `scaleX`              | Number (double)                                                                                | Horizontal scaling factor                               |
| `scaleY`              | Number (double)                                                                                | Vertical scaling factor                                 |
| `changePositions`     | Boolean, optional                                                                              | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                                              | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                                              | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                                              | Whether to transform stroke patterns                    |
| `changeLineWidths`    | Number (double), optional                                                                      | The amount to scale line widths                         |
| `scaleAbout`          | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about          |

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-rotate"></a>

### RasterItem.rotate()

`app.activeDocument.rasterItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])`

**Description**

Rotates the art item relative to the current rotation.

The object is rotated counter-clockwise if the `angle` value is positive, clockwise if the value is negative.

**Parameters**

| Parameter             | Type                                                                                           | Description                                             |
|-----------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `angle`               | Number (double)                                                                                | The angle amount to rotate the element                  |
| `changePositions`     | Boolean, optional                                                                              | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                                              | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                                              | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                                              | Whether to transform stroke patterns                    |
| `rotateAbout`         | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about          |

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-trace"></a>

### RasterItem.trace()

`app.activeDocument.rasterItems[index].trace()`

**Description**

Converts the raster art for this object to vector art, using default options.

Reorders the raster art into the source art of a plug-in group, and converts it into a group of filled and/or stroked paths that resemble the original image.

Creates and returns a [PluginItem](PluginItem.md#jsobjref-pluginitem) object that references a [TracingObject](TracingObject.md#jsobjref-tracingobject) object.

**Returns**

[PluginItem](PluginItem.md#jsobjref-pluginitem)

---

<a id="jsobjref-rasteritem-transform"></a>

### RasterItem.transform()

`app.activeDocument.rasterItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])`

**Description**

Transforms the art item by applying a transformation matrix.

**Parameters**

| Parameter              | Type                                                                                           | Description                                    |
|------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
| `transformationMatrix` | [Matrix](Matrix.md#jsobjref-matrix)                                                            | Transformation matrix to apply                 |
| `changePositions`      | Boolean, optional                                                                              | Whether to change Positions                    |
| `changeFillPatterns`   | Boolean, optional                                                                              | Whether to change Fill Patterns                |
| `changeFillGradients`  | Boolean, optional                                                                              | Whether to change Fill Gradients               |
| `changeStrokePattern`  | Boolean, optional                                                                              | Whether to change Stroke Pattern               |
| `changeLineWidths`     | Number (double), optional                                                                      | The amount to scale line widths                |
| `transformAbout`       | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about |

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-translate"></a>

### RasterItem.translate()

`app.activeDocument.rasterItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])`

**Description**

Repositions the art item relative to the current position, where `deltaX` is the horizontal offset and `deltaY` is the vertical offset.

**Parameters**

| Parameter                 | Type                      | Description                          |
|---------------------------|---------------------------|--------------------------------------|
| `deltaX`                  | Number (double), optional | Horizontal offset                    |
| `deltaY`                  | Number (double), optional | Vertical offset                      |
| `transformObjects`        | Boolean, optional         | Whether to transform Objects         |
| `transformFillPatterns`   | Boolean, optional         | Whether to transform Fill Patterns   |
| `transformFillGradients`  | Boolean, optional         | Whether to transform Fill Gradients  |
| `transformStrokePatterns` | Boolean, optional         | Whether to transform Stroke Patterns |

**Returns**

Nothing.

---

<a id="jsobjref-rasteritem-zorder"></a>

### RasterItem.zOrder()

`app.activeDocument.rasterItems[index].zOrder(zOrderCmd)`

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

**Returns**

Nothing.
