<a id="jsobjref-pathitem"></a>

# PathItem

`app.activeDocument.pathItems[index]`

**Description**

Specifies a path item, which contains [PathPoint](PathPoint.md#jsobjref-pathpoint) objects that define its geometry.

The `PathItem` class gives you complete access to paths in Illustrator.

The `setEntirePath` method provides an extremely efficient way to create paths comprised of straight lines.

---

## Properties

<a id="jsobjref-pathitem-area"></a>

### PathItem.area

`app.activeDocument.pathItems[index].area`

**Description**

The area of this path in square points.

If the area is negative, the path is wound counterclockwise.

Self-intersecting paths can contain sub-areas that cancel each other out, which makes this value zero even though the path has apparent area.

**Type**

Number (double); read-only.

---

<a id="jsobjref-pathitem-artworkknockout"></a>

### PathItem.artworkKnockout

`app.activeDocument.pathItems[index].artworkKnockout`

**Description**

Is this object used to create a knockout, and if so, what kind of knockout.

**Type**

[KnockoutState](scripting-constants.md#jsobjref-scripting-constants-knockoutstate)

---

<a id="jsobjref-pathitem-blendingmode"></a>

### PathItem.blendingMode

`app.activeDocument.pathItems[index].blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

<a id="jsobjref-pathitem-clipping"></a>

### PathItem.clipping

`app.activeDocument.pathItems[index].clipping`

**Description**

If `true`, this path should be used as a clipping path.

**Type**

Boolean

---

<a id="jsobjref-pathitem-closed"></a>

### PathItem.closed

`app.activeDocument.pathItems[index].closed`

**Description**

If `true`, this path is closed.

**Type**

Boolean

---

<a id="jsobjref-pathitem-controlbounds"></a>

### PathItem.controlBounds

`app.activeDocument.pathItems[index].controlBounds`

**Description**

The bounds of the object including stroke width and controls.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-pathitem-editable"></a>

### PathItem.editable

`app.activeDocument.pathItems[index].editable`

**Description**

If `true`, this item is editable.

**Type**

Boolean; read-only.

---

<a id="jsobjref-pathitem-evenodd"></a>

### PathItem.evenodd

`app.activeDocument.pathItems[index].evenodd`

**Description**

If `true`, the even-odd rule should be used to determine “insideness.”

**Type**

Boolean

---

<a id="jsobjref-pathitem-fillcolor"></a>

### PathItem.fillColor

`app.activeDocument.pathItems[index].fillColor`

**Description**

The fill color of the path.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-pathitem-filled"></a>

### PathItem.filled

`app.activeDocument.pathItems[index].filled`

**Description**

If `true`, the path is filled.

**Type**

Boolean

---

<a id="jsobjref-pathitem-filloverprint"></a>

### PathItem.fillOverprint

`app.activeDocument.pathItems[index].fillOverprint`

**Description**

If `true`, the art beneath a filled object should be overprinted.

**Type**

Boolean

---

<a id="jsobjref-pathitem-geometricbounds"></a>

### PathItem.geometricBounds

`app.activeDocument.pathItems[index].geometricBounds`

**Description**

The bounds of the object excluding stroke width.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-pathitem-guides"></a>

### PathItem.guides

`app.activeDocument.pathItems[index].guides`

**Description**

If `true`, this path is a guide object.

**Type**

Boolean

---

<a id="jsobjref-pathitem-height"></a>

### PathItem.height

`app.activeDocument.pathItems[index].height`

**Description**

The height of the group item.

**Type**

Number (double)

---

<a id="jsobjref-pathitem-hidden"></a>

### PathItem.hidden

`app.activeDocument.pathItems[index].hidden`

**Description**

If `true`, this item is hidden.

**Type**

Boolean

---

<a id="jsobjref-pathitem-isisolated"></a>

### PathItem.isIsolated

`app.activeDocument.pathItems[index].isIsolated`

**Description**

If `true`, this object is isolated.

**Type**

Boolean

---

<a id="jsobjref-pathitem-layer"></a>

### PathItem.layer

`app.activeDocument.pathItems[index].layer`

**Description**

The layer to which this item belongs.

**Type**

[Layer](Layer.md#jsobjref-layer); read-only.

---

<a id="jsobjref-pathitem-left"></a>

### PathItem.left

`app.activeDocument.pathItems[index].left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

---

<a id="jsobjref-pathitem-length"></a>

### PathItem.length

`app.activeDocument.pathItems[index].length`

**Description**

The length of this path in points.

**Type**

Number (double)

---

<a id="jsobjref-pathitem-locked"></a>

### PathItem.locked

`app.activeDocument.pathItems[index].locked`

**Description**

If `true`, this item is locked.

**Type**

Boolean

---

<a id="jsobjref-pathitem-name"></a>

### PathItem.name

`app.activeDocument.pathItems[index].name`

**Description**

The name of this item.

**Type**

String

---

<a id="jsobjref-pathitem-note"></a>

### PathItem.note

`app.activeDocument.pathItems[index].note`

**Description**

The note assigned to this item.

**Type**

String

---

<a id="jsobjref-pathitem-opacity"></a>

### PathItem.opacity

`app.activeDocument.pathItems[index].opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

---

<a id="jsobjref-pathitem-parent"></a>

### PathItem.parent

`app.activeDocument.pathItems[index].parent`

**Description**

The parent of this object.

**Type**

[Layer](Layer.md#jsobjref-layer) or [GroupItem](GroupItem.md#jsobjref-groupitem)

---

<a id="jsobjref-pathitem-pathpoints"></a>

### PathItem.pathPoints

`app.activeDocument.pathItems[index].pathPoints`

**Description**

The path points contained in this path item.

**Type**

[PathPoints](PathPoints.md#jsobjref-pathpoints); read-only.

---

<a id="jsobjref-pathitem-pixelaligned"></a>

### PathItem.pixelAligned

`app.activeDocument.pathItems[index].pixelAligned`

**Description**

`true` if this item is aligned to the pixel grid.

**Type**

Boolean

---

<a id="jsobjref-pathitem-polarity"></a>

### PathItem.polarity

`app.activeDocument.pathItems[index].polarity`

**Description**

The polarity of the path.

**Type**

[PolarityValues](scripting-constants.md#jsobjref-scripting-constants-polarityvalues)

---

<a id="jsobjref-pathitem-position"></a>

### PathItem.position

`app.activeDocument.pathItems[index].position`

**Description**

The position (in points) of the top left corner of the `pluginItem` object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers; read-only.

---

<a id="jsobjref-pathitem-resolution"></a>

### PathItem.resolution

`app.activeDocument.pathItems[index].resolution`

**Description**

The resolution of the path in dots per inch (dpi).

**Type**

Number (double)

---

<a id="jsobjref-pathitem-selected"></a>

### PathItem.selected

`app.activeDocument.pathItems[index].selected`

**Description**

If `true`, this item is selected.

**Type**

Boolean

---

<a id="jsobjref-pathitem-selectedpathpoints"></a>

### PathItem.selectedPathPoints

`app.activeDocument.pathItems[index].selectedPathPoints`

**Description**

All of the selected path points in the path.

**Type**

[PathPoints](PathPoints.md#jsobjref-pathpoints); read-only.

---

<a id="jsobjref-pathitem-sliced"></a>

### PathItem.sliced

`app.activeDocument.pathItems[index].sliced`

**Description**

If `true`, the item sliced.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-pathitem-strokecap"></a>

### PathItem.strokeCap

`app.activeDocument.pathItems[index].strokeCap`

**Description**

The type of line capping.

**Type**

[StrokeCap](scripting-constants.md#jsobjref-scripting-constants-strokecap)

---

<a id="jsobjref-pathitem-strokecolor"></a>

### PathItem.strokeColor

`app.activeDocument.pathItems[index].strokeColor`

**Description**

The stroke color for the path.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-pathitem-stroked"></a>

### PathItem.stroked

`app.activeDocument.pathItems[index].stroked`

**Description**

If `true`, the path should be stroked.

**Type**

Boolean

---

<a id="jsobjref-pathitem-strokedashes"></a>

### PathItem.strokeDashes

`app.activeDocument.pathItems[index].strokeDashes`

**Description**

Dash lengths. Set to an empty object, {}, for a solid line.

**Type**

Object

---

<a id="jsobjref-pathitem-strokedashoffset"></a>

### PathItem.strokeDashOffset

`app.activeDocument.pathItems[index].strokeDashOffset`

**Description**

The default distance into the dash pattern at which the pattern should be started.

**Type**

Number (double)

---

<a id="jsobjref-pathitem-strokejoin"></a>

### PathItem.strokeJoin

`app.activeDocument.pathItems[index].strokeJoin`

**Description**

Type of joints for the path.

**Type**

[StrokeJoin](scripting-constants.md#jsobjref-scripting-constants-strokejoin)

---

<a id="jsobjref-pathitem-strokemiterlimit"></a>

### PathItem.strokeMiterLimit

`app.activeDocument.pathItems[index].strokeMiterLimit`

**Description**

When a default stroke join is set to mitered, this property specifies when the join will be converted to beveled (squared-off ) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. A value of 1 specifies a bevel join. Range: 1 to 500. Default: 4

**Type**

Number (double)

---

<a id="jsobjref-pathitem-strokeoverprint"></a>

### PathItem.strokeOverprint

`app.activeDocument.pathItems[index].strokeOverprint`

**Description**

If `true`, the art beneath a stroked object should be overprinted.

**Type**

Boolean

---

<a id="jsobjref-pathitem-strokewidth"></a>

### PathItem.strokeWidth

`app.activeDocument.pathItems[index].strokeWidth`

**Description**

The width of the stroke (in points).

**Type**

Number (double)

---

<a id="jsobjref-pathitem-tags"></a>

### PathItem.tags

`app.activeDocument.pathItems[index].tags`

**Description**

The tags contained in this item.

**Type**

[Tags](Tags.md#jsobjref-tags); read-only.

---

<a id="jsobjref-pathitem-top"></a>

### PathItem.top

`app.activeDocument.pathItems[index].top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

---

<a id="jsobjref-pathitem-typename"></a>

### PathItem.typename

`app.activeDocument.pathItems[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

<a id="jsobjref-pathitem-url"></a>

### PathItem.uRL

`app.activeDocument.pathItems[index].uRL`

**Description**

The value of the Adobe URL tag assigned to this item.

**Type**

String

---

<a id="jsobjref-pathitem-visibilityvariable"></a>

### PathItem.visibilityVariable

`app.activeDocument.pathItems[index].visibilityVariable`

**Description**

The visibility variable bound to the item.

**Type**

[Variable](Variable.md#jsobjref-variable)

---

<a id="jsobjref-pathitem-visiblebounds"></a>

### PathItem.visibleBounds

`app.activeDocument.pathItems[index].visibleBounds`

**Description**

The visible bounds of the item including stroke width.

**Type**

Array of 4 numbers; read-only.

---

<a id="jsobjref-pathitem-width"></a>

### PathItem.width

`app.activeDocument.pathItems[index].width`

**Description**

The width of the item.

**Type**

Number (double)

---

<a id="jsobjref-pathitem-wrapinside"></a>

### PathItem.wrapInside

`app.activeDocument.pathItems[index].wrapInside`

**Description**

If `true`, the text frame object should be wrapped inside this object.

**Type**

Boolean

---

<a id="jsobjref-pathitem-wrapoffset"></a>

### PathItem.wrapOffset

`app.activeDocument.pathItems[index].wrapOffset`

**Description**

The offset to use when wrapping text around this object.

**Type**

Number (double)

---

<a id="jsobjref-pathitem-wrapped"></a>

### PathItem.wrapped

`app.activeDocument.pathItems[index].wrapped`

**Description**

If `true`, wrap text frame objects around this object (text frame must be above the object).

**Type**

Boolean

---

<a id="jsobjref-pathitem-zorderposition"></a>

### PathItem.zOrderPosition

`app.activeDocument.pathItems[index].zOrderPosition`

**Description**

The position of this item within the stacking order of the group or layer (`parent`) that contains the item.

**Type**

Number; read-only.

---

## Methods

<a id="jsobjref-pathitem-duplicate"></a>

### PathItem.duplicate()

`app.activeDocument.pathItems[index].duplicate([relativeObject][, insertionLocation])`

**Description**

Creates a duplicate of the selected object.

**Parameters**

| Parameter           | Type                                                                                               | Description                |
|---------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| `relativeObject`    | Object, optional                                                                                   | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to insert element |

**Returns**

[PathItem](#jsobjref-pathitem)

---

<a id="jsobjref-pathitem-move"></a>

### PathItem.move()

`app.activeDocument.pathItems[index].move(relativeObject, insertionLocation)`

**Description**

Moves the object.

**Parameters**

| Parameter           | Type                                                                                               | Description                   |
|---------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `relativeObject`    | Object                                                                                             | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#jsobjref-scripting-constants-elementplacement), optional | Location to move element to   |

**Returns**

[PathItem](#jsobjref-pathitem)

---

<a id="jsobjref-pathitem-remove"></a>

### PathItem.remove()

`app.activeDocument.pathItems[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

<a id="jsobjref-pathitem-resize"></a>

### PathItem.resize()

`app.activeDocument.pathItems[index].resize(scaleX, scaleY[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,changeLineWidths][,scaleAbout])`

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

<a id="jsobjref-pathitem-rotate"></a>

### PathItem.rotate()

`app.activeDocument.pathItems[index].rotate(angle[,changePositions][,changeFillPatterns][,changeFillGradients][,changeStrokePattern][,rotateAbout])`

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

<a id="jsobjref-pathitem-setentirepath"></a>

### PathItem.setEntirePath()

`app.activeDocument.pathItems[index].setEntirePath(pathPoints)`

**Description**

Sets the path using an array of [x, y] coordinate pairs.

**Parameters**

| Parameter    | Type                             | Description                       |
|--------------|----------------------------------|-----------------------------------|
| `pathPoints` | Array of [x, y] coordinate pairs | Array of point coordinates to set |

**Returns**

Nothing.

---

<a id="jsobjref-pathitem-transform"></a>

### PathItem.transform()

`app.activeDocument.pathItems[index].transform(transformationMatrix[, changePositions][, changeFillPatterns][, changeFillGradients][, changeStrokePattern][, changeLineWidths][, transformAbout])`

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

<a id="jsobjref-pathitem-translate"></a>

### PathItem.translate()

`app.activeDocument.pathItems[index].translate([deltaX][, deltaY][, transformObjects][, transformFillPatterns][, transformFillGradients][, transformStrokePatterns])`

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

<a id="jsobjref-pathitem-zorder"></a>

### PathItem.zOrder()

`app.activeDocument.pathItems[index].zOrder(zOrderCmd)`

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

### Setting colors in a path

```default
// Sets the stroke and fill of a path item to colors of a randomly selected swatch
if (app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
  var doc = app.activeDocument;

  for (var i = 0; i < doc.pathItems.length; i++) {
    var pathRef = doc.pathItems[i];
    pathRef.filled = true;
    pathRef.stroked = true;

    var swatchIndex = Math.round(Math.random() * (doc.swatches.length - 1));
    pathRef.fillColor = doc.swatches[swatchIndex].color;
    pathRef.strokeColor = doc.swatches[swatchIndex].color;
  }
}
```

---

### Creating a path from straight lines

```default
// This script illustrates the use of the setEntirePath method.
// Creates a new open path consisting of 10 straight lines
if (app.documents.length > 0) {
  var lineList = [];

  for (i = 0; i < lineList.length; i++) {
    lineList.push([i * 10 + 50, ((i - 5) ^ 2) * 5 + 50];
  }

  app.defaultStroked = true;
  newPath = app.activeDocument.pathItems.add();
  newPath.setEntirePath(lineList);
}
```
