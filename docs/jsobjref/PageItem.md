# PageItem

`app.activeDocument.pageItems[index`

**Description**

Any art item. Every art item and group in a document is a page item. You may refer to a page item as an element of a document, layer, or group item.

The `PageItem` class gives you complete access to every art item contained in an Illustrator document. The `PageItem` class is the superclass of all artwork objects in a document. The [CompoundPathItem](./CompoundPathItem.md), [GroupItem](./GroupItem.md), [MeshItem](./MeshItem.md), [PathItem](./PathItem.md), [PlacedItem](./PlacedItem.md), [PluginItem](./PluginItem.md), [RasterItem](./RasterItem.md), and [TextFrameItem](./TextFrameItem.md) classes each inherit a set of properties from the `PageItem` class.

You cannot create a `PageItem` directly, you must create one of the specific `PageItem` subclasses, such as [PathItem](./PathItem.md).

---

## Properties

### PageItem.artworkKnockout

`app.activeDocument.pageItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

### PageItem.blendingMode

`app.activeDocument.pageItems[index].blendingMode`

**Description**

The mode to use when compositing this object. An object is considered composited when its opacity is set to less than 100.0 (100%).

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

### PageItem.controlBounds

`app.activeDocument.pageItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Rect, read-only.

---

### PageItem.editable

`app.activeDocument.pageItems[index].editable`

**Description**

If `true`, this page item is editable.

**Type**

Boolean, read-only.

---

### PageItem.geometricBounds

`app.activeDocument.pageItems[index].geometricBounds`

**Description**

The object's bounds excluding the stroke width.

**Type**

Array of 4 numbers, read-only.

---

### PageItem.height

`app.activeDocument.pageItems[index].height`

**Description**

The height of the page item, calculated from the geometric bounds. Range: 0.0 to 16348.0.

**Type**

Number (double).

---

### PageItem.hidden

`app.activeDocument.pageItems[index].hidden`

**Description**

If `true`, this page item is hidden.

**Type**

Boolean.

---

### PageItem.isIsolated

`app.activeDocument.pageItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean.

---

### PageItem.layer

`app.activeDocument.pageItems[index].layer`

**Description**

The layer to which this page item belongs.

**Type**

[Layer](./Layer.md), read-only.

---

### PageItem.left

`app.activeDocument.pageItems[index].left`

**Description**

The left position of the art item.

**Type**

Number (double).

---

### PageItem.locked

`app.activeDocument.pageItems[index].locked`

**Description**

If `true`, this page item is locked.

**Type**

Boolean.

---

### PageItem.name

`app.activeDocument.pageItems[index].name`

**Description**

The name of this page item.

**Type**

String.

---

### PageItem.note

`app.activeDocument.pageItems[index].note`

**Description**

The note assigned to this item.

**Type**

String.

---

### PageItem.opacity

`app.activeDocument.pageItems[index].opacity`

**Description**

The opacity of this object, where 100.0 is completely opaque and 0.0 is completely transparent.

**Type**

Number (double).

---

### PageItem.parent

`app.activeDocument.pageItems[index].parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

### PageItem.pixelAligned

`app.activeDocument.pageItems[index].pixelAligned`

**Description**

`True` if this item is aligned to the pixel grid.

**Type**

Boolean.

---

### PageItem.position

`app.activeDocument.pageItems[index].position`

**Description**

The position (in points) of the top left corner of the item in the format {x, y}. Does not include stroke weight.

**Type**

Array of 2 numbers.

---

### PageItem.selected

`app.activeDocument.pageItems[index].selected`

**Description**

If `true`, this object is selected.

**Type**

Boolean.

---

### PageItem.sliced

`app.activeDocument.pageItems[index].sliced`

**Description**

If `true`, preserve slices.

**Type**

Boolean.

---

### PageItem.tags

`app.activeDocument.pageItems[index].tags`

**Description**

The collection of tags associated with this page item.

**Type**

[Tags](./Tags.md)

---

### PageItem.top

`app.activeDocument.pageItems[index].top`

**Description**

The top position of the art item.

**Type**

Number (double).

---

### PageItem.typename

`app.activeDocument.pageItems[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

### PageItem.uRL

`app.activeDocument.pageItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this page item.

**Type**

String.

---

### PageItem.uuid

`app.activeDocument.pageItems[index].uuid`

!!! note
    This functionality was added in Illustrator 24.0. (CC2020)

**Description**

The unique identifier for this pageItem

**Type**

String, read-only.

---

### PageItem.visibilityVariable

`app.activeDocument.pageItems[index].visibilityVariable`

**Description**

The visibility variable to which this page item path is bound.

**Type**

[Variable](./Variable.md)

---

### PageItem.visibleBounds

`app.activeDocument.pageItems[index].visibleBounds`

**Description**

The object's visible bounds, including stroke width of any objects in the illustration.

**Type**

Array of 4 numbers, read-only.

---

### PageItem.width

`app.activeDocument.pageItems[index].width`

**Description**

The width of the page item, calculated from the geometric bounds. Range: 0.0 to 16348.0.

**Type**

Number (double).

---

### PageItem.wrapInside

`app.activeDocument.pageItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean.

---

### PageItem.wrapOffset

`app.activeDocument.pageItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

---

### PageItem.wrapped

`app.activeDocument.pageItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

---

### PageItem.zOrderPosition

`app.activeDocument.pageItems[index].zOrderPosition`

**Description**

The drawing order of the art within its group or layer.

**Type**

Number (long), read-only.

---

## Methods

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

### PageItem.resize()

```javascript
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

### PageItem.rotate()

```javascript
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

### PageItem.transform()

```javascript
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
| `transformationMatrix` | [Matrix](./Matrix.md)                                                            | Transformation matrix to apply                 |
| `changePositions`      | Boolean, optional                                                                              | Whether to change Positions                    |
| `changeFillPatterns`   | Boolean, optional                                                                              | Whether to change Fill Patterns                |
| `changeFillGradients`  | Boolean, optional                                                                              | Whether to change Fill Gradients               |
| `changeStrokePattern`  | Boolean, optional                                                                              | Whether to change Stroke Pattern               |
| `changeLineWidths`     | Number (double), optional                                                                      | The amount to scale line widths                |
| `transformAbout`       | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about |

**Returns**

Nothing.

---

### PageItem.translate()

```javascript
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

### PageItem.zOrder()

`app.activeDocument.pageItems[index].zOrder(zOrderCmd)`

**Description**

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

**Parameters**

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

**Returns**

Nothing.
