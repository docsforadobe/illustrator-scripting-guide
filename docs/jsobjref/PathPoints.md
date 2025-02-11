<a id="jsobjref-pathpoints"></a>

# PathPoints

`app.activeDocument.pathItems[index].pathPoints`

**Description**

A collection of [PathPoint](PathPoint.md#jsobjref-pathpoint) objects in a specific path.

The elements are not named; you must access them by index.

---

## Properties

<a id="jsobjref-pathpoints-length"></a>

### PathPoints.length

`app.activeDocument.pathItems[index].pathPoints.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

<a id="jsobjref-pathpoints-parent"></a>

### PathPoints.parent

`app.activeDocument.pathItems[index].pathPoints.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-pathpoints-typename"></a>

### PathPoints.typename

`app.activeDocument.pathItems[index].pathPoints.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-pathpoints-add"></a>

### PathPoints.add()

`app.activeDocument.pathItems[index].pathPoints.add()`

**Description**

Creates a new object.

**Returns**

[PathPoint](PathPoint.md#jsobjref-pathpoint)

---

<a id="jsobjref-pathpoints-index"></a>

### PathPoints.index()

`app.activeDocument.pathItems[index].pathPoints.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[PathPoint](PathPoint.md#jsobjref-pathpoint)

---

<a id="jsobjref-pathpoints-removeall"></a>

### PathPoints.removeAll()

`app.activeDocument.pathItems[index].pathPoints.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Adding a path point to a path

```default
// Appends a new PathPoint to an existing path
// and initializes its anchor and handle points.
if (app.documents.length > 0) {
  var doc = app.activeDocument;

  var line = doc.pathItems.add();
  line.stroked = true;
  line.setEntirePath(Array(Array(220, 475), Array(375, 300)));

  // Append another point to the line
  var newPoint = doc.pathItems[0].pathPoints.add();
  newPoint.anchor = Array(220, 300);
  newPoint.leftDirection = newPoint.anchor;
  newPoint.rightDirection = newPoint.anchor;
  newPoint.pointType = PointType.CORNER;
}
```
