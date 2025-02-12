# SymbolItem

`app.activeDocument.symbolItems[index`

#### Description

An art item made reusable by adding it to the Symbols palette.

A `SymbolItem` is linked to the [Symbol](./Symbol.md) from which it was created and changes if you modify the associated `Symbol` object.

---

## Properties

### SymbolItem.artworkKnockout

`app.activeDocument.symbolItems[index].artworkKnockout`

#### Description

Is this object used to create a knockout, and if so, what kind of knockout.

#### Type

[KnockoutState](scripting-constants.md#knockoutstate)

---

### SymbolItem.blendingMode

`app.activeDocument.symbolItems[index].blendingMode`

#### Description

The blend mode used when compositing an object.

#### Type

[BlendModes](scripting-constants.md#blendmodes)

---

### SymbolItem.controlBounds

`app.activeDocument.symbolItems[index].controlBounds`

#### Description

The bounds of the object including stroke width and controls.

#### Type

Array of 4 Numbers; read-only.

---

### SymbolItem.editable

`app.activeDocument.symbolItems[index].editable`

#### Description

If `true`, this item is editable.

#### Type

Boolean; read-only.

---

### SymbolItem.geometricBounds

`app.activeDocument.symbolItems[index].geometricBounds`

#### Description

The bounds of the object excluding stroke width.

#### Type

Array of 4 Numbers; read-only.

---

### SymbolItem.height

`app.activeDocument.symbolItems[index].height`

#### Description

The height of the group item.

#### Type

Number (double)

---

### SymbolItem.hidden

`app.activeDocument.symbolItems[index].hidden`

#### Description

If `true`, this item is hidden.

#### Type

Boolean

---

### SymbolItem.isIsolated

`app.activeDocument.symbolItems[index].isIsolated`

#### Description

If `true`, this object is isolated.

#### Type

Boolean

---

### SymbolItem.layer

`app.activeDocument.symbolItems[index].layer`

#### Description

The layer to which this item belongs.

#### Type

[Layer](./Layer.md); read-only.

---

### SymbolItem.left

`app.activeDocument.symbolItems[index].left`

#### Description

The position of the left side of the item (in points, measured from the left side of the page).

#### Type

Number (double)

---

### SymbolItem.locked

`app.activeDocument.symbolItems[index].locked`

#### Description

If `true`, this item is locked.

#### Type

Boolean

---

### SymbolItem.name

`app.activeDocument.symbolItems[index].name`

#### Description

The name of this item.

#### Type

String

---

### SymbolItem.note

`app.activeDocument.symbolItems[index].note`

#### Description

The note assigned to this item.

#### Type

String

---

### SymbolItem.opacity

`app.activeDocument.symbolItems[index].opacity`

#### Description

The opacity of the object.

Range: 0.0 to 100.0

#### Type

Number (double)

---

### SymbolItem.parent

`app.activeDocument.symbolItems[index].parent`

#### Description

The parent of this object.

#### Type

[Layer](./Layer.md) or [GroupItem](./GroupItem.md); read-only.

---

### SymbolItem.position

`app.activeDocument.symbolItems[index].position`

#### Description

The position (in points) of the top left corner of the `symbolItem` object in the format [x, y]. Does not include stroke weight.

#### Type

Array of 2 Numbers

---

### SymbolItem.selected

`app.activeDocument.symbolItems[index].selected`

#### Description

If `true`, this item is selected.

#### Type

Boolean

---

### SymbolItem.sliced

`app.activeDocument.symbolItems[index].sliced`

#### Description

If `true`, the item sliced.

Default: `false`

#### Type

Boolean

---

### SymbolItem.symbol

`app.activeDocument.symbolItems[index].symbol`

#### Description

The symbol that was used to create this `symbolItem`.

#### Type

[Symbol](./Symbol.md)

---

### SymbolItem.tags

`app.activeDocument.symbolItems[index].tags`

#### Description

The tags contained in this item.

#### Type

[Tags](./Tags.md); read-only.

---

### SymbolItem.top

`app.activeDocument.symbolItems[index].top`

#### Description

The position of the top of the item (in points, measured from the bottom of the page).

#### Type

Number (double)

---

### SymbolItem.typename

`app.activeDocument.symbolItems[index].typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### SymbolItem.uRL

`app.activeDocument.symbolItems[index].uRL`

#### Description

The value of the Adobe URL tag assigned to this item.

#### Type

String

---

### SymbolItem.visibilityVariable

`app.activeDocument.symbolItems[index].visibilityVariable`

#### Description

The visibility variable bound to the item.

#### Type

Variable

---

### SymbolItem.visibleBounds

`app.activeDocument.symbolItems[index].visibleBounds`

#### Description

The visible bounds of the item including stroke width.

#### Type

Array of 4 Numbers; read-only.

---

### SymbolItem.width

`app.activeDocument.symbolItems[index].width`

#### Description

The width of the item.

#### Type

Number (double)

---

### SymbolItem.wrapInside

`app.activeDocument.symbolItems[index].wrapInside`

#### Description

If `true`, the text frame object should be wrapped inside this object.

#### Type

Boolean

---

### SymbolItem.wrapOffset

`app.activeDocument.symbolItems[index].wrapOffset`

#### Description

The offset to use when wrapping text around this object.

#### Type

Number (double)

---

### SymbolItem.wrapped

`app.activeDocument.symbolItems[index].wrapped`

#### Description

If `true`, wrap text frame objects around this object (text frame must be above the object).

#### Type

Boolean

---

### SymbolItem.zOrderPosition

`app.activeDocument.symbolItems[index].zOrderPosition`

#### Description

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

#### Type

Number; read-only.

---

## Methods

### SymbolItem.duplicate()

`app.activeDocument.symbolItems[index].duplicate([relativeObject][, insertionLocation])`

#### Description

Creates a duplicate of the selected object.

#### Parameters

|      Parameter      |                                 Type                                  |        Description         |
| ------------------- | --------------------------------------------------------------------- | -------------------------- |
| `relativeObject`    | Object, optional                                                      | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to insert element |

#### Returns

[SymbolItem](#jsobjref-symbolitem)

---

### SymbolItem.move()

`app.activeDocument.symbolItems[index].move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

|      Parameter      |                                 Type                                  |          Description          |
| ------------------- | --------------------------------------------------------------------- | ----------------------------- |
| `relativeObject`    | Object                                                                | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to move element to   |

#### Returns

[SymbolItem](#jsobjref-symbolitem)

---

### SymbolItem.remove()

`app.activeDocument.symbolItems[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### SymbolItem.resize()

```javascript
app.activeDocument.symbolItems[index].resize(
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

### SymbolItem.rotate()

```javascript
app.activeDocument.symbolItems[index].rotate(
    angle
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,rotateAbout]
)
```

#### Description

Rotates the art item relative to the current rotation.

The object is rotated counter-clockwise if the `angle` value is positive, clockwise if the value is negative.

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

### SymbolItem.transform()

```javascript
app.activeDocument.symbolItems[index].transform(
    transformationMatrix
    [, changePositions]
    [, changeFillPatterns]
    [, changeFillGradients]
    [, changeStrokePattern]
    [, changeLineWidths]
    [, transformAbout]
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

### SymbolItem.translate()

```javascript
app.activeDocument.symbolItems[index].translate(
    [deltaX]
    [, deltaY]
    [, transformObjects]
    [, transformFillPatterns]
    [, transformFillGradients]
    [, transformStrokePatterns]
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

### SymbolItem.zOrder()

`app.activeDocument.symbolItems[index].zOrder(zOrderCmd)`

#### Description

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

#### Parameters

|  Parameter  |                        Type                         |            Description            |
| ----------- | --------------------------------------------------- | --------------------------------- |
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#zordermethod) | Stacking order arrangement method |

#### Returns

Nothing.
