<a id="jsobjref-pageitem"></a>

# PageItem

`app.activeDocument.pageItems[index`

**Description**

Any art item. Every art item and group in a document is a page item. You may refer to a page item as an element of a document, layer, or group item.

The `PageItem` class gives you complete access to every art item contained in an Illustrator document. The `PageItem` class is the superclass of all artwork objects in a document. The [CompoundPathItem](CompoundPathItem.md#jsobjref-compoundpathitem), [GroupItem](GroupItem.md#jsobjref-groupitem), [MeshItem](MeshItem.md#jsobjref-meshitem), [PathItem](PathItem.md#jsobjref-pathitem), [PlacedItem](PlacedItem.md#jsobjref-placeditem), [PluginItem](PluginItem.md#jsobjref-pluginitem), [RasterItem](RasterItem.md#jsobjref-rasteritem), and [TextFrameItem](TextFrameItem.md#jsobjref-textframeitem) classes each inherit a set of properties from the `PageItem` class.

You cannot create a `PageItem` directly, you must create one of the specific `PageItem` subclasses, such as [PathItem](PathItem.md#jsobjref-pathitem).

---

## Properties

<a id="jsobjref-pageitem-artworkknockout"></a>

### PageItem.artworkKnockout

`app.activeDocument.pageItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

<a id="jsobjref-pageitem-blendingmode"></a>

### PageItem.blendingMode

`app.activeDocument.pageItems[index].blendingMode`

**Description**

The mode to use when compositing this object. An object is considered composited when its opacity is set to less than 100.0 (100%).

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

<a id="jsobjref-pageitem-controlbounds"></a>

### PageItem.controlBounds

`app.activeDocument.pageItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Rect, read-only.

---

<a id="jsobjref-pageitem-editable"></a>

### PageItem.editable

`app.activeDocument.pageItems[index].editable`

**Description**

If `true`, this page item is editable.

**Type**

Boolean, read-only.

---

<a id="jsobjref-pageitem-geometricbounds"></a>

### PageItem.geometricBounds

`app.activeDocument.pageItems[index].geometricBounds`

**Description**

The object’s bounds excluding the stroke width.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-pageitem-height"></a>

### PageItem.height

`app.activeDocument.pageItems[index].height`

**Description**

The height of the page item, calculated from the geometric bounds. Range: 0.0 to 16348.0.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-hidden"></a>

### PageItem.hidden

`app.activeDocument.pageItems[index].hidden`

**Description**

If `true`, this page item is hidden.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-isisolated"></a>

### PageItem.isIsolated

`app.activeDocument.pageItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-layer"></a>

### PageItem.layer

`app.activeDocument.pageItems[index].layer`

**Description**

The layer to which this page item belongs.

**Type**

[Layer](Layer.md#jsobjref-layer), read-only.

---

<a id="jsobjref-pageitem-left"></a>

### PageItem.left

`app.activeDocument.pageItems[index].left`

**Description**

The left position of the art item.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-locked"></a>

### PageItem.locked

`app.activeDocument.pageItems[index].locked`

**Description**

If `true`, this page item is locked.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-name"></a>

### PageItem.name

`app.activeDocument.pageItems[index].name`

**Description**

The name of this page item.

**Type**

String.

---

<a id="jsobjref-pageitem-note"></a>

### PageItem.note

`app.activeDocument.pageItems[index].note`

**Description**

The note assigned to this item.

**Type**

String.

---

<a id="jsobjref-pageitem-opacity"></a>

### PageItem.opacity

`app.activeDocument.pageItems[index].opacity`

**Description**

The opacity of this object, where 100.0 is completely opaque and 0.0 is completely transparent.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-parent"></a>

### PageItem.parent

`app.activeDocument.pageItems[index].parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

<a id="jsobjref-pageitem-pixelaligned"></a>

### PageItem.pixelAligned

`app.activeDocument.pageItems[index].pixelAligned`

**Description**

`True` if this item is aligned to the pixel grid.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-position"></a>

### PageItem.position

`app.activeDocument.pageItems[index].position`

**Description**

The position (in points) of the top left corner of the item in the format {x, y}. Does not include stroke weight.

**Type**

Array of 2 numbers.

---

<a id="jsobjref-pageitem-selected"></a>

### PageItem.selected

`app.activeDocument.pageItems[index].selected`

**Description**

If `true`, this object is selected.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-sliced"></a>

### PageItem.sliced

`app.activeDocument.pageItems[index].sliced`

**Description**

If `true`, preserve slices.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-tags"></a>

### PageItem.tags

`app.activeDocument.pageItems[index].tags`

**Description**

The collection of tags associated with this page item.

**Type**

[Tags](Tags.md#jsobjref-tags)

---

<a id="jsobjref-pageitem-top"></a>

### PageItem.top

`app.activeDocument.pageItems[index].top`

**Description**

The top position of the art item.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-typename"></a>

### PageItem.typename

`app.activeDocument.pageItems[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

<a id="jsobjref-pageitem-url"></a>

### PageItem.uRL

`app.activeDocument.pageItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this page item.

**Type**

String.

---

<a id="jsobjref-pageitem-uuid"></a>

### PageItem.uuid

`app.activeDocument.pageItems[index].uuid`

#### NOTE
This functionality was added in Illustrator 24.0. (CC2020)

**Description**

The unique identifier for this pageItem

**Type**

String, read-only.

---

<a id="jsobjref-pageitem-visibilityvariable"></a>

### PageItem.visibilityVariable

`app.activeDocument.pageItems[index].visibilityVariable`

**Description**

The visibility variable to which this page item path is bound.

**Type**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-pageitem-visiblebounds"></a>

### PageItem.visibleBounds

`app.activeDocument.pageItems[index].visibleBounds`

**Description**

The object’s visible bounds, including stroke width of any objects in the illustration.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-pageitem-width"></a>

### PageItem.width

`app.activeDocument.pageItems[index].width`

**Description**

The width of the page item, calculated from the geometric bounds. Range: 0.0 to 16348.0.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-wrapinside"></a>

### PageItem.wrapInside

`app.activeDocument.pageItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean.

---

<a id="jsobjref-pageitem-wrapoffset"></a>

### PageItem.wrapOffset

`app.activeDocument.pageItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

---

<a id="jsobjref-pageitem-wrapped"></a>

### PageItem.wrapped

`app.activeDocument.pageItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

---

<a id="jsobjref-pageitem-zorderposition"></a>

### PageItem.zOrderPosition

`app.activeDocument.pageItems[index].zOrderPosition`

**Description**

The drawing order of the art within its group or layer.

**Type**

Number (long), read-only.

---

## Methods

<a id="jsobjref-pageitem-bringinperspective"></a>

### PageItem.bringInPerspective()

`app.activeDocument.pageItems[index].bringInPerspective(posX, posY, perspectiveGridPlane)`

**Description**

Places art object(s) in a perspective grid at a specified position and grid plane.

**Parameters**

| Parameter              | Type                                                                                                     | Description                        |
|------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------|
| `posX`                 | Number                                                                                                   | X position to place art at         |
| `posY`                 | Number                                                                                                   | Y position to place art at         |
| `perspectiveGridPlane` | [PerspectiveGridPlaneType](scripting-constants.md#jsobjref-scripting-constants-perspectivegridplanetype) | Perspective grid plane type to use |

**Returns**

Returns.

---

<a id="jsobjref-pageitem-resize"></a>

### PageItem.resize()

```default
app.activeDocument.pageItems[index].resize(
    scaleX, scaleY [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,scaleAbout]
)
```

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

<a id="jsobjref-pageitem-rotate"></a>

### PageItem.rotate()

```default
app.activeDocument.pageItems[index].rotate(
    angle [,changePositions] [,changeFillPatterns]
    [,changeFillGradients] [,changeStrokePattern] [,rotateAbout]
)
```

**Description**

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the `angle` value is positive, clockwise if the value is negative.

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

<a id="jsobjref-pageitem-transform"></a>

### PageItem.transform()

```default
app.activeDocument.pageItems[index].transform(
    transformationMatrix [,changePositions] [,changeFillPatterns] [,changeFillGradients]
    [,changeStrokePattern] [,changeLineWidths] [,transformAbout]
)
```

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

<a id="jsobjref-pageitem-translate"></a>

### PageItem.translate()

```default
app.activeDocument.pageItems[index].translate(
    deltaX [,deltaY] [,transformObjects] [,transformFillPatterns]
    [,transformFillGradients] [,transformStrokePatterns]
)
```

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

<a id="jsobjref-pageitem-zorder"></a>

### PageItem.zOrder()

`app.activeDocument.pageItems[index].zOrder(zOrderCmd)`

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

**Returns**

Nothing.
