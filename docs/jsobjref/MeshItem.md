# MeshItem

`app.activeDocument.meshItems[index`

**Description**

A gradient mesh art item. You cannot create mesh items from a script. However, you can copy an existing mesh item with the `duplicate` method, then use the one of the move methods to place the copy at the proper location.

---

## Properties

### MeshItem.artworkKnockout

`app.activeDocument.meshItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

### MeshItem.blendingMode

`app.activeDocument.meshItems[index].blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

### MeshItem.controlBounds

`app.activeDocument.meshItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

---

### MeshItem.editable

`app.activeDocument.meshItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean, read-only.

---

### MeshItem.geometricBounds

`app.activeDocument.meshItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

---

### MeshItem.height

`app.activeDocument.meshItems[index].height`

**Description**

The height of the group item.

**Type**

Number (double).

---

### MeshItem.hidden

`app.activeDocument.meshItems[index].hidden`

**Description**

If `true`, this item is hidden.

**Type**

Boolean.

---

### MeshItem.isIsolated

`app.activeDocument.meshItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean.

---

### MeshItem.layer

`app.activeDocument.meshItems[index].layer`

**Description**

The layer to which this item belongs.

**Type**

[Layer](./Layer.md), read-only.

---

### MeshItem.left

`app.activeDocument.meshItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

---

### MeshItem.locked

`app.activeDocument.meshItems[index].locked`

**Description**

If `true`, this item is locked.

**Type**

Boolean.

---

### MeshItem.name

`app.activeDocument.meshItems[index].name`

**Description**

The name of this item.

**Type**

String.

---

### MeshItem.note

`app.activeDocument.meshItems[index].note`

**Description**

The note assigned to this item.

**Type**

String.

---

### MeshItem.opacity

`app.activeDocument.meshItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0.

**Type**

Number (double).

---

### MeshItem.parent

`app.activeDocument.meshItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](./Layer.md) or [GroupItem](./GroupItem.md), read-only.

---

### MeshItem.position

`app.activeDocument.meshItems[index].position`

**Description**

The position (in points) of the top left corner of the [MeshItem](#jsobjref-meshitem) object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

---

### MeshItem.selected

`app.activeDocument.meshItems[index].selected`

**Description**

If `true`, this item is selected.

**Type**

Boolean.

---

### MeshItem.sliced

`app.activeDocument.meshItems[index].sliced`

**Description**

If `true`, the item sliced. Default: `false`.

**Type**

Boolean.

---

### MeshItem.tags

`app.activeDocument.meshItems[index].tags`

**Description**

The tags contained in this item.

**Type**

[Tags](./Tags.md), read-only.

---

### MeshItem.top

`app.activeDocument.meshItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

---

### MeshItem.typename

`app.activeDocument.meshItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

### MeshItem.uRL

`app.activeDocument.meshItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String.

---

### MeshItem.visibilityVariable

`app.activeDocument.meshItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

[Variable](./Variable.md)

---

### MeshItem.visibleBounds

`app.activeDocument.meshItems[index].visibleBounds`

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers, read-only.

---

### MeshItem.width

`app.activeDocument.meshItems[index].width`

**Description**

The width of the item.

**Type**

Number (double).

---

### MeshItem.wrapInside

`app.activeDocument.meshItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean.

---

### MeshItem.wrapOffset

`app.activeDocument.meshItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

---

### MeshItem.wrapped

`app.activeDocument.meshItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

---

### MeshItem.zOrderPosition

`app.activeDocument.meshItems[index].zOrderPosition`

**Description**

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

**Type**

Number (long), read-only.

---

## Methods

### MeshItem.duplicate()

`app.activeDocument.meshItems[index].duplicate([relativeObject] [,insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[MeshItem](#jsobjref-meshitem)

---

### MeshItem.move()

`app.activeDocument.meshItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[MeshItem](#jsobjref-meshitem)

---

### MeshItem.remove()

`app.activeDocument.meshItems[index].move()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

### MeshItem.resize()

```default
app.activeDocument.meshItems[index].resize(
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

### MeshItem.rotate()

```default
app.activeDocument.meshItems[index].rotate(
    angle
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,rotateAbout]
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

### MeshItem.transform()

```default
app.activeDocument.meshItems[index].transform(
    transformationMatrix
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,changeLineWidths]
    [,transformAbout]
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

### MeshItem.translate()

```default
app.activeDocument.meshItems[index].translate(
    [deltaX]
    [,deltaY]
    [,transformObjects]
    [,transformFillPatterns]
    [,transformFillGradients]
    [,transformStrokePatterns]
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

### MeshItem.zOrder()

`app.activeDocument.meshItems[index].zOrder(zOrderCmd)`

**Description**

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

**Parameters**

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

**Returns**

Nothing.

---

## Example

### Example name

```default
// Locks all mesh items in the current document
if (app.documents.length > 0) {
    var doc = app.activeDocument;
    for (var i = 0; i < doc.meshItems.length; i++) {
        doc.meshItems[i].locked = true;
    }
}
```
