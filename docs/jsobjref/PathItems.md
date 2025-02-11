# PathItems

`app.activeDocument.pathItems`

**Description**

A collection of [PathItem](PathItem.md#jsobjref-pathitem) objects.

The methods `ellipse`, `polygon`, `rectangle`, `roundedRectangle`, and `star` allow you to create complex path items using straightforward parameters.

If you do not provide any parameters when calling these methods, default values are used.

---

## Properties

### PathItems.length

`app.activeDocument.pathItems.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

### PathItems.parent

`app.activeDocument.pathItems.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

### PathItems.typename

`app.activeDocument.pathItems.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### PathItems.add()

`app.activeDocument.pathItems.add()`

**Description**

Creates a new object.

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.ellipse()

`app.activeDocument.pathItems.ellipse([top][, left][, width][, height][, reversed][, inscribed])`

**Description**

Creates a new pathItem in the shape of an ellipse using the supplied parameters.

**Defaults**

| Parameter   | Value   |
|-------------|---------|
| `top`       | 100 pt. |
| `left`      | 100 pt. |
| `width`     | 50 pt.  |
| `height`    | 100 pt. |
| `reversed`  | false   |

**Parameters**

| Parameter   | Type                      | Description               |
|-------------|---------------------------|---------------------------|
| `top`       | Number (double), optional | Top of path               |
| `left`      | Number (double), optional | Left of path              |
| `width`     | Number (double), optional | Width of path             |
| `height`    | Number (double), optional | Height of path            |
| `reversed`  | Boolean, optional         | Whether path is reversed  |
| `inscribed` | Boolean, optional         | Whether path is inscribed |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.getByName()

`app.activeDocument.pathItems.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.index()

`app.activeDocument.pathItems.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.polygon()

`app.activeDocument.pathItems.polygon([centerX][, centerY][, radius][, sides][, reversed])`

**Description**

Creates a new `pathItem` in the shape of an polygon using the supplied parameters.

**Defaults**

| Parameter   | Value   |
|-------------|---------|
| `centerX`   | 200 pt. |
| `centerY`   | 300 pt. |
| `radius`    | 50 pt.  |
| `sides`     | 8       |
| `reversed`  | false   |

**Parameters**

| Parameter   | Type                      | Description              |
|-------------|---------------------------|--------------------------|
| `centerX`   | Number (double), optional | CenterX of path          |
| `centerY`   | Number (double), optional | CenterY of path          |
| `radius`    | Number (double), optional | Radius of path           |
| `sides`     | Number (long), optional   | Number of sides          |
| `reversed`  | Boolean, optional         | Whether path is reversed |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.rectangle()

`app.activeDocument.pathItems.rectangle(top, left, width, height[,reversed])`

**Description**

Creates a new `pathItem` in the shape of an polygon using the supplied parameters.

**Parameters**

| Parameter   | Type              | Description              |
|-------------|-------------------|--------------------------|
| `top`       | Number (double)   | Top of path              |
| `left`      | Number (double)   | Left of path             |
| `width`     | Number (double)   | Width of path            |
| `height`    | Number (double)   | Height of path           |
| `reversed`  | Boolean, optional | Whether path is reversed |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.removeAll()

`app.activeDocument.pathItems.removeAll()`

**Description**

Deletes all elements in this collection.

**Returns**

Nothing

---

### PathItems.roundedRectangle()

`app.activeDocument.pathItems.roundedRectangle(top, left, width, height[, horizontalRadius][, verticalRadius][, reversed])`

**Description**

Creates a new pathItem in the shape of a rectangle with rounded corners using the supplied parameters.

**Defaults**

| Parameter          | Value   |
|--------------------|---------|
| `horizontalRadius` | 15 pt.  |
| `verticalRadius`   | 20 pt.  |
| `reversed`         | false   |

**Parameters**

| Parameter          | Type                      | Description                         |
|--------------------|---------------------------|-------------------------------------|
| `top`              | Number (double)           | Top of path                         |
| `left`             | Number (double)           | Left of path                        |
| `width`            | Number (double)           | Width of path                       |
| `height`           | Number (double)           | Height of path                      |
| `horizontalRadius` | Number (double), optional | Horizontal radius of rounded corner |
| `verticalRadius`   | Number (double), optional | Vertical radius of rounded corner   |
| `reversed`         | Boolean, optional         | Whether path is reversed            |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

### PathItems.star()

`app.activeDocument.pathItems.star([centerX][, centerY][, radius][, innerRadius][, points][, reversed])`

**Description**

Creates a new path item in the shape of a star using the supplied parameters.

**Defaults**

| Parameter     | Value   |
|---------------|---------|
| `centerX`     | 200 pt. |
| `centerY`     | 300 pt. |
| `radius`      | 50 pt.  |
| `innerRadius` | 20 pt.  |
| `points`      | 5       |
| `reversed`    | false   |

**Parameters**

| Parameter     | Type                      | Description              |
|---------------|---------------------------|--------------------------|
| `centerX`     | Number (double), optional | CenterX of path          |
| `centerY`     | Number (double), optional | CenterY of path          |
| `radius`      | Number (double), optional | Radius of path           |
| `innerRadius` | Number (double), optional | Inner radius of path     |
| `points`      | Number (long), optional   | Number of points         |
| `reversed`    | Boolean, optional         | Whether path is reversed |

**Returns**

[PathItem](PathItem.md#jsobjref-pathitem)

---

## Example

### Creating shapes

```default
// Creates 5 shapes in layer 1 of document 1
// and applies a random graphic style to each
var doc = app.documents.add();
var artLayer = doc.layers[0];
app.defaultStroked = true;
app.defaultFilled = true;

var rect = artLayer.pathItems.rectangle(762.5, 87.5, 425.0, 75.0);
var rndRect = artLayer.pathItems.roundedRectangle(637.5, 87.5, 425.0, 75.0, 20.0, 10.0);

// Create ellipse, 'reversed' is false, 'inscribed' is true
var ellipse = artLayer.pathItems.ellipse(512.5, 87.5, 425.0, 75.0, false, true);

// Create octagon, and 8-sided polygon
var octagon = artLayer.pathItems.polygon(300.0, 325.0, 75.0, 8);

// Create a 4 pointed star
var star = artLayer.pathItems.star(300.0, 125.0, 100.0, 20.0, 4);

for (i = 0; i < artLayer.pathItems.length; i++) {
  var styleIndex = Math.round(Math.random() * (doc.graphicStyles.length - 1));
  doc.graphicStyles[styleIndex].applyTo(artLayer.pathItems[i]);
}
```
