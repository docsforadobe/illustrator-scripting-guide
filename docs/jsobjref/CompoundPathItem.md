<a id="jsobjref-compoundpathitem"></a>

# CompoundPathItem

`app.activeDocument.activeLayer.compoundPathItems[index`

**Description**

A compound path. These objects are composed of multiple intersecting paths, resulting in transparent interior spaces where the component paths overlap. The pathItems property provides access to the paths that make up the compound path.

Paths contained within a compound path or group in a document are returned as individual paths when a script asks for the paths contained in the document. However, paths contained in a compound path or group are not returned when a script asks for the paths in a layer that contains the compound path or group.

All paths within a compound path share property values. Therefore, if you set the value of a property of any one of the paths in the compound path, the properties of all other component paths are updated with the new value.

---

## Properties

<a id="jsobjref-compoundpathitem-artworkknockout"></a>

### CompoundPathItem.artworkKnockout

`app.activeDocument.activeLayer.compoundPathItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

<a id="jsobjref-compoundpathitem-blendingmode"></a>

### CompoundPathItem.blendingMode

`app.activeDocument.activeLayer.compoundPathItems[index].blendingMode`

**Description**

The mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

<a id="jsobjref-compoundpathitem-controlbounds"></a>

### CompoundPathItem.controlBounds

`app.activeDocument.activeLayer.compoundPathItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-compoundpathitem-editable"></a>

### CompoundPathItem.editable

`app.activeDocument.activeLayer.compoundPathItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean, read-only.

---

<a id="jsobjref-compoundpathitem-geometricbounds"></a>

### CompoundPathItem.geometricBounds

`app.activeDocument.activeLayer.compoundPathItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-compoundpathitem-height"></a>

### CompoundPathItem.height

`app.activeDocument.activeLayer.compoundPathItems[index].height`

**Description**

The height of the compound path item excluding stroke width.

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-hidden"></a>

### CompoundPathItem.hidden

`app.activeDocument.activeLayer.compoundPathItems[index].hidden`

**Description**

If `true`, this compound path item is hidden.

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-isisolated"></a>

### CompoundPathItem.isIsolated

`app.activeDocument.activeLayer.compoundPathItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-layer"></a>

### CompoundPathItem.layer

`app.activeDocument.activeLayer.compoundPathItems[index].layer`

**Description**

The layer to which this compound path item belongs.

**Type**

[Layer](Layer.md#jsobjref-layer), read-only.

---

<a id="jsobjref-compoundpathitem-left"></a>

### CompoundPathItem.left

`app.activeDocument.activeLayer.compoundPathItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-locked"></a>

### CompoundPathItem.locked

`app.activeDocument.activeLayer.compoundPathItems[index].locked`

**Description**

If `true`, this compound path item is locked.

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-name"></a>

### CompoundPathItem.name

`app.activeDocument.activeLayer.compoundPathItems[index].name`

**Description**

The name of this compound path item.

**Type**

String.

---

<a id="jsobjref-compoundpathitem-note"></a>

### CompoundPathItem.note

`app.activeDocument.activeLayer.compoundPathItems[index].note`

**Description**

The note assigned to this item.

**Type**

String.

---

<a id="jsobjref-compoundpathitem-opacity"></a>

### CompoundPathItem.opacity

`app.activeDocument.activeLayer.compoundPathItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-parent"></a>

### CompoundPathItem.parent

`app.activeDocument.activeLayer.compoundPathItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](Layer.md#jsobjref-layer) or [GroupItem](GroupItem.md#jsobjref-groupitem), read-only.

---

<a id="jsobjref-compoundpathitem-pathitems"></a>

### CompoundPathItem.pathItems

`app.activeDocument.activeLayer.compoundPathItems[index].pathItems`

**Description**

The path art items in this compound path.

**Type**

[PathItems](PathItems.md#jsobjref-pathitems), read-only.

---

<a id="jsobjref-compoundpathitem-position"></a>

### CompoundPathItem.position

`app.activeDocument.activeLayer.compoundPathItems[index].position`

**Description**

The position (in points) of the top left corner of the `compoundPathItem` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers.

---

<a id="jsobjref-compoundpathitem-selected"></a>

### CompoundPathItem.selected

`app.activeDocument.activeLayer.compoundPathItems[index].selected`

**Description**

If `true`, this compound path item is selected.

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-sliced"></a>

### CompoundPathItem.sliced

`app.activeDocument.activeLayer.compoundPathItems[index].sliced`

**Description**

If `true`, the item is sliced. Default: `false`

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-tags"></a>

### CompoundPathItem.tags

`app.activeDocument.activeLayer.compoundPathItems[index].tags`

**Description**

The tags contained in this object.

**Type**

[Tags](Tags.md#jsobjref-tags), read-only.

---

<a id="jsobjref-compoundpathitem-top"></a>

### CompoundPathItem.top

`app.activeDocument.activeLayer.compoundPathItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-typename"></a>

### CompoundPathItem.typename

`app.activeDocument.activeLayer.compoundPathItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-compoundpathitem-url"></a>

### CompoundPathItem.uRL

`app.activeDocument.activeLayer.compoundPathItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this compound path item.

**Type**

String.

---

<a id="jsobjref-compoundpathitem-visibilityvariable"></a>

### CompoundPathItem.visibilityVariable

`app.activeDocument.activeLayer.compoundPathItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

Variant.

---

<a id="jsobjref-compoundpathitem-visiblebounds"></a>

### CompoundPathItem.visibleBounds

`app.activeDocument.activeLayer.compoundPathItems[index].visibleBounds`

**Description**

The visible bounds of the compound path item including stroke width.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-compoundpathitem-width"></a>

### CompoundPathItem.width

`app.activeDocument.activeLayer.compoundPathItems[index].width`

**Description**

The width of the compound path item excluding stroke width.

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-wrapinside"></a>

### CompoundPathItem.wrapInside

`app.activeDocument.activeLayer.compoundPathItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-wrapoffset"></a>

### CompoundPathItem.wrapOffset

`app.activeDocument.activeLayer.compoundPathItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double).

---

<a id="jsobjref-compoundpathitem-wrapped"></a>

### CompoundPathItem.wrapped

`app.activeDocument.activeLayer.compoundPathItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean.

---

<a id="jsobjref-compoundpathitem-zorderposition"></a>

### CompoundPathItem.zOrderPosition

`app.activeDocument.activeLayer.compoundPathItems[index].zOrderPosition`

**Description**

The position of this art item within the stacking order of the group or layer (`Parent`) that contains the art item.

**Type**

Number (long), read-only.

---

## Methods

<a id="jsobjref-compoundpathitem-duplicate"></a>

### CompoundPathItem.duplicate()

`app.activeDocument.activeLayer.compoundPathItems[index].duplicate([relativeObject][,insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[CompoundPathItem](#jsobjref-compoundpathitem)

---

<a id="jsobjref-compoundpathitem-move"></a>

### CompoundPathItem.move()

`app.activeDocument.activeLayer.compoundPathItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

Nothing.

---

<a id="jsobjref-compoundpathitem-remove"></a>

### CompoundPathItem.remove()

`app.activeDocument.activeLayer.compoundPathItems[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

<a id="jsobjref-compoundpathitem-resize"></a>

### CompoundPathItem.resize()

```default
app.activeDocument.activeLayer.compoundPathItems[index].resize(
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

<a id="jsobjref-compoundpathitem-rotate"></a>

### CompoundPathItem.rotate()

```default
app.activeDocument.activeLayer.compoundPathItems[index].rotate(
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

<a id="jsobjref-compoundpathitem-transform"></a>

### compoundPathItem.transform()

```default
app.activeDocument.activeLayer.compoundPathItems[index].transform(
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

<a id="jsobjref-compoundpathitem-translate"></a>

### CompoundPathItem.translate()

```default
app.activeDocument.activeLayer.compoundPathItems[index].translate(
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

<a id="jsobjref-compoundpathitem-zorder"></a>

### CompoundPathItem.zOrder()

`app.activeDocument.activeLayer.compoundPathItems[index].zOrder(zOrderCmd)`

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

### Selecting paths in a document

```default
// Selects all paths not part of a compound path
if ( app.documents.length > 0 ) {
    var doc = app.activeDocument;
    var count = 0;
    if ( doc.pathItems.length > 0 ) {
        var thePaths = doc.pathItems;
        var numPaths = thePaths.length;
        for ( var i = 0; i < doc.pathItems.length; i++ ) {
        var pathArt = doc.pathItems[i];
        if ( pathArt.parent.typename != "compoundPathItem" ) {
            pathArt.selected = true;
            count++;
        }
    }
}
```

### Creating and modifying a compound path item

```default
// Creates a new compound path item containing 3 path
// items, then sets the width and the color of the stroke
// to all items in the compound path

if (app.documents.length > 0) {
  var doc = app.activeDocument;
  var newCompoundPath = doc.activeLayer.compoundPathItems.add();

  // Create the path items
  var newPath = newCompoundPath.pathItems.add();
  newPath.setEntirePath(Array(Array(30, 50), Array(30, 100)));

  newPath = newCompoundPath.pathItems.add();
  newPath.setEntirePath(Array(Array(40, 100), Array(100, 100)));

  newPath = newCompoundPath.pathItems.add();
  newPath.setEntirePath(Array(Array(100, 110), Array(100, 300)));

  // Set stroke and width properties of the compound path
  newPath.stroked = true;
  newPath.strokeWidth = 3.5;
  newPath.strokeColor = app.activeDocument.swatches[3].color;
}
```
