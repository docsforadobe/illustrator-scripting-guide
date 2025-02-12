# TextPath

`textPath`

#### Description

A path or list of paths for area or path text. A path consists of path points that define its geometry.

---

## Properties

### TextPath.area

`textPath.area`

#### Description

The area of this path in square points. If the area is negative, the path is wound counterclockwise.

Self-intersecting paths can contain sub-areas that cancel each other out, which makes this value zero even though the path has apparent area.

#### Type

Number (double); read-only.

---

### TextPath.blendingMode

`textPath.blendingMode`

#### Description

The blend mode used when compositing an object.

#### Type

[BlendModes](scripting-constants.md#blendmodes)

---

### TextPath.clipping

`textPath.clipping`

#### Description

If true, this path should be used as a clipping path.

#### Type

Boolean

---

### TextPath.closed

`textPath.closed`

#### Description

If true, this path is closed.

#### Type

Boolean

---

### TextPath.editable

`textPath.editable`

#### Description

Read-only. If true, this item is editable.

#### Type

Boolean

---

### TextPath.evenodd

`textPath.evenodd`

#### Description

If true, the even-odd rule should be used to determine insideness.

#### Type

Boolean

---

### TextPath.fillColor

`textPath.fillColor`

#### Description

The fill color of the path.

#### Type

[Color](./Color.md)

---

### TextPath.filled

`textPath.filled`

#### Description

If true, the path be filled.

#### Type

Boolean

---

### TextPath.fillOverprint

`textPath.fillOverprint`

#### Description

If true, the art beneath a filled object should be overprinted.

#### Type

Boolean

---

### TextPath.guides

`textPath.guides`

#### Description

If true, this path is a guide object.

#### Type

Boolean

---

### TextPath.height

`textPath.height`

#### Description

The height of the group item.

#### Type

Number (double)

---

### TextPath.left

`textPath.left`

#### Description

The position of the left side of the item (in points, measured from the left side of the page).

#### Type

Number (double)

---

### TextPath.note

`textPath.note`

#### Description

The note text assigned to the path.

#### Type

String

---

### TextPath.opacity

`textPath.opacity`

#### Description

The opacity of the object.

Range: 0.0 to 100.0

#### Type

Number (double)

---

### TextPath.parent

`textPath.parent`

#### Description

Read-only. The parent of this object.

#### Type

[Layer](./Layer.md) or [GroupItem](./GroupItem.md)

---

### TextPath.pathPoints

`textPath.pathPoints`

#### Description

Read-only. The path points contained in this path item.

#### Type

[PathPoints](./PathPoints.md)

---

### TextPath.polarity

`textPath.polarity`

#### Description

The polarity of the path.

#### Type

[PolarityValues](scripting-constants.md#polarityvalues)

---

### TextPath.position

`textPath.position`

#### Description

The position (in points) of the top left corner of the textPathItem object in the format [x, y]. Does not include stroke weight.

#### Type

Array of 2 numbers

---

### TextPath.resolution

`textPath.resolution`

#### Description

The resolution of the path in dots per inch (dpi).

#### Type

Number (double)

---

### TextPath.selectedPathPoints

`textPath.selectedPathPoints`

#### Description

Read-only. All of the selected path points in the path.

#### Type

[PathPoints](./PathPoints.md)

---

### TextPath.strokeCap

`textPath.strokeCap`

#### Description

The type of line capping.

#### Type

[StrokeCap](scripting-constants.md#strokecap)

---

### TextPath.strokeColor

`textPath.strokeColor`

#### Description

The stroke color for the path.

#### Type

[Color](./Color.md)

---

### TextPath.stroked

`textPath.stroked`

#### Description

If true, the path should be stroked.

#### Type

Boolean

---

### TextPath.strokeDashes

`textPath.strokeDashes`

#### Description

Dash lengths. Set to an empty object, {}, for a solid line.

#### Type

Object

---

### TextPath.strokeDashOffset

`textPath.strokeDashOffset`

#### Description

The default distance into the dash pattern at which the pattern should be started.

#### Type

Number (double)

---

### TextPath.strokeJoin

`textPath.strokeJoin`

#### Description

Type of joints for the path.

#### Type

[StrokeJoin](scripting-constants.md#strokejoin)

---

### TextPath.strokeMiterLimit

`textPath.strokeMiterLimit`

#### Description

When a default stroke join is set to mitered, this property specifies when the join will be converted to beveled (squared-off) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. A value of 1 specifies a bevel join.

Range: 1 to 500.

Default: 4

#### Type

Number (double)

---

### TextPath.strokeOverprint

`textPath.strokeOverprint`

#### Description

If true, the art beneath a stroked object should be overprinted.

#### Type

Boolean

---

### TextPath.strokeWidth

`textPath.strokeWidth`

#### Description

Width of the stroke.

#### Type

Number (double)

---

### TextPath.top

`textPath.top`

#### Description

The position of the top of the item (in points, measured from the bottom of the page).

#### Type

Number (double)

---

### TextPath.typename

`textPath.typename`

#### Description

Read-only. The class name of the referenced object.

#### Type

String

---

### TextPath.width

`textPath.width`

#### Description

The width of the item.

#### Type

Number (double)

---

## Methods

### TextPath.setEntirePath()

`textPath.setEntirePath(pathPoints)`

#### Description

Sets the path using the array of points specified as [x, y] coordinate pairs.

#### Parameters

|  Parameter   |               Type               |        Description         |
| ------------ | -------------------------------- | -------------------------- |
| `pathPoints` | Array of [x, y] coordinate pairs | Path points to set path as |

#### Returns

Nothing.

---

## Example
