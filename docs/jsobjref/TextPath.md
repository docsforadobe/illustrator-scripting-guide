<a id="jsobjref-textpath"></a>

# TextPath

`textPath`

**Description**

A path or list of paths for area or path text. A path consists of path points that define its geometry.

---

## Properties

<a id="jsobjref-textpath-area"></a>

### TextPath.area

`textPath.area`

**Description**

The area of this path in square points. If the area is negative, the path is wound counterclockwise.

Self-intersecting paths can contain sub-areas that cancel each other out, which makes this value zero even though the path has apparent area.

**Type**

Number (double), read-only.

---

<a id="jsobjref-textpath-blendingmode"></a>

### TextPath.blendingMode

`textPath.blendingMode`

**Description**

The blend mode used when compositing an object.

**Type**

[BlendModes](scripting-constants.md#jsobjref-scripting-constants-blendmodes)

---

<a id="jsobjref-textpath-clipping"></a>

### TextPath.clipping

`textPath.clipping`

**Description**

If true, this path should be used as a clipping path.

**Type**

Boolean

---

<a id="jsobjref-textpath-closed"></a>

### TextPath.closed

`textPath.closed`

**Description**

If true, this path is closed.

**Type**

Boolean

---

<a id="jsobjref-textpath-editable"></a>

### TextPath.editable

`textPath.editable`

**Description**

Read-only. If true, this item is editable.

**Type**

Boolean

---

<a id="jsobjref-textpath-evenodd"></a>

### TextPath.evenodd

`textPath.evenodd`

**Description**

If true, the even-odd rule should be used to determine insideness.

**Type**

Boolean

---

<a id="jsobjref-textpath-fillcolor"></a>

### TextPath.fillColor

`textPath.fillColor`

**Description**

The fill color of the path.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-textpath-filled"></a>

### TextPath.filled

`textPath.filled`

**Description**

If true, the path be filled.

**Type**

Boolean

---

<a id="jsobjref-textpath-filloverprint"></a>

### TextPath.fillOverprint

`textPath.fillOverprint`

**Description**

If true, the art beneath a filled object should be overprinted.

**Type**

Boolean

---

<a id="jsobjref-textpath-guides"></a>

### TextPath.guides

`textPath.guides`

**Description**

If true, this path is a guide object.

**Type**

Boolean

---

<a id="jsobjref-textpath-height"></a>

### TextPath.height

`textPath.height`

**Description**

The height of the group item.

**Type**

Number (double)

---

<a id="jsobjref-textpath-left"></a>

### TextPath.left

`textPath.left`

**Description**

The position of the left side of the item (in points, measured from the left side of the page).

**Type**

Number (double)

---

<a id="jsobjref-textpath-note"></a>

### TextPath.note

`textPath.note`

**Description**

The note text assigned to the path.

**Type**

String

---

<a id="jsobjref-textpath-opacity"></a>

### TextPath.opacity

`textPath.opacity`

**Description**

The opacity of the object. Range: 0.0 to 100.0

**Type**

Number (double)

---

<a id="jsobjref-textpath-parent"></a>

### TextPath.parent

`textPath.parent`

**Description**

Read-only. The parent of this object.

**Type**

[Layer](Layer.md#jsobjref-layer) or [GroupItem](GroupItem.md#jsobjref-groupitem)

---

<a id="jsobjref-textpath-pathpoints"></a>

### TextPath.pathPoints

`textPath.pathPoints`

**Description**

Read-only. The path points contained in this path item.

**Type**

[PathPoints](PathPoints.md#jsobjref-pathpoints)

---

<a id="jsobjref-textpath-polarity"></a>

### TextPath.polarity

`textPath.polarity`

**Description**

The polarity of the path.

**Type**

[PolarityValues](scripting-constants.md#jsobjref-scripting-constants-polarityvalues)

---

<a id="jsobjref-textpath-position"></a>

### TextPath.position

`textPath.position`

**Description**

The position (in points) of the top left corner of the textPathItem object in the format [x, y]. Does not include stroke weight.

**Type**

Array of 2 numbers

---

<a id="jsobjref-textpath-resolution"></a>

### TextPath.resolution

`textPath.resolution`

**Description**

The resolution of the path in dots per inch (dpi).

**Type**

Number (double)

---

<a id="jsobjref-textpath-selectedpathpoints"></a>

### TextPath.selectedPathPoints

`textPath.selectedPathPoints`

**Description**

Read-only. All of the selected path points in the path.

**Type**

[PathPoints](PathPoints.md#jsobjref-pathpoints)

---

<a id="jsobjref-textpath-strokecap"></a>

### TextPath.strokeCap

`textPath.strokeCap`

**Description**

The type of line capping.

**Type**

[StrokeCap](scripting-constants.md#jsobjref-scripting-constants-strokecap)

---

<a id="jsobjref-textpath-strokecolor"></a>

### TextPath.strokeColor

`textPath.strokeColor`

**Description**

The stroke color for the path.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-textpath-stroked"></a>

### TextPath.stroked

`textPath.stroked`

**Description**

If true, the path should be stroked.

**Type**

Boolean

---

<a id="jsobjref-textpath-strokedashes"></a>

### TextPath.strokeDashes

`textPath.strokeDashes`

**Description**

Dash lengths. Set to an empty object, {}, for a solid line.

**Type**

Object

---

<a id="jsobjref-textpath-strokedashoffset"></a>

### TextPath.strokeDashOffset

`textPath.strokeDashOffset`

**Description**

The default distance into the dash pattern at which the pattern should be started.

**Type**

Number (double)

---

<a id="jsobjref-textpath-strokejoin"></a>

### TextPath.strokeJoin

`textPath.strokeJoin`

**Description**

Type of joints for the path.

**Type**

[StrokeJoin](scripting-constants.md#jsobjref-scripting-constants-strokejoin)

---

<a id="jsobjref-textpath-strokemiterlimit"></a>

### TextPath.strokeMiterLimit

`textPath.strokeMiterLimit`

**Description**

When a default stroke join is set to mitered, this property specifies when the join will be converted to beveled (squared-off) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. A value of 1 specifies a bevel join. Range: 1 to 500. Default: 4

**Type**

Number (double)

---

<a id="jsobjref-textpath-strokeoverprint"></a>

### TextPath.strokeOverprint

`textPath.strokeOverprint`

**Description**

If true, the art beneath a stroked object should be overprinted.

**Type**

Boolean

---

<a id="jsobjref-textpath-strokewidth"></a>

### TextPath.strokeWidth

`textPath.strokeWidth`

**Description**

Width of the stroke.

**Type**

Number (double)

---

<a id="jsobjref-textpath-top"></a>

### TextPath.top

`textPath.top`

**Description**

The position of the top of the item (in points, measured from the bottom of the page).

**Type**

Number (double)

---

<a id="jsobjref-textpath-typename"></a>

### TextPath.typename

`textPath.typename`

**Description**

Read-only. The class name of the referenced object.

**Type**

String

---

<a id="jsobjref-textpath-width"></a>

### TextPath.width

`textPath.width`

**Description**

The width of the item.

**Type**

Number (double)

---

## Methods

<a id="jsobjref-textpath-setentirepath"></a>

### TextPath.setEntirePath()

`textPath.setEntirePath(pathPoints)`

**Description**

Sets the path using the array of points specified as [x, y] coordinate pairs.

**Parameters**

| Parameter    | Type                             | Description                |
|--------------|----------------------------------|----------------------------|
| `pathPoints` | Array of [x, y] coordinate pairs | Path points to set path as |

**Returns**

Nothing.

---

## Example
