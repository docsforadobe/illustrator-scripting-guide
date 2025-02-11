# PlacedItem

`app.activeDocument.placedItems[index`

**Description**

An artwork item placed in a document as a linked file.

For example, an artwork object created using the `File > Place` command in Illustrator or using the `add()` method of the `placedItems` collection object is a placed item.

For information, see [PlacedItems](./PlacedItems.md).

---

## Properties

### PlacedItem.artworkKnockout

`app.activeDocument.placedItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

### PlacedItem.blendingMode

`app.activeDocument.placedItems[index].blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

### PlacedItem.boundingBox

`app.activeDocument.placedItems[index].boundingBox`

**Description**

The dimensions of the placed art item regardless of transformations.

**Type**

Array of 4 numbers

---

### PlacedItem.contentVariable

`app.activeDocument.placedItems[index].contentVariable`

**Description**

The content variable bound to the item.

**Type**

[Variable](./Variable.md)

---

### PlacedItem.controlBounds

`app.activeDocument.placedItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

---

### PlacedItem.editable

`app.activeDocument.placedItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean; read-only.

---

### PlacedItem.file

`app.activeDocument.placedItems[index].file`

**Description**

The file containing the artwork.

**Type**

File; read-only.

---

### PlacedItem.geometricBounds

`app.activeDocument.placedItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

---

### PlacedItem.height

`app.activeDocument.placedItems[index].height`

**Description**

The height of the group item.

**Type**

Number (double)

---

### PlacedItem.hidden

`app.activeDocument.placedItems[index].hidden`

**Description**

If `true`, this item is hidden.

**Type**

Boolean

---

### PlacedItem.isIsolated

`app.activeDocument.placedItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean

---

### PlacedItem.layer

`app.activeDocument.placedItems[index].layer`

**Description**

The layer to which this item belongs.

**Type**

[Layer](./Layer.md); read-only.

---

### PlacedItem.left

`app.activeDocument.placedItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

---

### PlacedItem.locked

`app.activeDocument.placedItems[index].locked`

**Description**

If `true`, this item is locked.

**Type**

Boolean

---

### PlacedItem.matrix

`app.activeDocument.placedItems[index].matrix`

**Description**

The transformation matrix of the placed artwork.

**Type**

[Matrix](./Matrix.md)

---

### PlacedItem.name

`app.activeDocument.placedItems[index].name`

**Description**

The name of this item.

**Type**

String

---

### PlacedItem.note

`app.activeDocument.placedItems[index].note`

**Description**

The note assigned to this item.

**Type**

String

---

### PlacedItem.opacity

`app.activeDocument.placedItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

---

### PlacedItem.parent

`app.activeDocument.placedItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](./Layer.md) or [GroupItem](./GroupItem.md)

---

### PlacedItem.position

`app.activeDocument.placedItems[index].position`

**Description**

The position (in points) of the top left corner of the `pluginItem` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

---

### PlacedItem.selected

`app.activeDocument.placedItems[index].selected`

**Description**

If `true`, this item is selected.

**Type**

Boolean

---

### PlacedItem.sliced

`app.activeDocument.placedItems[index].sliced`

**Description**

If `true`, the item sliced.

Default: `false`

**Type**

Boolean

---

### PlacedItem.tags

`app.activeDocument.placedItems[index].tags`

**Description**

The tags contained in this item.

**Type**

[Tags](./Tags.md); read-only.

---

### PlacedItem.top

`app.activeDocument.placedItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

---

### PlacedItem.typename

`app.activeDocument.placedItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

### PlacedItem.uRL

`app.activeDocument.placedItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

---

### PlacedItem.visibilityVariable

`app.activeDocument.placedItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

[Variable](./Variable.md)

---

### PlacedItem.visibleBounds

`app.activeDocument.placedItems[index].visibleBounds`

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

---

### PlacedItem.width

`app.activeDocument.placedItems[index].width`

**Description**

The width of the item.

**Type**

Number (double)

---

### PlacedItem.wrapInside

`app.activeDocument.placedItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean

---

### PlacedItem.wrapOffset

`app.activeDocument.placedItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

---

### PlacedItem.wrapped

`app.activeDocument.placedItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

---

### PlacedItem.zOrderPosition

`app.activeDocument.placedItems[index].zOrderPosition`

**Description**

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

**Type**

Number; read-only.

---

## Methods

### PlacedItem.duplicate()

`app.activeDocument.placedItems[index].duplicate([relativeObject][, insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[PlacedItem](#jsobjref-placeditem)

---

### PlacedItem.embed()

`app.activeDocument.placedItems[index].embed()`

**Description**

Embeds this art in the document. Converts the art to art item objects as needed and deletes this object.

**Returns**

Nothing.

---

### PlacedItem.move()

`app.activeDocument.placedItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[PlacedItem](#jsobjref-placeditem)

---

### PlacedItem.relink()

`app.activeDocument.placedItems[index].relink(linkFile)`

**Description**

Relinks the art object with the file that defines its content.

**Parameters**

| Parameter   | Type        | Description    |
|-------------|-------------|----------------|
| `linkFile`  | File object | File to relink |

**Returns**

Nothing.

---

### PlacedItem.remove()

`app.activeDocument.placedItems[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

### PlacedItem.resize()

`app.activeDocument.placedItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])`

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

### PlacedItem.rotate()

`app.activeDocument.placedItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])`

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

### PlacedItem.trace

`app.activeDocument.placedItems[index].trace()`

**Description**

Converts the raster art for this object to vector art, using default options.

Reorders the raster art into the source art of a plug-in group, and converts it into a group of filled and/or stroked paths that resemble the original image.

Creates and returns a [PluginItem](./PluginItem.md) object that references a [TracingObject](./TracingObject.md) object.

**Returns**

[PluginItem](./PluginItem.md)

---

### PlacedItem.transform()

`app.activeDocument.placedItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])`

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

### PlacedItem.translate()

`app.activeDocument.placedItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])`

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

### PlacedItem.zOrder()

`app.activeDocument.placedItems[index].zOrder(zOrderCmd)`

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

### Changing the selection state of placed items

```default
// Toggles the selection state of all placed items.
if (app.documents.length > 0) {
  for (i = 0; i < app.activeDocument.placedItems.length; i++) {
    var placedArt = app.activeDocument.placedItems[i];
    placedArt.selected = !(placedArt.selected);
  }
}
```
