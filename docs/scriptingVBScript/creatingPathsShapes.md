# Creating paths and shapes

This section explains how to create items that contain paths.

---

## Paths

To create line or a freeform path, specify a series of path points, as a series of x-y coordinates or `PathPoint` objects.

Using x-y coordinates limits the path to straight segments. To created a curved path, you must create `PathPoint` objects. A path can comprise a combination of page coordinates and `PathPoint` objects.

### Specifying a series of x-y coordinates

To specify a path using page-coordinate pairs, use the `entire path` property of the `PathItems` object. The following script specifies three pairs of x-y coordinates, to create a path with three points

```basic
Set appRef = CreateObject ("Illustrator.Application")

Set firstPath = appRef.ActiveDocument.PathItems.Add
  firstPath.Stroked = True
firstPath.SetEntirePath(Array(Array(220, 475),Array(375, 300),Array(200, 300)))
```

### Using path point objects

To create a `PathPoint` object, you must define three values for the point.

- A fixed `anchor` point, which is the point on the path.
- A pair of direction points— `left direction` and `right direction` —which allow you to control the path segment's curve.

You define each property as an array of page coordinates in the format `(Array (x,y))`:

- If all three properties of a `PathPoint` object have the same coordinates, and the properties of the next `PathPoint` in the line are equal to each other, you create a straight-line segment.
- If two or more properties in a `PathPoint` object hold different values, the segment connected to the point is curved.

To create a path or add points to an existing path using `PathPoint` objects, create a `PathItem` object, then add the path points as child objects in the `PathItem`

```basic
Set appRef = CreateObject ("Illustrator.Application")

Set firstPath = appRef.ActiveDocument.PathItems.Add
  firstPath.Stroked = true
Set newPoint = firstPath.PathPoints.Add
'Using identical coordinates creates a straight segment
newPoint.Anchor = Array(75, 300)
newPoint.LeftDirection = Array(75, 300)
newPoint.RightDirection = Array(75, 300)

Set newPoint2 = firstPath.PathPoints.Add
newPoint2.Anchor = Array(175, 250)
newPoint2.LeftDirection = Array(175, 250)
newPoint2.RightDirection = Array(175, 250)

Set newPoint3 = firstPath.PathPoints.Add
'Using different coordinates creates a curve
newPoint3.Anchor = Array(275, 290)
newPoint3.LeftDirection = Array(135, 150)
newPoint3.RightDirection = Array(155, 150)
```

### Combining path point types

The following script sample creates a path with three points

```basic
Set appRef = CreateObject("Illustrator.Application")
Set myDoc = appRef.ActiveDocument
Set myLine = myDoc.PathItems.Add
  myLine.Stroked = True
  myLine.SetEntirePath( Array( Array(320, 475), Array(375, 300)))

' Append another point to the line
Set newPoint = myLine.PathPoints.Add
  'Using identical coordinates creates a straight segment
  newPoint.Anchor = Array(220, 300)
  newPoint.LeftDirection = Array(220, 300)
  newPoint.RightDirection = Array(220, 300)
```

---

## Shapes

To create a shape, you use the object that corresponds to the shape's name (like `ellipse`, `rectangle`, or `polygon`), and use the object's properties to specify the shape's position, size, and other information like the number of sides in a polygon.

Remember:

- The scripting engine processes all measurements and page coordinates as points. For details, see [Measurement Units](../scripting/measurementUnits.md#scripting-measurementunits).
- x and y coordinates are measured from the bottom-left corner of the document, as indicated in the Info panel in the Illustrator application. For details, see [Page-item positioning and dimensions](../scripting/positioning.md#scripting-positioning).

### Creating a rectangle

Consider the following sample

```basic
Set appRef = CreateObject("Illustrator.Application")
Set frontDocument = appRef.ActiveDocument
' Create a new rectangle with
' top = 144, left side = 144, width = 72, height = 144
Set newRectangle = frontDocument.PathItems.Rectangle(144,144,72,144)
```

The sample creates a rectangle with these properties:

- The top of the rectangle is 2 inches (144 points) from the bottom edge of the page.
- The left edge is 2 inches (144 points) from the left edge of the page.
- The rectangle is 1 inch (72 points) wide and 2 inches (144 points) long.

### Creating a polygon

Consider the following sample

```basic
Set appRef = CreateObject("Illustrator.Application")
Set frontDocument = appRef.ActiveDocument
' Create a new polygon with
' top = 144, left side = 288, width = 72, height = 144
Set newPolygon = frontDocument.PathItems.Polygon(144,288,72,7)
```

The sample creates a polygon with these properties:

- The center point of the object is inset is 2 inches (144 points) on the horizontal axis and 4 inches (288 points) on the vertical axis.
- The polygon has 7 sides.
- The length of the radius from the center point to each corner is 1 inch (72 points).
