# NonNativeItem

`nonNativeItems[index`

#### Description

A non-native artwork item.

---

## Properties

### NonNativeItem.artworkKnockout

`nonNativeItems[index].artworkKnockout`

#### Description

Is this object used to create a knockout, and if so, what kind of knockout.

#### Type

[KnockoutState](scripting-constants.md#knockoutstate)

---

### NonNativeItem.blendingMode

`nonNativeItems[index].blendingMode`

#### Description

The blend mode used when compositing an object.

#### Type

[BlendModes](scripting-constants.md#blendmodes)

---

### NonNativeItem.controlBounds

`nonNativeItems[index].controlBounds`

#### Description

The bounds of the object including stroke width and controls.

#### Type

Array of 4 numbers; read-only.

---

### NonNativeItem.editable

`nonNativeItems[index].editable`

#### Description

If `true`, this item is editable.

#### Type

Boolean; read-only.

---

### NonNativeItem.geometricBounds

`nonNativeItems[index].geometricBounds`

#### Description

The bounds of the object excluding stroke width.

#### Type

Array of 4 numbers; read-only.

---

### NonNativeItem.height

`nonNativeItems[index].height`

#### Description

The height of the group item.

#### Type

Number (double).

---

### NonNativeItem.hidden

`nonNativeItems[index].hidden`

#### Description

If `true`, this item is hidden.

#### Type

Boolean.

---

### NonNativeItem.isIsolated

`nonNativeItems[index].isIsolated`

#### Description

If `true`, this object is isolated.

#### Type

Boolean.

---

### NonNativeItem.layer

`nonNativeItems[index].layer`

#### Description

The layer to which this item belongs.

#### Type

[Layer](./Layer.md); read-only.

---

### NonNativeItem.left

`nonNativeItems[index].left`

#### Description

The position of the left side of the item (in points, measured from the left side of the page).

#### Type

Number (double).

---

### NonNativeItem.locked

`nonNativeItems[index].locked`

#### Description

If `true`, this item is locked.

#### Type

Boolean.

---

### NonNativeItem.name

`nonNativeItems[index].name`

#### Description

The name of this item.

#### Type

String.

---

### NonNativeItem.note

`nonNativeItems[index].note`

#### Description

The note assigned to this item.

#### Type

String.

---

### NonNativeItem.opacity

`nonNativeItems[index].opacity`

#### Description

The opacity of the object.

Range: 0.0 to 100.0.

#### Type

Number (double).

---

### NonNativeItem.parent

`nonNativeItems[index].parent`

#### Description

The parent of this object.

#### Type

[Document](./Document.md), [Layer](./Layer.md) or [GroupItem](./GroupItem.md); read-only.

---

### NonNativeItem.position

`nonNativeItems[index].position`

#### Description

The position (in points) of the top left corner of the `NonNativeItems[index` object in the format [x, y]. Does not include stroke weight.

#### Type

Array of 2 numbers.

---

### NonNativeItem.selected

`nonNativeItems[index].selected`

#### Description

If `true`, this item is selected.

#### Type

Boolean.

---

### NonNativeItem.sliced

`nonNativeItems[index].sliced`

#### Description

If `true`, the item sliced.

Default: `false`.

#### Type

Boolean.

---

### NonNativeItem.tags

`nonNativeItems[index].tags`

#### Description

The tags contained in this item.

#### Type

[Tags](./Tags.md); read-only.

---

### NonNativeItem.top

`nonNativeItems[index].top`

#### Description

The position of the top of the item (in points, measured from the bottom of the page).

#### Type

Number (double).

---

### NonNativeItem.typename

`nonNativeItems[index].typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### NonNativeItem.uRL

`nonNativeItems[index].uRL`

#### Description

The value of the Adobe URL tag assigned to this item.

#### Type

String.

---

### NonNativeItem.visibilityVariable

`nonNativeItems[index].visibilityVariable`

#### Description

The visibility variable bound to the item.

#### Type

[Variable](./Variable.md)

---

### NonNativeItem.visibleBounds

`nonNativeItems[index].visibleBounds`

#### Description

The visible bounds of the item including stroke width.

#### Type

Array of 4 numbers; read-only.

---

### NonNativeItem.width

`nonNativeItems[index].width`

#### Description

The width of the item.

#### Type

Number (double).

---

### NonNativeItem.wrapInside

`nonNativeItems[index].wrapInside`

#### Description

If `true`, the non-native-item object should be wrapped inside this object.

#### Type

Boolean.

---

### NonNativeItem.wrapOffset

`nonNativeItems[index].wrapOffset`

#### Description

The offset to use when wrapping text around this object.

#### Type

Number (double).

---

### NonNativeItem.wrapped

`nonNativeItems[index].wrapped`

#### Description

If `true`, wrap non-native-item objects around this object (non-native-item object must be above the object).

#### Type

Boolean.

---

### NonNativeItem.zOrderPosition

`nonNativeItems[index].zOrderPosition`

#### Description

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

#### Type

Number; read-only.

---

## Methods

### NonNativeItem.duplicate()

`nonNativeItems[index].duplicate([relativeObject]
[,insertionLocation])`

#### Description

Creates a duplicate of the selected object.

#### Parameters

|      Parameter      |                                 Type                                  |        Description         |
| ------------------- | --------------------------------------------------------------------- | -------------------------- |
| `relativeObject`    | Object, optional                                                      | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to insert element |

#### Returns

[NonNativeItem](#jsobjref-nonnativeitem)

---

### NonNativeItem.move()

`nonNativeItems[index].move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

|      Parameter      |                                 Type                                  |          Description          |
| ------------------- | --------------------------------------------------------------------- | ----------------------------- |
| `relativeObject`    | Object                                                                | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to move element to   |

#### Returns

[NonNativeItem](#jsobjref-nonnativeitem)

---

### NonNativeItem.remove()

`nonNativeItems[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### NonNativeItem.removeAll()

`nonNativeItems[index].removeAll()`

#### Description

Deletes all elements in this collection.

#### Returns

Nothing.

---

### NonNativeItem.resize()

```javascript
nonNativeItem.resize(
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

Scales the art item where `scaleX` is the horizontal scaling factor and `scaleY` is the vertical scaling factor. 100.0 = 100%.

#### Parameters

|       Parameter       |                               Type                                |                       Description                       |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `scaleX`              | Number (double)                                                   | Horizontal scaling factor                               |
| `scaleY`              | Number (double)                                                   | Vertical scaling factor                                 |
| `changePositions`     | Boolean, optional                                                 | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                 | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                 | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                 | Whether to transform stroke patterns                    |
| `changeLineWidths`    | Number (double), optional                                         | The amount to scale line widths                         |
| `scaleAbout`          | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about          |

#### Returns

Nothing.

---

### NonNativeItem.rotate()

```javascript
nonNativeItem.rotate(
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

|       Parameter       |                               Type                                |                       Description                       |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `angle`               | Number (double)                                                   | The angle amount to rotate the element                  |
| `changePositions`     | Boolean, optional                                                 | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                 | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                 | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                 | Whether to transform stroke patterns                    |
| `rotateAbout`         | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about          |

#### Returns

Nothing.

---

### NonNativeItem.transform()

```javascript
nonNativeItem.transform(
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

|       Parameter        |                               Type                                |                  Description                   |
| ---------------------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `transformationMatrix` | [Matrix](./Matrix.md)                                             | Transformation matrix to apply                 |
| `changePositions`      | Boolean, optional                                                 | Whether to change Positions                    |
| `changeFillPatterns`   | Boolean, optional                                                 | Whether to change Fill Patterns                |
| `changeFillGradients`  | Boolean, optional                                                 | Whether to change Fill Gradients               |
| `changeStrokePattern`  | Boolean, optional                                                 | Whether to change Stroke Pattern               |
| `changeLineWidths`     | Number (double), optional                                         | The amount to scale line widths                |
| `transformAbout`       | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about |

#### Returns

Nothing.

---

### NonNativeItem.translate()

```javascript
nonNativeItem.translate(
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

|         Parameter         |           Type            |             Description              |
| ------------------------- | ------------------------- | ------------------------------------ |
| `deltaX`                  | Number (double), optional | Horizontal offset                    |
| `deltaY`                  | Number (double), optional | Vertical offset                      |
| `transformObjects`        | Boolean, optional         | Whether to transform Objects         |
| `transformFillPatterns`   | Boolean, optional         | Whether to transform Fill Patterns   |
| `transformFillGradients`  | Boolean, optional         | Whether to transform Fill Gradients  |
| `transformStrokePatterns` | Boolean, optional         | Whether to transform Stroke Patterns |

#### Returns

Nothing.

---

### NonNativeItem.zOrder()

`nonNativeItems[index].zOrder(zOrderCmd)`

#### Description

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

#### Parameters

|  Parameter  |                        Type                         |            Description            |
| ----------- | --------------------------------------------------- | --------------------------------- |
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#zordermethod) | Stacking order arrangement method |

#### Returns

Nothing.
