# LegacyTextItem

`legacyTextItems[index`

#### Description

A text object created in Illustrator CS (version 10) or earlier, which is uneditable until converted. To convert legacy text, see [LegacyTextItems.convertToNative()](LegacyTextItems.md#jsobjref-legacytextitems-converttonative).

You can view, move, and print legacy text, but you cant edit it. Legacy text has an "x" through its bounding box when selected.

---

## Properties

### LegacyTextItem.artworkKnockout

`legacyTextItems[index].artworkKnockout`

#### Description

Is this object used to create a knockout, and if so, what kind of knockout.

#### Type

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

### LegacyTextItem.blendingMode

`legacyTextItems[index].blendingMode`

#### Description

The blend mode used when compositing an object.

#### Type

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

### LegacyTextItem.controlBounds

`legacyTextItems[index].controlBounds`

#### Description

The bounds of the object including stroke width and controls.

#### Type

Array of 4 numbers, read-only.

---

### LegacyTextItem.converted

`legacyTextItems[index].converted`

#### Description

If `true`, the legacy text item has been updated to a native text frame item.

#### Type

Boolean, read-only.

---

### LegacyTextItem.editable

`legacyTextItems[index].editable`

#### Description

If `true`, this item is editable.

#### Type

Boolean, read-only.

---

### LegacyTextItem.geometricBounds

`legacyTextItems[index].geometricBounds`

#### Description

The bounds of the object excluding stroke width.

#### Type

Array of 4 numbers, read-only.

---

### LegacyTextItem.height

`legacyTextItems[index].height`

#### Description

The height of the group item.

#### Type

Number (double).

---

### LegacyTextItem.hidden

`legacyTextItems[index].hidden`

#### Description

If `true`, this item is hidden.

#### Type

Boolean.

---

### LegacyTextItem.isIsolated

`legacyTextItems[index].isIsolated`

#### Description

If `true`, this object is isolated.

#### Type

Boolean.

---

### LegacyTextItem.layer

`legacyTextItems[index].layer`

#### Description

The layer to which this item belongs.

#### Type

[Layer](./Layer.md), read-only.

---

### LegacyTextItem.left

`legacyTextItems[index].left`

#### Description

The position of the left side of the item (in points, measured from the left side of the page).

#### Type

Number (double).

---

### LegacyTextItem.locked

`legacyTextItems[index].locked`

#### Description

If `true`, this item is locked.

#### Type

Boolean.

---

### LegacyTextItem.name

`legacyTextItems[index].name`

#### Description

The name of this item.

#### Type

String.

---

### LegacyTextItem.note

`legacyTextItems[index].note`

#### Description

The note assigned to this item.

#### Type

String.

---

### LegacyTextItem.opacity

`legacyTextItems[index].opacity`

#### Description

The opacity of the object. Range: 0.0 to 100.0.

#### Type

Number (double).

---

### LegacyTextItem.parent

`legacyTextItems[index].parent`

#### Description

The parent of this object.

#### Type

[Layer](./Layer.md) or [GroupItem](./GroupItem.md), read-only.

---

### LegacyTextItem.position

`legacyTextItems[index].position`

#### Description

The position (in points) of the top left corner of the `legacyTextItems[index` object in the format [x, y]. Does not include stroke weight.

#### Type

Array of 2 numbers.

---

### LegacyTextItem.selected

`legacyTextItems[index].selected`

#### Description

If `true`, this item is selected.

#### Type

Boolean.

---

### LegacyTextItem.sliced

`legacyTextItems[index].sliced`

#### Description

If `true`, the item sliced. Default: `false`.

#### Type

Boolean.

---

### LegacyTextItem.tags

`legacyTextItems[index].tags`

#### Description

The tags contained in this item.

#### Type

[Tags](./Tags.md), read-only.

---

### LegacyTextItem.top

`legacyTextItems[index].top`

#### Description

The position of the top of the item (in points, measured from the bottom of the page).

#### Type

Number (double).

---

### LegacyTextItem.typename

`legacyTextItems[index].typename`

#### Description

The class name of the referenced object.

#### Type

String, read-only.

---

### LegacyTextItem.uRL

`legacyTextItems[index].uRL`

#### Description

The value of the Adobe URL tag assigned to this item.

#### Type

String.

---

### LegacyTextItem.visibilityVariable

`legacyTextItems[index].visibilityVariable`

#### Description

The visibility variable bound to the item.

#### Type

[Variable](./Variable.md)

---

### LegacyTextItem.visibleBounds

`legacyTextItems[index].visibleBounds`

#### Description

The visible bounds of the item including stroke width.

#### Type

Array of 4 numbers, read-only.

---

### LegacyTextItem.width

`legacyTextItems[index].width`

#### Description

The width of the item.

#### Type

Number (double).

---

### LegacyTextItem.wrapInside

`legacyTextItems[index].wrapInside`

#### Description

If `true`, the text frame object should be wrapped inside this object.

#### Type

Boolean.

---

### LegacyTextItem.wrapOffset

`legacyTextItems[index].wrapOffset`

#### Description

The offset to use when wrapping text around this object.

#### Type

Number (double).

---

### LegacyTextItem.wrapped

`legacyTextItems[index].wrapped`

#### Description

If `true`, wrap text frame objects around this object (text frame must be above the object).

#### Type

Boolean.

---

### LegacyTextItem.zOrderPosition

`legacyTextItems[index].zOrderPosition`

#### Description

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

#### Type

Number (long), read-only.

---

## Methods

### LegacyTextItem.convertToNative()

`legacyTextItems[index].convertToNative()`

#### Description

Converts the legacy text item to a text frame and deletes the original legacy text.

#### Returns

[GroupItem](./GroupItem.md)

---

### LegacyTextItem.duplicate()

`legacyTextItems[index].duplicate([relativeObject]
[,insertionLocation])`

#### Description

Creates a duplicate of the selected object.

#### Parameters

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

#### Returns

[LegacyTextItem](#jsobjref-legacytextitem)

---

### LegacyTextItem.move()

`legacyTextItems[index].move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

#### Returns

[LegacyTextItem](#jsobjref-legacytextitem)

---

### LegacyTextItem.remove()

`legacyTextItems[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### LegacyTextItem.resize()

```javascript
legacyTextItem.resize(
    scaleX,
    scaleY
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,changeLineWidths]
    [,scaleAbout]
)
```

#### Description

Scales the art item where scaleX is the horizontal scaling factor and scaleY is the vertical scaling factor. 100.0 = 100%.

#### Parameters

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

#### Returns

Nothing.

---

### LegacyTextItem.rotate()

```javascript
legacyTextItem.rotate(
    angle
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,rotateAbout]
)
```

#### Description

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the `angle` value is positive, clockwise if the value is negative.

#### Parameters

| Parameter             | Type                                                                                           | Description                                             |
|-----------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `angle`               | Number (double)                                                                                | The angle amount to rotate the element                  |
| `changePositions`     | Boolean, optional                                                                              | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                                              | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                                              | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                                              | Whether to transform stroke patterns                    |
| `rotateAbout`         | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about          |

#### Returns

Nothing.

---

### LegacyTextItem.transform()

```javascript
legacyTextItem.transform(
    transformationMatrix
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,changeLineWidths]
    [,transformAbout]
)
```

#### Description

Transforms the art item by applying a transformation matrix.

#### Parameters

| Parameter              | Type                                                                                           | Description                                    |
|------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
| `transformationMatrix` | [Matrix](./Matrix.md)                                                            | Transformation matrix to apply                 |
| `changePositions`      | Boolean, optional                                                                              | Whether to change Positions                    |
| `changeFillPatterns`   | Boolean, optional                                                                              | Whether to change Fill Patterns                |
| `changeFillGradients`  | Boolean, optional                                                                              | Whether to change Fill Gradients               |
| `changeStrokePattern`  | Boolean, optional                                                                              | Whether to change Stroke Pattern               |
| `changeLineWidths`     | Number (double), optional                                                                      | The amount to scale line widths                |
| `transformAbout`       | [Transformation](scripting-constants.md#jsobjref-scripting-constants-transformation), optional | The point to use as anchor, to transform about |

#### Returns

Nothing.

---

### LegacyTextItem.translate()

```javascript
legacyTextItem.translate(
    [deltaX]
    [,deltaY]
    [,transformObjects]
    [,transformFillPatterns]
    [,transformFillGradients]
    [,transformStrokePatterns]
)
```

#### Description

Repositions the art item relative to the current position, where `deltaX` is the horizontal offset and `deltaY` is the vertical offset.

#### Parameters

| Parameter                 | Type                      | Description                          |
|---------------------------|---------------------------|--------------------------------------|
| `deltaX`                  | Number (double), optional | Horizontal offset                    |
| `deltaY`                  | Number (double), optional | Vertical offset                      |
| `transformObjects`        | Boolean, optional         | Whether to transform Objects         |
| `transformFillPatterns`   | Boolean, optional         | Whether to transform Fill Patterns   |
| `transformFillGradients`  | Boolean, optional         | Whether to transform Fill Gradients  |
| `transformStrokePatterns` | Boolean, optional         | Whether to transform Stroke Patterns |

#### Returns

Nothing.

---

### LegacyTextItem.zOrder()

`legacyTextItems[index].zOrder(zOrderCmd)`

#### Description

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

#### Parameters

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

#### Returns

Nothing.
