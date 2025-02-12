# PathPoint

`app.activeDocument.pathItems[index].pathPoints[index`

#### Description

A point on a specific path.

Each path point is made up of an anchor point (`anchor`) and a pair of handles (`leftDirection` and `rightDirection`).

---

## Properties

### PathPoint.anchor

`app.activeDocument.pathItems[index].pathPoints[index].anchor`

#### Description

The position of this point's anchor point.

#### Type

Array of 2 numbers

---

### PathPoint.leftDirection

`app.activeDocument.pathItems[index].pathPoints[index].leftDirection`

#### Description

The position of this path point's in control point.

#### Type

Array of 2 numbers

---

### PathPoint.parent

`app.activeDocument.pathItems[index].pathPoints[index].parent`

#### Description

The path item that contains this path point.

#### Type

[PathItem](./PathItem.md); read-only.

---

### PathPoint.pointType

`app.activeDocument.pathItems[index].pathPoints[index].pointType`

#### Description

The type of path point, either a curve or a corner. Any point can considered a corner point.

Setting the type to a corner forces the left and right direction points to be on a straight line when the user attempts to modify them in the user interface.

#### Type

[PointType](scripting-constants.md#pointtype)

---

### PathPoint.rightDirection

`app.activeDocument.pathItems[index].pathPoints[index].rightDirection`

#### Description

The position of this path point's out control point.

#### Type

Array of 2 numbers

---

### PathPoint.selected

`app.activeDocument.pathItems[index].pathPoints[index].selected`

#### Description

Are points of this path point selected, and if so, which ones.

#### Type

[PathPointSelection](scripting-constants.md#pathpointselection)

---

### PathPoint.typename

`app.activeDocument.pathItems[index].pathPoints[index].typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

## Methods

### PathPoint.remove()

`app.activeDocument.pathItems[index].pathPoints[index].remove()`

#### Description

Removes the referenced point from the path.

#### Returns

Nothing.
