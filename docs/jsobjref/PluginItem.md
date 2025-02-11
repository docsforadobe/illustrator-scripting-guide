# PluginItem

`app.activeDocument.pluginItems[index`

**Description**

An art item created by an Illustrator plug-in.

Scripts can create a plug-in item using [PlacedItem.trace](PlacedItem.md#jsobjref-placeditem-trace) or [RasterItem.trace()](RasterItem.md#jsobjref-rasteritem-trace), and can copy existing plug-in items using the `duplicate` method, but cannot create `PluginItem` objects directly.

---

## Properties

### PluginItem.artworkKnockout

`app.activeDocument.pluginItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

### PluginItem.blendingMode

`app.activeDocument.pluginItems[index].blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

### PluginItem.controlBounds

`app.activeDocument.pluginItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

---

### PluginItem.editable

`app.activeDocument.pluginItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean; read-only.

---

### PluginItem.geometricBounds

`app.activeDocument.pluginItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

---

### PluginItem.height

`app.activeDocument.pluginItems[index].height`

**Description**

The height of the group item.

**Type**

Number (double)

---

### PluginItem.hidden

`app.activeDocument.pluginItems[index].hidden`

**Description**

If `true`, this item is hidden.

**Type**

Boolean

---

### PluginItem.isIsolated

`app.activeDocument.pluginItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean

---

### PluginItem.isTracing

`app.activeDocument.pluginItems[index].isTracing`

**Description**

If `true`, this plug-in group represents a vector art item created by tracing a raster art item.

The `tracing` property contains the tracing object associated with the options used to create it.

**Type**

Boolean

---

### PluginItem.layer

`app.activeDocument.pluginItems[index].layer`

**Description**

The layer to which this item belongs.

**Type**

[Layer](Layer.md#jsobjref-layer); read-only.

---

### PluginItem.left

`app.activeDocument.pluginItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

---

### PluginItem.locked

`app.activeDocument.pluginItems[index].locked`

**Description**

If `true`, this item is locked.

**Type**

Boolean

---

### PluginItem.name

`app.activeDocument.pluginItems[index].name`

**Description**

The name of this item.

**Type**

String

---

### PluginItem.note

`app.activeDocument.pluginItems[index].note`

**Description**

The note assigned to this item.

**Type**

String

---

### PluginItem.opacity

`app.activeDocument.pluginItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

---

### PluginItem.parent

`app.activeDocument.pluginItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](Layer.md#jsobjref-layer) or [GroupItem](GroupItem.md#jsobjref-groupitem)

---

### PluginItem.position

`app.activeDocument.pluginItems[index].position`

**Description**

The position (in points) of the top left corner of the `pluginItem` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

---

### PluginItem.selected

`app.activeDocument.pluginItems[index].selected`

**Description**

If `true`, this item is selected.

**Type**

Boolean

---

### PluginItem.sliced

`app.activeDocument.pluginItems[index].sliced`

**Description**

If `true`, the item sliced.

Default: `false`

**Type**

Boolean

---

### PluginItem.tags

`app.activeDocument.pluginItems[index].tags`

**Description**

The tags contained in this item.

**Type**

[Tags](Tags.md#jsobjref-tags); read-only.

---

### PluginItem.top

`app.activeDocument.pluginItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

---

### PluginItem.tracing

`app.activeDocument.pluginItems[index].tracing`

**Description**

When this plug-in group was created by tracing (`isTracing` is `true`), the tracing object associated with the options used to create it.

**Type**

[TracingObject](TracingObject.md#jsobjref-tracingobject)

---

### PluginItem.typename

`app.activeDocument.pluginItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

### PluginItem.uRL

`app.activeDocument.pluginItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

---

### PluginItem.visibilityVariable

`app.activeDocument.pluginItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

[Variable](Variable.md#jsobjref-variable)

---

### PluginItem.visibleBounds

`app.activeDocument.pluginItems[index].visibleBounds`

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

---

### PluginItem.width

`app.activeDocument.pluginItems[index].width`

**Description**

The width of the item.

**Type**

Number (double)

---

### PluginItem.wrapInside

`app.activeDocument.pluginItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean

---

### PluginItem.wrapOffset

`app.activeDocument.pluginItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

---

### PluginItem.wrapped

`app.activeDocument.pluginItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

---

### PluginItem.zOrderPosition

`app.activeDocument.pluginItems[index].zOrderPosition`

**Description**

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

**Type**

Number; read-only.

---

## Methods

### PluginItem.duplicate()

`app.activeDocument.pluginItems[index].duplicate([relativeObject][, insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[PluginItem](#jsobjref-pluginitem)

---

### PluginItem.move()

`app.activeDocument.pluginItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[PluginItem](#jsobjref-pluginitem)

---

### PluginItem.remove()

`app.activeDocument.pluginItems[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

### PluginItem.resize()

`app.activeDocument.pluginItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])`

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

### PluginItem.rotate()

`app.activeDocument.pluginItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])`

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

### PluginItem.transform()

`app.activeDocument.pluginItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])`

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

### PluginItem.translate()

`app.activeDocument.pluginItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])`

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

### PluginItem.zOrder()

`app.activeDocument.pluginItems[index].zOrder(zOrderCmd)`

**Description**

Arranges the art item’s position in the stacking order of the group or layer (parent) of this object.

**Parameters**

| Parameter   | Type                                                                             | Description                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------|
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#jsobjref-scripting-constants-zordermethod) | Stacking order arrangement method |

**Returns**

Nothing.

---

## Example

### Copying a plug-in item

```default
// Creates new plug-in art by copying an existing plug-in art item
if (app.documents.length > 0 && app.activeDocument.pluginItems.length > 0) {
  var doc = app.activeDocument;
  var pluginArt = doc.pluginItems[0];
  pluginArt.duplicate(pluginArt.parent, ElementPlacement.PLACEATBEGINNING);
}
```
