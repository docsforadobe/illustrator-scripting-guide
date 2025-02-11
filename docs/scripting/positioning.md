# Page-item positioning and dimensions

Illustrator uses simple, two-dimensional geometry in the form of points to record the position of page item objects in a document. Every page item object in a document has a position property that
defines a fixed point as a pair of page coordinates in the format [x, y]. The fixed point is the top-left corner of the object's bounding box.

For information on the types of objects that comprise the page items collection, see "The artwork tree" on

A point is designated by a pair of coordinates:

- The horizontal position, x
- The vertical position, y

You can see these coordinates in the Info panel when you select or create an object in Illustrator.

For the artboard, the default coordinate origin, (0,0), is the top-left corner, reflected in the ruler origin property of the artboard object. X coordinate values increase from left to right, and Y values increase from top to bottom. This changed in the CS5 release; to maintain script compatability, a document created by a script still uses the older system, with the origin at the bottom left of the artboard, and the Y value increasing from bottom to top. The page origin property of a document object defines the bottom-left corner of the printable region of the document as a fixed point.

Each page item object has width and height properties. The maximum value allowed for the width or height of a page item is 16348 points.

---

## Art item bounds

Every page item object has three properties that use fixed rectangles to describe the object's overall extent:

- The geometric bounds of a page item are the rectangular dimensions of the object's bounding box, excluding stroke width.
- The visible bounds of a page item are the dimensions of the object, including any stroke widths.
- The control bounds define the rectangular dimensions of the object, including in and out control points.

The following figure illustrates these properties, using JavaScript naming conventions.

![Art Item Bounds](_static/artItemBounds.jpg)
