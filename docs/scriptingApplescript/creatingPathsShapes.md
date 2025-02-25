# Creating paths and shapes

This section explains how to create items that contain paths.

---

## Paths

To create line or a freeform path, specify a series of path points, as a series of x-y coordinates or `path` point objects.

Using x-y coordinates limits the path to straight segments. To created a curved path, you must create `path point` objects. A path can comprise a combination of page coordinates and `path point` objects.

### Specifying a series of x-y coordinates

To specify a path using page-coordinate pairs, use the `entire path` property of the `path items` object. The following script specifies three pairs of x-y coordinates, to create a path with three points:

```applescript
tell application "Adobe Illustrator"
set docRef to make new document
-- set stroked to true so we can see the path
set lineRef to make new path item in docRef with properties {stroked:true}
set entire path of lineRef to { {220, 475},{200, 300},{375, 300} }
end tell
```

### Using path point objects

To create a `path point` object, you must define three values for the point.

- A fixed `anchor` point, which is the point on the path.
- A pair of direction points— `left direction` and `right direction` —which allow you to control the path segment's curve.

You define each property as an array of page coordinates in the format [x, y]:

- If all three properties of a `path point` object have the same coordinates, and the properties of the next `path point` in the line are equal to each other, you create a straight-line segment.
- If two or more properties in a `path point` object have different values, the segment connected to the point is curved.

To create a path or add points to an existing path using `path point` objects, create a `path item` object, then add the path points as child objects in the `path item`:

```applescript
tell application "Adobe Illustrator"
set docRef to make new document
-- set stroked to true so we can see the path
set lineRef to make new path item in docRef with properties {stroked:true}
    --giving the direction points the same value as the
    --anchor point creates a straight line segment
set newPoint to make new path point of lineRef with properties
    {anchor:{220, 475},left direction:{220, 475},right direction:{220, 475}, point type:corner}

set newPoint2 to make new path point of lineRef with properties
    {anchor:{375, 300},left direction:{375, 300},right direction:{375, 300}, point type:corner}

    --giving the direction points the different values
    --creates a curve
set newPoint3 to make new path point of lineRef with properties
    {anchor:{220, 300},left direction:{180, 260},right direction:{240, 320}, point type:corner}

end tell
```

### Combining path point types

The following script sample creates a path with three points, by combining the entire path property with a `path point` object

```applescript
tell application "Adobe Illustrator"
set docRef to make new document
-- set stroked to true so we can see the path
set lineRef to make new path item in docRef with properties {stroked:true}
set entire path of lineRef to { {220, 475},{375, 300} }
set newPoint to make new path point of lineRef with properties
    {anchor:{220, 300},left direction:{180, 260},right direction:{240, 320}, point type:corner}
end tell
```

---

## Shapes

To create a shape, you use the object that corresponds to the shape's name (like `ellipse`, `rectangle`, or `polygon`), and use the object's properties to specify the shape's position, size, and other information like the number of sides in a polygon.

Remember:

- The scripting engine processes all measurements and page coordinates as points. For details, see [Measurement Units](../scripting/measurementUnits.md).
- x and y coordinates are measured from the bottom-left corner of the document, as indicated in the Info panel in the Illustrator application. For details, see [Page-item positioning and dimensions](../scripting/positioning.md).

### Write-once access

Properties for path-item shapes use the "write-once" access status, which indicates that the property is writeable only when the object is created. For existing path-item objects, the properties are read-only
properties whose values cannot be changed.

### Creating a rectangle

Consider the following sample:

```applescript
tell application "Adobe Illustrator"
set docRef to make new document
set rectRef to make new rectangle in docRef with properties
    { bounds:{288, 360, 72, 144} }
end tell
```

The sample creates a rectangle with these properties:

- The top-right corner of the of the rectangle is inset 4 inches (288 points) from the bottom of the page and 5 inches (360 points) from the left edge of the page.
- The lower-left corner of the rectangle is inset 1 inch (72 points) from the left edge of the page and 2 inches (144 points) from the bottom of the page.

### Creating a polygon

Consider the following sample:

```applescript
tell application "Adobe Illustrator"
set docRef to make new document
set pathRef to make new polygon in docRef with properties
{center point:{144, 288},sides:7,radius:72.0}
end tell
```

The sample creates a polygon with these properties:

- The center point of the object is inset is 2 inches (144 points) on the horizontal axis and 4 inches (288 points) on the vertical axis.
- The polygon has 7 sides.
- The length of the radius from the center point to each corner is 1 inch (72 points).
